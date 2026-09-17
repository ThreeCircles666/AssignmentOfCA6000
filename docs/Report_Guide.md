# Report Guide

This file is a writing aid for the project report. It does not add experiments.

Use only numbers and statements that already appear in the notebooks or in the saved figures listed below. Do not copy bar heights from `outputs/figures/05_model/` into the report as exact metrics. Those charts are not annotated with printed values in `05_model.ipynb`.

Official evaluation numbers, from `notebooks/06_evaluation.ipynb`:

- MAE: 491.243061
- RMSE: 731.555819
- R²: 0.958850

## 1. Introduction

Write:

- Project background: daily sales forecasting for Rossmann stores.
- Problem definition: supervised regression from known store, calendar, promotion, and historical features to daily `Sales`.
- Prediction target: `Sales` on a future store-day. The official test window is 2015-08-01 to 2015-09-17 and has no `Sales` labels in this project.

Source:

- `notebooks/05_model.ipynb`, section 5.1
- `notebooks/01_check.ipynb` for the raw tables

Do not write that the model replaces human decisions or guarantees accuracy.

## 2. Data Understanding

Write:

- Data source: Rossmann store sales tables used by the project (`train.csv`, `store.csv`, `test.csv`).
- Scale: training has 1,017,209 daily store rows, 2013-01-01 to 2015-07-31; `store.csv` has 1,115 stores; test has 41,088 rows, 2015-08-01 to 2015-09-17.
- Fields: training includes `Sales` and `Customers`. The test file has no `Sales` and no `Customers`. That missing customer column is part of the original test schema.

Source notebook:

- `notebooks/01_check.ipynb`

Cleaning follow-up, if the report needs it:

- `notebooks/02_clean.ipynb`
- cleaned exports: `data/processed/train_clean.csv`, `data/processed/store_clean.csv`

## 3. Exploratory Data Analysis

Write from executed EDA, not from a new plot:

- Operating-day sales are right-skewed: mean 6,955.51, median 6,369. Closed stores were separated because they have zero sales by construction.
- Weekday differences, promotion association, holiday patterns, store type, assortment, and competition distance.
- Operating-day `Customers`–`Sales` Pearson correlation: 0.8236. This is descriptive. Same-day `Customers` is not a test feature.
- Promo operating-day mean sales: 8,228.28 (n = 376,896) versus 5,929.41 without promo (n = 467,496).
- `CompetitionDistance` versus sales Pearson correlation: −0.0364.

Source notebook:

- `notebooks/03_eda.ipynb`

Figures, all under `outputs/figures/03_eda/`:

- `03_sales_distribution_operating_days.png`
- `03_sales_boxplot_operating_days.png`
- `03_daily_average_sales_trend_ma7.png`
- `03_weekday_sales_boxplot.png`
- `03_customers_sales_scatter.png`
- `03_sales_promotion_boxplot.png`
- `03_customers_promotion_boxplot.png`
- `03_sales_stateholiday_boxplot.png`
- `03_average_sales_stateholiday.png`
- `03_sales_schoolholiday_boxplot.png`
- `03_average_sales_storetype.png`
- `03_store_distribution_assortment.png`
- `03_average_sales_assortment.png`
- `03_competition_distance_distribution.png`
- `03_competition_distance_sales_scatter.png`

There is no separate unsmoothed file named `daily_average_sales_trend.png`. Use the `ma7` file.

## 4. Feature Engineering

Write:

- Why features were built: temporal pattern, promotion, store attributes, and historical demand.
- Lag features: `Sales_lag_1`, `Sales_lag_7`, `Sales_lag_14`, `Sales_lag_28`, plus customer lags.
- Rolling features: `Sales_rolling_7`, `Sales_rolling_30`, `Customers_rolling_7`, generated on the combined timeline and then split back.
- Temporal features include `DayOfWeek`, `Day`, `WeekOfYear`, and the encoded week terms used in the importance table.
- Same-day `Customers` stays out of the modeling matrix.

Cite printed results, not approximations presented as new measurements:

