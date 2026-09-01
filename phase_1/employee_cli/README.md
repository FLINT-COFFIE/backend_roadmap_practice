# Employee Manager CLI

A command-line tool to manage employee records — add, remove, view details, 
and track headcount — built with Python and OOP fundamentals.

## Features
- Add employees (with pay validation — rejects negative pay)
- Remove employees by name
- View individual employee details
- View total employee count
- Auto-generated email and full name via computed properties

## Tech
- Python 3
- No external dependencies

## Setup
\`\`\`bash
git clone https://github.com/FLINT-COFFIE/employee_cli.git
cd employee_cli
python3 -m venv venv
source venv/bin/activate
python3 main.py
\`\`\`

## What I learned
- Classes, `@property`, `@classmethod`
- Custom validation via exceptions
- CLI loop design and input handling
