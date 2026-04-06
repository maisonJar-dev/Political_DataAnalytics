
# V-Dem Political & Economic Predictive Pipeline



**Authors:** Maison Gulyas & Erkhtuguldur Iderbat 

This project implements an end-to-end data analytics pipeline designed to predict national economic trajectories and democratic stability using the Varieties of Democracy (V-Dem) dataset. By leveraging a cloud-native architecture, we identify "Red Flags" in institutional health that serve as leading indicators for GDP per capita changes and democratic backsliding.

## Table of Contents
- [Project Overview](#project-overview)
- [Dependencies](#dependencies)
- [AWS Architecture](#aws-architecture)
- [Machine Learning Models](#machine-learning-models)
- [General Pipeline](#general-pipeline)
- [Useful Resources](#useful-resources)

## Project Overview
The core objective is to analyze why certain countries maintain democratic stability and wealth while others experience institutional decay. We utilize longitudinal data to predict outcomes three years into the future ($t+3$).

## Dependencies
- **boto3**: The AWS SDK for Python, used to programmatically interact with S3 and Lambda.
- **pandas**: Primary library for data manipulation and temporal shifting of GDP metrics.
- **scikit-learn**: Used to train Random Forest Regressors and Classifiers for predictive modeling.
- **joblib**: Essential for serializing our trained models and storing the "model brains" in S3.
- **python-dotenv**: Used to securely manage AWS IAM credentials locally without committing secrets to version control.

## AWS Architecture
- **S3 (Simple Storage Service)**: Utilizes a multi-bucket strategy. `political-eda` serves as the raw landing zone, while `cleaned-filtered-data` stores sanitized outputs and model artifacts.
- **Lambda**: A serverless compute service that automatically triggers to clean, filter, and offload specific CSV data between S3 buckets.
- **IAM (Identity and Access Management)**: Manages secure roles and permissions for team members to access the cloud resources.

## Machine Learning Models
We implement two primary Random Forest models using Scikit-Learn:
- **GDP Forecaster**: A regressor that predicts future GDP per capita with a verified $R^2$ of 0.53, identifying Regime Type and Government Effectiveness as top predictors.
- **Backsliding Sentinel**: A classifier targeting democratic crashes in the bottom 5th percentile. It provides a high-precision early warning system (67% precision), with Accountability serving as the leading "Red Flag."

## General Pipeline
1. **Ingestion**: Raw V-Dem CSV data is uploaded to the initial S3 bucket.
2. **Automated Cleaning**: AWS Lambda triggers to filter the data for the Modern Era (1945–Present) and specific institutional indicators.
3. **Predictive Modeling**: Scikit-Learn pulls "cleaned-filtered-data" to perform feature engineering, regularization, and k-fold cross-validation.
4. **Model Storage**: Trained `.joblib` artifacts are stored in S3 for persistence and collaborative use.
5. **Visualization**: Enriched results are connected to Tableau for global risk mapping and trend analysis.

## Useful Resources
- [V-Dem Dataset Official Source](https://v-dem.net/)
- [Boto3 S3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [Scikit-Learn Random Forest Guide](https://scikit-learn.org/stable/modules/ensemble.html#forest)
