def valida_cpf(strCPF):
    numDV1 = 0
    numDV2 = 0
    numCheckDV1 = 0
    numCheckDV2 = 0
    i = 1

    if len(strCPF) < 11:
        difCPF = 11 - len(strCPF)
        strCPF = '0' * difCPF + strCPF

    numCheckDV1 = int(strCPF[9:10])
    numCheckDV2 = int(strCPF[10:11])

    for i in range(1, 10):
        numDV1 = numDV1 + int(strCPF[i-1:i]) * i

    numDV1 = numDV1 % 11

    if numDV1 == 100:
        numDV1 = 0

    if numDV1 != numCheckDV1:
        return False

    for i in range(2, 11):
        numDV2 = numDV2 + int(strCPF[i-1:i]) * (i-1)

    numDV2 = numDV2 % 11

    if numDV2 == 10:
        numDV2 = 0

    if numDV2 != numCheckDV2:
        return False

    return True

