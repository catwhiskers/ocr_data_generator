# -*- coding: utf-8 -*-
# @Time    : 11/4/20 4:03 PM
# @Author  : Jackie
# @File    : convert.py
# @Software: PyCharm
import os
from shutil import copyfile
from sys import exit
import sys 
import json


def convert(input_folder,output_folder,prefix, label_f):
    global all_files
    file_ls = os.listdir(input_folder)
    txt_file = os.path.join(input_folder,'labels.txt')
    f = open(txt_file, 'r')
    res = f.readlines()
    f.close()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img_ls = [i.split(' ')[0] for i in res]
    label_ls = [' '.join(i.split(' ')[1:]).replace('\n','') for i in res]
    name_ls = [' '.join(i.split(' ')[1:]).replace('\n','.jpg') for i in res]
    
    # adding exception handling
    for i in range(len(img_ls)):
        try:
            filename = str(all_files)+".jpg"
            copyfile(os.path.join(input_folder,img_ls[i]),os.path.join(output_folder,filename))
            label_f.write(prefix+"/"+filename+"\t"+label_ls[i]+"\n")
            all_files += 1 
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)

    # generate dictionary
    label = ''.join(label_ls)

    # return max length
    len_ls = [len(i)-4 for i in name_ls]
    return max(len_ls), label

def _string_to_json_file(string, string2, dict_file):
    ids = list(string+string2)
    #unique
    ids = list(set(ids))
    #d = {i: ids[i] for i in range(len(ids))}
    #print (d)
    for i in ids:
        dict_file.write(str(i)+'\n');
    dict_file.close()

    print ("<<<save dictionary file")

all_files = 0 
import shutil 
if __name__ == '__main__':
    
    output_folder='./ocr_data/'
    shutil.rmtree(output_folder)
    os.mkdir(output_folder)
    prefix = "train"
    img_output_folder = os.path.join(output_folder, prefix)
    os.mkdir(img_output_folder)
    label_f = open(os.path.join(output_folder, "train.txt"), 'w')
    input_folder_en='./images/train_en'
    input_folder_cn='./images/train_cn'
    
    print ("<<<< move folder for en")
    len_en, label_en = convert(input_folder_en,img_output_folder, prefix, label_f)
    print ("<<<< move folder for cn")
    len_cn, label_cn= convert(input_folder_cn,img_output_folder, prefix, label_f)
    print ("<<<<max length: ", max(len_en,len_cn))
    dict_file=open(os.path.join(output_folder, "dictionary.txt"),'w')
    _string_to_json_file(label_en,label_cn, dict_file)

