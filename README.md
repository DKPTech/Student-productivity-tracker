# Student-productivity-tracker
Student Productivity Tracker is a simple command-line productivity tracking application built using Python and SQLite.
This project helps students record their study tasks, track the number of hours studied, and view their total study time.

Features

- Add study tasks with subject and hours
- View all saved tasks
- Track total study hours
- Delete tasks
- Data stored permanently using SQLite database
- Clean terminal table display

Tech Stack

- Python
- SQLite (database)
- Tabulate (for table formatting)

Project Structure

productivity_tracker.py   # Main program
student_productivity.db   # SQLite database (auto-created)
README.md                 # Project documentation

Installation

1. Install Python.
2. Install required package:

pip install tabulate

3. Download or clone the repository:

git clone https://github.com/yourusername/student-productivity-tracker.git

4. Run the program:

python productivity_tracker.py

How It Works

- User enters study task details.
- Data is stored in a SQLite database.
- Tasks can be viewed or deleted.
- Total study hours can be calculated anytime.

Future Improvements

- Subject-wise statistics
- Weekly study report
- Graph visualization using matplotlib
- Web version using Flask

Author

Dheeraj Kumar Panda
