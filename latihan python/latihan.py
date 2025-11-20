import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata-rata nilai:", data['nilai'].mean())
print("Median nilai:", data['nilai'].median())
print("Modus nilai:", data['nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(inggris) 

Indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(Indonesia)

data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color=['blue', '#ff7f0e', 'green', 'red', 'purple'])
plt.title('Rata-rata Nilai Siswa per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Rata-rata Nilai')
plt.show()

sn.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Matpel')
plt.tight_layout()
plt.show()