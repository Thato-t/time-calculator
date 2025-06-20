# Time Calculator

A Python function that adds a duration to a start time and handles various time-related calculations, including support for AM/PM format and days of the week.

## Getting Started

To use or edit this project, you can clone the repository using the following command:

```bash
git clone https://github.com/Thato-t/Time_Calculator.git
cd Time_Calculator
```

Replace `your-username` with your actual GitHub username if you fork or host the project yourself.

## Description

The Time Calculator is a Python function that performs time arithmetic. It takes a start time in 12-hour clock format and adds a duration to it, handling various edge cases and time format conversions. The function can also track the day of the week and calculate how many days have passed.

## Features

- Add hours and minutes to a given time
- Support for 12-hour clock format (AM/PM)
- Optional day of the week tracking
- Automatic handling of next day and multiple days later
- Proper time formatting with leading zeros for minutes
- Case-insensitive day of the week input

## Usage

```python
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
```

## Parameters

- `start_time` (required): A string representing the start time in 12-hour clock format (e.g., "3:00 PM")
- `duration` (required): A string representing the duration to add in hours:minutes format (e.g., "3:10")
- `start_day` (optional): A string representing the starting day of the week (case insensitive)

## Return Format

The function returns a string in the following formats:
- Basic: "5:30 PM"
- With day: "5:30 PM, Monday"
- Next day: "5:30 PM (next day)"
- Multiple days: "5:30 PM (n days later)"
- Combined: "5:30 PM, Monday (2 days later)"

## Limitations

- Does not import any Python libraries
- Assumes all input start times are valid times
- Duration minutes must be a whole number less than 60
- Duration hours can be any whole number
