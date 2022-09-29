#! python3
# deleting files larger then XXX MB

import os,send2trash

from pathlib import Path

def del_sel(folder,size):
    folder = os.path.abspath(folder) # make sure folder is absolute

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(Path(foldername) / filename) > size*1000000:
                print(str(Path(foldername) / filename) + ' size is ' + str(int(os.path.getsize(Path(foldername) / filename)/1000000)) + 'MB')
                while True:
                    act = input('Proceed to delete(Y/N)?\n')
                    if act.upper() == 'Y':
                        send2trash.send2trash(str(Path(foldername) / filename))
                        print(str(Path(foldername) / filename) + ' ...was deleted')
                        break
                    elif act.upper() == 'N':
                        print('No file deleted')
                        break
                    else:
                        print('Please input Y/N')

del_sel(r'C:\Users\19ard',1000)
