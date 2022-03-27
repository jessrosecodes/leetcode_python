def none_replace(ls):
    ret = []
    prev_val = None
    for i in ls:
        if i:
            prev_val = i
            ret.append(i)
        else:
            ret.append(prev_val)
    return ret

print('Replaced None List:', none_replace([None, None, 1, 2, None, None, 3, 4, None, 5, None, None]))


# Meta Data Engineer Test Prep Questions
# Session 1
# 03/27/2022
#1. Fill the None values with the previous none None value
#[1, None, 1, 2, None] → [1, 1, 1, 2, 2]

list = [1, None, 1, 2, None]

def replace_none():
    newlist = []
    prefval = None