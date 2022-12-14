# input
kalimat = input("Masukkan suatu kalimat : ")

# mendeklarasikan dan memberi nilai
kalimat = [*kalimat]
i = len(kalimat)
invers_kalimat = []

# loop
while i >= 1:
    invers_kalimat.append(kalimat[i-1])
    i -= 1

# kondisi
if kalimat == invers_kalimat:
    print("Kalimat termasuk palindrom")
elif kalimat != invers_kalimat:
    print("Kalimat tidak termasuk palindrom")