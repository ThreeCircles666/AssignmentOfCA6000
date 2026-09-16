# CA6000 Rossmann Sales Prediction Project Work Log

## 0. Project Workflow and Notebook Writing Rules

### 0.1 Overall workflow

This project follows a complete data analysis and artificial
intelligence modelling workflow:

    Data Understanding
            ↓
    Data Quality Checking (01_check.ipynb)
            ↓
    Data Cleaning (02_clean.ipynb)
            ↓
    Exploratory Data Analysis (03_eda.ipynb)
            ↓
    Feature Engineering (04_features.ipynb)
            ↓
    Neural Network Modelling and Evaluation (05_model.ipynb)

The purpose of maintaining this work log is to preserve the current
project state, confirmed findings, analytical decisions, and
implementation rules. Future development should always refer to this
document before making changes.

A more detailed Chinese log, including every EDA method, figure choice,
and plotting parameter, is in `CA6000_项目开发者日志.md`.

### 0.2 Notebook development format

Each analytical step in the notebook should follow this structure:

1.  **Markdown cell**
    -   Explain what will be analysed.
    -   Explain why this analysis is necessary.
    -   Explain the methodology.
    -   Explain why this method is appropriate.
    -   Connect the analysis with previous conclusions.
    -   Define variables and analytical scope.
    -   Include mathematical formulas when statistical concepts or
        evaluation metrics are introduced.
2.  **Code cell**
    -   Implement exactly the method described in the preceding Markdown
        cell.
    -   Include clear comments.
    -   Produce reproducible outputs.
    -   Save important figures when required.
3.  **Notebook summary Markdown cell**
    -   At the end of every notebook, include an independent summary
        section.
    -   Summarize completed work.
    -   Summarize important findings.
    -   Explain implications for subsequent analysis.

### 0.3 Visualization requirements

All figures should satisfy two priorities:

1.  Correctly and clearly communicate data characteristics.
2.  Maintain a clean scientific visualization style.

The visualization style should follow the existing EDA notebook
examples:

-   Use a SCI-paper-inspired elegant style.
-   Use light pastel colours when appropriate:
    -   pastel red;
    -   pastel yellow;
    -   pastel green;
    -   pastel blue;
    -   pastel purple;
    -   pastel pink;
    -   pastel orange.
-   Avoid excessive decoration.
-   Avoid misleading visual effects.
-   Ensure labels, scales, legends and annotations are readable.
-   High-resolution figures should be generated.

Each important figure must satisfy:

-   displayed inside the notebook;
-   separately saved in the project figure folder:

```{=html}
<!-- -->
```
    outputs/figures/

The notebook version and external PNG version should be consistent.

Data interpretation is always more important than visual attractiveness.

------------------------------------------------------------------------

# 1. Conclusions from 01_check.ipynb

## 1.1 Dataset structure

The Rossmann dataset contains:

### train.csv

-   1,017,209 daily store records.
-   Variables include:
    -   Store
    -   Date
    -   Sales
    -   Customers
    -   Open
    -   Promo
    -   StateHoliday
    -   SchoolHoliday

### store.csv

-   1,115 store-level records.
-   Contains:
    -   StoreType
    -   Assortment
    -   CompetitionDistance
    -   Promo2 information
    -   Competition information

The two datasets can be successfully connected through:

    Store

No unmatched store IDs were detected.

------------------------------------------------------------------------

## 1.2 Missing value conclusions

Missing values were mainly identified in:

-   Promo2-related variables;
-   Competition-related variables.

Important conclusion:

These missing values are mostly structural missingness rather than data
errors.

Examples:

-   Stores without Promo2 naturally have missing Promo2 timing
    information.
-   Stores without available competition information contain unknown
    competition attributes.

Therefore:

-   Missing values should not be blindly replaced.
-   The original meaning should be preserved.

------------------------------------------------------------------------

## 1.3 Duplicate data conclusions

Checks showed:

-   No complete duplicate rows in train dataset.
-   No complete duplicate rows in store dataset.
-   No duplicated Store-Date business keys.

Therefore:

No duplicate removal is required.

------------------------------------------------------------------------

## 1.4 Data consistency conclusions

Important findings:

### StateHoliday

Different representations existed:

-   numeric 0;
-   string "0".

This is a representation inconsistency.

It should be standardized during cleaning.

### Date

Date values are valid and suitable for temporal analysis.

### Numerical variables

No physically impossible values were detected:

-   Sales are not negative.
-   Customers are not negative.
-   CompetitionDistance is not negative.

