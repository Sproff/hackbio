# User Information Organizer

This project organizes user information using an array of objects in Python. Each object represents an individual, storing their details such as name, Slack username, email, hobby, country, discipline, and preferred programming language.

## Project Structure

- The user information is stored in a list of dictionaries.
- Each dictionary contains key-value pairs representing the user’s attributes.
- The program prints the data in a structured and readable format.

## Data Structure Used

The data is structured as a list of dictionaries:

```python
user_info = [
    {
        "Names": "Samuel Ogunleye",
        "Slack Username": "Sproff",
        "Email": "hellodevsproff@gmail.com",
        "Hobby": "Music",
        "Countries": "Nigeria",
        "Discipline": "Biochemistry",
        "Preferred Programming Language": "Python"
    },

   # other details
]
```

## Printing Method

To avoid using loops, a multiline f-string approach is used:

```python
print("User Information:")

print(f'''
Names: {user_info[1]['Names']}
Slack Username: {user_info[1]['Slack Username']}
Email: {user_info[1]['Email']}
Hobby: {user_info[1]['Hobby']}
Countries: {user_info[1]['Countries']}
Discipline: {user_info[1]['Discipline']}
Preferred Programming Language: {user_info[1]['Preferred Programming Language']}
''')

# other details
```

## How to Run the Script

1. Ensure you have Python installed (version 3.x recommended).
2. Copy and paste the script into a Python environment.
3. Run the script to see the formatted user details displayed in the console.

## Purpose

This project demonstrates how to structure and display user data in a clean, readable format without using loops, functions, or complex logic.

## Author

This script was created as a simple demonstration of basic Python data structures and string formatting.
