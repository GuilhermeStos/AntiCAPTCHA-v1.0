# Importando a biblioteca OpenCV
import cv2

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

i = 0
imgs = []
for i in range(6):
    imgs.append(cv2.imread(f"C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot{i}.png"))

img = concat_tile([[imgs[5], imgs[0]],
                   [imgs[1], imgs[2]], 
                   [imgs[3], imgs[4]]])
# temp_img1 = cv2.vconcat([img1, img3, img5])
# temp_img2 = cv2.vconcat([img2, img4, img6])
# img = cv2.hconcat([temp_img1, temp_img2])
cv2.imwrite("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screen.png", img)