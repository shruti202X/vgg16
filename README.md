# VGG16 Transfer Learning Project

This project demonstrates the use of VGG16, a pre-trained convolutional neural network, for transfer learning.

The full code can be accessed [here](https://github.com/shruti202X/vgg16/blob/main/FracAtlas/TransferLearning/vgg-model-9.ipynb).

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Model Architecture](#model-architecture)
4. [Results](#results)

## Introduction

Developed by the Visual Geometry Group at the University of Oxford, VGG16 stands out for its straightforward architecture, comprising 16 weight layers, hence the nomenclature. These layers include 13 convolutional layers followed by 3 fully connected layers, forming a deep neural network capable of extracting intricate features from input images.

At its core, VGG16 employs a series of small 3x3 convolutional filters with a stride of 1 pixel and a padding of 1 pixel, facilitating the preservation of spatial information throughout the network. By utilizing such small filters, VGG16 achieves a deeper network architecture while maintaining a manageable number of parameters. Additionally, max-pooling layers interspersed between convolutional blocks serve to down-sample feature maps, enhancing computational efficiency and reducing overfitting.

img here!!

One of the defining characteristics of VGG16 is its homogeneity in architecture, where each convolutional block comprises multiple convolutional layers followed by a max-pooling layer. This uniformity simplifies model design and fosters interpretability, making VGG16 an attractive choice for researchers and practitioners alike. Furthermore, the availability of pre-trained weights on large-scale image datasets such as ImageNet has accelerated its adoption and facilitated transfer learning, enabling the model to be repurposed for various image recognition tasks with minimal data requirements.

In the following discourse, we delve deeper into the architecture and workings of VGG16, exploring its applications across diverse domains ranging from object recognition in natural images to medical image analysis.

## Dataset

For this project, we are using [Fracatlas Dataset](https://www.kaggle.com/datasets/tommyngx/fracatlas/data). Having 3366 non-fractured and 717 fractured images.

## Model Architecture

The VGG16 model is a 16-layer deep convolutional neural network, pre-trained on ImageNet. In this project, we:
- Remove the fully connected layers.
- Add custom dense layers for fine-tuning to adapt to the specific dataset.

## Result

The fine-tuned VGG16 model achieved an accuracy of 80.8% on the test set after 26 epochs.
