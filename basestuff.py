from functools import lru_cache

class Alphabet:
    def __getitem__(self, index):
        return chr(index)

alphabet = Alphabet()


def is_emirp(n, b):
    based = as_base(n, b)
    return based != based[::-1] and is_prime(n) and is_prime(from_base(based[::-1], b))


@lru_cache()
def is_prime(num):
    if num in (2, 3):
        return True
    for d in range(2, int(num ** 0.5) + 1):
        if not num % d:
            return False
    return True


def as_base(num, base):
    # alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=<>,./?;:'[{]}\||"
    cur = ""
    while num:
        num, m = divmod(num, base)
        cur = alphabet[m] + cur
    return cur


def from_base(num, base):
    # if 2 <= base <= 36:
    #     return int(num, base)
    things = list(reversed(num))
    value = 0
    while things:
        value *= base
        value += ord(things.pop())
    return value


assert from_base(as_base(5423, 93), 93) == 5423


def emirpness(num):
    return sum(is_emirp(num, base) for base in range(2, num))

if __name__ == '__main__':
    top = 0
    for i in range(2, 100000000):
        en = emirpness(i)
        if en > top:
            print(i, "has emirpness", emirpness(i))
            top = en
