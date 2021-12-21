#使用之前必须读说明书#

///////////////////
图片标动的说明书
///////////////////
需要创建3个文件
Annotations：存放标定后的数据
JPEGImages：存放训练图片的文件
photo：存放标定的图片

标注步骤
1、打开anaconda  Prompt
2、使用命令conda activate 环境（激活编译环境），打开环境后使用命令conda install labelimg（下载标注的工具）
3、安装完成后，在相应的环境下使用命令labelimg（打开标注工具）
4、在标注工具中点击Open Dir打开photo进行标注,点击Change Save Dir选择存放标定后数据   注：标注前开启View中的Auto Save mode
快捷键：（1）按w+鼠标左键圈出标定的位置 
             （2）使用A和D进行图片的切换
5、标注完后将photo的图片放入JPEGImages中

////////////////////////////
VOC格式处理说明书配例程
////////////////////////////

训练所需要的3个文件
Annotations：存放标定后的数据
JPEGImages：存放训练图片的文件
ImageSets: 存放训练和测试的数据
（1）trainval.txt:训练所需要的训练数据和推理数据集
（2）train.txt: 训练数据
（3）val.txt:推理数据
（4）test.txt:测试数据

处理数据步骤
1、创建VOC_storage文件存放ImageSets、JPEGImages和ImageSets
2、执行VOC_FirstFution.py生成对应的txt
3、再运行VOC_SecendFution.py，运行前需要将classes改成你自己的classes。
4、就会生成对应的2021_train.txt，每一行对应其图片位置及其真实框的位置