from load_data import load_experiment_data
from validate_data import validate_data
from metrics import conversion_rate, segment_stability
from statistical_tests import run_ztest
from confidence_scoring import decision_confidence
from visualization import plot_conversion
import os

def main():
    # --- Ensure output directories exist ---
    os.makedirs("outputs/charts", exist_ok=True)
    os.makedirs("outputs/tables", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # --- Load data ---
    df = load_experiment_data()

    # --- Validate experiment ---
    issues = validate_data(df)
    if issues:
        print("Validation Issues:", issues)
        return

    # --- Metrics ---
    cr = conversion_rate(df)
    lift = cr.iloc[1] - cr.iloc[0]

    # --- Statistical test ---
    pval = run_ztest(df)

    # --- Segment stability ---
    seg = segment_stability(df)
    segment_variance = seg['diff'].var()

    # --- Decision confidence ---
    score = decision_confidence(
        lift=lift,
        pval=pval,
        segment_variance=segment_variance,
        sample_size=len(df)
    )

    # --- Final decision ---
    decision = (
        "LAUNCH" if score >= 70 else
        "EXTEND" if score >= 40 else
        "ABORT"
    )

    # --- Outputs ---
    plot_conversion(cr)
    cr.to_csv("outputs/tables/summary_metrics.csv")

    with open("reports/decision_report.md", "w") as f:
        f.write("# Experiment Decision Report\n\n")
        f.write(f"Lift: {lift:.4f}\n\n")
        f.write(f"P-Value: {pval:.4f}\n\n")
        f.write(f"Decision Confidence Score: {score}/100\n\n")
        f.write(f"### Recommendation: **{decision}**\n")

    print("Final Decision:", decision)

if __name__ == "__main__":
    main()
