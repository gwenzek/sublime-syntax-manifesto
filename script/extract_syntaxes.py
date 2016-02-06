import os
import sys
import zipfile


def extract(filename, output_path):
    f = zipfile.ZipFile(filename)

    def path(syntax):
        return os.path.join(output_path, os.path.basename(syntax))

    for syntax in filter(lambda x: x.endswith('.sublime-syntax'), f.namelist()):
        with open(path(syntax), 'wb') as out:
            out.write(f.read(syntax))

if __name__ == '__main__':

    args = sys.argv
    archive = args[1] if len(args) > 1 else 'Packages-master.zip'
    folder = args[2] if len(args) > 2 else 'syntaxes'
    print archive, folder
    extract(archive, folder)
