def validate_data(df):
    issues = []
    if df.isnull().sum().sum() > 0:
        issues.append("Missing values detected.")
    if df['variant'].nunique() != 2:
        issues.append("Exactly two variants required.")
    return issues
