import os
import sys
import yaml


def extract_scopes(filename):
    scopes = set(extract_all_scopes(filename))
    return sorted(scopes)


def extract_all_scopes(filename):
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
            print 'found', len(scopes), 'scopes in syntax file', os.path.basename(filename)

    write_summary(count, 'summary.syntaxes.txt')
