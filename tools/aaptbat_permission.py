#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import zipfile
import re
from collections import defaultdict
import operator
import numpy as np
import scipy.io as scio

listres=[]


permission_frequency=defaultdict(int)
Dic = {}

app_path = "G:\\VirusShare2018\\Virsus2019"
# app_path ="G:\\CICInvesAndMal2017\\Virsus"


appnum=len(os.listdir(app_path))
permissionnum=0
permission_list=[]




def text_save(filename, data):#CSV filename
    file = open(filename,'a')
    for i in range(len(data)):
        s= str(data[i])+"\n"
        # s = str(data[i]).replace('[[','').replace(']]','\n').replace('[','').replace(']','')#
        # s = s.replace("'",'').replace(',','')
        # print (s1+'\n')
        # print (s)
        file.write(s)
    file.close()
    print("successfully")



def getAppBaseInfo(apkpath,index):
    try:
        output = os.popen("aapt d badging %s" % apkpath).read()
    except FileNotFoundError:
        print("FileNotFoundError: no file")
        print(apkpath)
        os.remove(apkpath)

    except UnicodeDecodeError:
        print("UnicodeDecodeError: no file")
        print(apkpath)
        os.remove(apkpath)
    else:
        listres = list()

        # print(output)
        # command = "aapt d badging %s" % apkpath + "> 1.txt"
        # os.system(command)

        # match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(
        #     output)
        # if not match:
        #     raise Exception("can't get packageinfo")
        #
        # packagename = match.group(1)
        # versionCode = match.group(2)
        # versionName = match.group(3)
        # print (u" packagename：%s \n version：%s \n version name：%s " % (packagename, versionCode, versionName))
        # listres.append(packagename)
        # listres.append(versionCode)
        # listres.append(versionName)


        outList = output.split('\n')
        listtem=[]
        # print(outList)
        for line in outList:
            if line.startswith('uses-permission:') and ("android.permission") in line:
                s_permission = line.split(':')[1].split('\'')[1].split('.')[2].replace(" ", "").upper()  # 输出所有的权限
                # if (s_permission in Dic and s_permission not in listres):
                #     Dic[s_permission] += 1
                #     listres.append(s_permission)

                if(s_permission not in listtem):
                    listtem.append(s_permission)

                # if(s_permission in permission_list):
                #     p_index = permission_list.index(s_permission)
                #     M[index,p_index]=1
                # else:
                #     print(s_permission + "not found!")
        for s_permission in listtem :
            if (s_permission not in permission_frequency):
                permission_frequency[s_permission] = 1
            else:
                permission_frequency[s_permission] = permission_frequency[s_permission] + 1


if __name__ == "__main__":
    index=0

#     with open("G:\\app_res\\total_permission_name.txt", "r") as f:
#         for line in f:
#             # print(line.replace("[","").replace("]","").split(","))
#             permission_list = line.split("[")[1].split(']')[0].split(",")
#

#     permission_list = [item.replace("'","").replace(" ","").replace("\"","") for item in permission_list]
#     permissionnum=len(permission_list)


    # Benign_permission = np.load("G:\\app_res\\Benign_permission_only.npy")
    # for i in range(0,Benign_permission.shape[0]):
    #     suoin=Benign_permission[i][0]
    #     Dic[permission_list[suoin]]=0
    # print(Dic)

    apklist = os.listdir(app_path)
    for apk in apklist:
        filename = app_path + "/" + apk
        # print(filename)
        print(apk)
        print(index)
        getAppBaseInfo(filename,index)
        print("\n")
        index+=1
    # print(Dic)

#Benign   Vir
    # np.save('G:\\app_res\\permission\\VirAPP_BenignPER.npy', Dic)

    # M=np.zeros((appnum, permissionnum))
    # print(M.shape)
    # print(M)
    #
    # dataFile = 'G:\\app_res\\Benign_permission.mat'
    # scio.savemat(dataFile, {'permission':M})



    word_sort = sorted(permission_frequency.items(), key=operator.itemgetter(1), reverse=True)
    print(word_sort)

    # for per in permission_frequency.keys():
    #     if(permission_frequency[per]>1):
    #         listres.append(per)
    #
    # with open('G:\\app_res\\permission\\Benign_permission_list.txt','w') as f:
    #     f.write(str(listres))
    #
    # with open('G:\\app_res\\permission\\Benign_permission_frequency.txt','w') as f:
    #     f.write(str(word_sort))