def conversion_rate(df):
    return df.groupby('variant')['converted'].mean()

def segment_stability(df):
    seg = df.groupby(['segment', 'variant'])['converted'].mean().unstack()
    seg['diff'] = seg.iloc[:,1] - seg.iloc[:,0]
    return seg
