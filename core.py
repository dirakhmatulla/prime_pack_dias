import random
from typing import List


def is_prime(x: int) -> bool:
    """Check if x is a prime number."""
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def primes(count: int) -> List[int]:
    """Return first `count` prime numbers in ascending order."""
    result: List[int] = []
    candidate = 2
    while len(result) < count:
        if is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return result


def checksum(x: List[int]) -> int:
    """Compute checksum: for each element add to acc, multiply by 113, mod 10_000_007."""
    acc = 0
    for val in x:
        acc = (acc + val) * 113 % 10_000_007
    return acc


def pipeline(count: int = 1000, seed: int = 100) -> int:
    """Generate `count` primes, shuffle with `seed`, return checksum."""
    prime_list = primes(count)
    random.seed(seed)
    random.shuffle(prime_list)
    return checksum(prime_list)
