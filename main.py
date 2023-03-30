#During the algorithm's operation, we will be searching for a block of length D that has the most ones. Let's say this number is equal to max_one. 
#We will need to change D-max_one bits from zero to one in this sequence, while for the remaining positions, we will want to perform flips of ones, 
#that is, num_of_one-max_one times.
from cmath import inf


list=[]
open('zad4_output.txt', 'w').close()
for line in open('zad4_input.txt'):
    list = line.split()
    num = [int(s) for s in list[1] if s.isdigit()]#change from 'num' to num
    num = num[0]
    num_of_one = 0                                #numer of 1 in a 0/1 sequence
    list[1] = num
    i = 0
    max_onecurr = 0                               #the current number of ones in sequences of length D
    max_one = 0                                   #the maximum number of ones in sequences of length D
    for j in range(0, len(list[0])):
        if list[0][j] == '1':
            num_of_one += 1
    while i != len(list[0]) - list[1] + 1:
        max_onecurr = 0
        for j in range(i, i + list[1]):
            if list[0][j] == '1':
                max_onecurr += 1
        if max_onecurr > max_one:
            max_one = max_onecurr
        i += 1
    res = list[1] - max_one + num_of_one - max_one
    file = open("zad4_output.txt","a")
    print(res, file = file)
    file.close()