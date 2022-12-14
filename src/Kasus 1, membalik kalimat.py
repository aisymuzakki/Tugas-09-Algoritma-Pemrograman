input_kalimat = input("Masukkan suatu kalimat : ")

# deklarasi:
kalimat = [*input_kalimat]
i = len(kalimat)
inverse_kalimat = []

# loop:
while i >= 1:
    inverse_kalimat.append(kalimat[i-1])
    i -= 1

print(inverse_kalimat)

print("END")
