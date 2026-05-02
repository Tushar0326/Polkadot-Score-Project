# Polkadot-Score-Project

A Python project that computes a "Polkadot Score" for ASCII art representations. The score is calculated based on the positions of 'O' characters (representing polkadots or pupils) relative to detected "lips" in the ASCII art.

## Features

- **Score Calculation**: Analyzes ASCII art to detect lips and count 'O' characters inside and outside the lip region, then computes a score.
- **Visualization**: Displays the ASCII art with 'O' characters marked as inside ([O]) or outside ( O ) the lips.
- **Modular Design**: Separate modules for solving, visualizing, and testing.

## Project Structure

- `main.py`: Main script that defines the core functions and runs the program with a sample ASCII art.
- `solver.py`: Contains the `compute_polkadot_score` function for score calculation.
- `visualizer.py`: Contains the `visualize` function to display the ASCII art with annotations.
- `tests.py`: Unit tests for the score calculation function.
- `README.md`: This file.

## How It Works

1. **Lip Detection**: The script identifies the "lips" by finding a line in the ASCII art that contains both ',' and "'" characters. The start and end positions of non-space characters in that line define the lip region.

2. **Pupil Detection**: Searches for a line containing the pattern "O   O" and counts the number of 'O' characters in that line to determine pupil characteristics.

3. **Score Calculation**: Counts 'O' characters inside and outside the lip region, then computes the score using the formula: `outside + inside * pupil_chars`.

4. **Visualization**: Marks 'O' characters as [O] if inside lips, or " O " if outside.

## Installation

Ensure you have Python 3.x installed. No additional dependencies are required.

## Usage

### Running the Main Script

```bash
python main.py
```

This will display the visualization of the sample ASCII art and print the final score.

### Running Tests

```bash
python tests.py
```

This will run the basic test case and print the score.

### Using the Functions

You can import and use the functions in your own code:

```python
from solver import compute_polkadot_score
from visualizer import visualize

art = """
Your ASCII art here
"""

score = compute_polkadot_score(art)
print("Score:", score)

visualize(art)
```

## Example

With the provided ASCII art, the script detects lips, counts 'O' characters, and outputs a visualization along with a score of 72.

## Contributing

Feel free to contribute by improving the detection algorithms, adding more test cases, or enhancing the visualization.

## License

This project is open-source. Please check for any licensing information.