# Synthetic Data Generation for Object Detection and Instance Segmentation

![Output Example](doc/images/output_example.PNG)

This code allows you to create a synthetic data-set, for Instance Segmentation or Object Detection. The [data_generation.py](data_generation.py) script outputs data in [LabelMe format](https://roboflow.com/formats/labelme-json), which can also be converted to other formats like the [COCO JSON format](https://cocodataset.org/).

 ## Installation

 1. Clone the repository 
    ```git clone https://github.com/TannerGilbert/Object-Detection-Synthetic-Data-Generation```

 2. Install dependencies
    ```
    cd Object-Detection-Synthetic-Data-Generation
    pip3 install -r requirements.txt
    ```

 ## Creating input data

 Before you can start generating your synthetic data-set, you'll have to get some input images. You'll need to kinds of input images:
 - Foreground images
 - Background images

 For background images, you can take some pictures or download them from the internet (no additional processing needed). For the foreground images, you'll have to take pictures of the object and then remove the image's background.

 I recommend labeling a few images with LabelMe and then run my [create_input_images_from_labelme.py script](create_input_images_from_labelme.py) to extract the objects. For more information check out [create_input_images_with_labelme.md](doc/create_input_images_with_labelme.md).

 You can also make use of a tool look Photoshop or GIMP.
 - [Photoshop CC 2020: How To Remove a Background (Easiest Way)](https://www.youtube.com/watch?v=DWSa5SYzZu8)
 - [5 Ways To Remove A Background with GIMP](https://www.youtube.com/watch?v=lOzSiOIipSM)

 ## Generating images

 To generate images, run the [*data_generation.py*](data_generation.py) script.

```
usage: data_generation.py [-h] --input_dir INPUT_DIR --output_dir OUTPUT_DIR
                          [--augmentation_path AUGMENTATION_PATH]
                          --image_number IMAGE_NUMBER
                          [--max_objects_per_image MAX_OBJECTS_PER_IMAGE]
                          [--image_width IMAGE_WIDTH]
                          [--image_height IMAGE_HEIGHT]

Synthetic Image Generator

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Path to the input directory. It must contain a
                        backgrounds directory and a foregrounds directory
  --output_dir OUTPUT_DIR
                        The directory where images and label files will be
                        placed
  --augmentation_path AUGMENTATION_PATH
                        Path to albumentations augmentation pipeline file
  --image_number IMAGE_NUMBER
                        Number of images to create
  --max_objects_per_image MAX_OBJECTS_PER_IMAGE
                        Maximum number of objects per images
  --image_width IMAGE_WIDTH
                        Width of the output images
  --image_height IMAGE_HEIGHT
                        Height of the output images
```

Example:
 `python data_generation.py --input_dir input/ --output_dir output/ --image_number 50`

## Converting output into other formats

If the LabelMe format doesn't work for you, you can convert the data into another format.

### Convert to COCO

You can convert the JSON files created by labelme to COCO using the [labelme2coco.py](https://github.com/Tony607/labelme2coco/blob/master/labelme2coco.py) file created by Github user [Tony607](https://github.com/Tony607).

## Inspired by / Based on

- [cocosynth](https://github.com/akTwelve/cocosynth) by [Adam Kelly](https://github.com/akTwelve)
- [cocosynth fork](https://github.com/basedrhys/cocosynth) by [Rhys Compton](https://github.com/basedrhys)
- [syndata-generation](https://github.com/debidatta/syndata-generation) by [debidatta](https://github.com/debidatta)



# 自己

## 图片准备

背景照片：自己拍摄，修改分辨率（咨询一下普渡的是最好的，拍摄视频的每一帧的图像的分辨率）

前景(目标)图片：先自己拍摄，利用labelme进行分割出来（对应的目标起好对应的名字），利用create_in...文件将其扣成前景图片（会自动生成对应的文件夹，图片是4channel的RGBA）。

## 数据生成

使用data_generation.py文件生成图片和对应的json文件（在outout_dir文件夹中，以labelme标注完的格式）

## 数据转换

上述生成的数据(图片以及对应的json文件)，使用labelme2coco.py文件将其转换成coco的数据格式，生成一个一个json文件。

再将coco格式转成yolo格式，使用coco格式的json文件作为输入，输出对应图片的txt文件和class.txt。（txt中包括标签信息和框归一化之后的四点信息）。

## 数据划分

对于训练和测试集的划分，目前可以在生成图片之后直接移动一部分作为测试集和验证集来使用。

对于下一次继续生成数据的id问题，需要接上id则需在进行修改（见代码注释）