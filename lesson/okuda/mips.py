s1 = 4
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 1
s7 = 0
t0 = 0
array = [2, -3, 4, -5, 6, -7, 8, -9]

# s2=総和
# s3=正の数の総和
# s4=負の数の総和
# s5=s1と同じになる
# s6=総和した要素数
# s7=総和した最後の数


def L1():
    global s1, s2, s3, s4, s5, s6, s7, t0, array
    if s5 < s1:
        t0 = 1
    else:
        t0 = 0

    if t0 == 0:
        L4()
        exit()

    s7 = array[s6]

    s2 += s7

    if 0 < s7:
        t0 = 1
    else:
        t0 = 0

    if t0 == 0:
        L2()

    s3 += s7

    L3()


def L2():
    global s1, s2, s3, s4, s5, s6, s7, t0, array
    if s7 < 0:
        t0 = 1
    else:
        t0 = 0

    if t0 == 0:
        L3()

    s4 += s7

    L3()


def L3():
    global s1, s2, s3, s4, s5, s6, s7, t0, array
    s5 += 1
    s6 += 1
    L1()


def L4():
    global s1, s2, s3, s4, s5, s6, s7, t0, array
    print("s1: {} \n"
          "s2: {} \n"
          "s3: {} \n"
          "s4: {} \n"
          "s5: {} \n"
          "s6: {} \n"
          "s7: {} \n"
          .format(s1, s2, s3, s4, s5, s6, s7))


L1()


