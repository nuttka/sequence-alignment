
from ast import Raise


filename = 'input'


def Needleman_Wunsch(str1, str2):
    # raise NotImplementedError
    return str1, str2



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