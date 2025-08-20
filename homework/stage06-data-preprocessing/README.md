# bootcamp_Chensi_Zhang

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Local small retailers face inefficient inventory management, leading to frequent overstocking or stockouts. This issue results in excessive capital tie-up and lost sales opportunities. By analyzing sales data and inventory turnover rates, we can help retailers optimize their inventory levels to reduce costs and improve availability.

## Stakeholder & User
The primary stakeholder is the retail store manager, who will decide whether to adopt our solution. The end users are inventory staff who will use the system daily. The solution must provide recommendations one week before monthly inventory audits.

## Useful Answer & Decision
This is a predictive analysis problem. We will deliver:optimal inventory level predictions；A dashboard displaying recommended stock levels；Key metric: Model accuracy (error rate arange)

## Assumptions & Constraints
historical sales data available;prediction updates required;Solution must run on standard laptops;External factors excluded

## Known Unknowns / Risks
Uncertain impact of promotional events on sales；Potential data quality issues；User adoption challenges
Mitigation: Analyze historical promotion data, conduct data quality checks, and test prototypes with users.

## Lifecycle Mapping
Goal → Stage → Deliverable
Define inventory optimization problem → Problem Framing & Scoping → Scoping document
Collect/process data → Data Collection & Processing → Cleaned dataset
Develop model → Modeling → Predictive model
Create interface → Deployment → Inventory dashboard

## Repo Plan
/data/: Raw and processed data
/src/: Python scripts
/notebooks/: Jupyter notebooks
/docs/: Project documentation
Weekly updates every Friday with descriptive commit messages.

# Data Storage

## Folder structure
data/
raw/          # Stores raw data (CSV format)
processed/    # Stores processed data (Parquet format)

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

