# Full Python Code
import os
import json

try:
    import torch
    import torchvision
    import PIL
    import tensorflow
except:
    os.system("""pip install torch torchvision pillow tensorflow matplotlib prefetch_generator""")
os.system('cd C:/Users/vatdu/Desktop/test')
os.system("""pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" git+https://github.com/NVIDIA/apex.git@master""")
input("CHECK WHETHER APEX LIBRARY HAS BEEN INSTALLED WITHOUT ERRORS")

os.system("""pip install git+https://github.com/Maluuba/nlg-eval.git@master""")
os.system("""nlg-eval --help""")
input("CHECK WHETHER nlg-eval LIBRARY HAS BEEN INSTALLED WITHOUT ERRORS")

os.system("""mkdir .\\data""")
os.system("""mkdir .\\data\\visual-genome""")
os.system("""mkdir model_params""")
os.system("""git clone https://github.com/soloist97/densecap-pytorch.git""")
os.system("""xcopy /E /I densecap-pytorch\\* .\\""")
os.system("""copy densecap-pytorch\\*.* .\\""")
os.system("""rmdir /s /q densecap-pytorch""")

# DOWNLOAD DATASET FROM https://www.kaggle.com/datasets/dannywu375/visualgenome
os.system("""pip install opendatasets --upgrade""")
import opendatasets as od
print('-'*100)
print("MESSAGE\n")
print("ENTER THE FOLLOWING CREDENTIALS INTO THE INPUT FIELDS")
print("Username:  vatsaldutt")
print("Key:       1fa843f5755cdc1ed7c26b40307059d6")
print('-'*100)
dataset_url = 'https://www.kaggle.com/datasets/dannywu375/visualgenome'
od.download(dataset_url)

# Download from https://web.archive.org/web/20220629013958/https://visualgenome.org/static/data/dataset/region_descriptions.json.zip
download = input("Do you want to download the region_descriptions.json file [y/n]: ").lower()
if 'y' in download:
    os.system("""wget https://web.archive.org/web/20220629013958/https://visualgenome.org/static/data/dataset/region_descriptions.json.zip""")
    os.system("""unzip region_descriptions.json""")
    try:
        with open('region_descriptions.json', 'r') as file:
            print(str(json.load(file))[0:500])
        print('-'*100)
        print("MESSAGE\n")
        print("FILE SUCCESSFULLY DOWNLOADED")
        print('-'*100)
    except:
        print('-'*100)
        print("MESSAGE\n")
        print("ERROR DOWNLOADING FILE FOR REGION DESCRIPTIONS")
        print("PLEASE MANUALLY DOWNLOAD THE FILE FROM https://web.archive.org/web/20220629013958/https://visualgenome.org/static/data/dataset/region_descriptions.json.zip AND PUT IT INSIDE THIS DIRECTORY")
        print("DIRECTORY PATH: ", end='')
        os.system('cd')
        print('-'*100)
        input("PRESS ENTER WHEN DONE")
    os.system("""copy region_descriptions.json .\\data\\visual-genome""")
    os.system("""del region_descriptions.json region_descriptions.json.zip""")
else:
    print('-'*100)
    print("MESSAGE\n")
    print("MANUALLY PUT THE region_descriptions.json FILE IN ./data/visual-genome/ FOLDER")
    print("DOWNLOAD LINK: https://web.archive.org/web/20160603225350/https://visualgenome.org/static/data/dataset/region_descriptions.json.zip")
    print('-'*100)
    input("PRESS ENTER WHEN DONE")
    os.system("""copy region_descriptions.json .\\data\\visual-genome""")
    os.system("""del region_descriptions.json region_descriptions.json.zip""")

os.system("""xcopy /E /I .\\visualgenome\\images .\\data\\visual-genome""")
os.system("""xcopy /E /I .\\visualgenome\\images2 .\\data\\visual-genome""")
os.system("""copy .\\visualgenome\\image_data.json\\image_data.json .\\data\\visual-genome""")
os.system("""rmdir /s /q visualgenome""")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('.\\data\\visual-genome\\VG_100K\\107922.jpg')
imgplot = plt.imshow(img)
plt.show()

os.system("""python preprocess.py""")

os.system("""python train.py""")