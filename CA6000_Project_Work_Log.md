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

## 3.1 EDA Objective and Analysis Scope

The exploratory data analysis stage investigates the statistical characteristics, temporal patterns, operational factors, store characteristics, and external competition factors related to Rossmann daily sales.

The objectives of this stage are:

1. Understand the distribution characteristics of Sales and Customers;
2. Identify important temporal patterns;
3. Explore relationships between sales and operational variables;
4. Evaluate the predictive value of store-level and external features;
5. Provide evidence for feature engineering and neural network modelling.

All analyses focus on identifying statistical associations and predictive signals rather than establishing causal relationships.

---

# 3.2 Data Overview and Operating-Day Selection

The cleaned training dataset contains:

- 1,017,209 daily store observations.

According to the `Open` variable:

| Condition | Number of observations |
|---|---:|
| Open = 1 | 844,392 |
| Open = 0 | 172,817 |

Closed stores naturally generate:

\[
Sales=0
\]

and

\[
Customers=0
\]

These observations represent structural zeros rather than normal operating conditions.

Therefore, operating-day observations:

\[
Open=1
\]

are mainly used for sales performance analysis.

---

# 3.3 Sales and Customer Distribution Analysis

## Sales Distribution

For operating days:

Mean daily sales:

\[
Mean(Sales)=6955.51
\]

Median daily sales:

\[
Median(Sales)=6369
\]


The mean value is higher than the median value, indicating that daily sales follow a positively skewed distribution.

High-sales observations exist in the dataset. However, these observations are not automatically removed because they may represent:

- high-performing stores;
- peak demand periods;
- genuine business variation.

---

## Sales Outlier Analysis

The interquartile range method was used to identify potential extreme sales observations.

For operating-day Sales:

\[
Q1=4859
\]

\[
Q3=8360
\]

\[
IQR=3501
\]


The upper statistical boundary is:

\[
Q3+1.5\times IQR=13611.5
\]


Some observations exceed this threshold.

However, extreme sales values are retained because they may contain valuable business information.

Conclusion:

> Statistical outliers should be investigated but should not be automatically removed.

---

## Customer Distribution

Customer traffic also shows a positively skewed distribution.

For operating days:

Mean Customers:

\[
Mean(Customers)=762.73
\]


Median Customers:

\[
Median(Customers)=676
\]


Customer volume varies substantially among different stores and dates.

---

# 3.4 Temporal Pattern Analysis

## Daily Sales Trend

Daily average sales were analysed using operating stores only.

The daily average sales metric was defined as:

$$
\bar{S_t}
=
\frac{\sum_{i=1}^{n_t}Sales_{i,t}}
{n_t}
$$

where:

- \(t\) represents date;
- \(n_t\) represents the number of operating stores on date \(t\).

This removes the influence caused by different numbers of open stores on different dates.

The analysis identified clear temporal variation in daily sales.

Therefore, date-related information is expected to provide useful predictive signals.

---

## Weekly Seasonality

Sales performance varies across different weekdays.

The analysis indicates that weekday information contains predictive value.

Potential temporal features for later modelling include:

- Year;
- Month;
- Week;
- DayOfWeek.

---

# 3.5 Relationship Between Customers and Sales

The relationship between customer traffic and sales was analysed.

Pearson correlation coefficient:

$$
r=0.8236
$$


This indicates a strong positive relationship between Customers and Sales.

Customer traffic is therefore one of the strongest predictors of daily sales.

However, the scatter plot shows increasing variation when customer numbers become higher.

This indicates:

- Customers alone cannot fully explain sales variation;
- Additional operational and store-level factors are required.

---

# 3.6 Promotion Impact Analysis

Sales performance under promotion and non-promotion conditions was compared.

Results:

| Promo | Mean Sales |
|---|---:|
| 0 | 5929.41 |
| 1 | 8228.28 |

The relative difference is:

\[
\frac{8228.28-5929.41}{5929.41}
=
38.8\%
\]


Promotion periods show substantially higher average sales.

Further analysis shows that promotion is also associated with increased customer traffic.

Therefore, promotion may influence sales through:

\[
Promo
\rightarrow
Customers
\rightarrow
Sales
\]

The `Promo` variable should be considered an important modelling feature.

---

# 3.7 Holiday Impact Analysis

## StateHoliday

Different state holiday categories were analysed.

The results show that holiday categories are associated with different sales performance levels.

Therefore:


StateHoliday


contains useful predictive information.

---

## SchoolHoliday

Sales distributions were compared between:

- SchoolHoliday = 0;
- SchoolHoliday = 1.

The results indicate differences between school holiday and non-school holiday periods.

Therefore:


SchoolHoliday


should also be considered during feature engineering.

---

# 3.8 Store Characteristics Analysis

Store-level information was merged with daily sales records.

## StoreType

Different store types show different average sales performance.

This indicates that store operation mode influences sales behaviour.

Potential feature:


StoreType


---

## Assortment

Different assortment categories show different sales performance.

The analysis considered:

1. Store distribution among assortment categories;
2. Average sales performance among categories.

This indicates that product assortment structure provides additional predictive information.

Potential feature:


Assortment


---

# 3.9 Competition Analysis

Competition distance was analysed as an external market factor.

The variable:


CompetitionDistance


shows substantial variation among stores.

The relationship between CompetitionDistance and Sales is not strongly linear.

This suggests that competition effects may interact with:

- store location;
- market environment;
- store characteristics.

Therefore:


CompetitionDistance


should be retained as a potential feature rather than removed.

---

# 3.10 Promotion and Customer Traffic Interaction

The relationship between promotion and customer traffic was further investigated.

The results indicate that promotion periods are associated with changes in customer numbers.

This suggests that promotion may improve sales partly through increasing customer visits.

Because average basket size is unavailable in the dataset, customer traffic provides an important intermediate indicator for understanding promotion effects.

---

# 3.11 Feature Engineering Implications

Based on all EDA results, the following variables should be considered in the feature engineering stage.

## Temporal Features

Potential features:

- Year;
- Month;
- Week;
- DayOfWeek.

Reason:

Sales show clear temporal variation and weekday differences.

---

## Customer and Promotion Features

Potential features:

- Customers;
- Promo.

Reason:

Customers show strong correlation with Sales, while Promo significantly increases average sales.

---

## Holiday Features

Potential features:

- StateHoliday;
- SchoolHoliday.

Reason:

Holiday conditions are associated with sales variation.

---

## Store Characteristics

Potential features:

- StoreType;
- Assortment.

Reason:

Different store structures show different sales performance.

---

## Competition Features

Potential feature:

- CompetitionDistance.

Reason:

External market environment may provide additional predictive information.

---

# 3.12 Overall Conclusion

The exploratory data analysis demonstrates that Rossmann sales variation is influenced by multiple factors:

- customer traffic;
- promotion activities;
- temporal patterns;
- holiday conditions;
- store characteristics;
- competition environment.

No single variable can fully explain daily sales variation.

Therefore, the following feature engineering stage should combine:

- temporal information;
- operational variables;
- store-level characteristics;
- external competition information;

to construct comprehensive input features for the neural network prediction model.

------------------------------------------------------------------------

# 4. Feature Engineering Progress

(To be completed)

------------------------------------------------------------------------

# 5. Model Development Progress

(To be completed)
