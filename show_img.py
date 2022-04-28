import numpy as np
import matplotlib.pyplot as plt

img = np.load('images/323528_491000_427521_26200_155877_227741_263288.npy',allow_pickle=True)
B, H, W, C = img.shape

fig = plt.figure(figsize=(8,8))

for i in range(B):
    fig.add_subplot(1, 7, i)
    plt.imshow(img[i])
plt.show()
