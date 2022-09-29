#! python3
# selective copy files with certain extension to selected folder

import shutil, os, re

from pathlib import Path

def select_copy(folder,ext,f_out):
    end_ext = '.*\.' + ext
    folder = os.path.abspath(folder) # make sure folder is absolute
    if (Path(folder) / f_out).exists() is False:
        os.makedirs(Path(folder) / f_out)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if re.compile(end_ext).search(filename) != None:
                print('copying ... ' + str(Path(foldername) / filename))
                shutil.copy(Path(foldername) / filename, Path(foldername) / f_out)
                print('copied to ...' + str(Path(foldername) / f_out))

select_copy(r'C:\Users\19ard\mu_code','txt','copy_test3')

