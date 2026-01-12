# Pneumonia Diagnosis App

A Streamlit web application for pneumonia detection from chest X-ray images using a convolutional neural network.

## Overview

This application allows users to upload chest X-ray images and receive automated pneumonia diagnosis predictions. The model is trained on the Kaggle Chest X-Ray Images dataset and provides probability scores for its predictions.

This application is created as a final project for SECB3103 (Bioinformatics II) using a modl built in SECB3203 (Programming for Bioinformatics). This is solely for educational purposes and should not be used as a substitute for professional medical diagnosis.

## Model

The model is a convolutional neural network trained on chest X-ray images. It accepts 128x128 grayscale images and outputs a binary classification (Normal vs Pneumonia).

## Dataset

Training data sourced from the Kaggle Chest X-Ray Images (Pneumonia) dataset by Paul Mooney.