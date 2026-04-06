# outbreak-analysis
Exploratory data analysis and predictive modeling on a simulated outbreak dataset, focusing on sparse data handling.

This project explores exploratory data analysis and basic predictive modeling
on a synthetic outbreak-style time-series dataset. The goal is to demonstrate
data handling, time-series reasoning, and applied machine learning workflows
under realistic public health data constraints.

All data used in this project is fully synthetic and does not represent any
real disease, population, or outbreak scenario.

---

## Project Structure

synthetic-outbreak-analysis/
├── data/
│   ├── generate_synthetic_data.py
│   ├── synthetic_outbreak.csv
│   └── README.md
├── analysis/
│   ├── eda.ipynb
│   └── modeling.ipynb
├── requirements.txt
└── README.md

---

## Data Generation

The dataset is generated using a Python script (`generate_synthetic_data.py`)
that simulates a single outbreak wave with:

- Noisy daily reported case counts
- Sparse symptom reporting
- Variable testing volume
- Intentional missing values

The generated CSV is treated as a fixed dataset for analysis and modeling.

See `data/README.md` for detailed assumptions and limitations.

---

## Exploratory Data Analysis

The `analysis/eda.ipynb` notebook examines:

- Dataset structure and distributions
- Temporal trends and smoothing via moving averages
- Missing data patterns and reporting gaps
- Known artifacts and analytical limitations

The notebook is written as a readable analytical document with embedded
visualizations and interpretation.

---

## Predictive Modeling

The `analysis/modeling.ipynb` notebook demonstrates a simple modeling workflow:

- Feature engineering using rolling statistics
- Time-aware train/test splitting
- Logistic regression as an interpretable baseline model
- Evaluation with appropriate caution given dataset size and synthetic nature

The modeling is intended for methodological illustration rather than
real-world outbreak prediction.

---

## Limitations and Ethics

- All data is synthetic and simplified
- Results are not intended for real-world forecasting or decision-making
- Small dataset size limits statistical power
- No sensitive or personal data is used

Synthetic data is used intentionally to support ethical, reproducible analysis
without privacy concerns.

---

## Requirements

The project uses standard Python data science libraries. Dependencies are listed
in `requirements.txt`.

---

## Intended Audience

This project is intended as a demonstration of applied data analysis and
modeling practices for educational and internship-level evaluation.


