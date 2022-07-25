

def matching_byPhraseEntered(ls, temp_ls):
    count = 0
    if ls in temp_ls:
        count += 1
    return count

def string_matching(ls, temp_ls):
    count = 0
    for i in range(len(ls)):
        temp = ls[i]
        if temp in temp_ls:
            count += 1
            break
            pass

    return count

def sorting_dict(list_forSort):
    for i in range(len(list_forSort) - 1):
        currentMax = list_forSort[i][1]
        currentMax_Index = i
        for j in range(i + 1, len(list_forSort)):
            if currentMax < list_forSort[j][1]:
                currentMax = list_forSort[j][1]
                currentMax_Index = j
        if currentMax_Index != i:
            tup = list_forSort[i]
            list_forSort[i] = list_forSort[currentMax_Index]
            list_forSort[currentMax_Index] = tup
    return list_forSort

def list_of_sentenes():
    f = open("text.txt")
    text_str = f.read()
    ls = text_str.split(".")
    return ls

def func(ls, dict, str1, sentence):
    choice = int(input("Enter 1 if you want phrasal search other wise enter 0 : "))
    if choice == 0:
        for i in range(len(str1)):
            temp_ls = str1[i].split(" ")
            count = string_matching(ls, temp_ls)
            dict[str1[i]] = count
        list_forSort = list(dict.items())
        sorted_list = sorting_dict(list_forSort)
        results = 0
        for i in range(len(sorted_list)):
            if sorted_list[i][1] == 0:
                break
            else:
                results += 1
        print(f"\nSo we get {results} results for you.\n")
        for i in range(len(sorted_list)):
            if sorted_list[i][1] == 0:
                break
            else:
                print(f"{i+1}. {sorted_list[i][0]}")
    else:
        for i in range(len(str1)):
            temp_ls = str1[i].split(" ")
            count = matching_byPhraseEntered(ls, temp_ls)
            dict[str1[i]] = count
        list_forSort = list(dict.items())
        sorted_list = sorting_dict(list_forSort)
        results = 0
        for i in range(len(sorted_list)):
            if sorted_list[i][1] == 0:
                break
            else:
                results += 1
        print(f"\nSo we get {results} results for you.\n")
        for i in range(len(sorted_list)):
            if sorted_list[i][1] == 0:
                break
            else:
                print(f"{i+1}. {sorted_list[i][0]}")



if __name__ == '__main__':
    sentence = input("Enter a sentence : ")
    str1 = list_of_sentenes()
    ls = sentence.split(" ")
    dict = {}
    func(ls, dict, str1, sentence)
