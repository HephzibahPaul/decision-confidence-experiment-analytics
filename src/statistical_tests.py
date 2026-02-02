from statsmodels.stats.proportion import proportions_ztest

def run_ztest(df):
    success = df.groupby('variant')['converted'].sum()
    total = df.groupby('variant')['converted'].count()
    stat, pval = proportions_ztest(success.values, total.values)
    return pval
