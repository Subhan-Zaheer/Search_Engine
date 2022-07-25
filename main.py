

def string_matching(ls, temp_ls):
    count = 0
    for i in range(len(ls)):
        temp = ls[i]
        k = 0   # will point a first index of list and move in increasing order.
        l = len(temp_ls) - 1   # will point at last index of list and move in decreasing order.
        a = int(len(temp_ls)/2)   # will point at center of list and move towards k (starting point)
        b = int(len(temp_ls)/2)   # will point at center of list and move towards l (ending point)
        while k <= a or l >= b:
            if temp == temp_ls[k] or temp == temp_ls[l] or temp == temp_ls[a] or temp == temp_ls[b]:
                count += 1
                break
            k += 1
            l -= 1
            a -= 1
            b += 1

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

if __name__ == '__main__':
    sentence = input("Enter a sentence : ")
    str1 = ["Python is good.", "Python is not python snake.", "This is good book."]
    ls = sentence.split(" ")
    dict = {}
    for i in range(len(str1)):
        temp_ls = str1[i].split(" ")
        count = string_matching(ls, temp_ls)
        dict[str1[i]] = count
    list_forSort = list(dict.items())
    sorted_list = sorting_dict(list_forSort)
    for i in range(len(sorted_list)):
        if sorted_list[i][1] == 0:
            break
        else:
            print(sorted_list[i][0])
