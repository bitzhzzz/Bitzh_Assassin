import os
import random
import numpy as np

#xml文件的存放地址
xmlfilter = r'./VOC_storage/VOC2021/Annotations'
#处理后文件的存放地址
savebasefilter = r'./VOC_storage/VOC2021/ImageSets'

#训练数据中推理和训练的百分比
trainval_percent = 1
#训练数据中训练的百分比
train_percent = 1

temp_xml = os.listdir(xmlfilter)
total_xml = []
for xml in temp_xml:
    if xml.endswith('.xml'):
        total_xml.append(xml)

num = len(total_xml)
list = range(num)
trainval_num = int(num*trainval_percent)
train_num = int(trainval_num*train_percent)
trainval_list = random.sample(list, trainval_num)
train_list = random.sample(trainval_list,train_num)

trainval_filter = open(os.path.join(savebasefilter,'trainval.txt'),'w')
train_filter = open(os.path.join(savebasefilter,'train.txt'),'w')
val_filter = open(os.path.join(savebasefilter,'val.txt'),'w')
test_filter = open(os.path.join(savebasefilter,'test.txt'),'w')

for i in list:
    num = total_xml[i][:-4]+'\n'
    if i in trainval_list:
        trainval_filter.write(num)
        if i in train_list:
            train_filter.write(num)
        else:
            val_filter.write(num)
    else:
        test_filter.write(num)

trainval_filter.close()
train_filter.close()
val_filter.close()
test_filter.close()