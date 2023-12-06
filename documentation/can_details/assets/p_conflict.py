from functools import reduce

# Calculation of the probability that two packets will meet at the base ID allocation. The probability 
# is calculated based on the birthday pradoxxon.

def birthday_problem(persons, days):
    return 1.0 - reduce(lambda x, y: x*y, range(days-persons+1, days), 1)/days**(persons-1)

# validate formula, see https://de.wikipedia.org/wiki/Geburtstagsparadoxon
# p = birthday_problem(23, 365)
# print(p)

datagram_slots = 200_000*64 # 200_000 time slots, 64 usable request ids
devices = 10                # 10 Devices at CAN bus

p =  birthday_problem(devices, datagram_slots)
print(f"P for {devices} Devices to confilct: {p*1e3:.3f} per mille")
