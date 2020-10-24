import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

array = [[9.14, 15.72, 0.0],
         [2.9, 44.25, 1.85],
         [0.0, 14.11, 12.00]]
df_cm = pd.DataFrame(array, index=[i for i in "012"], columns=[i for i in "012"])
plt.figure(figsize=(10, 7))
sn.heatmap(df_cm, annot=True, cmap="YlGnBu")
plt.show()
