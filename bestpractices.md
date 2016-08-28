# Programming Best Practices

## Goals:

* Easy debugging
* Easy modification
* Understandability (now, after passage of time, and to another person)
* Speed

## Strategies
* Plan – consider likely rate-limiting steps and best methodology before starting
* Modularize – test subcomponents, brainstorm sanity checks
* **_python-specific:_** avoid "import" for scripts -- they will run at the time of import! use the "def main" protocol if you want your code to be both callable like a script and importable like a package -- see [this link](https://en.wikibooks.org/wiki/Python_Programming/Modules)

* Check variable values, types, array sizes by hand (print statements or interrupted run)
* Don’t assume “running” = “working”
* **_python-specific:_** don't define a function in the middle of a program, even though python may let you -- it muddles whether variables are defined inside or outside the function

* Use meaningful variable names (more than one letter!) that are not too similar
* Keep standard defaults: e.g. i, j reserved for integer loop counters
* Replace hardwired numbers with constant names at top
* **_python-specific:_** you can't use the variable name "lambda", it's a reserved word

* Write comments (including at end of command sets, e.g. in if-then)
* Take advantage of helpful visual appearance: white space, syntax highlighting
* **_python-specific:_** standard indentation of code levels is 4 spaces; do not use tabs

* Avoid loops when unnecessary (possible tradeoff with understandability)
* Manage I/O and memory
* Use print and system time statements to find out where code fails/slows
* **_python-specific:_** where speed is essential use libraries written in C and/or set up to multi-thread

