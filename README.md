# aoc2019
Advent of code 2019, where I maybe actually try to use python for once

Usage
-----
To use this code, you must install the aocutils library in editable mode.
I recommend installing it into a virtual environment, which you can create
and activate as follows:
```
python -m venv venv
source venv/bin/activate
```

To install the library:
```
pip install -e .
```

This tells pip to install links back to the library code.
Any changes to the code will be automatically picked up the next time the
module is loaded.

Development
-----------
To install for development, run:
```
pip install -e .[dev]
```
(where [dev] is the name of the requirements group from setup.py)

Tests
-----
The tests are run with pytest:
```
python3 -m pytest <testfile>
```