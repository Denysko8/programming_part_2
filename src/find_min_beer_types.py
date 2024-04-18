def min_amount_of_beer_types(workers, beer_types, beer_preferences):
    beer_set = set()
    beer_types_counted = 0

    if not beer_preferences:
        return None

    for i in range(workers):
        possible_set = set()

        for j in range(beer_types):
            if beer_preferences[i * beer_types + j] == "Y":
                possible_set.add(j)

        if not beer_set & possible_set:
            beer_set.update(possible_set)
            beer_types_counted += 1

    if len(beer_preferences) != (workers * beer_types):
        return None

    if workers <= 0 or workers >= 50 or beer_types <= 0 or beer_types >= 50:
        return None

    if 'Y' not in beer_preferences:
        return None

    if beer_types_counted == 0:
        return None
    else:
        return beer_types_counted


# print(min_amount_of_beer_types(2, 2, "YNNY"))  # 2
# print(min_amount_of_beer_types(6, 3, "YNNYNYNYNYYNYYNYNY"))  # 2
# print(min_amount_of_beer_types(1, 3, "YNY"))  #1
# print(min_amount_of_beer_types(2, 2, "YNYN"))  # 1
