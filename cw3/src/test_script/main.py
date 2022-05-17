from typing import Iterable, Union, Any
def de_bruijn(k: Union[Iterable[Any], int], n: int) -> str:
    """de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return [alphabet[i] for i in sequence]

br = de_bruijn([0, 1], 8)
n = len(br)
final = []
for i in range(n):
    if br[i]==1 and br[(i-1)%n]==0 and br[(i-2)%n] == 1 and br[(i-3)%n]==1:
        final.append(2*br[i] + 1)
    else:
        final.append(2*br[i])

final = final + final[:7]
print("Data:")
print("\n".join("0000000"+str(v) for v in final), end='')
print()
print("Initial:")
print("0000")
print("Final:")
print(str(len(final)).zfill(4))

