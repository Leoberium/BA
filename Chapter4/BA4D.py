aa_int_masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def number_of_peptides(mass):
    arr = [0] * (mass + 1)
    masses = set(aa_int_masses.values())
    # initialization
    for m in masses:
        arr[m] += 1
    # calculating the numbers
    min_mass = min(masses)
    for m in range(min_mass, mass + 1):
        for am in masses:
            r = m - am
            if r < 0:
                continue
            arr[m] += arr[r]
    return arr[mass]


def main():
    m = int(input())
    print(number_of_peptides(mass=m))


if __name__ == '__main__':
    main()
