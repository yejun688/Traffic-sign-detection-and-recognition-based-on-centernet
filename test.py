import cv2
import json
import os

# img_dir = "/media/mingxuzhu/Extreme SSD/programm_design/vehicleKeyPointsDetection/data/images"
# img_list = os.listdir(img_dir)
# print(img_list)
#
# for img_path in img_list:
#     raw_path = img_path
#     img_path = img_dir + "/" + img_path
#     img = cv2.imread(img_path)
#     img = cv2.resize(img,(832,448))
#     #print(img)
#     cv2.imwrite("/media/mingxuzhu/Extreme SSD/programm_design/vehicleKeyPointsDetection/data/my_data/"+raw_path,img)
res = json.load(open("/media/mingxuzhu/Extreme SSD/programm_design/vehicleKeyPointsDetection/data/zhuban.json"))
for anno in res:
    for one_anno in anno["annotations"]:
        one_anno['x'] = one_anno['x'] * (832.0 / 1920)
        one_anno['y'] = one_anno['y'] * (448.0 / 1080)
        one_anno['width'] = one_anno['width']* (832.0 / 1920)
        one_anno['height'] = one_anno['height'] * (448.0 / 1080)
f = open("zhuban_448_832.json","w")
json.dump(res,f,indent=4)
