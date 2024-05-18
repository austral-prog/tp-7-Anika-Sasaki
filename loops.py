def index_of_by_index(word, list, index):
    for elem in list[index:]:
        if word == elem:
            return index
        index += 1
    return -1

def index_of_empty(list):
    index = 0
    for elem in list:
        if elem == "":
            return index
        index += 1
    return -1

def index_of(word, list):
    index = 0 
    for elem in list:
        if word == elem:
            return index
        index += 1
    return -1

def put(word, list):
    index = 0
    for elem in list:
        if elem == "":
            del list[index]
            list.insert(index, word)
            return index
        index += 1
    return -1

def remove(word, list):
    eliminaciones = 0
    index = 0
    new_list = []
    for elem in list:
        if elem == word:
            new_list.append(index)
            eliminaciones += 1
        index += 1
    for i in new_list:
        del list[i]
        list.insert(i, "")
    return len(new_list)
