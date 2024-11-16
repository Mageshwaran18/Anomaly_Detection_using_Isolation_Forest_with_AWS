# 🔍 Anomaly Detection using Isolation Forest with AWS

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📋 Overview

A robust, cloud-based anomaly detection system leveraging the Isolation Forest algorithm and AWS services. This solution provides real-time identification of unusual patterns and outliers in large-scale datasets.

## 🌟 Key Features

- Real-time anomaly detection using Isolation Forest
- Scalable data processing with AWS Lambda
- Model deployment through AWS SageMaker
- Secure data storage using AWS S3
- Automated pipeline for continuous monitoring
- Interactive dashboards for visualization

## 🚀 Getting Started

Data Source: [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)

## 🏗️ Architecture

```plaintext
┌─────────────┐     ┌──────────┐     ┌────────────┐     ┌───────────┐
│   Data      │────>│   AWS    │────>│    AWS     │────>│    AWS    │
│   Source    │     │    S3    │     │  Lambda    │     │ SageMaker │
└─────────────┘     └──────────┘     └────────────┘     └───────────┘
                                           │
                                           ▼
                                    ┌────────────┐
                                    │  Anomaly   │
                                    │ Detection  │
                                    └────────────┘
