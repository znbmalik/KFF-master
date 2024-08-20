To extract 3-channel key flow frames from video and trained using a 3D convolutional neural networks to recognize human activity this code is based on flow_toolbox-master (to extract 3-channel Brox algorithm-based flow frames), KFF-algorithm (to extract 3-channel key flow frames (KFF) and ltc-master (to recognize human action through processing KFF using a 3D CNN-based models). 

For the execution of mentioned steps, three different environments have been used which can be pulled using following pull request.

1. docker pull dockerhubznb/phd:opencv3_cuda9_tensorflow_v1

2. docker pull dockerhubznb/phd:rapidsai-22.12-cuda11.5-runtime-ubuntu18.04-py3.9-v1

3. docker pull dockerhubznb/phd:mauvilsa-torch-cuda9.2-ubuntu16.04-v1



## **Extract 3-Channel Optical flow Frames**

download UCF50 dataset from "https://www.crcv.ucf.edu/data/UCF50.php" 
download JHMDB dataset from "http://jhmdb.is.tue.mpg.de/challenge/JHMDB/datasets" and place under
download Penn Action dataset from "https://dreamdragon.github.io/PennAction" and place under

and place under KFF-LTC-master/WT/my_model/my_data

Execute the following command to execute docker container

sudo docker run --gpus all -it -v /KFF-LTC-master:/home -p 9991:9999 -p 8521:8888 dockerhubznb/phd:opencv3_cuda9_tensorflow_v1  bash

cd home/WT/my_model/my_Scripts/flow_toolbox-master

run python3 computeBroxFlows.py

Above code will create a directory "UCF50-OP/flows/jpg" in my_data containing 3-channel optical flow frames for each video within each action category.


Do the same for JHMDB and Penn action dataset. For these dataset we need to change the path in computeBroxFlows.py that is available in home/WT/my_model/my_Scripts/flow_toolbox-master


## **Extract 3-channel key flow frames**

Execute the following command to execute docker container

sudo docker run --gpus all --rm -it -v /KFF-LTC-master:/rapids/notebooks/host/home -p 8520:8888 -p 8787:8787 -p 8786:8786 rapidsai/rapidsai:22.12-cuda11.5-runtime-ubuntu18.04-py3.9-v1 

cd home/WT/my_model/my_Scripts/keyframe

run python3 imageClusteringUsingCuML.py

Above code will create a directory "UCF50-OP/key_flows/jpg" in my_data containing 3-channel key flow frames for each video within each action category.

rename key-flow images to be in sequence, execute "home/WT/my_model/my_Scripts/keyfrmae/renameKeyFlows.py" 



## **Prepare Data for training using 3D-CNN**

Copy "../../my_data/UCF50-OP/key_flows/jpg" to /home/ltc-master/datasets as UCF50/rgb/jpg

Execute ltc-master/preprocessing/preprocess_rgb.lua to generate t7 files

create folder splits in /home/ltc-master/datasets/UCF50 and then from ltc-master/preprocessing execute split.m and then rgb_new_generate_sliding_test_clips.m



## **Train LTC-model with 16 initial Key flow frames**

Execute the following command to execute docker container

sudo docker run --gpus all -it -v /home/facial/znb/Zainab-Code/ltc-master:/home -p 8522:8888 -p 8001:8000 -p 16007:6006 dockerhubznb/phd:mauvilsa-torch-cuda9.2-ubuntu16.04-v1   bash

cd home/ltc-master

run to train

th  main.lua -nFrames 16  -loadHeight 128 -loadWidth 171 -sampleHeight 112 -sampleWidth 112 -stream rgb -expName rgb_16f_d5 -dataset UCF50 -netType ltc-batch -batchSize 30 -slide 4 
-evaluate -modelNo 17

run to test
th  main.lua -loadHeight 128 -loadWidth 171 -sampleHeight 112 -sampleWidth 112 -stream rgb -expName rgb_16f_d5 -nFrames 16 -dataset UCF50 -slide 4 -evaluate -modelNo 17

run to continue training

th  main.lua -nFrames 16  -loadHeight 128 -loadWidth 171 -sampleHeight 112 -sampleWidth 112 -stream rgb -expName rgb_16f_d5 -dataset UCF50 -dropout 0.5 -batchSize 30 -LRfile LR/UCF101/rgb_d5.lua -continue -epochNumber 5
