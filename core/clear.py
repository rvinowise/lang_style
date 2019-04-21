#!python

import os, shutil, glob

bad_names = ['__pycache__', '.pytest_cache', '.cache']
ignored_dirs = ['venv']


def remove_autogenerated_objects(dir):
    bad_dirs = []
    for name in bad_names:
        bad_dirs.extend(glob.glob('./**/'+name, recursive=True))

    skipped = []
    print('removing:')
    for dir in bad_dirs:
        if is_inside_ignored_dir(dir):
            skipped.append(dir)
            continue
        print(dir)
        shutil.rmtree(dir)

    print('skipped:')
    for dir in skipped:
        print(dir)

def is_inside_ignored_dir(dir):
    dir = os.path.normpath(dir)
    dir_list = dir.split(os.sep)
    for name in dir_list:
        if name in ignored_dirs:
            return True

if __name__ == '__main__':
    remove_autogenerated_objects('.')