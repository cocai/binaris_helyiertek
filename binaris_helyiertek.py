bekeres = input("Give binary numbers: ")
helyi_ertek = 0

for i in range(len(bekeres)):
    helyi_ertek += 2**len(bekeres[i:-1]) * int(bekeres[i])

    megoldas = 2**len(bekeres[i:-1])
    print(megoldas, "*", bekeres[i])

print(f"Result: {helyi_ertek}")
