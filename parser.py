import argparse
import os
import re


def take_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p')
    parser.add_argument('-reg')
    parser.add_argument('-end')
    args = parser.parse_args()
    return args


def file_dir(args):
    if os.path.isfile(args.p):  # функция принимает на вход аргументы, переданные пользователем
        return [args.p]  # обрабатывает их, и на выходе мы получаем все файлы, нужные нам для парсинга
    else:
        files = os.listdir(path=args.p)
        if files:
            rg = re.compile(args.end)
            return [args.p + '/' + p for p in os.listdir(path=args.p) if os.path.isfile(args.p + '/' + p) and re.match(p)]


def read(file_path):
    with open (file_path, 'r') as f:   #функция находит файл по пути и возвращает все строки файла
        return f.read()

def new_file():
    filename = 'newlog.log'
    with open(filename, 'a') as f:
        f.write('_')


