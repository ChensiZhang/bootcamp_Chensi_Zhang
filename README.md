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
