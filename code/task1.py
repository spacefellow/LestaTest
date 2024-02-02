def isEven(value):
    return value % 2 == 0


def isEven(value):
    return value & 1 == 0


def isEven(value):
    return (value >> 1) << 1 == value


def isEven(value):
    buf = {'0', '2', '4', '6', '8'}
    return str(value)[-1] in buf
