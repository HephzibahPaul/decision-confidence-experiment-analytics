# Decision-Confidence Experiment Evaluation System

This project is an industry-oriented Data Analyst project that evaluates A/B
experiment results using a decision-confidence approach, instead of relying
only on statistical significance.

The goal is to answer a real business question:

> Should we launch a new feature, extend the experiment, or stop it?

---

## Project Overview

In real companies, experiment results can look statistically significant but
still be risky to act on due to:
- Small sample sizes
- Inconsistent performance across user segments
- Weak practical impact

This project simulates how product and growth analytics teams evaluate
experiments before making high-stakes decisions.

---

## What This Project Does

- Compares conversion rates between Control (A) and Treatment (B)
- Measures conversion lift
- Performs statistical testing (proportion z-test)
- Checks segment-level stability
- Calculates a Decision Confidence Score
- Produces a final recommendation:
  - LAUNCH
  - EXTEND
  - ABORT

---

## Key Concepts Used

- Conversion rate and lift
- Hypothesis testing (z-test for proportions)
- Segment stability analysis
- Decision confidence scoring
- Risk-aware business recommendations

No machine learning models are used. This is pure Data Analyst work.

---

## Project Structure

Decision_Confidence_Experiment_Project/
├── data/
│ └── experiment_data.csv
├── src/
│ ├── load_data.py
│ ├── validate_data.py
│ ├── metrics.py
│ ├── statistical_tests.py
│ ├── confidence_scoring.py
│ ├── visualization.py
│ └── decision_engine.py
├── outputs/
│ ├── charts/
│ │ └── conversion_comparison.png
│ └── tables/
│ └── summary_metrics.csv
├── reports/
│ └── decision_report.md
├── requirements.txt
├── README.md
└── LICENSE


---

## How to Run the Project

### Step 1: Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
Step 2: Install required libraries
pip install -r requirements.txt
Step 3: Run the analysis
python src/decision_engine.py
Outputs Generated
After execution, the following files are created automatically:

Conversion comparison chart
outputs/charts/conversion_comparison.png

Summary metrics table
outputs/tables/summary_metrics.csv

Decision report (main deliverable)
reports/decision_report.md

Example console output:

Final Decision: LAUNCH
Decision Report
The decision_report.md explains:

Conversion lift

Statistical confidence

Decision confidence score

Final recommendation with reasoning

This report represents how analysts communicate insights to stakeholders.

Why This Project Is Valuable
Focuses on decision-making rather than just calculations

Mirrors real-world analytics workflows

Script-based execution without notebooks

Easy to explain in interviews

Suitable for long-term portfolio use

License
This project is licensed under the MIT License.

Author: M S Hephzibah Paul
Role: Aspiring Data Analyst


Author: M S Hephzibah Paul
Role: Data Analyst (Aspiring)
