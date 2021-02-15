#%%
import random

def myRandInt(min=0, max=100):

    if (min > max) or (max < 0):
        return 0
    range = max - min
    return round(random.random() * range + min)