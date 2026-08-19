# 用于初始化 CA6000 项目目录和基础文件；只创建缺失内容，不覆盖已有文件。

from pathlib import Path
import json


# ============================================================
# 1. 项目根目录
# ============================================================

# 本脚本应放在 AssignmentOfCA6000 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent


# ============================================================
# 2. 需要创建的目录
# ============================================================

DIRECTORIES = [
    "data/processed",
    "notebooks",
    "models",
    "outputs",
    "docs",
]


# ============================================================
# 3. 普通文件
# ============================================================

TEXT_FILES = {
    "data/processed/.gitkeep":
        "# 用于保留 processed 数据目录；后续存放清洗和特征处理后的数据。\n",

    "models/.gitkeep":
        "# 用于保留 models 目录；后续存放训练完成的模型文件。\n",

    "outputs/.gitkeep":
        "# 用于保留 outputs 目录；后续存放图表、评价指标和预测结果。\n",

    "docs/AI_USAGE_LOG.md":
        "<!-- 用于记录 CA6000 项目开发过程中 AI 工具的使用情况。 -->\n",

    "README.md":
        "<!-- 用于说明 CA6000 项目的选题、数据集、环境和运行方法。 -->\n",

    "requirements.txt":
        """# 用于记录 CA6000 项目运行所需的 Python 第三方依赖。

pandas==3.0.3
numpy==2.5.1
matplotlib==3.11.1
scikit-learn==1.9.0
""",

    ".gitignore":
        """# 用于定义不需要提交到 Git 仓库的临时文件和缓存文件。

__pycache__/
*.py[cod]

.ipynb_checkpoints/

.venv/
venv/

.DS_Store
Thumbs.db
""",
}


# ============================================================
# 4. Notebook 文件
# ============================================================

NOTEBOOKS = {
    "notebooks/01_check.ipynb":
        "# 本 Notebook 用于加载和检查原始数据，包括结构、类型、缺失值、重复值、异常值和其他数据质量问题。",

    "notebooks/02_clean.ipynb":
        "# 本 Notebook 用于处理数据检查阶段发现的问题，并验证清洗后的数据质量。",

    "notebooks/03_eda.ipynb":
        "# 本 Notebook 用于进行描述性统计、探索性数据分析（EDA）和必要的数据可视化。",

    "notebooks/04_features.ipynb":
        "# 本 Notebook 用于构建门店月度建模数据，并生成客流、促销、节假日、时间和门店等预测特征。",

    "notebooks/05_model.ipynb":
        "# 本 Notebook 用于数据划分、预处理、Baseline、神经网络训练、模型评价和结果分析。",
}


# ============================================================
# 5. 创建目录
# ============================================================

def create_directory(relative_path):
    path = PROJECT_ROOT / relative_path

    if path.exists():
        print(f"[SKIP DIR]    {relative_path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[CREATE DIR]  {relative_path}")


# ============================================================
# 6. 创建普通文件
# ============================================================

def create_text_file(relative_path, content):
    path = PROJECT_ROOT / relative_path

    # 已存在就不覆盖
    if path.exists():
        print(f"[SKIP FILE]   {relative_path}")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

    print(f"[CREATE FILE] {relative_path}")


# ============================================================
# 7. 创建 Notebook
# ============================================================

def create_notebook(relative_path, first_comment):
    path = PROJECT_ROOT / relative_path

    # 已存在就不覆盖
    if path.exists():
        print(f"[SKIP NB]     {relative_path}")
        return

    path.parent.mkdir(parents=True, exist_ok=True)

    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    first_comment + "\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.12.7"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with path.open("w", encoding="utf-8") as file:
        json.dump(
            notebook,
            file,
            ensure_ascii=False,
            indent=2
        )

    print(f"[CREATE NB]   {relative_path}")


# ============================================================
# 8. 显示当前项目结构
# ============================================================

def show_project_tree():
    print("\n" + "=" * 60)
    print("Project Structure")
    print("=" * 60)

    important_dirs = [
        "data",
        "notebooks",
        "models",
        "outputs",
        "docs"
    ]

    for directory_name in important_dirs:
        directory = PROJECT_ROOT / directory_name

        if not directory.exists():
            continue

        print(f"\n{directory_name}/")

        for path in sorted(directory.rglob("*")):
            if path.is_file():
                relative = path.relative_to(directory)
                print(f"    {relative}")


# ============================================================
# 9. 显示找到的数据文件
# ============================================================

def show_data_files():
    print("\n" + "=" * 60)
    print("Detected Data Files")
    print("=" * 60)

    data_dir = PROJECT_ROOT / "data"

    if not data_dir.exists():
        print("data directory not found.")
        return

    files = [
        file
        for file in data_dir.rglob("*")
        if file.is_file() and file.suffix.lower() in {".csv", ".xlsx", ".xls"}
    ]

    if not files:
        print("No data files found.")
        return

    for file in sorted(files):
        print(file.relative_to(PROJECT_ROOT))


# ============================================================
# 10. 主程序
# ============================================================

def main():
    print("=" * 60)
    print("CA6000 Project Initializer")
    print("=" * 60)

    print(f"\nProject root:")
    print(PROJECT_ROOT)

    print("\nCreating directories...")

    for directory in DIRECTORIES:
        create_directory(directory)

    print("\nCreating files...")

    for relative_path, content in TEXT_FILES.items():
        create_text_file(relative_path, content)

    print("\nCreating notebooks...")

    for relative_path, comment in NOTEBOOKS.items():
        create_notebook(relative_path, comment)

    show_data_files()
    show_project_tree()

    print("\n" + "=" * 60)
    print("Initialization completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()