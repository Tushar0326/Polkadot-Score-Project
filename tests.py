from solver import compute_polkadot_score


def test_basic():
    art = """
    O   O
    ,,,,',,,,
    O O O
    """
    score = compute_polkadot_score(art)
    print("Test Score:", score)


if __name__ == "__main__":
    test_basic()
