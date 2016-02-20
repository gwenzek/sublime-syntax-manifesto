import os
import sys
import zipfile


def extract(filename, output_path, extension):
    f = zipfile.ZipFile(filename)

    def path(syntax):
        return os.path.join(output_path, os.path.basename(syntax))

    for syntax in filter(lambda x: x.endswith(extension), f.namelist()):
        with open(path(syntax), 'wb') as out:
            out.write(f.read(syntax))

if __name__ == '__main__':

    args = sys.argv
    archive = args[1]
    folder = args[2]
    extension = args[3]
    print 'extracting all', extension, 'from archive', archive, 'to folder', folder
    extract(archive, folder, extension)
