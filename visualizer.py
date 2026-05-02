def visualize(ascii_art: str):
    lines = ascii_art.split("\n")

    lips_start, lips_end = None, None

    for line in lines:
        if ',' in line and "'" in line:
            indices = [i for i, ch in enumerate(line) if ch != ' ']
            if indices:
                lips_start = min(indices)
                lips_end = max(indices)
                break

    for line in lines:
        new_line = ""
        for i, ch in enumerate(line):
            if ch == 'O':
                if lips_start is not None and lips_start <= i <= lips_end:
                    new_line += '[O]'  # inside lips
                else:
                    new_line += ' O '  # outside lips
            else:
                new_line += ch
        print(new_line)
