# Input nilai variabel
a=input("Masukkan variabel a:")
b=input("Masukkan variabel b:")

# Cetak nilai variabel
print("Variabel a=",a)
print("Variabel b=",b)

# Cetak hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# Konversi niliai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
