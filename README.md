# Openspace Organizer

A simple Python application that randomly organizes colleagues into tables for openspace seating arrangements. 

## Features

- **Random Seating Assignment**: Automatically shuffles and assigns people to tables
- **Flexible Table Management**: Creates additional tables when needed
- **CSV File Support**: Load colleague names from a CSV file
- **Sample Data Generation**: Automatically creates sample data if no CSV file exists
- **Visual Display**: Shows the final seating arrangement with table and seat details

## Project Structure

```
openspace-organizer/
├── main.py              # Main application entry point
├── utils/
│   ├── file_utils.py    # CSV file handling utilities
│   ├── openspace.py     # Main openspace organization logic
│   └── table.py         # Table and seat class definitions
└── colleagues.csv       # CSV file with colleague names (auto-generated if missing)
```

## Requirements

- Python 3.7+
- pandas

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install pandas
   ```

## Usage

### Basic Usage

Run the application:
```bash
python main.py
```

The application will:
1. Look for a `colleagues.csv` file in the current directory
2. If the file doesn't exist, create a sample file with 30 random names
3. Load the names from the CSV file
4. Randomly organize them into tables (4 people per table by default)
5. Display the final seating arrangement

### Using Your Own Data

Create a CSV file named `colleagues.csv` with the following format:

```csv
Name
Person 1
Person 2
Person 3
Person 4

etc.
...
```

The CSV file should have a column header named "Name" followed by one name per row.

### Sample Output

```
Simple Openspace organizer algorythm
==============================
Loaded 26 colleagues
Added new table for Yassine

Openspace Layout:

Table 1:
  Seat 1: Alberto
  Seat 2: Mengstu
  Seat 3: Megan
  Seat 4: Klebert

Table 2:
  Seat 1: Yves
  Seat 2: Emmanuel
  Seat 3: Jordi
  Seat 4: Aida

Table 3:
  Seat 1: Nadiya
  Seat 2: Augustin
  Seat 3: Kenny
  Seat 4: Caterina

Table 4:
  Seat 1: Charly
  Seat 2: Sofia
  Seat 3: Choti
  Seat 4: Younes

Table 5:
  Seat 1: Evi
  Seat 2: Hanieh
  Seat 3: Preeti
  Seat 4: Fang

Table 6:
  Seat 1: Hajer
  Seat 2: Floriane
  Seat 3: Dragos
  Seat 4: Moussa

Table 7:
  Seat 1: Yassine
  Seat 2: Marc
  Seat 3: Empty
  Seat 4: Empty

Total people: 26
Total tables: 7
```

## Configuration

### Table Capacity

By default, each table seats 4 people. You can modify this by changing the `capacity` parameter in the `Table` class constructor in `table.py`:

```python
def __init__(self, capacity: int = 4):  # Change 4 to your desired capacity
```

### Number of Initial Tables

The default number of initial tables is 6. You can modify this in the `Openspace` class constructor in `openspace.py`:

```python
def __init__(self, number_of_tables=6):  # Change 6 to your desired number
```

Note: The application will automatically create additional tables if needed to accommodate all people.

## Classes Overview

### `Seat`
- Represents an individual seat at a table
- Tracks whether the seat is free or occupied
- Handles seat assignment logic

### `Table`
- Represents a table with multiple seats
- Default capacity of 4 seats per table
- Manages seat availability and assignments

### `Openspace`
- Main organizer class that manages multiple tables
- Handles the random assignment algorithm
- Creates additional tables when needed
- Displays the final seating arrangement

## Algorithm

The seating assignment algorithm works as follows:

1. **Shuffle**: Randomly shuffle the list of colleague names
2. **Assign**: For each person, try to find an available seat at existing tables
3. **Expand**: If no seats are available, create a new table
4. **Display**: Show the final arrangement with all table and seat assignments

## Error Handling

- Handles missing CSV files by creating sample data
- Manages CSV reading errors gracefully
- Filters out empty or invalid names from the CSV file
- Provides informative error messages
