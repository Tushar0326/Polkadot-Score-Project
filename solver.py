def compute_polkadot_score(ascii_art: str) -> int:
    lines = ascii_art.split("\n")

    lips_start, lips_end = None, None

    # Detect pupils from eye pattern line
for line in lines:
    if "O   O" in line:
        pupil_chars = line.count('O')
        break