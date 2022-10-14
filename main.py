
from ast import Raise


filename = 'input'

blosum62 = {
    'C': {'C': 9, 'S': -1, 'T': -1, 'P': -3, 'A': 0,  'G': -3, 'N': -3, 'D': -3, 'E': -4, 'Q': -3, 'H': -3, 'R': -3, 'K': -3, 'M': -1, 'I': -1, 'L': -1, 'V': -1, 'F': -2, 'Y': -2, 'W': -2},
    'S': {'C': -1, 'S': 4,  'T': 1,  'P': -1, 'A': 1,  'G': 0,  'N': 1,  'D': 0,  'E': 0,  'Q': 0,  'H': -1, 'R': -1, 'K': 0,  'M': -1, 'I': -2, 'L': -2, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'T': {'C': -1, 'S': 1,  'T': 4,  'P': 1,  'A': -1, 'G': 1,  'N': 0,  'D': 1,  'E': 0,  'Q': 0,  'H': 0,  'R': -1, 'K': 0,  'M': -1, 'I': -2, 'L': -2, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'P': {'C': -3, 'S': -1, 'T': 1,  'P': 7,  'A': -1, 'G': -2, 'N': -1, 'D': -1, 'E': -1, 'Q': -1, 'H': -2, 'R': -2, 'K': -1, 'M': -2, 'I': -3, 'L': -3, 'V': -2, 'F': -4, 'Y': -3, 'W': -4},
    'A': {'C': 0, 'S': 1,  'T': -1, 'P': -1, 'A': 4,  'G': 0,  'N': -1, 'D': -2, 'E': -1, 'Q': -1, 'H': -2, 'R': -1, 'K': -1, 'M': -1, 'I': -1, 'L': -1, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'G': {'C': -3, 'S': 0,  'T': 1,  'P': -2, 'A': 0,  'G': 6,  'N': -2, 'D': -1, 'E': -2, 'Q': -2, 'H': -2, 'R': -2, 'K': -2, 'M': -3, 'I': -4, 'L': -4, 'V': 0,  'F': -3, 'Y': -3, 'W': -2},
    'N': {'C': -3, 'S': 1,  'T': 0,  'P': -2, 'A': -2, 'G': 0,  'N': 6,  'D': 1,  'E': 0,  'Q': 0,  'H': -1, 'R': 0,  'K': 0,  'M': -2, 'I': -3, 'L': -3, 'V': -3, 'F': -3, 'Y': -2, 'W': -4},
    'D': {'C': -3, 'S': 0,  'T': 1,  'P': -1, 'A': -2, 'G': -1, 'N': 1,  'D': 6,  'E': 2,  'Q': 0,  'H': -1, 'R': -2, 'K': -1, 'M': -3, 'I': -3, 'L': -4, 'V': -3, 'F': -3, 'Y': -3, 'W': -4},
    'E': {'C': -4, 'S': 0,  'T': 0,  'P': -1, 'A': -1, 'G': -2, 'N': 0,  'D': 2,  'E': 5,  'Q': 2,  'H': 0,  'R': 0,  'K': 1,  'M': -2, 'I': -3, 'L': -3, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'Q': {'C': -3, 'S': 0,  'T': 0,  'P': -1, 'A': -1, 'G': -2, 'N': 0,  'D': 0,  'E': 2,  'Q': 5,  'H': 0,  'R': 1,  'K': 1,  'M': 0,  'I': -3, 'L': -2, 'V': -2, 'F': -3, 'Y': -1, 'W': -2},
    'H': {'C': -3, 'S': -1, 'T': 0,  'P': -2, 'A': -2, 'G': -2, 'N': 1,  'D': 1,  'E': 0,  'Q': 0,  'H': 8,  'R': 0,  'K': -1, 'M': -2, 'I': -3, 'L': -3, 'V': -2, 'F': -1, 'Y': 2,  'W': -2},
    'R': {'C': -3, 'S': -1, 'T': -1, 'P': -2, 'A': -1, 'G': -2, 'N': 0,  'D': -2, 'E': 0,  'Q': 1,  'H': 0,  'R': 5,  'K': 2,  'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'K': {'C': -3, 'S': 0,  'T': 0,  'P': -1, 'A': -1, 'G': -2, 'N': 0,  'D': -1, 'E': 1,  'Q': 1,  'H': -1, 'R': 2,  'K': 5,  'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'M': {'C': -1, 'S': -1, 'T': -1, 'P': -2, 'A': -1, 'G': -3, 'N': -2, 'D': -3, 'E': -2, 'Q': 0,  'H': -2, 'R': -1, 'K': -1, 'M': 5,  'I': 1,  'L': 2,  'V': -2, 'F': 0,  'Y': -1, 'W': -1},
    'I': {'C': -1, 'S': -2, 'T': -2, 'P': -3, 'A': -1, 'G': -4, 'N': -3, 'D': -3, 'E': -3, 'Q': -3, 'H': -3, 'R': -3, 'K': -3, 'M': 1,  'I': 4,  'L': 2,  'V': 1,  'F': 0,  'Y': -1, 'W': -3},
    'L': {'C': -1, 'S': -2, 'T': -2, 'P': -3, 'A': -1, 'G': -4, 'N': -3, 'D': -4, 'E': -3, 'Q': -2, 'H': -3, 'R': -2, 'K': -2, 'M': 2,  'I': 2,  'L': 4,  'V': 3,  'F': 0,  'Y': -1, 'W': -2},
    'V': {'C': -1, 'S': -2, 'T': -2, 'P': -2, 'A': 0,  'G': -3, 'N': -3, 'D': -3, 'E': -2, 'Q': -2, 'H': -3, 'R': -3, 'K': -2, 'M': 1,  'I': 3,  'L': 1,  'V': 4,  'F': -1, 'Y': -1, 'W': -3},
    'F': {'C': -2, 'S': -2, 'T': -2, 'P': -4, 'A': -2, 'G': -3, 'N': -3, 'D': -3, 'E': -3, 'Q': -3, 'H': -1, 'R': -3, 'K': -3, 'M': 0,  'I': 0,  'L': 0,  'V': -1, 'F': 6,  'Y': 3,  'W': 1},
    'Y': {'C': -2, 'S': -2, 'T': -2, 'P': -3, 'A': -2, 'G': -3, 'N': -2, 'D': -3, 'E': -2, 'Q': -1, 'H': 2,  'R': -2, 'K': -2, 'M': -1, 'I': -1, 'L': -1, 'V': -1, 'F': 3,  'Y': 7,  'W': 2},
    'W': {'C': -2, 'S': -3, 'T': -3, 'P': -4, 'A': -3, 'G': -2, 'N': -4, 'D': -4, 'E': -3, 'Q': -2, 'H': -2, 'R': -3, 'K': -3, 'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': 1,  'Y': 2,  'W': 11}
}


def Needleman_Wunsch(sequence_1, sequence_2):

    main_matrix = np.zeros((len(sequence_1) + 1, len(sequence_2) + 1))
    matching_matrix = np.zeros((len(sequence_1), len(sequence_2)))

    reward_match = 1
    penalty_mismatch = -5
    gap_penalty = -2

    for i in range(len(sequence_1)):
        for j in range(len(sequence_2)):
            if sequence_1[i] == sequence_2[j]:
                matching_matrix[i][j] = reward_match
            else:
                matching_matrix[i][j] = penalty_mismatch

    for i in range(len(sequence_1) + 1):
        main_matrix[i][0] = i * gap_penalty
    for j in range(len(sequence_2) + 1):
        main_matrix[0][j] = j * gap_penalty

    for i in range(1, len(sequence_1) + 1):
        for j in range(1, len(sequence_2) + 1):
            main_matrix[i][j] = max(main_matrix[i - 1][j - 1] + matching_matrix[i - 1][j - 1],
                                    main_matrix[i - 1][j] + gap_penalty,
                                    main_matrix[i][j - 1] + gap_penalty)
    score = main_matrix[-1][-1]

    aligned_1 = ""
    aligned_2 = ""

    seq_i, seq_j = len(sequence_1), len(sequence_2)

    while seq_i > 0 or seq_j > 0:
        if seq_i > 0 and seq_j > 0 and main_matrix[seq_i][seq_j] == main_matrix[seq_i - 1][seq_j - 1] + \
                matching_matrix[seq_i - 1][seq_j - 1]:
            aligned_1 = sequence_1[seq_i - 1] + aligned_1
            aligned_2 = sequence_2[seq_j - 1] + aligned_2

            seq_i -= 1
            seq_j -= 1

        elif seq_i > 0 and main_matrix[seq_i][seq_j] == main_matrix[seq_i - 1][seq_j] + gap_penalty:
            aligned_1 = sequence_1[seq_i - 1] + aligned_1
            aligned_2 = "-" + aligned_2

            seq_i -= 1

        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = sequence_2[seq_j - 1] + aligned_2

            seq_j -= 1

    return aligned_1, aligned_2


def output(title1, sequence1, title2, sequence2):
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Comparing ", title1, " and ", title2)
    print(title1)
    print(sequence1)
    print(title2)
    print(sequence2)


def inputTreatment():
    titles = [""] * 11
    contents = [""] * 11
    with open(filename) as f:
        mylist = f.read().splitlines()

        idx = -1

        for line in mylist:
            if line.startswith(">"):
                idx += 1
                title = line[1:]
                titles[idx] = title
            else:
                contents[idx] += line

    return titles, contents


def main():
    titles, contents = inputTreatment()

    for idx1, content1 in enumerate(contents):
        for idx2, content2 in enumerate(contents):
            sequence1, sequence2 = Needleman_Wunsch(content1, content2)

            output(titles[idx1], sequence1, titles[idx2], sequence2)


if __name__ == "__main__":
    main()
