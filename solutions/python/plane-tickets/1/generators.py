"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seats = ["A", "B", "C", "D"]
    index = 0

    for _ in range(number):
        yield seats[index]
        index = (index + 1) % 4


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""
    row = 1
    generated = 0

    while generated < number:
        # Skip row 13
        if row == 13:
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:
            if generated >= number:
                break
            yield f"{row}{letter}"
            generated += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""
    seat_gen = generate_seats(len(passengers))
    
    return {
        passenger: next(seat_gen)
        for passenger in passengers
    }


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""
    for seat in seat_numbers:
        # Required format: seat + flight_id + "000"
        code = f"{seat}{flight_id}"
        yield (code + "000")[:12]