
from ast import Raise


filename = 'input'

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
