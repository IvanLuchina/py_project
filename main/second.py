import seaborn as sns
import pandas as pd
import numpy as np 

df = sns.load_dataset('penguins')
sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm', hue='species', size='body_mass_g') #Точечные графики
sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm', hue='species', size='body_mass_g') #Второй точечный график
g = sns.PairGrid(df, vars=['bill_length_mm', 'flipper_length_mm', 'body_mass_g'])
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
sns.histplot(data=df, x='body_mass_g') #Гистограммы
sns.histplot(data=df, x='bill_length_mm') #Вторая гистограмма
df['height_group'] = pd.cut(df['bill_length_mm'], bins=[0, 35, 42, np.inf], labels=['low', 'middle', 'high']) #Создание нового столбца и гистограмма с оттенком
sns.histplot(data=df, x='flipper_length_mm', hue='height_group')
