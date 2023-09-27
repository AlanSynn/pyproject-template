import os
import argparse

def change_extension(file_path, new_extension, append_extension=False):
    base = os.path.splitext(file_path)[0]
    base_extension = os.path.splitext(file_path)[1]
    if append_extension is True and base_extension != new_extension:
        new_extension = os.path.splitext(file_path)[1] + new_extension

    os.rename(file_path, base + new_extension)

def change_string(file_path, search_string, new_string):
    with open(file_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(content.replace(search_string, new_string))

def main():
    parser = argparse.ArgumentParser(description='Change file extensions and add prompt if string exists in file.')

    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory to scan')
    parser.add_argument('-s', '--string', type=str, required=True, help='String to search for')
    parser.add_argument('-n', '--new_string', type=str, required=True, help='New string to replace old string')
    parser.add_argument('-e', '--extension', type=str, required=True, help='New file extension')
    parser.add_argument('-a', '--append', action='store_true', help='Append new extension to old extension')

    args = parser.parse_args()

    directory = args.directory
    search_string = args.string
    new_string = args.new_string
    new_extension = args.extension
    append_extension = args.append

    excluded_dirs = ['static', 'imgs', '__pycache__']

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excluded_dirs] # exclude certain directories
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                with open(file_path, 'r') as f:
                    content = f.read()

                    try:
                        if search_string in content:
                            change_string(file_path, search_string, new_string)
                            change_extension(file_path, new_extension, append_extension)
                    except:
                        raise Exception(f'Could not change string {search_string} to {new_string} in file {file_path}')
            except:
                raise Exception(f'Could not open file {file_path}')

if __name__ == '__main__':
    main()
