# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Problem: Predict stock closing price.Goal: Build an accurate LSTM model for forecasting and trading decisions.Constraints: Limited to price/volume data; requires GPU for training; has automatic failure safeguards.Assumptions: Historical patterns will repeat; markets are somewhat predictable; no unexpected market crashes. | Scoping Challenges: Balancing model complexity with deployment simplicity.Competing Objectives: High accuracy vs. low latency; full automation vs. risk control.Ambiguity: Defining "good enough" performance; unclear regulatory boundaries for automated trading. | Resolved Scope: Prioritized core prediction pipeline first (data→model→prediction), deferred advanced features like real-time execution.Defined Success Metrics: Primary: Directional accuracy >55% (beats random);Secondary: RMSE <30% of price volatility;Guardrail: Auto-rollback if accuracy drops >20% from baseline| Anchor to Business Value: Define success as "percentage of models generating alpha" not just accuracy metrics.Phase Objectives: Split into "MVP (minimum viable prediction)" and "V2 (live trading integration)".Constraint Mapping: Explicitly link technical limits (e.g., GPU memory) to max model size/sequence length.Uncertainty Budget: Quantify acceptable error margins for different market regimes upfront.|
| **2. Tooling Setup** | Data: pandas, NumPy;ML: TensorFlow/Keras, scikit-learn | CUDA/GPU Compatibility: TensorFlow-CUDA version mismatches caused training failures.Dependency Conflicts: scikit-learn and pandas version upgrades broke preprocessing logic. | Standardized Environment;Resource Optimization;Automated Dependency Management | Data validation and preprocessing pipelines.Prediction generation and report delivery.Alerting for system failures/data anomalies|
| **3. Python Fundamentals** |Data: pandas, NumPy;ML: TensorFlow/Keras, scikit-learn | code interpretation | code reviews, practice| coding,reading |
| **4. Data Acquisition / Ingestion** | APIs, CSVs | Forward-fill minor gaps, drop unrecoverable rows| Cleaning: Forward-fill minor gaps, drop unrecoverable rows.Feature engineering: returns, volatility markers, volume trends.Scaling: StandardScaler fitted incrementally | robustness, automation |
| **5. Data Storage** | CSVs | NO | Separated data ingestion, preprocessing, training, and inference into discrete, reusable modules. | parquet. |
| **6. Data Preprocessing** | Handling Missing Data;Outlier Treatmen;tFeature Engineering | Missing Market Data;Outliers from Errors | Forward-fill for prices;Cap values at ±3σ | Dynamic Outlier Handling;Smarter Imputation |
| **7. Outlier Analysis** | Model-Based Residuals | real event | Outlier Handling Rules:Data is provably erroneous;Cap Outliers:Extreme but plausible values;Keep Outliers:Rare market events | Incorporate market regime detection |
| **8. Exploratory Data Analysis (EDA)** | Error Analysis;Performance Summaries | High R² with Overfitting;Feature Importance without Causality | Distribution Comparison | Lead-Lag Cross-Correlation;Non-Linear Relationship Check |
| **9. Feature Engineering** | lags, ratios,ln | ratios | RMSE | Macro-Sensitive Indicators |
| **10. Modeling (Regression / Time Series / Classification)** | LSTM,ACCURATE AND SUITABLE | overfitting | Baseline Establishment;Final Selection Criteria | RANDOM FOREST |
| **11. Evaluation & Risk Communication** | RMSE;MAE | Overfitting despite Validation;Regime Change Risk | Scenario-Based Reporting | Regime-Specific Testing;Monte Carlo Stress Testing |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Slides, reports | Plots and data | slides | NO |
| **13. Productization** | Automated Retraining Pipeline;Model Serving Infrastructure | API Load;Data Drift | Idempotent Pipelines；Model Performance Guardrails | NO |
| **14. Deployment & Monitoring** | the most significant is regime change risk - sudden market shifts (like COVID-19 or the 2008 crisis) wouldrender historical patterns useless. Overfitting risk is equally concerning, as the model might perform well backtested but fail with new data. Data quality risk could introduce garbage-in-garbage-out scenarios, while latency risk might cause delayed predictions in fast-moving markets. | Alert Fatigue；Metric Proliferation | Data Drift Detection；System Performance Metrics；Concept Drift Detection | Data Layer: Monitor feature distributions, missing data rates, and sudden statistical shifts in inputdata. Model Layer: Track prediction drift, accuracy metrics degradation, and feature importance changes. System Layer: Watch latency, throughput, error rates, and resource utilization. Business Layer: Monitor P&L impact, win rates, Sharpe ratio, and maximum drawdowns. |
| **15. Orchestration & System Design** | Monitoring Integration;Orchestration Tool | Data Pipeline Dependencies;Resource Contention | Simplified complex dependencies by breaking large tasks into smaller, parallelizable units | Centralize feature computation and storage to ensure consistency between training and inference, reducing drift and duplication. |
| **16. Lifecycle Review & Reflection** | A robust, interpretable model with reliable data pipelines outperforms a complex black box that fails unpredictably.Garbage in, garbage out. Time spent on validation, cleaning, and monitoring data pays higher returns than model tuning. | coding and reading | Strictly separated training, validation, and test sets by time to avoid lookahead bias and better simulate real-world performance. | Integrate MLflow for experiment tracking, Kubeflow for orchestration, and Grafana for monitoring from day one.Design models to output prediction intervals (e.g., Bayesian methods) rather than point estimates. |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
- Which stage was the most **rewarding**?  
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
- If you repeated this project, what would you **do differently across the lifecycle**?  
- Which skills do you most want to **strengthen** before your next financial engineering project?  

---
