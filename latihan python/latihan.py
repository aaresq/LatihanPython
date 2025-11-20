import pandas as pd 
import seaborn as sn
import matplotlib.pyplot as plt

# Load the
data = pd.read_csv('nilai_siswa.csv') 
# Display the first few rows of the datales
print(data.info())
print(data.head())
print(data.describe())
data.info()

#print("Rata-rata:", data.gr['Nilai'].mean())
#print("Median:", data['Nilai'].median())
#print("Modus:", data['Nilai'].mode()[0])

matematika = data [data ['Mapel'] == 'Matematika']
print(matematika)

Inggris = data [data ['Mapel'] == 'Bahasa Inggris']
print(Inggris)

Indonesia = data [data ['Mapel'] == 'Bahasa indonesia']
print(Indonesia)

produktif = data [data ['Mapel'] == 'Produktif']
print(produktif)

data.groupby('Mapel')['Nilai'].agg(['max','min'])
rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar', color=['blue', '#ff7f0b'])
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sn.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('sebaran Nilai per mata pelajaran')
plt.tight_layout()
plt.show()


#1. Mapel mana yang memiliki rata-rata nilai tertinggi? Matemtika
#2. Mapel mana yang memiliki nilai terendah? Bahasa Indonesia dan Produktif
#3. Bagaimana visualisasi membantu dalam memahami data? Dengan visualisasi, kita dapat dengan mudah melihat perbandingan nilai rata-rata antar mata pelajaran serta sebaran nilai siswa dalam setiap mata pelajaran. Grafik batang menunjukkan rata-rata nilai, sementara boxplot memperlihatkan distribusi nilai, termasuk median, kuartil, dan outlier.
#4. Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data? Saya belajar bagaimana menggunakan library pandas untuk analisis data dan matplotlib serta seaborn untuk visualisasi data. Saya juga memahami pentingnya visualisasi dalam menyampaikan informasi secara efektif.
#5. Kesulitan apa yang kamu alami dalam membuat grafik? Beberapa kesulitan yang saya alami termasuk memilih jenis grafik yang tepat untuk data yang ada, menyesuaikan tampilan grafik agar lebih informatif, dan memahami parameter-parameter dalam fungsi plotting untuk mendapatkan hasil yang diinginkan.
#6. Menurtu kamu AI apa membantu dalam analysis sebua data? Ya, AI sangat membantu dalam analisis data karena dapat mempercepat proses pengolahan data, memberikan wawasan yang lebih mendalam melalui teknik analisis lanjutan, dan membantu dalam visualisasi data yang kompleks sehingga lebih mudah dipahami.
#7. Bagaimana menurut kamu AI dapat membantu dalam proses pembelajaran data science? AI dapat membantu dalam proses pembelajaran data science dengan menyediakan alat dan teknik yang memudahkan analisis data, memberikan rekomendasi berdasarkan pola yang ditemukan dalam data, serta memungkinkan otomatisasi tugas-tugas rutin sehingga fokus dapat dialihkan pada aspek kreatif dan strategis dari data science.