import numpy as np

def envelope(n, attack, release):
    """
    n       ... dolžina ovojnice v vzorcih
    attack  ... relativno trajanje nastopa (0–1)
    release ... relativno trajanje odhoda (0–1)
    """
    n_attack = int(n * attack)
    n_release = int(n * release)

    # napad (attack)
    x1 = np.logspace(0, 1, n_attack) / 10

    # odhod (release)
    x2 = np.logspace(1, 0, n_release) / 10

    # srednji del (konstanta 1)
    n_middle = n - n_attack - n_release
    if n_middle < 0:
        raise ValueError("Attack + release ne smeta presegati 1")

    middle = np.ones(n_middle)

    # združevanje
    y = np.concatenate((x1, middle, x2))
    return y