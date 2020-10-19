def get_nm(sys1,nmb,sys2):
    #decimal to binary
    if sys2 == 2:
        a = int(nmb)
        b = ""

        while a/2 != 0:
            b += str(a % 2)
            a = a // 2
        return b[::-1]

    # decimal to octal
    if sys2 == 8:
        b = ""

        while int(nmb) / 8 != 0:
            b += str(int(nmb) % 8)
            nmb = int(nmb) // 8
        return b[::-1]
    # decimal to decimal
    if sys2 == 10:
        return nmb
    # decimal to hexdecimal
    if sys2 == 16:
        lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        lst2 = []
        nm = nmb
        sttr = ""

        while True:
            res = nm % 16
            if int(res) == 0:
                break
            lst2.append(int(res))
            nm /= 16
        lst2 = lst2[::-1]
        for i in lst2:
            sttr += lst[i - 1]
        return sttr

sys1 = int(input("positional system_1: "))
nmb = str(input("number: "))
sys2 = int(input("positional system_2: "))

#binary to decimal
if sys1 == 2:
    a = str(nmb)
    b = 0
    c = 0

    while b < len(a):
        c += int(a[b]) * (2 ** (len(a) - b - 1))
        b += 1
    nmb = c

#octal to decimal
if sys1 == 8:
    a = str(nmb)
    b = 0
    c = 0

    while b < len(a):
        c += int(a[b]) * (8 ** (len(a) - b - 1))
        b += 1
    nmb = c

#decimal to decimal
if sys1 == 10:
    nmb = nmb

#hexdecimal to decimal
if sys1 == 16:
    nmb = int(nmb, 16)

print(get_nm(sys1,nmb,sys2))

