import sys


def genome_path(dna):
    text = dna[0]
    for j in range(1, len(dna)):
        text += dna[j][-1]
    return text


def main():
    dna = []
    for line in sys.stdin:
        line = line.strip()
        dna.append(line)
    print(genome_path(dna))


if __name__ == '__main__':
    main()
