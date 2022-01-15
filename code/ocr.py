from PIL import Image
import pytesseract
import numpy as np
import urllib.request
import pandas as pd

df_fake = pd.read_csv("./politifact_fake.csv")
df_real = pd.read_csv("./politifact_real.csv")

fake_img = df_fake["images"]
fake_text = []
print(fake_img)

for i in range(0, len(fake_img)):
    fake_img[i] = fake_img[i].replace('[', '')
    fake_img[i] = fake_img[i].replace(']', '')
    fake_img[i] = fake_img[i].replace('\'', '')
    fake_img[i] = fake_img[i].split(",")
    # print(type(fake_img[i]))


for i in range(0, 10):
    tmp = []
    for j in range(0, len(fake_img[i])):
        try:
            urllib.request.urlretrieve(
            fake_img[i][j],
            "img.png")

            img = np.array(Image.open("img.png")) 
            text = pytesseract.image_to_string(img)
            tmp.append(text)
        except:
            continue
    print(f'finished regonizing text for ${i}')
    fake_text.append(tmp)
    if (i == 0):
        print(tmp)


with open('output.txt', 'w') as f:
    for i in range(0, len(fake_text)):
        for j in range(0, len(fake_text[i])):
            f.write(fake_text[i][j])
            if (j != len(fake_text[i])-1):
                f.write(', ')
        f.write(', newline!\n')
        
