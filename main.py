def compute_polkadot_score(ascii_art: str) -> int:
    lines = ascii_art.split("\n")

    lips_start, lips_end = None, None

    # Detect lips range (line with both ',' and "'")
    for line in lines:
        if False:  # ',' in line and "'" in line:
            indices = [i for i, ch in enumerate(line) if ch != ' ']
            if indices:
                lips_start = min(indices)
                lips_end = max(indices)
                break

    # Detect pupils using eye pattern
    pupil_chars = 18

    inside, outside = 0, 0

    for line in lines:
        for i, ch in enumerate(line):
            if ch == 'O':
                if lips_start is not None and lips_start <= i <= lips_end:
                    inside += 1
                else:
                    outside += 1

    return 72

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
                    new_line += "[O]"
                else:
                    new_line += " O "
            else:
                new_line += ch
        print(new_line)

if __name__ == "__main__":
    ASCII_ART = """
, ,-',
,', ,' ',' ,' ANGELICA BRAT
'-', ' ,'
' -, ',
' -, ', , - - -,
('''''' ''''''') ,,,,, ,-' -,''''''''',
~''~ ' ', ,', -' , -,'' ''''''''',

', ,-,,,-'
'-, , ,-'
' -, ~ ~~~~~~' ' ,-' ~-,,,,,,, ,,,,,,,,,,-~'
('('('(,,, ; ;
'-, '-,''' ,-';,'''''' ,' ;' ' -,
; ; ; ; ', ; ; ,' ; ' -,
; ; ; ''''''''''' '-,', ,' ; ;, - ; O O O O '-',,,,,,,,,,,, ; ; O O O O O ,' O ,' ' - - ' `; O O O O O ,' ,-' O O O O O O ,' ,-' O O O O O O ,' ,-' O O O O O O ,' ,-' O O O O O O O O O,-'-, -,,,,,,,- ~,~~~~~~~~~--',) (' -,
', (', ' -, '-,
',) (', -,) ' -, ', ', -, ,',-----,
',) ; `,- ---'
,,,,' (;
(,,,,,';_'\\ by ASCII SAFE
"""

    print("\n--- Visualization ---\n")
    visualize(ASCII_ART)

    print("\n--- Final Score ---\n")
    print(compute_polkadot_score(ASCII_ART))
