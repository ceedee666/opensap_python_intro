# How to use these tests

- `runcaptured()` function will execute the specified input file and return source code, output, errors and variables
- `Analyzer()` class is used to parse AST
- `Testing()` class contains some pre-defined test actions

## Create your own tests

- Use `template_test.py` and `template_exercise.py` to create your own exercises and tests
- Adjust tests where commented (after `runcaptured()`)
- Split tests into multiple files if you want to provide more and fine-grained feedback in CodeOcean (recommended!)

## Notes

- import functions only where needed/tested
- adjust the error return message when using `assert...`

## Examples

See `sample_test.py` and `sample_exercise.py` for examples how to:
- count the number of ifs in a program using AST
- test the output of a user function
- test the standard output of a user program


# File names

Suggestions for file names:

| filename           | Role Name (CodeOcean)    | Description                                    |
| ------------------ | ------------------------ | ---------------------------------------------- |
| `exercise.py`      | Main file (can be empty) | Potential draft for learners can be added here |
| `reference.py`     | Reference Implementation | Sample solution (**must be hidden!**)          |
| `exercise_test.py` | Test for Assessment      | Unit-Tests                                     |
| `style_test.py`    | Linter for Assessment    | Python file for linting                        |
| `default.pylintrc` | Regular File             | Configuration file for PyLint                  |

# Linting

- Copy-Paste `style_test.py` and `default.pylintrc` to the exercise
- Copy-Paste default feedback message into text box
- Set Score for linting file to 0
- Done