- `Sales_lag_14` correlation with sales: r = 0.795
- `Sales_lag_28`: r = 0.779
- `Sales_lag_7`: r = 0.675
- `Customers_lag_7`: r = 0.680
- `DayOfWeek`: r = −0.462
- `Promo`: r = 0.452
- Random Forest importance: `Open` 0.472434, `Sales_lag_14` 0.287071, `Promo` 0.023480
- Group contribution: historical demand 89.35%, temporal 5.19%, promotion 4.67%, store characteristics 0.78%

State that the Random Forest is an interpretation model, not the forecasting model.

Source notebook:

- `notebooks/04_features.ipynb`

Figures, under `outputs/figures/04_feature_engineering/`:

- `04_historical_feature_missing_rate.png`
- `04_feature_correlation_heatmap.png`
- `04_top20_feature_importance.png`
- `04_feature_group_contribution.png`
- `04_feature_group_contribution_percentage.png`
- `04_train_test_promo_distribution.png`
- `04_train_test_dayofweek_distribution.png`
- `04_train_test_storetype_distribution.png`
- `04_train_test_sales_lag_14_distribution.png`
- `04_train_test_sales_lag_28_distribution.png`
- `04_train_test_sales_rolling_30_distribution.png`

## 5. Model Development

Write:

- Time split: train through 2015-06-30, validation 2015-07-01 to 2015-07-31, official test 2015-08-01 to 2015-09-17.
- Scaling is fit on the training period only. The saved preprocessor is `outputs/models/preprocessor.pkl`.
- Final architecture, matching the saved file and recorded in notebook 05:

128 → 64 → 32 neural network

Saved settings: ReLU, Adam, `learning_rate_init=0.001`, `max_iter=50`, `early_stopping=False`, `random_state=42`, 49 input features.

- The pickle `outputs/models/final_sales_model.pkl` is the evaluated model. Do not describe a re-run of training as if it produced these weights.

Exploration figures may be shown as process evidence. Do not type exact RMSE or MAE values from those bars unless a notebook cell prints them. Current notebook 05 does not print those bar values.

Source notebook:

- `notebooks/05_model.ipynb`, sections 5.1–5.6

Figures, under `outputs/figures/05_model/`:

- `05_baseline_prediction_vs_actual.png`
- `05_baseline_residual_distribution.png`
- `05_baseline_vs_log_target_error.png`
- `05_architecture_comparison_rmse.png`
- `05_final_model_comparison.png`

Use these to describe that baseline, log-target, architecture, and early-stopping variants were compared on validation RMSE. The retained model named in the report should still be the saved 128 → 64 → 32 network, with numeric performance taken from section 6 below.

## 6. Model Evaluation

Write the printed validation results only:

- MAE: 491.243061
- RMSE: 731.555819
- R²: 0.958850
- Validation shape: 34,565 rows, 49 features
- Mean residual (actual − predicted): 27.449545
- Residual standard deviation: 731.040655
- Error by sales level (`qcut`, three groups): Low 247.110986, Medium 481.630176, High 745.055776

Interpretation that is supported by these numbers:

- Residuals are centered relative to their spread: the mean residual is about 27, while the residual standard deviation is about 731.
- Absolute error increases from low to high sales. High-sales days are harder in this validation window.
- Metrics are for July 2015, not for the unlabeled August–September test file.

Source notebook:

- `notebooks/06_evaluation.ipynb`

Figures, under `outputs/figures/06_evaluation/`:

- Actual vs predicted: `06_final_actual_vs_predicted.png`
- Residual analysis: `06_final_residual_distribution.png`
- Error analysis: `06_error_analysis_by_sales_level.png`

## 7. Conclusion

Use `notebooks/07_conclusion.ipynb`. Cover only what that notebook already states:

- Key findings: historical sales features dominate the interpretation model; the retained forecaster is the saved 128 → 64 → 32 network; validation MAE, RMSE, and R² are the numbers above.
- Practical implications: the forecast can support review of busy and quiet store-days. It does not replace a decision and does not guarantee accuracy.
- Limitations: no same-day `Customers` in the test file; weather, events, and prices were not tested; the network is not a sequence model; metrics are from one validation month; later test rows often lack complete rolling windows.

Do not add a claim that an unprinted comparison chart beat the saved model by a specific amount.
