# Yolov5-dsal--Trainning
**Yolov5s weight conversion to tflite.**

**Steps to convert yolov5 weight file last.pt to tflite weight file best.tflite**
1. First we need to change yolov5 weight file to .pb format for that we need tf.py file to be placed in models folder.


2. Now run the command with the last.pt weight file path:

 PYTHONPATH=. python3  models/tf.py --img 640 --weights /home/dsalguradv1050ti/yolov5/runs/train/exp14/weights/last.pt --cfg models/yolov5s.yaml --tf-nms

3. Will get the saved_model folder at the same path of yolov5s last.pt path 
4. Now run tfliteconversion.py file to get the best.tflite file (tflite weight file)


