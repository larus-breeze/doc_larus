
def create(*dps):
    composed = ','.join(dps)
    cs = 0
    for c in composed[1:]:
        cs ^= ord(c)
    return f"{composed}*{cs:02X}"

print(create("$PLARS", "L", "MC", "1.3"))
print(create("$PLARS", "L", "BAL", "1.25"))
print(create("$PLARS", "L", "BUGS", "15"))
print(create("$PLARS", "L", "QNH", "1013.2"))
print(create("$PLARS", "L", "CIR", "1"))
print(create("$PLARS", "L", "CIR", "0"))
print()
print(create("$PLARS", "H", "MC", "2.1"))
print(create("$PLARS", "H", "BAL", "1.00"))
print(create("$PLARS", "H", "BUGS", "0"))
print(create("$PLARS", "H", "QNH", "1031.4"))
print(create("$PLARS", "H", "CIR", "0"))
print()
print(create("$PLARB", "12.33"))
print(create("$PLARB", "12.33", "-23.8"))
print()
print(create("$PLARV", "1.46", "2.98", "2608", "90"))
print(create("$PLARV", "1.46", "2.98", "2608", "90", "002.23"))
print(create("$PLARS", "L", "MC", "001"))

