"""Functions to automate Conda airlines ticketing system."""

from typing import Generator

def generate_seat_letters(number: int) -> Generator:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ['A', 'B', 'C', 'D']
    count = 0
    while count < number:
        yield seats[count % 4]
        count += 1


def generate_seats(number: int) -> Generator:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    row = 1
    count = 0
    seat_letter_gen = generate_seat_letters(number)
    while count < number:
        yield str(row) + seat_letter_gen.__next__()
        count += 1
        if count % 4 == 0:
            row += 1 if row != 12 else 2 # skip row 13

def assign_seats(passengers: list[str]) -> dict[str, int]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    assigns = {}
    seat_gen = generate_seats(len(passengers))
    for passenger in passengers:
        assigns[passenger] = seat_gen.__next__()
    return assigns

def generate_codes(seat_numbers: list[str], flight_id: str) -> Generator:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f'{seat + flight_id:012}'
