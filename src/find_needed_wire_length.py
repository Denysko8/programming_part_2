from math import sqrt


def find_needed_wire_length(distance_between_pillars, pillars):
    needed_wire_length = 0

    if 0 >= distance_between_pillars < 100:
        return None

    for i in range(1, len(pillars)):
        if any(0 >= pillar < 100 for pillar in pillars):
            return None
        distance_between_pillars_in_height = pillars[i] - pillars[i - 1]
        wire_between_pillars = sqrt(
            distance_between_pillars_in_height**2 + distance_between_pillars**2
        )
        needed_wire_length += wire_between_pillars
    return round(needed_wire_length, 2)
