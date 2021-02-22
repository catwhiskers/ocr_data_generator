#!/usr/bin/env bash
train_count=1000

#zh
rm -rf "images/train_cn"
#trdg \
#-c $train_count -l cn -i '/home/ec2-user/SageMaker/ESD/source/data_generation/data/ZH_1.txt' -na 2 \
#-b 1 --output_dir "images/train_cn" --font_dir "./font/"

trdg \
-c $train_count -l cn -i './data/ZH_1.txt' -na 2 \
-b 1 --output_dir "images/train_cn" -ft "./setofont/setofont.ttf"

#en
rm -rf "images/train_en"
trdg \
-c $train_count -l cn -i './data/EN_1.txt' -na 2 -b 1 \
--output_dir "images/train_en" -ft "./font/Aller_Bd.ttf"

#move raw images
python convert.py

#mkdir -p ocr_train
#mkdir -p ocr_train/train 
#cp output/images/*.jpg ocr_train/train 
#cp labels.txt ocr_train/