------------------------------------------------------------------------

## 1.5 Business logic checks

The following relationships were checked:

-   Closed stores should have zero sales.
-   Closed stores should have zero customers.

No systematic logical errors were detected.

A small number of special cases exist:

-   Open stores with zero sales.

These observations are retained because they may represent real
operational situations.

------------------------------------------------------------------------

## 1.6 Outlier conclusions

Potential outliers were identified using statistical methods.

However:

Extreme sales values are not automatically errors because
high-performing stores may naturally generate high sales.

Therefore:

-   Outliers are investigated.
-   Outliers are not removed automatically.

------------------------------------------------------------------------

# 2. Conclusions from 02_clean.ipynb

## 2.1 Cleaning principles

The cleaning strategy follows:

    Evidence-based cleaning

Only confirmed data quality problems are corrected.

Unknown but meaningful information is preserved.

------------------------------------------------------------------------

## 2.2 Completed cleaning operations

### Date conversion

Date variables were converted into datetime format.

Purpose:

Support:

-   yearly analysis;
-   monthly aggregation;
-   temporal feature engineering.

### StateHoliday normalization

Different representations were unified.

Purpose:

Ensure consistent categorical analysis.

### Data validation

After cleaning:

-   data structure remained unchanged;
-   row count was preserved;
-   processed files were generated.

Outputs:

    data/processed/train_clean.csv

    data/processed/store_clean.csv

------------------------------------------------------------------------

# 3. Conclusions from 03_eda.ipynb

Status: exploratory analysis is complete.

A more detailed Chinese developer log, including every analysis method,
figure choice, and plotting parameter, is maintained separately in:

    CA6000_项目开发者日志.md

The EDA notebook has 34 cells. It covers descriptive statistics, one
histogram, one time-series plot, one scatter relationship, grouped
boxplots, categorical bar charts, competition analysis, and a
promotion-versus-traffic comparison. Fifteen figures were saved under
`outputs/figures/`.

The notebook does not yet contain the required end-of-notebook summary
section specified in Section 0.2. That documentation gap is covered by
this work log and the Chinese log.

## 3.1 Completed: EDA environment preparation

Completed:

-   Load `data/processed/train_clean.csv` and `store_clean.csv`.
-   Restore `Date`, `StateHoliday`, nullable competition fields, and
    Promo2 fields.
-   Create `outputs/figures/`.
-   Establish the shared SCI-style Matplotlib configuration.

Confirmed setup:

-   1,017,209 train rows, 9 columns.
-   1,115 store rows, 10 columns.
-   `Date` dtype: `datetime64[us]`.
-   `StateHoliday` dtype: `string`.

Later EDA cells often reload the CSV independently instead of reusing
the setup DataFrame. Some reloads omit `dtype`, which raises a
`StateHoliday` mixed-type warning. This does not change the completed
analysis, but feature engineering should load data once with explicit
dtypes.

## 3.2 Completed: Descriptive statistics

Analysed:

-   Sales
-   Customers

Two scopes were considered:

1.  All daily records.
2.  Operating days (`Open = 1`).

Reason:

Closed stores create structural zeros.

Important findings:

-   1,017,209 daily records.
-   844,392 operating days (83.01%).
-   172,817 closed-store days (16.99%).

Operating-day Sales:

-   Mean: 6,955.51
-   Median: 6,369.00
-   Standard deviation: 3,104.21
-   Q1: 4,859.00
-   Q3: 8,360.00
-   IQR: 3,501.00
-   Maximum: 41,551.00

Operating-day Customers:

-   Mean: 762.73
-   Median: 676.00
-   Standard deviation: 401.23
-   IQR: 374
-   Maximum: 7,388

Both distributions are right-skewed. The mean-minus-median gap for
operating-day Sales is 586.51. Calculation audits for mean, sample
variance (`ddof=1`), standard deviation, and IQR all returned True.

## 3.3 Completed: Sales distribution and boxplot

Figures:

-   `outputs/figures/sales_distribution_open.png`
-   `outputs/figures/sales_boxplot_open.png`

Conclusions:

-   The histogram shows a unimodal, positively skewed distribution with
    a long high-sales tail.
-   The Tukey upper fence is 13,611.5.
-   30,769 operating-day sales observations (3.64%) lie above that
    fence.
-   These observations are retained. They are statistical extremes, not
    confirmed errors.
-   A later model should consider a skewed target, for example a log
    transform or a robust loss. Do not delete the tail by default.

