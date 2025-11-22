import cv2
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
image = cv2.imread(r"D:\SEM 3\PWP\MU.jpg")
padded_image = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])
cv2.imwrite('padded_image.jpg', padded_image)
padded_image_rgb = cv2.cvtColor(padded_image, cv2.COLOR_BGR2RGB)
plt.imshow(padded_image_rgb)
plt.axis('off')
plt.show()

