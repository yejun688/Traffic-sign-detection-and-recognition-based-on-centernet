
train step:
python main.py --dataset coco ctdet --exp_id traffic_debug --arch res_18  --num_epochs 100 --lr_step 45,60

inference step:
python demo.py --dataset coco ctdet --demo /home/mingxuzhu/test_imgs --arch res_18 --load_model ../exp/ctdet/traffic_debug/model_100.pth --show_new_bbox

eval step:

