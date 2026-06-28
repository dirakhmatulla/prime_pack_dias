"""
Tests for prime_pack_dias.
Covers: is_prime, primes, checksum, pipeline — positive and negative cases.
"""
import pytest
from prime_pack_dias.core import is_prime, primes, checksum, pipeline


# ── is_prime ──────────────────────────────────────────────────────────────────

class TestIsPrime:
    # --- positive: known primes ---
    @pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                                    71, 73, 79, 83, 89, 97])
    def test_known_primes(self, n):
        assert is_prime(n) is True, f"{n} must be prime"

    # --- negative: composites and edge cases ---
    @pytest.mark.parametrize("n", [0, 1, 4, 6, 8, 9, 10, 12, 14, 15,
                                    16, 18, 20, 21, 25, 27, 35, 49, 77,
                                    91, 100, 121])
    def test_known_composites(self, n):
        assert is_prime(n) is False, f"{n} must not be prime"

    def test_returns_bool(self):
        assert type(is_prime(2)) is bool
        assert type(is_prime(4)) is bool

    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_even_ge_4_not_prime(self):
        for n in range(4, 200, 2):
            assert is_prime(n) is False, f"even {n} must not be prime"

    # explicit checks from the spec ("typical broken code" hints)
    def test_43_is_prime(self):
        assert is_prime(43) is True

    def test_1_is_not_prime(self):
        assert is_prime(1) is False

    def test_larger_primes(self):
        for n in [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]:
            assert is_prime(n) is True

    def test_larger_composites(self):
        for n in [99, 102, 111, 115, 119, 121, 125, 133, 143]:
            assert is_prime(n) is False


# ── primes ────────────────────────────────────────────────────────────────────

class TestPrimes:
    def test_length_1(self):
        assert len(primes(1)) == 1

    def test_length_10(self):
        assert len(primes(10)) == 10

    def test_length_100(self):
        assert len(primes(100)) == 100

    def test_length_1000(self):
        assert len(primes(1000)) == 1000

    # spec hint: primes(2) must NOT return [1, 2]
    def test_two_primes(self):
        assert primes(2) == [2, 3]

    def test_first_prime_is_2(self):
        assert primes(1) == [2]

    def test_first_ten(self):
        assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_ascending_order(self):
        result = primes(50)
        assert result == sorted(result)

    def test_all_elements_prime(self):
        for p in primes(50):
            assert is_prime(p), f"{p} in primes list is not prime"

    def test_no_composites(self):
        result = set(primes(30))
        for n in [1, 4, 6, 8, 9, 10]:
            assert n not in result

    def test_no_duplicates(self):
        result = primes(100)
        assert len(result) == len(set(result))

    def test_1000th_prime_is_7919(self):
        """The 1000th prime number is 7919."""
        assert primes(1000)[-1] == 7919

    def test_returns_list(self):
        assert isinstance(primes(5), list)

    # 1 not in list
    def test_one_not_included(self):
        assert 1 not in primes(10)


# ── checksum ──────────────────────────────────────────────────────────────────

class TestChecksum:
    def test_empty_list(self):
        assert checksum([]) == 0

    def test_single_one(self):
        # (0+1)*113 = 113
        assert checksum([1]) == 113

    def test_single_two(self):
        # (0+2)*113 = 226
        assert checksum([2]) == 226

    def test_two_elements(self):
        # [1,2]: 113 → (113+2)*113 = 12_995
        assert checksum([1, 2]) == 12_995

    def test_spec_example(self):
        """Spec example: checksum([1, 2, 6, 24]) == 6_012_369."""
        assert checksum([1, 2, 6, 24]) == 6_012_369

    def test_result_in_range(self):
        for lst in [[], [1], [2, 3], list(range(1, 100))]:
            r = checksum(lst)
            assert 0 <= r < 10_000_007

    def test_returns_int(self):
        assert isinstance(checksum([1, 2, 3]), int)

    def test_order_matters(self):
        """Checksum is order-sensitive."""
        assert checksum([1, 2]) != checksum([2, 1])

    def test_modulo_applied(self):
        """Large input must stay within modulo bound."""
        big = list(range(1, 500))
        assert checksum(big) < 10_000_007


# ── pipeline ──────────────────────────────────────────────────────────────────

class TestPipeline:
    def test_default_result(self):
        """count=1000, seed=100 → 7_785_816 (from the spec)."""
        assert pipeline() == 7_785_816

    def test_explicit_args(self):
        assert pipeline(count=1000, seed=100) == 7_785_816

    def test_returns_int(self):
        assert isinstance(pipeline(count=10, seed=0), int)

    def test_result_in_range(self):
        assert 0 <= pipeline(count=10, seed=42) < 10_000_007

    def test_deterministic(self):
        """Same args → same result."""
        assert pipeline(count=50, seed=7) == pipeline(count=50, seed=7)

    def test_seed_affects_result(self):
        assert pipeline(count=100, seed=0) != pipeline(count=100, seed=1)

    def test_count_affects_result(self):
        assert pipeline(count=10, seed=100) != pipeline(count=20, seed=100)
