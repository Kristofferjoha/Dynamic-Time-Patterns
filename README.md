# knn-dtw-algorithm

A k-Nearest Neighbors (kNN) forecasting model for forex trading based on standardized EMA returns.

This project implements a trading algorithm that predicts forex returns using historical patterns. It leverages multiple distance metrics—ASD, CID, DTW, and Euclidean—to compare time series embeddings, making it a robust tool for analyzing GBP/USD 5-minute data.

## Highlights
- GBP/USD 5-minute forex prices from 2021.
  - USD/DKK 5-minute forex prices from 2024.
  - Sourced from [histdata.com](https://www.histdata.com/) via MetaTrader.
- **Method**: kNN forecasting with custom embeddings and distance metrics.
- **Goal**: Predict standardized EMA returns for time series forecasting.

- ## Notebook about the algorithm
[`Dynamic_Time_Patterns.ipynb`](Dynamic_Time_Patterns.ipynb), which includes:
- preprocessing
- Math behind algorithms.
- Full implementation and results.

- ## Inspiration
The inspiration for this project comes from [Machine Learning Dynamic Time Patterns in Algorithmic Trading](https://www.linkedin.com/pulse/machine-learning-dynamic-time-patterns-algorithmic-trading-nikolaev/) by Nikolaev.