## 3.4 Completed: Temporal patterns

Figures:

-   `outputs/figures/daily_average_sales_trend_ma7.png`
-   `outputs/figures/weekday_sales_boxplot.png`

Methods:

-   Daily average sales per operating store, so changes in the number of
    open stores are not mistaken for demand changes.
-   A 7-day moving average (`window=7`, `min_periods=1`) was added to
    separate short-term noise from the broader trend.
-   Weekday boxplots compare distributions, not only means. Extreme
    points are hidden (`showfliers=False`) so the boxes remain readable.

Weekday operating-day Sales:

| Weekday | Count  | Mean     | Median | IQR    |
|---------|--------|----------|--------|--------|
| Mon     | 137,560| 8,216.07 | 7,539  | 4,595  |
| Tue     | 143,961| 7,088.11 | 6,502  | 3,561  |
| Wed     | 141,936| 6,728.12 | 6,210  | 3,158  |
| Thu     | 134,644| 6,767.31 | 6,246  | 3,087  |
| Fri     | 138,640| 7,072.68 | 6,580  | 3,119  |
| Sat     | 144,058| 5,874.84 | 5,425  | 3,307  |
| Sun     | 3,593  | 8,224.72 | 6,876  | 8,104  |

Conclusions:

-   Monday is the strongest regular weekday.
-   Saturday has the lowest typical sales among regularly open days.
-   Sunday has very few operating observations and the largest IQR.
-   Weekday distributions overlap substantially, so day of week is
    useful but not sufficient.
-   The train period is 2013-01-01 to 2015-07-31. The official test
    period is 2015-08-01 to 2015-09-17. Modelling must use a time-aware
    split, not a random split.

## 3.5 Completed: Customers and sales

Figure:

-   `outputs/figures/customers_sales_scatter.png`

Result:

-   Pearson correlation on all operating days: **0.8236**.
-   The scatter uses a reproducible sample of 30,000 points
    (`random_state=42`) plus a degree-1 trend fitted on that sample.
-   The correlation is strong and positive.

Modelling restriction:

`Customers` is available in `train.csv` but **not** in `test.csv`.
Same-day customer count cannot be used as an inference feature. Using
it would leak information that is unavailable at prediction time. It
may still be studied as a mechanism, or used only through historical
lags known before the forecast date.

## 3.6 Completed: Promotion, holidays, and traffic

Figures:

-   `outputs/figures/sales_promotion_boxplot.png`
-   `outputs/figures/sales_stateholiday_boxplot.png`
-   `outputs/figures/average_sales_stateholiday.png`
-   `outputs/figures/sales_schoolholiday_boxplot.png`
-   `outputs/figures/customers_promotion_boxplot.png`

Operating-day comparison:

| Condition | Sales mean | Sales median | Customers mean |
|-----------|------------|--------------|----------------|
| Promo = 0 | 5,929.41   | 5,459        | 696.86         |
| Promo = 1 | 8,228.28   | 7,649        | 844.43         |
| SchoolHoliday = 0 | 6,896.78 | 6,326   | — |
| SchoolHoliday = 1 | 7,200.18 | 6,562   | — |

State-holiday operating days are rare:

-   No holiday: 843,482 observations, mean sales 6,953.52.
-   Holiday A: 694 observations, mean 8,487.47.
-   Holiday B: 145 observations, mean 9,887.89.
-   Holiday C: 71 observations, mean 9,743.75.

Conclusions:

-   Promotion is a large, usable effect. It is present in the test set.
-   Promotion raises both sales and customer traffic, so the sales lift
    is not only a higher spend per existing customer.
-   School holiday has a small positive difference and should be kept as
    a feature, but it is weaker than Promo and weekday.
-   Open stores on state holidays have higher average sales, but the
    samples are tiny and selected: most holiday stores are closed.
    Holiday effects must be modelled together with `Open`, not as a
    simple additive boost estimated only from open holiday days.

## 3.7 Completed: Store characteristics and competition

Figures:

-   `outputs/figures/average_sales_storetype.png`
-   `outputs/figures/store_distribution_assortment.png`
-   `outputs/figures/average_sales_assortment.png`
-   `outputs/figures/competition_distance_distribution.png`
-   `outputs/figures/competition_distance_sales_scatter.png`

Store type, operating days, sorted by mean sales:

