"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

import math

def get_rounds(number: int):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    for rnd in rounds:
        if rnd == number:
            return True
    return False


def card_average(hand: list):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    avg = card_average(hand)
    if math.isclose(avg, (hand[0] + hand[-1]) / 2):
        return True
    if math.isclose(avg, (hand[(len(hand) // 2)])): # all hands odd
        return True
    return False


def average_even_is_average_odd(hand: list):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_sum = 0
    even_sum = 0
    for index, card in enumerate(hand):
        if index % 2 == 0: 
            even_sum += card
        else:
            odd_sum += card
    return even_sum / math.ceil(len(hand) / 2) == odd_sum / (len(hand) // 2)


def maybe_double_last(hand: list):
    """Multiply a Jack card value (11) in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
