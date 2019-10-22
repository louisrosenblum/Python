

def translate(x):
    if x == "A":
        za = 4.0
        return za
    if x == "a":
        zb = 4.0
        return zb
    if x == "A-":
        zc = 3.7
        return zc
    if x == "a-":
        zd = 3.7
        return zd
    if x == "B+":
        ze = 3.3
        return ze
    if x == "b+":
        zf = 3.3
        return zf
    if x == "B":
        zg = 3.0
        return zg
    if x == "b":
        zh = 3.0
        return zh
    if x == "B-":
        zi = 2.7
        return zi
    if x == "b-":
        zj = 2.7
        return zj
    if x == "C+":
        zk = 2.3
        return zk
    if x == "c+":
        zl = 2.3
        return zl
    if x == "C":
        zm = 2.0
        return zm
    if x == "c":
        zn = 2.0
        return zn
    if x == "C-":
        zo = 1.7
        return zo
    if x == "c-":
        zp = 1.7
        return zp
    if x == "D+":
        zq = 1.3
        return zq
    if x == "d+":
        zr = 1.3
        return zr
    if x == "D":
        zs = 1.0
        return zs
    if x == "d":
        zt = 1.0
        return zt
    if x == "F":
        zu = 0.0
        return zu
    if x == "f":
        zv = 0.0
        return zv


result = translate(input("Please enter a letter: "))
print(result)
        
