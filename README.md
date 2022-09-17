# YoloX anonymizer

We trained a YoloX model for human head detection for anonymization purposes. This repository code provides inference code to perform deidentification.

## Install

Creating a fresh conda environment is recommended:

    conda create -n yolox
    conda activate yolox

Let's start with installing a Pytorch environment:

    conda install pytorch==1.10.1 torchvision==0.11.2 cudatoolkit=11.3 -c pytorch -c conda-forge

Finally, we fetch a specific YoloX version from the Github repo:

    git clone -b 0.2.0 --single-branch https://github.com/Megvii-BaseDetection/YOLOX.git

Install the YoloX library with

    pip3 install -v -e .

## How to run
- To run the anonymization on video input:

    python infer.py video -f exp.py -c mhm_extended.pth --path test_video.mp4 --labels head --conf 0.5 --nms 0.65 --save_result --mode overlay --overlay <overlay-image>

Alternatives for `mode` are `blur`, `blacken`, `noisen`.

- To run the anonymization on a folder of images:

    python infer.py image -f exp.py -c mhm_extended.pth --path <image_folder> --labels head --conf 0.5 --nms 0.65 --save_result --mode blacken
