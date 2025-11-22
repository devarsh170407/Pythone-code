import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r"D:\SEM 3\PWP\MU.jpg")
blue, green, red = cv2.split(image)
plt.subplot(131), plt.imshow(red, cmap='gray'), plt.title('Red')
plt.subplot(132), plt.imshow(green, cmap='gray'), plt.title('Green')
plt.subplot(133), plt.imshow(blue, cmap='gray'), plt.title('Blue')
plt.show()


