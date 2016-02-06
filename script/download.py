import os
import wget
import zipfile


def extract(filename, output_path):
    f = zipfile.ZipFile(filename)

    def path(syntax):
        return os.path.join(output_path, os.path.basename(syntax))

    for syntax in filter(lambda x: x.endswith('.sublime-syntax'), f.namelist()):
        with open(path(syntax), 'wb') as out:
            out.write(f.read(syntax))

if __name__ == '__main__':

    wget.download("https://github.com/sublimehq/Packages/archive/master.zip")
    extract('Packages-master.zip', 'syntaxes')
