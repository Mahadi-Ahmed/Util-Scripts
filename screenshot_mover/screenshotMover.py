#!/usr/bin/python3
import glob, os
import shutil

os.chdir('/Users/mahadiahmed/Desktop')
screenshots = [file for file in glob.glob('Screenshot*.png')]

for screenshot in screenshots:
    shutil.move(screenshot,'/Users/mahadiahmed/Documents/screenshots')
print('moved files: ')
print(screenshots)
exit()

