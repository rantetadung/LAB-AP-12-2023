# Konversi Suhu

print("\nKonversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit\n")

input_celcius = float(input("Masukkan suhu dalam celcius = "))

# Celcius ke Kelvin
suhu_dalam_kelvin = int(input_celcius + 273)
print(f"Hasil konversi dari suhu {round(input_celcius)} derajat Celcius ke Kelvin adalah = {suhu_dalam_kelvin} K")

# Celcius ke Reamur
suhu_dalam_reamur = int((4 / 5) * input_celcius)
print(f"Hasil konversi dari suhu {round(input_celcius)} derajat Celcius ke Reamur adalah = {suhu_dalam_reamur} R")

# Celcius ke Fahrenheit
suhu_dalam_fahrenheit = int((9 / 5) * input_celcius + 32)
print(f"Hasil konversi dari suhu {round(input_celcius)} derajat Celcius ke Fahrenheit adalah = {suhu_dalam_fahrenheit} F")