import pandas as pd

df_output = pd.read_csv('.././Dataset/output.csv', header=None)
df_output.columns = ['source', 'target', 'weight']
non_zero_weights_df = df_output.loc[(df_output['weight'] != 0)]
print(len(non_zero_weights_df))
cols_to_norm = ['weight']
non_zero_weights_df[cols_to_norm] = non_zero_weights_df[cols_to_norm].apply(
    lambda x: (x - x.min()) / (x.max() - x.min()))
non_zero_weights_df['relation'] = "U_U"

df_greater_threashold = non_zero_weights_df.loc[(non_zero_weights_df['weight'] >= 0.02)]
print(len(df_greater_threashold))
print(df_greater_threashold['weight'].median(), df_greater_threashold['weight'].mean())
new_cols = ["target", "source", "weight", "relation"]
df_greater_threashold = df_greater_threashold.reindex(columns=new_cols)
df_greater_threashold.to_csv('Dataset/u_u.csv', mode='a', index=False, header=False)
