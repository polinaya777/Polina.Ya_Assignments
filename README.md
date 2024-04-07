# Polina.Ya_Assignments
This repository contains my assignments for the Prjctr Python course.

## Table of Contents
- [Milestone 1](milestone_1)

Solver for quadratic equations. The user enters an equation as a string of the form: `<a>x^2 + <b>x + <c> = 0`

- [Milestone 2](milestone_2)

Encrypt and decrypt messages using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

- [Milestone 3](milestone_3)

Create [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) with the number of rows from command line: `python triangle.py 5`

- [Milestone 4](milestone_4)

The game: you have a random list of numbers and have to find the pair of numbers such that they add up to a pre-agreed number. Implemented in 2 approaches - more and less time complexity.

- [Milestone 5](milestone_5)

`generate_data.py` generates synthetic data about employees and writes it to `database.csv` file.
`report.py` takes as arguments the database file name and month and will print the search result:
`python report.py database.csv april`

- [Milestone 7](milestone_7)

`app.py` - Flask application with two routes: `/birthdays` and `/anniversaries`. Each route accepts month and department as query parameters. Data provided from `database.csv` file.
`fetch_report.py` dynamically constructs the URL to query the Flask API's `/birthdays` and `/anniversaries` endpoints with the specified month and department. It then parses the JSON responses to display a summary report in the console:
`python fetch_report.py april Engineering`

- [Milestone 8](milestone_8)

`bookshelf.py` - classes for organizing books (Book, Shelf, Room)
`main.py` - creates a sample of books and organize them in the room

- [Assignments in Jupyter notebook]()
