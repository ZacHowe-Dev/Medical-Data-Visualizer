import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
filepath = 'medical_examination.csv'
df = pd.read_csv(filepath)

# 2
# use np.where to find values from the calculation that are > 25
# and return 1 if true(overweight) 0 if false(not overweight)
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100) ** 2) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)

df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     var_name='variable', value_name='value')

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio').fig
    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio').fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #df_heat = df[
        #(df['ap_lo'] <= df['ap_hi']) &
        #(df['height'] >= df['height'].quantile(0.025)) &
       # (df['height'] <= df['height'].quantile(0.975)) &
        #(df['weight'] >= df['weight'].quantile(0.025)) &
        #(df['weight'] <= df['weight'].quantile(0.975))
        # ]
    df_heat = df[(df['weight'] <= df['weight'].quantile(0.975))  # 5 weight is more than the 97.5th percentile
                 & (df['weight'] >= df['weight'].quantile(0.025))  # 4 weight is less than the 2.5th percentile
                 & (df['height'] <= df['height'].quantile(0.975))  # 3 height is more than the 97.5th percentile
                 & (df['height'] >= df['height'].quantile(0.025))  # 2 height is less than the 2.5th percentile
                 & (df['ap_lo'] <= df['ap_hi'])]

    # 12
    corr = df_heat.corr()

    # 13
    #mask = np.triu(np.ones_like(corr, dtype=bool))
    mask= np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(data=corr, annot=True, mask=mask, cmap='coolwarm', linewidths=1, square=True, fmt='.1f', center=0.08, cbar_kws={"shrink":0.5})
    # 16
    fig.savefig('heatmap.png')
    return fig
