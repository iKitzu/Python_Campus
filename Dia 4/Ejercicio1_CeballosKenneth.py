def pares(T_n, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i + 1, n):
            if (T_n[i] + T_n[j]) % k == 0:
                pairs.add((min(T_n[i], T_n[j]), max(T_n[i], T_n[j])))
    return len(pairs)

T = int(input())
for case in range(T):
    text = input("")
    nums = input("")
    n = 0
    k = 0
    T_n = list()
    textoLista = text.split(" ")
    numsLista = nums.split(" ")
    n = int(textoLista[0])
    k = int(textoLista[1])
    for p in range(n):
        number = int(numsLista[p])
        T_n.append(abs(number))
    result = pares(T_n, n, k)
    print("Case {}: {}".format(case + 1, result))