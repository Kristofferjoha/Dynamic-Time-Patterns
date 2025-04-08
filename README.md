# knn-forecasting-algorithm

A k-Nearest Neighbors (kNN) forecasting model for predicting standardized EMA returns.

This project provides an educational walkthrough of using the K-Nearest Neighbors (KNN) algorithm for time series forecasting. The core focus is on implementing, explaining, and comparing the impact of different **distance metrics** commonly used for sequential data:

*   Euclidean Distance
*   Dynamic Time Warping (DTW)
*   Mean Squared Error Distance (MSED)
*   Complexity-Invariant Distance (CID)

The Jupyter Notebook (`Dynamic_Time_Patterns.ipynb`) uses smoothed and standardized 5-minute GBP/USD Forex data as a practical example to illustrate these concepts, evaluate their performance, and demonstrate hyperparameter tuning.

## Key Features & Concepts Covered:

*   **KNN for Time Series:** Detailed explanation of the KNN algorithm adapted for forecasting sequential data.
*   **Distance Metrics:** In-depth implementation and mathematical breakdown of the four key distance metrics listed above.
*   **Data Preprocessing:** Demonstration of common time series preprocessing techniques:
    *   Log Returns Calculation
    *   Exponential Moving Average (EMA) Smoothing
    *   Rolling Window Standardization
*   **Forecasting & Evaluation:**
    *   Implementation of a KNN forecasting function using different metrics.
    *   Visualization of actual vs. predicted values and forecast residuals.
    *   Quantitative performance evaluation using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
    *   Discussion of relative and absolute forecast accuracy.
*   **Hyperparameter Tuning:**
    *   Demonstration of a manual Grid Search setup to optimize `window_size`, `embed_size`, and `k`.
    *   Presentation and discussion of optimized parameters and performance improvement (with significant runtime warnings).
*   **Reproducibility:** Implementation of a "Load or Compute" strategy using a pre-computed results file (`knn_predictions.csv`) to allow fast exploration of the analysis by default.

## The Notebook

The main content is within the Jupyter Notebook:

*   [`Dynamic_Time_Patterns.ipynb`](Dynamic_Time_Patterns.ipynb)

This notebook covers all the steps from data loading and preprocessing, through the theory and implementation of KNN and distance metrics, to visualization, evaluation, and hyperparameter optimization setup.

The code blocks have already been executed, showing the results and iterations of the grid search. You can modify the parameters and run it yourself, though it may take a long time depending on the parameters chosen.

- ## Inspiration
The initial exploration for this project drew inspiration from the concepts discussed in [Machine Learning Dynamic Time Patterns in Algorithmic Trading](https://www.linkedin.com/pulse/machine-learning-dynamic-time-patterns-algorithmic-trading-nikolaev/) by Nikolaev, although the focus shifted towards a detailed educational comparison of distance metrics rather than a direct trading application.

I also just wanted to learn more about subjects like preprocessing, distance metrics, error metrics, etc... which is why i made it "educational", where i explain the math behind everything.
