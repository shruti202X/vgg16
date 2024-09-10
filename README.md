# VGG16 Transfer Learning Project

This project demonstrates the use of VGG16, a pre-trained convolutional neural network, for transfer learning.

The full code can be accessed using [this](https://github.com/shruti202X/vgg16/blob/main/FracAtlas/TransferLearning/vgg-model-9.ipynb) jupyter notebook.

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

We used the 13 convolutional layers of VGG16 for feature extraction and replace the fully connected layers with a custom head tailored for binary classification. The custom layers added are as follows:

- **Global Average Pooling**: This layer summarizes the presence of features across the spatial dimensions.
- **Dense Layer**: A fully connected layer with 128 units, using the ReLU activation function. A kernel regularizer (l2) is applied to prevent overfitting.
- **Dropout Layer**: To prevent overfitting, a dropout layer is added with a 50% dropout rate, randomly setting half of the neurons to zero during each training step.
- **Output Layer**: A single neuron with a sigmoid activation function is used for binary classification.

## Result

The fine-tuned VGG16 model achieved an accuracy of 80.8% on the test set after 26 epochs.
