# Mencari Luas dan Keliling Segitiga

print("\nMenghitung luas permukaan dan keliling segitiga\n")
X = input("Masukkan Nilai X = ")
Y = input("Masukkan Nilai Y = ")
Z =  (X ** 2 + Y ** 2) ** 0.5

keliling = X + Y + Z
luas = (Y * X) / 2

print(f"Jadi, luas segitiga adalah {luas: .2f}")
print(f"Jadi, keliling segitiga adalah {keliling: .2f}")