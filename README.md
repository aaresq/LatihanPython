# 📊✨ Analisis Nilai Siswa — Data Analysis Project

Project ini dibuat buat ngolah dan nge-visualisasiin data nilai siswa berdasarkan mata pelajaran.  
Pake **Pandas** buat ngolah data, **Matplotlib** + **Seaborn** buat gambar grafik biar makin keliatan insight-nya.

---

## 🚀 Tech Stack
- 🐍 Python  
- 📦 Pandas  
- 📊 Matplotlib  
- 🎨 Seaborn  

---

## 📥 Input Data
Program baca file:

**`nilai_siswa.csv`**

Format minimal kolom:
- `Nilai`
- `Matpel`
- `nilai` (dipake buat statistik dasar)

> Pastikan nama kolom bener biar gak error ya ges.

---

## 📌 Fitur Analisis

### 🔹 1. Informasi Dataset
- Struktur data (`info()`)
- 5 data pertama (`head()`)
- Statistik deskriptif (`describe()`)

### 🔹 2. Statistik Nilai
- Rata-rata
- Median
- Modus

### 🔹 3. Filter Data per Mata Pelajaran
- Matematika  
- Bahasa Inggris  
- Bahasa Indonesia  

### 🔹 4. Analisis Group By
- Nilai maksimum & minimum per mapel  
- Rata-rata nilai setiap mata pelajaran  

### 🔹 5. Visualisasi
**📊 Bar Chart**  
Rata-rata nilai tiap mapel.

**📦 Boxplot**  
Sebaran nilai (median, quartile, min, max).

---

## 🖼️ Output Grafik
- Bar chart  
- Boxplot  

Keduanya muncul otomatis via `plt.show()`.

---

## ▶️ Cara Menjalankan

1️⃣ Install dependency:
2️⃣ Pastikan file `nilai_siswa.csv` ada di folder yang sama.  
3️⃣ Jalankan script:


---

## 📝 Catatan
- Hati-hati sama huruf besar/kecil di nama kolom.  
- Kalau beda, tinggal sesuaikan di script.  
- Warna grafik bisa kamu custom lagi sesuai selera aesthetic kamu.  

---

## 🧩 Script Utama (Opsional kalau mau dicantumin)
```python
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

