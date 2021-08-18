# O(n^1.58) time | O(log(n)) space
def karatsuba(n1, n2):
    if n1 < 10 or n2 < 10:
        return n1 * n2

    half = max(len(str(n1)), len(str(n2))) // 2
    a = n1 // (10 ** half)
    b = n1 % (10 ** half)
    c = n2 // (10 ** half)
    d = n2 % (10 ** half)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_plus_bc * (10 ** half) + bd

if __name__ == "__main__":
    n1 = 123456789
    n2 = 987654321
    print(karatsuba(n1, n2))