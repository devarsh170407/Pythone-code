import cv2
image = cv2.imread(r"D:\SEM 3\PWP\MU.jpg")
height, width, channels = image.shape
min_pixel_value_B = image[:, :, 0].min()
print(f"Dimensions: {width}x{height}, Channels: {channels}")
print(f"Min pixel value at channel B: {min_pixel_value_B}")