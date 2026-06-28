import click
from prime_pack_dias.core import pipeline


@click.command()
@click.option("--count", default=1000, show_default=True, help="Number of prime numbers to generate")
@click.option("--seed", default=100, show_default=True, help="Random seed for shuffling")
def main(count: int, seed: int) -> None:
    """Generate primes, shuffle, compute and print checksum."""
    print(pipeline(count=count, seed=seed))


if __name__ == "__main__":
    main()
