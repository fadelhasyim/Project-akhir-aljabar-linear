

# Commented out IPython magic to ensure Python compatibility.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

img_path = 'Ainun fatwa .png'
img = cv2.imread(img_path)
print(img.shape)
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
R, G, B, = fix_img[:,:,0], fix_img[:,:,1], fix_img[:,:,2]
print(np.array(fix_img))

fix_img[:] = np.max(fix_img, axis=-1, keepdims=1)/2 + np.min(fix_img, axis=-1, keepdims=1)/2
print(np.array(fix_img[:]))

plt.axis('off')
plt.imshow(fix_img[:])
plt.savefig('Metode Lightness', bbox_inches='tight')

gray_img = np.mean(fix_img, axis=-1)
print(np.array(gray_img[:]))

plt.axis('off')
plt.imshow(gray_img, cmap='gray')
plt.savefig('Metode Lightness', bbox_inches='tight')

lumi_img = (0.2126*R) + (0.7152*G) + (0.0722*B)
print(np.array(lumi_img))

plt.axis('off')
plt.imshow(lumi_img, cmap='gray')
plt.savefig('Metode Luminosity',  bbox_inches='tight')

lumi2_img = (0.299*R) + (0.587*G) + (0.114*B)
print(np.array(lumi2_img))
plt.axis('off')
plt.imshow(lumi2_img, cmap='gray')
plt.savefig('python lumi2 gambar', bbox_inches='tight')

