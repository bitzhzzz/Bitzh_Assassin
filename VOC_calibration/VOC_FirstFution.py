import os
import random
import numpy as np

xmlfilter = r'./VOC_storage/VOC2021/Annotations'
savebasefilter = r'./VOC_storage/VOC2021/ImageSets'

trainval_percent = 1
train_percent = 1

temp_xml = os.listdir(xmlfilter)

total_xml=[]
for xml in temp_xml:
    if xml.endswith('.xml'):
        total_xml.append(xml)

num = len(total_xml)
list =range(num)

trainval_num = int(num*trainval_percent)
train_num = int(trainval_num*train_percent)

trainval_list = random.sample(list, trainval_num)
train_list = random.sample(trainval_list,train_num)

trainval_filters = open(os.path.join(savebasefilter,'trainval.txt'),'w')
train_filters = open(os.path.join(savebasefilter,'train.txt'),'w')
val_filters = open(os.path.join(savebasefilter,'val.txt'),'w')
test_filters = open(os.path.join(savebasefilter,'test.txt'),'w')

for i in list:
    name = total_xml[i][:-4]+'\n'
    if i in trainval_list:
        trainval_filters.write(name)
        if i in train_list:
            train_filters.write(name)
        else:
            val_filters.write(name)
    else:
        test_filters.write(name)

trainval_filters.close()
train_filters.close()
val_filters.close()
test_filters.close()