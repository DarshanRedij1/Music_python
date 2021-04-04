import random
import time
from Utilities import *
from playsound import playsound
def music(no_of_notes, raag,patti=pandhari_1):
    i = 0
    notations = []
    x= [0,0,0,0.1,0.2,0.3]

    while True:
        if i<no_of_notes:
            notations.append(Raag[raag.lower()][random.randrange(len(Raag[raag.lower()]))])
            i+=1
        else:
            break
    for j in notations:
        if j in patti:
            playsound(patti[j])
            time.sleep(x[random.randrange(len(x))])





    return print(notations)