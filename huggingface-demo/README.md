---
title: Vietnamese Sign Language Classification
emoji: 🤟
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# Vietnamese Sign Language Classification

This is a demo application for classifying Vietnamese Sign Language hand gestures using a MobileNet-based deep learning model.

## Model

- Architecture: MobileNet
- Input size: 224x224 RGB images
- Output: 25 classes (A-Z excluding J)
- Framework: TensorFlow/Keras

## Usage

1. Upload an image of a Vietnamese Sign Language hand gesture
2. The model will predict the letter and show confidence scores for top 5 predictions

## Examples

The demo includes sample images for letters C, E, P, and T.

## Performance

The model is optimized for mobile deployment with MobileNet architecture, providing fast inference while maintaining good accuracy.
