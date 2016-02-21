import os
import sys
import plistlib
import yaml


def extract_scopes(filename):
    if filename.endswith('.tmTheme'):
        scopes = set(extract_scopes_from_plist(filename))
    elif filename.endswith('.sublime-syntax'):
        scopes = set(extract_scopes_from_yaml(filename))
    else:
        raise Exception('Format not recognized for: ' + filename)

    scopes = set(flatten(yield_scopes_and_subscopes, scopes))
    return sorted(scopes)


def extract_scopes_from_plist(filename):
    theme = plistlib.readPlist(file(filename))
    settings = theme['settings']
    scopes = []
    for settings in theme['settings']:
        if 'scope' in settings:
            scopes += list(split(settings['scope'], ' -', ',', ' '))
    return scopes


def extract_scopes_from_yaml(filename):
    syntax = yaml.load(file(filename))
    scopes = [syntax['scope']]
    # scopes = []
    for context in syntax['contexts']:
        scopes += list(_extract_scopes_from_yaml(syntax['contexts'][context]))
    return scopes


def _extract_scopes_from_yaml(array):
    if isinstance(array, list):
        for n in array:
            if 'scope' in n:
                for s in n['scope'].split():
                    yield s
            if 'meta_scope' in n:
                for s in n['meta_scope'].split():
                    yield s
            if 'meta_content_scope' in n:
                for s in n['meta_content_scope'].split():
                    yield s
            if 'captures' in n:
                for capture in n['captures']:
                    yield n['captures'][capture]
            if 'with_prototype' in n:
                for s in _extract_scopes_from_yaml(n['with_prototype']):
                    yield s
            if 'push' in n:
                for s in _extract_scopes_from_yaml(n['push']):
                    yield s
            if 'set' in n:
                for s in _extract_scopes_from_yaml(n['set']):
                    yield s


def yield_scopes_and_subscopes(scope):
    parts = scope.split('.')
    s = ''
    for p in parts:
        s = p if s == '' else s + '.' + p
        yield s


def flatten(f, l):
    for x in l:
        for y in f(x):
            yield y


def split(string, *sep):
    l = [string]
    for s in sep:
        l = list(map(lambda x: x.strip().strip('(').strip(')'), flatten(lambda x: x.split(s), l)))
    return l


def increment_count(count, scope):
    if scope in count:
        count[scope] += 1
    else:
        count[scope] = 1


def write_summary(count, filename):

    scopes = sorted(count.iteritems())
    with open(filename, 'w') as out:
        for (scope, c) in scopes:
            out.write('%s\t%d\n' % (scope, c))

if __name__ == '__main__':

    args = sys.argv[1:]
    syntaxes_dir = args[0]
    scopes_dir = args[1]
    summary = args[2]

    count = {}

    for filename in os.listdir(syntaxes_dir):
        out_path = os.path.join(scopes_dir, os.path.splitext(filename)[0] + '.txt')
        with open(out_path, 'w') as out:
            scopes = extract_scopes(os.path.join(syntaxes_dir, filename))
            for scope in scopes:
                if scope in count:
                    count[scope] += 1
                else:
                    count[scope] = 1

                out.write(scope)
                out.write('\n')
            print 'found', len(scopes), 'scopes in theme file', os.path.basename(filename)

    write_summary(count, summary)
