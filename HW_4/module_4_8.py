def game(terra, power):
    for element in terra:
        for simple in element:
            if simple <= power:
                power += simple
            else:
                break
    return power


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))
