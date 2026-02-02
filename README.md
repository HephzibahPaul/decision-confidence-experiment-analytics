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

<pre>
Decision_Confidence_Experiment_Project/
├── data/
│   └── experiment_data.csv
├── src/
│   ├── load_data.py
│   ├── validate_data.py
│   ├── metrics.py
│   ├── statistical_tests.py
│   ├── confidence_scoring.py
│   ├── visualization.py
│   └── decision_engine.py
├── outputs/
│   ├── charts/
│   │   └── conversion_comparison.png
│   └── tables/
│       └── summary_metrics.csv
├── reports/
│   └── decision_report.md
├── requirements.txt
├── README.md
└── LICENSE
</pre>

---

<h2>How to Run the Project</h2>

<h3>Step 1: Create and activate virtual environment</h3>
<pre>
python -m venv venv
venv\Scripts\activate
</pre>

<h3>Step 2: Install required libraries</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>Step 3: Run the analysis</h3>
<pre>
python src/decision_engine.py
</pre>

<hr>

<h2>Outputs Generated</h2>

<ul>
  <li>Conversion comparison chart<br>
      <code>outputs/charts/conversion_comparison.png</code></li>
  <li>Summary metrics table<br>
      <code>outputs/tables/summary_metrics.csv</code></li>
  <li>Decision report (main deliverable)<br>
      <code>reports/decision_report.md</code></li>
</ul>

<pre>
Final Decision: LAUNCH
</pre>

<h2>Decision Report</h2>

<p>The <code>decision_report.md</code> explains:</p>
<ul>
  <li>Conversion lift</li>
  <li>Statistical confidence</li>
  <li>Decision confidence score</li>
  <li>Final recommendation with reasoning</li>
</ul>

<p>This report represents how analysts communicate insights to stakeholders.</p>

<h2>Why This Project Is Valuable</h2>

<ul>
  <li>Focuses on decision-making rather than just calculations</li>
  <li>Mirrors real-world analytics workflows</li>
  <li>Script-based execution without notebooks</li>
  <li>Easy to explain in interviews</li>
  <li>Suitable for long-term portfolio use</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>

<p>
Author: M S Hephzibah Paul<br>
Role: Aspiring Data Analyst
</p>
