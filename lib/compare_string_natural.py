import jellyfish

def similar_string(string1, string2):
    new_s1 = string1.lower()
    new_s2 = string2.lower()
    lev_distance = jellyfish.damerau_levenshtein_distance(new_s1, new_s2)
    bigger = max(len(new_s1), len(new_s2))
    percent_diff = (bigger - lev_distance)/bigger
    if percent_diff > 0.70:
        return True
    else:
        return False


#A five second solution is not always a good solution!
def old_similar_string(string1, string2):
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
