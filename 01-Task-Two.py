from re import findall
CONVERSION_RATE = 1.609344


def output_stats(stats):
    for key in stats.keys():
        value = stats.get(key)
        print(f'{key}: {round(value, 2)} MPH, {round(value*CONVERSION_RATE, 2)} KPH')


if __name__ == '__main__':
    print('Swallow Speed Analysis 1.0')
    speeds_uk = []

    while True:
        reading = input('Enter the Next Reading: ').upper()
        if not reading:
            break
        try:
            [species, speed] = findall(r'U|E|(?:\-?\d+(?:\.\d+)?)', reading)
        except ValueError:
            print("Your reading wasn't formatted correctly, please try again.")
            continue
        speed = float(speed)
        speeds_uk.append(speed if species == "U" else speed/CONVERSION_RATE)

    speeds_uk = [0.0] if len(speeds_uk) == 0 else speeds_uk
    statistics = {
        'Max Speed': max(speeds_uk),
        'Min Speed': min(speeds_uk),
        'Avg Speed': sum(speeds_uk) / len(speeds_uk)
    }

    output_stats(statistics)
