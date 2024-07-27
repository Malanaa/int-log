#returns True if similar and Returns False if not similar


def similar_string(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    sim_var = 0

    if string1 == string2:
        return True

    elif len(string2) > len(string1):
        for i in range(len(string2)):
            if string2[i] in string1:
                sim_var += 1

        if sim_var > len(string2)/1.2:
            return True
        else:
            return False

    elif len(string1) > len(string2):
        for i in range(len(string2)):
            if string1[i] in string2:
                sim_var += 1

        if sim_var > len(string1)/1.5:
            return True
        else:
            return False

