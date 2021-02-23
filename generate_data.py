import os 
import shutil

from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)


def get_strings(file_name): 
    f = open(file_name, 'r')
    results = []
    for l in f.readlines():
        if l and l.strip():
            results.append(l.strip())
    return results
        

def get_fonts(font_dir):
    onlyfiles = [os.path.join(font_dir, f) for f in os.listdir(font_dir) if os.path.isfile(os.path.join(font_dir, f))]
    return onlyfiles
    


def get_training_data_img_and_labels(string_file, font_dir, output_folder, img_prefix, limit=1000): 
    strings = get_strings(string_file)
    fonts = get_fonts(font_dir)
    print(strings)
    print(fonts)
    generator = GeneratorFromStrings(
        strings,
        fonts = ['setofont/setofont.ttf'], 
        blur=2,
        random_blur=True
    )
    labels = [] 
    i = 0 
    for img, lbl in generator:
        if i<=limit: 
            file_name = os.path.join(output_folder, img_prefix, str(i)+".jpg")
            img.save(file_name)
            labels.append((lbl, file_name))
            i+=1 
        else: 
            break

    label_file = open(os.path.join(output_folder, "train.txt"), 'w')
    for l in labels: 
        line = '\t'.join(l)
        label_file.write(line)
        label_file.write('\n')

        
output_folder='./ocr_data/'
shutil.rmtree(output_folder)
os.mkdir(output_folder)
prefix = "train"
os.mkdir(os.path.join(output_folder, prefix))
get_training_data_img_and_labels('data/ZH_1.txt', 'setofont', output_folder, prefix)    






