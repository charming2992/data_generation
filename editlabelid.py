import os
txts = os.listdir('D:/H/THU/paper/data/Data-Generation/output/newway/fornow')  #labels所在的文件夹
for txt in txts:
    if txt.endswith('txt'):
        f = open('D:/H/THU/paper/data/Data-Generation/output/newway/fornow/'+txt, 'r')  #逐个打开txt文件
        lines = f.readlines()                                                           #读取行
        f1 = open('D:/H/THU/paper/data/Data-Generation/output/newway/labels/'+txt, 'w') #新建对应的文件

        for line in lines:
            line = '2'+ line[1:]                                                        #把第一个字改成想要的，后面的照抄
            f1.write(line)