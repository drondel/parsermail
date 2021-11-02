import argparse
import os
import regex as re
from tqdm import tqdm


def take_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', required=True)
    parser.add_argument('-reg', required=True)
    parser.add_argument('-end', required=True)
    args = parser.parse_args()
    return args


def files_path(args):
    if os.path.isfile(args.p):
        return [args.p]
    elif os.path.isdir(args.p):
        dir = os.listdir(path=args.p)
        if not dir:
            print('Directory is empty')
        else:           #пытался разобраться, почему не хочет читать файлы из заданного пути, так и не понял
            rg = re.compile(args.end)      #при этом если указывать путь с конкретным файлом, все работает(((
            return [args.p + '/' + p for p in dir if os.path.isfile(args.p + '/' + p) and rg.match(p)]

def reading(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def new_file(lines):
    filename = 'new.log'
    with open(filename, 'a') as f:
        f.writelines(lines)


def line_check(file_path, regexp, lines):
    res = [file_path + ': ' + line + '\n' for line in tqdm(lines) if re.match(regexp, line)]
    new_file(res)
    return res


if __name__ == '__main__':
    args = take_args()
    files_path = files_path(args)
    count_files = len(files_path)
    print(count_files)
    count_files_now = 0
    for file_path in files_path:
        count_files_now += 1
        print(f'Reading {file_path} {count_files_now}/{count_files} files')
        regexp = args.reg
        lines = reading(file_path).split('\n')
        line_check(file_path, regexp, lines)
