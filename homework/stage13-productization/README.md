# bootcamp_Chensi_Zhang

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Predicting Apple Inc. (AAPL) stock price movements is crucial for investors, traders, and financial analysts to make informed decisions. Stock prices are influenced by a complex interplay of factors including company performance, market sentiment, macroeconomic indicators, and news events. Traditional statistical models often struggle to capture these non-linear relationships and temporal dependencies. A deep learning approach has the potential to identify complex patterns in historical data and generate more accurate forecasts, thereby providing a valuable tool for investment strategy and risk management.

## Stakeholder & User
The primary stakeholder are  quantitative analysts, algorithmic traders, and investment portfolio managers. Fund managers and individual investors who will use the predictions to inform buy/sell/hold decisions.Predictions are needed daily, ideally before the market opens. The output should be easily integratable into existing trading platforms or dashboards for real-time decision support.

## Useful Answer & Decision
Predictive (aiming for directional accuracy - predicting if the price will go UP or DOWN the next day, and the predicted closing price).
Goodness of fit (R^2) , Mean Absolute Error (MAE) or Root Mean Squared Error (RMSE) for price value prediction.
A trained deep learning model serialized for production.

## Assumptions & Constraints
Historical daily OHLCV (Open, High, Low, Close, Volume) data for AAPL is obtainable via APIs.
Model training is a one-time intensive compute task, but daily inference is lightweight.
Daily predictions do not require ultra-low latency.
The project is for research and educational purposes. Any real-world financial application must comply with relevant regulations.
The model will use a fixed historical window to predict the next day's price.

## Known Unknowns / Risks
The efficient market hypothesis suggests significant price movements might be fundamentally unpredictable, limiting maximum accuracy.
High risk of overfitting to noise in the historical data due to the stochastic nature of markets. Will be mitigated using rigorous walk-forward validation and dropout layers.
Market regimes change. Model performance will be monitored continuously for degradation, and retraining schedules will be established.
Unforeseen "black swan" events are not captured in historical data and will cause prediction errors.

## Lifecycle Mapping
Goal → Stage → Deliverable
Define Prediction Goal & Success Metrics → Problem Framing & Scoping → Project Charter (this document)
Acquire & Process Financial Data → Data Acquisition & Preparation → Cleaned, featurized dataset(s)
Develop & Train Predictive Models → Modeling & Analysis → Trained Model Files & Performance Report
Deploy Model for Daily Inference → Deployment & Integration → Prediction API/Service

## Repo Plan
/data/: Raw and processed data
/src/: Python scripts
/notebooks/: Jupyter notebooks
/docs/: Project documentation
Feature branches for development. Merge to `main` upon completion of each major stage. Daily commits encouraged.

# Data Storage

## Folder structure
data/
raw/          
processed/    

## Formats used and why
CSV	Raw data storage	Human-readable, widely compatible	Large size, no type preservation
Parquet	Processed data storage	Efficient compression, type preservation, fast queries	Binary (not human-readable)

## How your code reads/writes using env variables
Store the folder path in env, define the file name, combine the two to form a complete path, and then store and read the dataframe

# cleaing strategy

## Assumptions of the fill_missing_median Function

Numeric Data: By default, it only processes numeric columns, assuming non-numeric columns do not require filling or should be handled by other methods
Median Appropriateness: Assumes that the median is a reasonable choice for filling missing values. If the data is highly skewed or the business context requires other imputation methods , this may not be appropriate.
Column Independence: Assumes that missing value imputation for each column does not depend on other columns.

## Assumptions of the drop_missing Function

Missingness Mechanism: Assumes that missing data is random, and dropping it will not introduce bias. If missingness follows a specific pattern, deletion may distort the sample.
Threshold Selection: The threshold parameter assumes the user can set a reasonable ratio, but it does not validate whether the threshold is appropriate for the dataset size.
Column Specification: If columns are provided, it assumes missing values in these columns are critical, while missing values in other columns can be ignored.

## Assumptions of the normalize_data Function

Need for Scaling: Assumes the input data requires normalization. If the data is already standardized or does not require scaling, this step is redundant.

Method Choice:
minmax assumes clear data boundaries.
StandardScaler assumes the data is approximately normally distributed, and the mean and standard deviation are representative of the distribution.
Sensitivity to Outliers: Both methods are affected by outliers, assuming the data has been cleaned or outliers handled beforehand.

# feature definition

ln_open = log(1+open)
ln_close = log(1+close)
ln_high = log(1+high)
ln_low = log(1+low)
open/close 
high/low
