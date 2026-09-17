# 报告撰写助手

这份文件只帮助写报告，不新增实验。

报告里的数字和结论，只能来自 notebook 已经打印的结果，或下面列出的图。`outputs/figures/05_model/` 里的比较图没有在 `05_model.ipynb` 中打印精确柱高，不要把柱高估读成正式指标。

已评估模型的正式指标来自 `notebooks/06_evaluation.ipynb`：

- MAE：491.243061
- RMSE：731.555819
- R²：0.958850

## 1. Introduction

需要写：

- 项目背景：Rossmann 门店日销售额预测。
- 问题定义：用预测日前已知的门店、日历、促销和历史特征，做有监督回归，预测当天 `Sales`。
- 预测目标：未来的门店日销售额。官方测试窗口是 2015-08-01 至 2015-09-17。本项目的测试文件没有 `Sales` 标签。

材料位置：

- `notebooks/05_model.ipynb` 第 5.1 节
- 原始表说明见 `notebooks/01_check.ipynb`

不要写模型可以完全替代人工决策，也不要写模型保证预测准确。

## 2. Data Understanding

需要写：

- 数据来源：项目使用的 Rossmann 表，`train.csv`、`store.csv`、`test.csv`。
- 规模：训练表 1,017,209 行，2013-01-01 至 2015-07-31；`store.csv` 1,115 家门店；测试表 41,088 行，2015-08-01 至 2015-09-17。
- 字段：训练表有 `Sales` 和 `Customers`。测试表没有 `Sales`，也没有 `Customers`。测试集缺少当天顾客数，是原始文件结构，不是清洗时删掉的。

对应 notebook：

- `notebooks/01_check.ipynb`

如果报告要写清洗：

- `notebooks/02_clean.ipynb`
- 清洗结果：`data/processed/train_clean.csv`、`data/processed/store_clean.csv`

`data/raw/sample_submission.csv` 不需要放进数据分析。它有 41,088 行，字段只有 `Id` 和 `Sales`，`Sales` 全部为 0，`Id` 与 `test.csv` 一一对应。它是 Kaggle 提交文件的格式样例，不是训练数据，也不是模型结果。报告不必单独分析它。只有课程明确要求交一份按 `Id` 填写预测销售额的文件时，才按这个列结构组织输出。

## 3. Exploratory Data Analysis

只写已经跑出的探索结果，不要另做新图。

需要写：

- 营业日销售右偏：均值 6,955.51，中位数 6,369。关门日销售额按业务规则为 0，所以主要分析用 `Open = 1`。
- 星期、促销、假日、门店类型、品类和竞争距离的差异。
- 营业日 `Customers` 与 `Sales` 的 Pearson 相关为 0.8236。这是描述关系。当天 `Customers` 不能作为测试特征。
- 促销日营业日平均销售 8,228.28（n = 376,896），非促销日 5,929.41（n = 467,496）。
- `CompetitionDistance` 与销售的 Pearson 相关为 −0.0364。

对应 notebook：

- `notebooks/03_eda.ipynb`

图片都在 `outputs/figures/03_eda/`：

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

没有单独的 `daily_average_sales_trend.png`。日趋势用带 7 日移动平均的那张图。

## 4. Feature Engineering

需要写：

- 特征为什么这样设计：时间规律、促销、门店属性、历史需求。
- 滞后特征：`Sales_lag_1`、`Sales_lag_7`、`Sales_lag_14`、`Sales_lag_28`，以及顾客滞后。
- 滚动特征：`Sales_rolling_7`、`Sales_rolling_30`、`Customers_rolling_7`。它们在合并后的 Store–Date 时间线上生成，再拆回训练表和测试表。
- 时间特征包括 `DayOfWeek`、`Day`、`WeekOfYear`，以及重要性表里用到的周周期编码。
- 当天 `Customers` 不进入建模矩阵。

引用已经打印的结果：

