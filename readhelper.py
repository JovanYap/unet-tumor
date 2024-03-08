import glob
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
def read_img(img_path):
    return sitk.GetArrayFromImage(sitk.ReadImage(img_path))

t1 = glob.glob("./BraTS_segmentation/*/*t1.nii.gz")
img = (read_img(t1[0])[100]).astype(np.uint8)
plt.imshow(img)
plt.show(block=False)