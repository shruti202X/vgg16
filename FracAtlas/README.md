# FracAtlas

## About the database

This database has 4083 images.

Out of this 3366 images are not fractures images and 717 are fractured images.

These fractured images have a fracture count associated with it. It ranges between 1 to 5 and it is 0 for non fractured images.

## Python Code to extract image files:

```python
import os
import cv2

countt=0
fracture = []
nonfrac = []
for dirname, _, filenames in os.walk('/kaggle/input/fracatlas/FracAtlas/images/Fractured'):
    for filename in filenames:
        img_path  = os.path.join(dirname,filename)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(256,256))
        fracture.append(img)
        countt+=1
        if countt==50:
            break

countt = 0
for dirname, _, filenames in os.walk('/kaggle/input/fracatlas/FracAtlas/images/Non_fractured'):
    for filename in filenames:
        img_path  = os.path.join(dirname,filename)
        try:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = cv2.resize(img,(256,256))
            if img is not None:
                nonfrac.append(img)
                countt+=1
                if countt==50:
                    break
        except:
            print(f"Error processing image {img_path}")
```

