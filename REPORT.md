# Software Engineering Project Report

## Project Name
Task Manager COCOMO Software Project

## Purpose
The purpose of this software is to provide a simple command-line task manager that helps users track tasks, priorities, and completion status. This implementation supports the software engineering cost estimation assignment by providing an actual working software artifact that can be connected to COCOMO cost driver ratings.

## Functional Requirements
1. The system shall allow a user to add a new task.
2. The system shall allow a user to list saved tasks.
3. The system shall allow a user to mark a task as complete.
4. The system shall allow a user to delete a task.
5. The system shall save tasks persistently using a JSON file.
6. The system shall validate task title and priority.

## Non-Functional Requirements
1. The software should be easy to run from the command line.
2. The software should be modular and maintainable.
3. The software should include automated tests.
4. The software should have readable documentation.

## Design Summary
The project uses a modular Python structure:

- `task.py`: defines the Task data model.
- `storage.py`: handles JSON file saving and loading.
- `manager.py`: contains the main task management logic.
- `cli.py`: provides the command-line interface.
- `tests/test_task_manager.py`: includes automated tests.

## Testing Summary
Pytest is used to verify the main features. The tests check task creation, validation, completion, deletion, and file persistence.

## COCOMO Cost Driver Discussion
The most important cost drivers for this project were TOOL and SCED.

TOOL had a high impact because GitHub, ChatGPT, and Pytest improved productivity, reduced debugging time, and supported automated validation. These tools helped the development process become faster and more reliable.

SCED had a high impact because the schedule influenced how much time could be spent on development, testing, documentation, and cleanup. A tighter schedule increases the importance of planning and using efficient tools.

## Conclusion
The final software is a working Python command-line task manager with modular code, automated tests, documentation, and a clear connection to the COCOMO cost estimation assignment.
