from Skyline import skyline

if __name__ == "__main__":
    test_buildings = [
        (6, 1, 6),
        (8, 3, 5),
        (4, 4, 9),
        (2, 7, 12),
        (7, 11, 14)
    ]

    result = skyline(test_buildings)

    print(result)
