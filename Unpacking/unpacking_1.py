"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons: int) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagons]


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, wagon_1, *rest = each_wagons_id
    return [wagon_1, *missing_wagons, *rest, first, second]

def add_missing_stops(route: dict[str, str], **stops: dict[str, str] | tuple[str, str]) -> dict[str, str]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, 'stops': list(stops.values())}


def extend_route_information(route: dict[str, str], more_route_information: dict[str, str]) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple[int, str]]]) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [[*item] for item in zip(*wagons_rows)]


# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando"))
# print(fix_wagon_depot([
#                     [(2, "red"), (4, "red"), (8, "red")],
#                     [(5, "blue"), (9, "blue"), (13,"blue")],
#                     [(3, "orange"), (7, "orange"), (11, "orange")],
#                     ]))