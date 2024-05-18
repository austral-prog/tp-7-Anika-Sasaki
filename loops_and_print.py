def enumerate_list(list):
    new_list = []
    index = 0
    for element in list:
        if element != "":
            new = f"{index}. " + element
            index += 1
            new_list.append(new)
    return new_list

def enumerate_backwards(list):
    new_list = []
    index = 0
    for element in list:
        if element != "":
            new = f"{index}. " + str(element[::-1])
            index += 1
            new_list.append(new)
    return new_list
