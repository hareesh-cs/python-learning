from stack import Stack


def dec_to_bin(num):
    if num == 0:
        return 0

    s = Stack()

    while num > 0:
        rem = num % 2
        s.push(rem)
        num //= 2

    binary = ""
    while not s.is_empty():
        binary += str(s.pop())

    return binary

print(dec_to_bin(48))
print(dec_to_bin(4))
print(dec_to_bin(35))
