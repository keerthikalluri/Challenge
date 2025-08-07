def sort(width, height, length, mass):
    # Check if the package is bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Check if the package is heavy
    is_heavy = mass >= 20

    # Determine the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
