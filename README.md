# lsat_logic_reasoning_data_tracker
python code for keeping track of your correct rate of LR session

# How to use this code?

step1: download three files: 
1) main.py
2) funcs.py
3) setup.py

step2 -- initial setup: 
open the terminal or any other IDE and redirect to your selected working directory. 
here I show the terminal way only:

run $ python setup.py
>> you will get a txt file named "updated_data.txt" which shows you havn't input any data of your practice result into it since the 2nd column of it is all zeros.
>> you also get a txt file named "accurate_list" which keeps record of your LR correct rate and the initial file conctains nothing except my "chicken soup"!

CAUTION:
you ONLY run this step once or you will lose all your data since you initiate it more than once.

step3 -- input pracice data:

run $ python main.py
>> you will be asked to input the number of your wrong questions. (split each number by one space, like this " ")
>> you will get two plots. one is "histogram.png", the other is "accurate_rate.png"

Note: "histogram.png" will show the time you update it so as to avoid any confusion. It also only shows the accurate rate of the latest LR sesstion you've done. the "accurate_rate.png" will show the history!



# what else?
I just realized this could be used for any self-learning process besides LSAT. If you find this helpful and use this for your own test preparation, I would be extremely happy if you could kindly send me an email saying "hey veronica! good job and keep working! you will be a good investigator one day :)"