| StoreType | Mean sales | Median | Stores | Observations |
|-----------|------------|--------|--------|--------------|
| b         | 10,231.41  | 9,130  | 17     | 15,563       |
| c         | 6,932.51   | 6,407  | 148    | 112,978      |
| a         | 6,925.17   | 6,285  | 602    | 457,077      |
| d         | 6,822.14   | 6,395  | 348    | 258,774      |

Assortment:

| Assortment | Stores | Mean sales | Median |
|------------|--------|------------|--------|
| a          | 593    | 6,621.02   | 6,082  |
| b          | 9      | 8,639.35   | 8,081  |
| c          | 513    | 7,300.53   | 6,675  |

Competition distance, non-missing operating days (842,206 rows):

-   Median distance: 2,320.
-   Mean distance: 5,457.98.
-   Maximum: 75,860.
-   Pearson correlation with Sales: **-0.0364**.

Conclusions:

-   StoreType `b` and Assortment `b` are high-performing but rare.
    They should be encoded, not dropped, and should not be interpreted
    from the mean alone.
-   Types a, c, and d have similar average sales. Store identity or
    other store attributes may matter more than StoreType among these
    three.
-   Competition distance is strongly right-skewed and almost linearly
    uncorrelated with daily sales. Do not expect a linear distance term
    to carry much signal. Bins, missing indicators, or competition-open
    duration are more appropriate than a raw linear feature.
-   Three stores still have missing distance. They must be handled
    explicitly.

## 3.8 EDA implications for the next stage

Confirmed feature directions:

1.  Do not predict closed-store sales as ordinary demand. If `Open` is
    known, closed days can be set to zero. Test `Open` has 11 missing
    values that need an explicit rule.
2.  Time features: weekday, month, week of year, and a time-based
    validation window. The forecast horizon is the six weeks after
    2015-07-31.
3.  Promo is a primary operational feature.
4.  StateHoliday and SchoolHoliday should be retained, with care about
    rare holiday categories and the open-store selection effect.
5.  StoreType and Assortment should be categorical features.
6.  Same-day Customers must not be used as a model input for the test
    period.
7.  Promo2 and competition-opening fields were preserved during cleaning
    but were not yet explored in EDA. They belong in feature
    engineering, not in another blind imputation step.
8.  The target is right-skewed. Transform or evaluate accordingly.
9.  IQR extremes remain in the data.

Known implementation notes, not blocking conclusions:

-   Section 5.1 markdown describes an unsmoothed figure named
    `daily_average_sales_trend.png`. The saved figure is the moving-
    average version `daily_average_sales_trend_ma7.png`.
-   StoreType markdown mentions a store-count chart, but only the
    average-sales bar chart was implemented.
-   The competition histogram y-axis is labelled "Number of Stores",
    while the plotted data are daily records.
-   `sales_boxplot_open.png` uses the deprecated Matplotlib argument
    `vert=False`.

------------------------------------------------------------------------

# 4. Feature Engineering Progress

Not started. `notebooks/04_features.ipynb` still contains only the
planned scope comment.

Planned scope from the notebook stub:

-   Build the modelling table.
-   Generate customer-history, promotion, holiday, time, and store
    features.

Decisions that must be made before coding, based on completed EDA:

1.  Prediction grain. The official test set is daily, store-level,
    2015-08-01 to 2015-09-17, 41,088 rows, 8 columns, no `Sales` and no
    `Customers`. The notebook stub mentions monthly store data. Monthly
    aggregation would not match the required submission grain. The
    default next step should be a daily store-level feature table
    unless the course requirement explicitly changes the target.
2.  Same-day `Customers` is explanatory only. Allowed substitutes are
    historical lags and historical store customer levels known before
    the forecast date.
3.  Missing Promo2 details stay structurally missing. Encode
    "not applicable" rather than imputing a week or year.
4.  Missing competition dates stay missing. Add missing indicators
    instead of inventing dates.
5.  Preserve the 54 open-store zero-sales review cases and the IQR
    tail.

------------------------------------------------------------------------

# 5. Model Development Progress

Not started. `notebooks/05_model.ipynb` still contains only the planned
scope comment.

Planned scope:

-   Data split
-   Preprocessing
-   Baseline
-   Neural network training
-   Evaluation and result analysis

Constraints already fixed by the project state:

-   Use a temporal split. Training ends on 2015-07-31. The test window
    begins on 2015-08-01.
-   `requirements.txt` currently lists pandas, numpy, matplotlib, and
    scikit-learn. A neural-network library has not been added yet.
-   A simple baseline should be built before the neural network, so
    later neural-network gains can be interpreted.
-   Evaluation must not use same-day `Customers` as an input feature.
