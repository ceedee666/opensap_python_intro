# How to use these tests

- `runcaptured()` function will execute the specified input file and return source code, output, errors and variables
- `Analyzer()` class is used to parse AST
- `Testing()` class contains some pre-defined test actions
## Create your own tests

- Use `template_test.py` and `template_exercise.py` to create your own exercises and tests
- adjust tests where commented (after `runcaptured()`)

## Notes

- import functions only where needed/tested
- adjust the error return message when using `assert...`

## Examples

See `sample_test.py` and `sample_exercise.py` for examples how to:
- count the number of ifs in a program using AST
- test the output of a user function
- test the standard output of a user program