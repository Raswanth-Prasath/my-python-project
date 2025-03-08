# My Python Project

A basic Python project with standard package structure.

## Installation

```bash
# Clone the repository
git clone https://github.com/Raswanth-Prasath/my-python-project.git
cd my-python-project

# Install the package in development mode
pip install -e .
```

## Usage

```python
from my_package.core import hello_world, add

# Print hello world message
print(hello_world())

# Add two numbers
result = add(5, 3)
print(f"5 + 3 = {result}")
```

## Running Tests

```bash
python -m unittest discover
```

## Project Structure

```
my-python-project/
├── my_package/          # Main package directory
│   ├── __init__.py      # Package initialization file
│   └── core.py          # Core functionality
├── tests/               # Test directory
│   ├── __init__.py      # Test initialization file
│   └── test_core.py     # Tests for core.py
├── .gitignore           # Git ignore file
├── README.md            # Project README file
└── setup.py             # Package setup file
```
