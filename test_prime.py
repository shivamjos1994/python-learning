from prime import is_prime

# function to test the expected output
def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"Error on is_prime({n}), expected: {expected}")
