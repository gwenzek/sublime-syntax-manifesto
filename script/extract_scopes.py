import os
import yaml


def extract_scopes(filename):
    scopes = set(extract_all_scopes(filename))
    return sorted(scopes)


def extract_all_scopes(filename):
    syntax = yaml.load(file(filename))
    # scopes = [syntax['scope']]
    scopes = []
    for context in syntax['contexts']:
        scopes += list(_extract_scopes_from_yaml(syntax['contexts'][context]))
    return scopes


def _extract_scopes_from_yaml(array):
    if isinstance(array, list):
        for n in array:
            if 'scope' in n:
                yield n['scope']
            if 'meta_scope' in n:
                yield n['meta_scope']
            if 'meta_content_scope' in n:
                yield n['meta_content_scope']
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

if __name__ == '__main__':
    for filename in os.listdir('syntaxes'):
        out_path = os.path.join('scopes', os.path.splitext(filename)[0] + '.txt')
        with open(out_path, 'w') as out:
            scopes = extract_scopes(os.path.join('syntaxes', filename))
            for scope in scopes:
                out.write(scope)
                out.write('\n')
            print 'found', len(scopes), 'scopes in syntax file', os.path.basename(filename)
