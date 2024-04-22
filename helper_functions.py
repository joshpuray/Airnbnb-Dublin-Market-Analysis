import re
def string_to_list(string):
    li = re.split(r',', string)
    li = set(li) # remove duplicates
    out_li = [word for word in li if word != '']
    return out_li

    