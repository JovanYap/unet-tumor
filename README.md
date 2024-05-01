# Brain Tumor Segmentation using 3D U-Net on MRI Scans
## Overview
This [project](./Project%20Report.pdf) focuses on the accurate segmentation of brain tumors from MRI scans, a critical step for advancing diagnostic and therapeutic approaches in neuro-oncology. Utilizing the powerful 3D U-Net architecture, this study aims to enhance segmentation accuracy and provide reliable quantification of brain tumors. The model leverages the BRATS dataset, incorporates data augmentation strategies to address class imbalance, and employs advanced filters and feature extraction techniques. 

## Objective
To develop a robust 3D U-Net model that improves brain tumor segmentation accuracy, comparing its performance against 2D U-Net and investigating the efficacy of model ensembling and potential integrations with cutting-edge models like UnetFormer and MedSegDiff.

## Dataset
This project uses the BRATS 2021 dataset, which includes a diverse array of MRI images, facilitating a comprehensive training regime that underscores the significance of extensive and varied training data.

## Features
- Extensive Preprocessing: Streamlining data for optimal neural network performance.
- Data Augmentation: Mitigating the issue of class imbalance to enhance model generalizability.
- Advanced Filtering and Feature Extraction: Refining inputs to improve model outcomes.
- Comparative Analysis: Evaluating 2D and 3D U-Net models and exploring the benefits of model ensembling.
- Performance Metrics: Rigorous accuracy assessments to gauge model effectiveness.

## Installation and Usage
Detailed instructions on setting up the environment, installing dependencies, and running the project are included in the jupyter notebooks in this github repo or alternatively it can be downloaded through the linked Google Drive folder:
- [Code files](https://drive.google.com/drive/folders/1VyDjyxmIOIqtz3fJIiDmQX-El107EVYy)

## Results
Initial findings indicate superior performance of the 3D U-Net models trained on the BRATS 2021 dataset, highlighting the project's potential as a significant contribution to the field of medical imaging and artificial intelligence.

## Credits
- Team Members:
    - Jovan Yap
    - Xu Boyu
    - Duan Lingbo
    - Kai Chan
    - Shu Bohan

## References
- [UNetFormer: A Unified Vision Transformer Model and Pre-Training Framework for 3D Medical Image Segmentation](https://paperswithcode.com/paper/unetformer-a-unified-vision-transformer-model)
- [Brain Tumor Segmentation Using an Ensemble of 3D U-Nets and Overall Survival Prediction Using Radiomic Features](https://www.frontiersin.org/articles/10.3389/fncom.2020.00025/full)
- [BRATS Dataset 2020](https://www.med.upenn.edu/cbica/brats2020/data.html)
- [BRATS Dataset 2021](http://braintumorsegmentation.org/)
