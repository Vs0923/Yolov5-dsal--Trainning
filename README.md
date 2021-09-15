# Yolov5-dsal--Trainning
Yolov5s trainning 
Steps for Yolov5s custom data Training
Clone the yolov5 repo from:https://github.com/DeepSightAILabs/yolov5
Setup the Environment using pip install -r requirements.txt
Now download the dataset from: https://drive.google.com/drive/folders/1l9Z3Cnr_BPeCKcNkkaZsv77IT1o-Ro-V
Divide the dataset into train and val folder in 90:10 ratio and name the directory train_data containing train and val folder
Create the custom_data.yaml file with paths for the train and val folder and no.of classes with the class name 
Place the custom_data.yaml file in data folder of yolov5.
Now run the train.py for training specifying the batch size and epoch.
Check the accuracy map and all
The results and confusion matrix obtained will be in run folder of yolov5.
