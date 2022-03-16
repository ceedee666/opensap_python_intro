# How to use these tests

- `runcaptured()` function will execute the specified input file and return source code, output, errors and variables
- `Analyzer()` class is used to parse AST
- `Testing()` class contains some pre-defined test actions

## Create your own tests

- Use `template_test.py` and `template_exercise.py` to create your own exercises and tests
- Adjust tests where commented (after `runcaptured()`)
- Split tests into 2 files:
    - Functional tests - Is the code producing the required output?
    - Structural tests - Are all demanded structures used (`if`, `for`, *function definition*...)?
- Tests can be split into multiple files for larger exercises/tests to provide more and fine-grained feedback in
  CodeOcean. Likely only necessary for complex tasks

## Notes

- import functions only where needed/tested
- adjust the error return message when using `assert...`


## Examples

See `sample_test.py` and `sample_exercise.py` for examples how to:
- count the number of ifs in a program using AST
- test the output of a user function
- test the standard output of a user program


# File names for exercises in CodeOcean

Rules for file names:

| Filename              | Role Name (CodeOcean)    | Description                                    |
| --------------------- | ------------------------ | ---------------------------------------------- |
| `exercise.py`         | Main file (can be empty) | Potential draft for learners can be added here |
| `reference.py`        | Reference Implementation | Sample solution (**must be hidden!**)          |
| `functional_tests.py` | Test for Assessment      | Unit-Tests (see above for more info)           |
| `structural_tests.py` | Test for Assessment      | Unit-Tests (see above for more info)           |
| `style_test.py`       | Linter for Assessment    | Python file for linting                        |
| `default.pylintrc`    | Regular File             | Configuration file for PyLint                  |


# Linting

- Copy-Paste `style_test.py` and `default.pylintrc` to the exercise
- Copy-Paste the following *default feedback message* into text box:
    - The formatting of your code differs from the recommendation. Please check the details below.
- Set Score for linting file to 0
- **Done**