# current working directory is : /Users/veronicaplanck/Desktop/CS/LsatAnalysis

import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime

now = datetime.now()

CURRENT = now.strftime("%D - %H:%M")
LABEL = "time: " + CURRENT + '\n' + "correct rate of the latest set: "
ACCURATE_RATE = 0

# write the freqency dictionary into a txt file

def write_updated_frequency(dictionary):
    write_updated_data = open("updated_data.txt", 'w')
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for k in range(len(keys)):
        write_updated_data.write("%i\t %i\t" % (keys[k], values[k]))
        write_updated_data.write("\n")
    
    return write_updated_data.close()

# read the previous/existing txt file and update/replace it with adding new wrong quesiton numbers

def read_and_replace(alist):
        
    # read the previous data in nested list form -- As
    read_data = open("updated_data.txt", 'r')
    lines = read_data.readlines()
    
    loaded_data = []
    
    for line in lines:
        sline = line.split()
        for i in range(0, len(sline)): 
            sline[i] = int(sline[i]) 
        loaded_data += [sline]
    
    # convert the nested list A into a dictionary -- B (update_number_frequency)

    update_number_frequency = dict()
    for i in range(len(loaded_data)):
        update_number_frequency[loaded_data[i][0]] = loaded_data[i][1]
    
    # update the B 

    for j in alist:
        update_number_frequency[j] += 1
    
    write_updated_frequency(update_number_frequency)

def LR_update():
    global ACCURATE_RATE
    CHOICE = input("number of the wrong question: ")
    CHOICE = CHOICE.split(' ')
    for i in range(len(CHOICE)):
        CHOICE[i] = int(CHOICE[i])

    ACCURATE_RATE = round((26 - len(CHOICE)) / 26, 4)

    with open("accurate_list.txt", "a") as text_file:
        text_file.write(str(ACCURATE_RATE) + "\n")
    
    return read_and_replace(CHOICE)

def histogram_it():
    
    NUMBER, FREQ = [loadtxt("updated_data.txt", comments = '#', unpack = True, usecols = [i]) for i in range(2)]

    data_for_his = []
    for i in range(len(NUMBER)):
        data_for_his.extend([NUMBER[i]]*int(FREQ[i]))
    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.hist(data_for_his, bins=26, label=LABEL + str(round(ACCURATE_RATE*100,2)) + "%")
    
    plt.title("my LSAT LR frequency of number of wrong question \n set practice ")
    plt.xlabel("question #")
    plt.ylabel("frequency")
    plt.legend(loc='upper right')
    
    return plt.savefig('histogram', dpi=200)


def get_accurate_rate_plot():
    
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    accurate_list = loadtxt("accurate_list.txt", comments = '#', unpack = True, usecols = [0])
    plt.plot(accurate_list,'-^', color="grey", markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2.5)
    
    plt.title("Accurate Rate of My LR Session Practice")
    plt.xlabel("set")
    plt.ylabel("accuracy")
    
    return plt.savefig('accurate_rate', dpi=200)