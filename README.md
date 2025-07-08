# format-date

A lightweight Python utility for formatting dates using standard format strings.

## Features

- ✅ Simple utility with no external dependencies
- ✅ Customizable output patterns based on input arguments
- ✅ Includes internal unit tests for easy validation

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/format-date.git
cd format-date
```


## Usage

This module provides functions to format date strings according to a specified pattern.

You can integrate it into your own project or run the included tests.

## Running Tests

To run the internal unit tests:

1. Open `format_date.py` in your editor.
2. If you are using VS Code with a configured `launch.json`, press <kbd>F5</kbd> to start debugging and run the tests automatically.
3. All tests should execute and pass if the implementation is correct.

Alternatively, from the terminal:
```bash
python format_date.py
```

**Example**:
```python
from format_date import format_date

formatted = format_date("2025-07-05", separator="/", format_type=DateFormat.DDMMYYYY)
print(formatted)  # Output: 05/07/2025
```


## License

MIT License