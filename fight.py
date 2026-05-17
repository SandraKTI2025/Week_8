import random

def calculate_hit(name, weapon):
    baas = len(name)
    boonus = random.randint(0, len(weapon))

    return baas + boonus
