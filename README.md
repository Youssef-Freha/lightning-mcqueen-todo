# Lightning McQueen To-Do List

This is my solution for Task 3 in MIA Robotics Electrical Team Training. 

It is a simple command-line To-Do List application written in Python to help Lightning McQueen organize his tasks before the race.

## Features
- Add new tasks to the list.
- View all tasks with status (Done or Pending).
- Mark any task as completed.
- Delete tasks from the list.

## How to Run
1. Make sure you have Python installed.
2. Open terminal in the project folder.
3. Run the script:
   python main.py

## Challenges
While building this project, I needed to make sure the program doesn't crash if the user enters letters instead of numbers when picking a task. I fixed this by using `try-except` blocks to handle invalid inputs safely.
