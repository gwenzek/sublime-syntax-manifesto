import sys


def load_scopes(filename):
    with open(filename) as f:
        for line in f:
            parts = line.split('\t')
            yield parts[0], int(parts[1])


def scope_is_valide(scope):
    languages = ['html', 'js', 'css', 'ruby', 'php', 'shell', 'makefile', 'sql', 'markdown', 'json', 'latex', 'xml', 'tex', 'yaml', 'diff', 'c', 'python', 'begin', 'end']
    if any(scope.endswith('.' + ext) for ext in languages):
        return False

    return True


if __name__ == '__main__':
    args = sys.argv[1:]
    syntax_scopes = list(load_scopes(args[0]))
    theme_scopes = list(load_scopes(args[1]))

    syntax_dict = dict(syntax_scopes)
    theme_dict = dict(theme_scopes)

    with open('summary.non_existing.txt', 'w') as o:
        for scope, count in theme_scopes:
            if scope not in syntax_dict:
                o.write('%s\t%d\n' % (scope, count))

    cleaned = 0
    with open('summary.themes.cleaned.txt', 'w') as o:
        for scope, count in theme_scopes:
            if scope in syntax_dict and count > 2:
                if scope_is_valide(scope):
                    o.write('%s\t%d\n' % (scope, count))
                    cleaned += 1

    print 'Themes uses %d scopes, %d after cleaning' % (len(theme_scopes), cleaned)

    with open('summary.not_matched.txt', 'w') as o:
        for scope, count in syntax_scopes:
            if scope not in theme_dict:
                o.write('%s\t%d\n' % (scope, count))
