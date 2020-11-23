def mess(phrase):
    accumulator = ''
    for char in phrase:
        char = char.replace('r', 'R')
        char = char.replace('s', 'S')
        char = char.replace('t', 'T')
        char = char.replace('v', 'V')
        char = char.replace('w', 'W')
        char = char.replace('x', 'X')
        char = char.replace('y', 'Y')
        char = char.replace('z', 'Z')
        char = char.replace(' ', '-')
        accumulator = accumulator + char
    return accumulator
