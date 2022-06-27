# Видео по статистике

Используя датасет о чаевых рассчитать основные статистические показатели, построить гистограмму и boxplot:

- по всей выборке
- только по курящим мужчинам
- только по некурящим женщинам, которые ходят в пятницу на ужин

```python
import seaborn as sns

tips_df = sns.load_dataset("tips")
tips_df.head()

tips_df.describe()
tips_df.hist()
tips_df.boxplot()

smoking_man = tips_df[(tips_df['sex'] == 'Male') & (tips_df['smoker'] == 'Yes')]

smoking_man.describe()
smoking_man.hist()
smoking_man.boxplot()

female = tips_df[(tips_df['sex'] == 'Female') & (tips_df['smoker'] == 'No') & (tips_df['time'] == 'Dinner')]

female.describe()
female.hist()
female.boxplot()
```
