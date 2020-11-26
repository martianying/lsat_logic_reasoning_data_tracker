# initial setup 
import funcs
import numpy as np

numbers = np.arange(1, 27)
frequency = [0] * max(numbers)
setup = dict()

for i in range(max(numbers)):
    setup[numbers[i]] = frequency[i]

funcs.write_updated_frequency(setup)

accurate_write = open("accurate_list.txt", "w")
accurate_write.write("%s" % ("# Record of My Logic Reasoning Accurate Rate Data. \n# Here begins the journey! \n# Always remember: Sometimes you win, sometimes you learn.\n# Happy learning and improving! \n"))