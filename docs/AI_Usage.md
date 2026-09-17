# AI Assistance Summary in Project Development

# 项目开发中的 AI 辅助总结

------

## 1. Overview of AI Usage

## 1. AI 使用概述

**English**

During this project, AI coding assistants were used as supporting tools throughout the development process. AI was not used to independently complete the project or replace the developer's decision-making. Instead, AI was mainly used for improving development efficiency, providing alternative solutions, debugging assistance, and expanding technical considerations.

The overall workflow, dataset selection, feature engineering strategy, model selection, experiment design, and final evaluation decisions were manually reviewed and determined by the developer.

**中文**

在本项目开发过程中，AI 编程助手作为辅助工具参与了多个阶段的开发工作。AI 并不是独立完成整个项目，也没有替代开发者进行关键决策，而主要用于提高开发效率、提供方案建议、辅助代码调试以及扩展技术思路。

项目的数据选择、整体流程设计、特征工程策略、模型选择、实验方案以及最终评价分析均由开发者进行判断和确认。

------

# 2. AI-Assisted Code Development

# 2. AI 辅助代码开发

**English**

AI assistants were used to help write and improve parts of the Python implementation.

The main assistance included:

- Suggesting implementation approaches for data processing and feature engineering.
- Helping improve code structure and readability.
- Providing suggestions for using Python libraries such as Pandas, NumPy, Matplotlib, and Scikit-learn.
- Identifying possible coding issues and suggesting corrections.

For example, during the feature engineering stage, AI helped review the design of lag features, rolling statistics, temporal features, and data transformation procedures. However, the final feature selection was based on data analysis results and validation experiments.

**中文**

AI 助手用于辅助 Python 代码开发和优化。

主要帮助包括：

- 提供数据处理和特征工程实现方案建议；
- 改进代码结构，提高代码可读性；
- 提供 Pandas、NumPy、Matplotlib 和 Scikit-learn 等工具使用建议；
- 帮助定位代码错误并提出修改方案。

例如，在特征工程阶段，AI 协助分析滞后特征（lag features）、滑动统计特征（rolling statistics）、时间特征以及数据转换流程的实现方式。但最终特征选择仍基于实际数据分析结果和模型验证结果确定。

------

# 3. AI-Assisted Debugging and Problem Solving

# 3. AI 辅助调试和问题解决

**English**

AI assistants were used during debugging to analyze error messages and identify possible causes.

Examples include:

- Resolving variable dependency issues between different notebooks.
- Improving the connection between feature engineering and model evaluation stages.
- Identifying missing preprocessing pipelines when moving from model training to independent evaluation.
- Suggesting better project organization practices.

For instance, after separating the model training and evaluation notebooks, AI helped identify that preprocessing objects needed to be saved and reused instead of being recreated. This improved the reproducibility of the machine learning pipeline.

**中文**

AI 助手参与了项目调试过程，用于分析错误信息和定位潜在原因。

主要包括：

- 解决不同 notebook 之间变量依赖问题；
- 改进特征工程阶段与模型评价阶段之间的数据连接；
- 发现模型训练与独立评价过程中缺少预处理流程保存的问题；
- 提供更规范的项目文件组织建议。

例如，在将模型训练和模型评价拆分为独立 notebook 后，AI 帮助发现预处理对象需要保存并重新加载，而不是在评价阶段重新创建。这提高了机器学习流程的可重复性。

------

# 4. AI-Assisted Method Selection and Idea Expansion

# 4. AI 辅助方案选择与思路扩展

**English**

AI was also used as a discussion partner during project planning.

The assistance included:

- Comparing possible modeling approaches.
- Discussing advantages and limitations of different feature engineering strategies.
- Suggesting additional evaluation methods.
- Helping organize the logical structure of the project.

For example, AI suggested evaluating not only overall metrics but also prediction behavior through:

- Actual vs Predicted analysis;
- Residual distribution analysis;
- Error analysis across different sales levels.

These suggestions helped improve the completeness of model evaluation.

**中文**

AI 也作为项目设计过程中的讨论工具，用于扩展研究思路。

主要包括：

- 比较不同模型方案；
- 分析不同特征工程方法的优缺点；
- 提供额外模型评价方法建议；
- 帮助梳理项目整体逻辑。

例如，AI 建议模型评价不仅关注整体指标，还应该进一步分析：

- 真实值与预测值关系；
- 残差分布；
- 不同销售水平下的预测误差。

这些建议提高了模型评价部分的完整性。

------

# 5. Human Decision and Validation

# 5. 人工判断与验证

**English**

Although AI provided suggestions and technical assistance, all important decisions were manually reviewed.

The developer was responsible for:

- Selecting the dataset and defining the prediction task.
- Designing the feature engineering strategy.
- Selecting the final neural network architecture.
- Interpreting experimental results.
- Checking whether AI suggestions were appropriate for the project.

All generated code and suggestions were tested, modified, and validated before being included in the final project.

**中文**

虽然 AI 提供了方案建议和技术辅助，但所有关键决策均由开发者进行审核。

开发者负责：

- 数据集选择和预测任务定义；
- 特征工程方案设计；
- 最终神经网络结构选择；
- 实验结果解释；
- 判断 AI 建议是否适用于当前项目。

所有 AI 生成的代码和建议均经过测试、修改和验证后才纳入最终项目。

------

# 6. Summary

# 6. 总结

**English**

AI played the role of an assistant throughout this project. It improved coding efficiency, supported debugging, provided alternative approaches, and helped expand analytical perspectives.

However, the project workflow, modeling decisions, experiment interpretation, and final conclusions were controlled and validated by the developer.

**中文**

AI 在本项目中主要承担辅助角色，包括提高代码开发效率、协助调试、提供方案选择建议以及扩展分析思路。

但是，项目流程设计、模型决策、实验结果解释以及最终结论均由开发者独立判断并验证。