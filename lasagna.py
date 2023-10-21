EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate amount of baking time remaining.

    :param time_in_oven: int - Time already spent in oven.
    :return: int - Time remaining (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate amount of time needed to prepare a given amount of layers
    :param number_of_layers: int - Number of layers to prepare
    :return: int - amount of time needed to prepare layers in minutes
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate amount of time elapsed in minutes
    :param number_of_layers: int - Number of layers prepared
    :param elapsed_bake_time: int - Time that lasagna has been baking
    :return: int - Time elapsed (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

