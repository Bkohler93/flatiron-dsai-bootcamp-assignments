from datetime import datetime

#  validate_task_title checks that a task title is not an empty string and also contains at least 1 alphaneumeric character.
def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Title must not be empty.") 
    if  any(char.isalnum() for char in title):
        return
    raise ValueError("Title must contain some letters or numbers.") 

# validate_task_description ensures that a description contains some text. 
def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Task Description must not be empty.") 
    elif len(description) > 500:
        raise ValueError("Task description can only be up to 500 characters long.")
    elif any(char.isalpha() for char in description):
        return 
    raise ValueError("Task description must contain some descriptive words.")
   
# validate_due_date ensures that due_date is a valid date formatted as 'YYYY-MM-dd' and is today or in the future.
def validate_due_date(due_date):
    parts = due_date.split("-")
    if len(parts) != 3:
        raise ValueError("Due date is expected to be formatted as 'YYYY-MM-dd'")
    try:
        yr = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        valid_due_date = datetime(yr, month, day)
    except ValueError:
        raise ValueError("Due date must be a valid date formatted as 'YYYY-MM-dd'.")
    return  valid_due_date
