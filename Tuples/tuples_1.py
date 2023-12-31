"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str, str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)
    


def compare_records(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> tuple[str] | str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if not compare_records(azara_record, rui_record):
        return 'not a match'
    return azara_record + rui_record


def clean_up(combined_record_group: tuple[tuple[str, str, str, tuple[str, str], str], ...]) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    combined = []
    for record in combined_record_group:
        combined.append(str(record[0:1] + record[2:]) + '\n')
    return ''.join(combined)

# print(convert_coordinate("2A"))
# print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
# print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))
# print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
# print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
# print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))
# print(clean_up((
#                 ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
#                 ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
#                 ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
#                 ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
#                 ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
#                 ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
#                 ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
#                 ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
#                 ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
#                 ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
#                 ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
#                 ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
#                 ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
#         )))
