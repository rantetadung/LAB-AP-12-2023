# Menentukan Karakter Huruf Kapital, Huruf Kecil dan Angka dari Inputan yang Dilemparkan

print("\nMenentukan Karakter Huruf Kapital, Huruf Kecil dan Angka dari Inputan yang Dilemparkan\n")
print("Pengujian Jenis Karakter")
print("------------------------")
character = input("Karakter = ")

# Huruf Kapital
kapital = character.isupper()
print(f"\nHuruf kapital? {kapital}")

# Huruf Kecil
kecil = character.islower()
print(f"Huruf kecil? {kecil}")

# Angka
angka = character.isdigit()
print(f"Angka? {angka}")