import cv2

img = cv2.imread('assets/nature.jpeg', -1)

print(img.shape)

tag = img[100:200, 200:300]
img[239:339, 350:450] = tag

# set top half to negative
# for i in range(int(img.shape[0]/2)):
#     for j in range(img.shape[1]):
#         r_val = 255 - img[i][j][2]
#         g_val = 255 - img[i][j][1]
#         b_val = 255 - img[i][j][0]
#         img[i][j] = [b_val, g_val, r_val]

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(4):
    cv2.waitKey(1)

quit()