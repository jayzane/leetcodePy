SOURCE = [
    [41, -61, 41, 98, -74, -66, -61, -75, -44, 93, 99, -57, -11, 41, 44, -64, 52, 27, -87, -85],
]
DESTINATION = [
    [-87, -85, -75, -74, -66, -64, -61, -61, -57, -44, -11, 27, 41, 41, 41, 44, 52, 93, 98, 99],
]


def validate(func):
    for n, data in enumerate(SOURCE):
        assert func(data) == DESTINATION[n], 'Validate Error'
    print('success!')
