import xml.etree.ElementTree as ET
from os import getcwd

sets = [('2021','train'),('2021','test'),('2021','val')]
#获取文件的绝对路径
wd = getcwd()
classes = ['paper']


def function(year, image_id,list_file):
    in_file = open('VOC_storage/VOC%s/Annotations/%s.xml'%(year,image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    if root.find('object') == None:
        return
    list_file.write('%s/VOC_storage/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
    for obj in root.iter('object'):
        cls = obj.find('name').text
        difficult = obj.find('difficult').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        bndbox = obj.find('bndbox')
        b = (int(bndbox.find('xmin').text),int(bndbox.find('ymin').text),int(bndbox.find('xmax').text),int(bndbox.find('ymax').text))
        list_file.write(' '+','.join([str(a) for a in b])+','+str(cls_id))
    list_file.write('\n')




for year, image_set in sets:
    image_ids = open('VOC_storage/VOC%s/ImageSets/%s.txt'%(year, image_set)).read().strip().split()
    print(image_ids)
    list_file = open('%s_%s.txt'%(year,image_set),'w')
    for image_id in image_ids:
        function(year, image_id, list_file)
    list_file.close()