# Task Manager COCOMO Software Project

## Project Overview
This project is a small command-line task management application built in Python. It allows users to create, list, complete, and delete tasks. The project was created as the actual software implementation for the COCOMO cost driver analysis.

## Features
- Add a task with title, description, priority, and optional due date
- List all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to a JSON file
- Unit tests using Pytest

## Tools Used
- GitHub: version control and team collaboration
- ChatGPT: development assistance, debugging, and documentation support
- Pytest: automated testing
- Python: main programming language

## How to Run

```bash
python -m task_manager.cli add "Finish report" --priority high
python -m task_manager.cli list
python -m task_manager.cli complete 1
python -m task_manager.cli delete 1
```

From a local environment, install the project first:

```bash
pip install -e .
```

Then run:

```bash
task-manager add "Finish report" --priority high
task-manager list
```

## How to Test

```bash
pip install pytest
pytest
```

## Team Member
| Name | Role |
|---|---|
| Shyam Thummar | Developer |
| Liam Binell | Developer |
| Abigail Orellana | Developer |
| Taha Farooqui | Developer |
| Reshma Sheikh | Developer |
| Ahmad Shawkha | Developer |
| Jacob C | Developer |
| Diego Aragon | Tester |
| Emmanuel Sanchez | Tester |
| Juan Cruz | Tester |
| Brandon Dutt | Tester |


## COCOMO Connection
The project supports the COCOMO analysis because it includes real development work, testing, tool usage, and documentation. TOOL and SCED were selected as major impact drivers because tool support and schedule pressure affected implementation and testing effort.
