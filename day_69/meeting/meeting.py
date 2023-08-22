# 1st solution
def meeting(names: str) -> str:
    """
    Makes the string uppercase and sorted it in alphabetical order
    by last name.
    """
    guests = names.upper().split(';')
    formatted_guests = []

    for guest in guests:
        first_name, last_name = guest.split(':')
        formatted_guests.append(f"({last_name}, {first_name})")

    sorted_guests = sorted(formatted_guests)

    return ''.join(sorted_guests)


# 2nd solution
def meeting_one_liner(names: str) -> str:
    return ''.join(sorted([f"({last_name}, {first_name})" for guest in names.upper().split(';') for first_name, last_name in guest.split(':')]))