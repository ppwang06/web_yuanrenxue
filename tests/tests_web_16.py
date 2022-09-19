"""
17题测试

Z7HSF5X7ZRf3xPsb6d6a6c940ca5edbe7060f7d00593560fYFCZDYjiK
y7nC4UtCx7nO4UUOy
y7nC4UtCx7aE3UUOy   1663565978000"
y7nC4UtCxrUA4UUOy   1663566023000"
"""
from loguru import logger


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def get_cal17():
    base_str = "U9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi+9876543210zyxwvutsrqpomnlkjihgfdecbaZXYWVUTSRQPONABHICESQWK2Fi"
    e = "1663569051000"
    c = []
    o, a, s, ll = 0, 0, 0, 0
    while True:
        if ll >= len(e):
            break
        a = ord(e[ll])
        s = ll % 6
        if s == 0:
            index = int_overflow(a >> 2)
            c.append(base_str[index])
        if s == 1:
            index = int_overflow((2 & o) << 3) | int_overflow(a >> 4)
            c.append(base_str[index])
        if s == 2:
            index = int_overflow((15 & o) << 2) | int_overflow(a >> 6)
            c.append(base_str[index])
            index = a & 63
            c.append(base_str[index])
        if s == 3:
            index = int_overflow(a >> 3)
            c.append(base_str[index])
        if s == 4:
            index = int_overflow((o & 4) << 6) | int_overflow(a >> 6)
            c.append(base_str[index])
        if s == 5:
            index = int_overflow((o & 15) << 4) | int_overflow(a >> 8)
            c.append(base_str[index])
            index = a & 63
            c.append(base_str[index])
        o = a
        ll += 1
    index = int_overflow((o & 3) << 4)
    c.append(base_str[index])
    c.append("FM")
    print("".join(c))


if __name__ == '__main__':
    get_cal17()