- `Sales_lag_14` 与销售相关 r = 0.795
- `Sales_lag_28`：r = 0.779
- `Sales_lag_7`：r = 0.675
- `Customers_lag_7`：r = 0.680
- `DayOfWeek`：r = −0.462
- `Promo`：r = 0.452
- 随机森林重要性：`Open` 0.472434，`Sales_lag_14` 0.287071，`Promo` 0.023480
- 分组贡献：历史需求 89.35%，时间特征 5.19%，促销 4.67%，门店特征 0.78%

要写明：随机森林只用于解释特征，不是最终预测模型。

对应 notebook：

- `notebooks/04_features.ipynb`

图片在 `outputs/figures/04_feature_engineering/`：

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

需要写：

- 时间切分：训练到 2015-06-30，验证期 2015-07-01 至 2015-07-31，官方测试期 2015-08-01 至 2015-09-17。
- 标准化只在训练时间段上拟合。保存的预处理器是 `outputs/models/preprocessor.pkl`。
- 最终架构与已保存文件、notebook 05 的记录一致：

128 → 64 → 32 neural network

已保存设置：ReLU、Adam、`learning_rate_init=0.001`、`max_iter=50`、`early_stopping=False`、`random_state=42`、49 个输入特征。

- `outputs/models/final_sales_model.pkl` 才是被评估的模型。不要把后来没有重训的记录写成“又训练了一次”。

探索图可以用来说明做过比较。除非 notebook 打印了数字，不要从柱状图上估一个精确 RMSE 或 MAE。当前 `05_model.ipynb` 没有打印这些柱高。

对应 notebook：

- `notebooks/05_model.ipynb` 第 5.1–5.6 节

图片在 `outputs/figures/05_model/`：

- `05_baseline_prediction_vs_actual.png`
- `05_baseline_residual_distribution.png`
- `05_baseline_vs_log_target_error.png`
- `05_architecture_comparison_rmse.png`
- `05_final_model_comparison.png`

这些图可以说明比较过 baseline、log target、网络结构和 early stopping，比较轴是验证集 RMSE。报告里点名的最终模型仍应是已保存的 128 → 64 → 32 网络。数值表现用下一节的评估结果。

## 6. Model Evaluation

只写已经打印的验证集结果：

- MAE：491.243061
- RMSE：731.555819
- R²：0.958850
- 验证集形状：34,565 行，49 个特征
- 平均残差（实际 − 预测）：27.449545
- 残差标准差：731.040655
- 按销售额分三档的平均绝对误差：Low 247.110986，Medium 481.630176，High 745.055776

这些数字能够支持的解释：

- 残差相对自身波动大致居中：平均残差约 27，残差标准差约 731。
- 绝对误差从低销售额到高销售额上升。在这个验证窗口里，高销售日更难预测。
- 指标来自 2015 年 7 月，不是没有标签的 8–9 月测试文件。

对应 notebook：

- `notebooks/06_evaluation.ipynb`

图片在 `outputs/figures/06_evaluation/`：

- 实际对预测：`06_final_actual_vs_predicted.png`
- 残差分析：`06_final_residual_distribution.png`
- 分档误差：`06_error_analysis_by_sales_level.png`

## 7. Conclusion

以 `notebooks/07_conclusion.ipynb` 为准，只写那里已经有证据的内容：

- 主要发现：解释模型里历史销售特征占主导；保留的预测模型是已保存的 128 → 64 → 32 网络；验证集 MAE、RMSE、R² 用上面的数字。
- 实际含义：预测可以辅助查看哪些门店日可能更忙或更闲。它不替代人工决策，也不保证准确。
- 限制：测试文件没有当天 `Customers`；天气、活动和价格没有纳入并测试；网络不是序列模型；指标只来自一个月的验证窗口；测试期较晚的行常常没有完整滚动窗口。

不要写某一张没有打印数值的比较图以某个具体差值胜过最终模型。
