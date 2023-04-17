def add_time(start, duration, day=None):
    # Splitting the start time into hours, minutes and am/pm indicator
    start_time, meridian = start.split()
    start_hour, start_min = map(int, start_time.split(':'))

    # Converting the start time into 24-hour format for easier calculations
    if meridian == 'PM':
        if start_hour != 12:
            start_hour += 12
    elif start_hour == 12:
        start_hour = 0

    # Splitting the duration into hours and minutes
    duration_hour, duration_min = map(int, duration.split(':'))

    # Adding the duration to the start time
    end_hour = start_hour + duration_hour
    end_min = start_min + duration_min

    # Handling the carryover when minutes exceed 60
    if end_min >= 60:
        end_min -= 60
        end_hour += 1

    # Handling the carryover when hours exceed 24
    end_day_count = 0
    while end_hour >= 24:
        end_hour -= 24
        end_day_count += 1

    # Converting the end time back to 12-hour format
    if end_hour == 0:
        end_hour = 12
        meridian = 'AM'
    elif end_hour < 12:
        meridian = 'AM'
    elif end_hour == 12:
        meridian = 'PM'
    else:
        end_hour -= 12
        meridian = 'PM'

    # Building the result string
    result = f"{end_hour:02d}:{end_min:02d} {meridian}"

    # Adding day of the week, if provided
    if day:
        day = day.lower().capitalize()
        result += f", {day}"

    # Adding day count, if necessary
    if end_day_count == 1:
        result += " (next day)"
    elif end_day_count > 1:
        result += f" ({end_day_count} days later)"

    return result
