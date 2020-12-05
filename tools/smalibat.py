#encoding : utf-8
import os
import sys
import time

def decompilation(filename,outdir):
    #command = "apktool.jar d " + filename
    command = "apktool.jar d {0} -o {1}".format(filename, outdir)
    os.system(command)

if __name__ == '__main__':
    index=0
    #apk
    path = "VirusShare2018\\Virsus2019\\"
    apklist = os.listdir(path)
    time_start = time.time()

    for apk in apklist:
        outdir="out-of-sample-2019\\"+apk
        filename=path+apk
        print(filename)
        print(index)
        decompilation(filename,outdir)
        index+=1
    time_end = time.time()
    print('time cost', time_end - time_start, 's')

    