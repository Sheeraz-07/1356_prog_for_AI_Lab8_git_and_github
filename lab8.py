import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
df.to_csv('copy_df.csv',index = False)