import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/student_performance.csv")

pass_fail = df['Result'].value_counts()

plt.figure()
pass_fail.plot(kind='pie', autopct='%1.1f%%')
plt.title("Overall Pass/Fail Rate")
plt.ylabel("")
plt.show()

subject_avg = df.groupby('Subject')['Marks'].mean()

plt.figure()
subject_avg.plot(kind='bar')
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

correlation = df['Attendance'].corr(df['Marks'])
print("Correlation between Attendance and Marks:", correlation)

plt.figure()
sns.scatterplot(x='Attendance', y='Marks', data=df)
plt.title("Attendance vs Marks")
plt.show()
