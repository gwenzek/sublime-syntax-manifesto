import os
import sys
import plistlib


def extract_scopes(filename):
    scopes = set(extract_all_scopes(filename))
    scopes = set(flatten(yield_scopes_and_subscopes, scopes))
    return sorted(scopes)


def extract_all_scopes(filename):
    theme = plistlib.readPlist(file(filename))
    settings = theme['settings']
    scopes = []
    for settings in theme['settings']:
        if 'scope' in settings:
            scopes += list(split(settings['scope'], ' -', ',', ' '))
    return scopes


def yield_scopes_and_subscopes(scope):
    parts = scope.split('.')
    s = ''
    for p in parts:
        s = p if s == '' else s + '.' + p
        yield scope


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
    parts = scope.split('.')
    s = ''
    for p in parts:
        s = p if s == '' else s + '.' + p
        if s in count:
            count[s] += 1
        else:
            count[s] = 1


def write_summary(count, filename):

    scopes = sorted(count.iteritems())
    with open(filename, 'w') as out:
        for (scope, c) in scopes:
            out.write('%s\t%d\n' % (scope, c))

if __name__ == '__main__':

    args = sys.argv[1:]
    syntaxes_dir = args[0]
    scopes_dir = args[1]

    count = {}

    for filename in os.listdir(syntaxes_dir):
        out_path = os.path.join(scopes_dir, os.path.splitext(filename)[0] + '.txt')
        with open(out_path, 'w') as out:
            scopes = extract_scopes(os.path.join(syntaxes_dir, filename))
            for scope in scopes:
                increment_count(count, scope)
                out.write(scope)
                out.write('\n')
            print 'found', len(scopes), 'scopes in theme file', os.path.basename(filename)

    write_summary(count, 'summary.themes.txt')
