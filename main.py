from time_calculator import add_time

# Test Case 1
print(add_time("3:00 PM", "3:10")) # Expected Output: 6:10 PM

# Test Case 2
print(add_time("11:30 AM", "2:32", "Monday")) # Expected Output: 2:02 PM, Monday

# Test Case 3
print(add_time("11:43 AM", "00:20")) # Expected Output: 12:03 PM

# Test Case 4
print(add_time("10:10 PM", "3:30")) # Expected Output: 1:40 AM (next day)

# Test Case 5
print(add_time("11:43 PM", "24:20", "tueSday")) # Expected Output: 12:03 AM, Thursday (2 days later)

# Test Case 6
print(add_time("6:30 PM", "205:12")) # Expected Output: 7:42 AM (9 days later)
