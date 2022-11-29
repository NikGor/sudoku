# SUDOKU SOLVER

This is a simple sudoku solver written in _python_. It uses a _backtracking algorithm_ to solve the puzzle.

## Usage

To use the solver, simply run the following command:

```bash
python3 sudoku.py
```

The program will prompt you to enter the sudoku puzzle. 
The puzzle should be entered as a single line of 81 characters, with '*' representing an empty cell. 
divided into 9 rows of 9 characters each.
For example, the following puzzle:
    
```bash
5*3****7*
*1*3*98**
****4****
**1*****9
*****6***
*9*2*83**
**74*2*8*
*2**6****
****1*4**
```

the program can highlight the input with colours:

**green** - if the empty cell has only one possible value

**yellow** - if the empty cell has two possible values

**red** - if the empty cell has three possible values

**white** - if the empty cell has more than three possible values

the result will be printed using a 3x3 grid format:
```bash
-------------------------
| 5 4 3 | 6 8 1 | 9 7 2 |
| 7 1 6 | 3 2 9 | 8 4 5 |
| 2 8 9 | 7 4 5 | 6 3 1 |
-------------------------
| 8 7 1 | 5 3 4 | 2 6 9 |
| 4 3 2 | 1 9 6 | 7 5 8 |
| 6 9 5 | 2 7 8 | 3 1 4 |
-------------------------
| 9 6 7 | 4 5 2 | 1 8 3 |
| 1 2 4 | 8 6 3 | 5 9 7 |
| 3 5 8 | 9 1 7 | 4 2 6 |
-------------------------
```

## Demo

[![asciicast](https://asciinema.org/a/W08IQQ9Ty4mLNJXBmqbYTiBuj.svg)](https://asciinema.org/a/W08IQQ9Ty4mLNJXBmqbYTiBuj)


## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details


