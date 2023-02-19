import random

'''f = open('Scrambled Arrays/number.txt','w')
for x in range(number):
    f.write(str(random.randint(1,number)) + ' ')
f.close()
'''
array_list = []
with open('Scrambled Arrays/100.txt') as f:
    hundred_array = [int(x) for x in f.read().split()]
array_list.append(hundred_array)

with open('Scrambled Arrays/500.txt') as f:
    fivehundred_array = [int(x) for x in f.read().split()]
array_list.append(fivehundred_array)

with open('Scrambled Arrays/1k.txt') as f:
    thousand_array = [int(x) for x in f.read().split()]
array_list.append(thousand_array)

with open('Scrambled Arrays/3k.txt') as f:
    threethousand_array = [int(x) for x in f.read().split()]
array_list.append(threethousand_array)

with open('Scrambled Arrays/5k.txt') as f:
    fivethousand_array = [int(x) for x in f.read().split()]
array_list.append(fivethousand_array)

with open('Scrambled Arrays/7k.txt') as f:
    seventhousand_array = [int(x) for x in f.read().split()]
array_list.append(seventhousand_array)

with open('Scrambled Arrays/10k.txt') as f:
    tenthousand_array = [int(x) for x in f.read().split()]
array_list.append(tenthousand_array)

with open('Scrambled Arrays/15k.txt') as f:
    fifteenthousand_array = [int(x) for x in f.read().split()]
array_list.append(fifteenthousand_array)

with open('Scrambled Arrays/25k.txt') as f:
    twentyfivethousand_array = [int(x) for x in f.read().split()]
array_list.append(twentyfivethousand_array)

with open('Scrambled Arrays/35k.txt') as f:
    thirtyfivethousand_array = [int(x) for x in f.read().split()]
array_list.append(thirtyfivethousand_array)

with open('Scrambled Arrays/50k.txt') as f:
    fiftythousand_array = [int(x) for x in f.read().split()]
array_list.append(fiftythousand_array)

with open('Scrambled Arrays/65k.txt') as f:
    sixtyfivethousand_array = [int(x) for x in f.read().split()]
array_list.append(sixtyfivethousand_array)

with open('Scrambled Arrays/80k.txt') as f:
    eightythousand_array = [int(x) for x in f.read().split()]
array_list.append(eightythousand_array)

with open('Scrambled Arrays/100k.txt') as f:
    hundredthousand_array = [int(x) for x in f.read().split()]
array_list.append(hundredthousand_array)




with open('Scrambled Arrays/500k.txt') as f:
    fivehundredthousand_array = [int(x) for x in f.read().split()]
array_list.append(fivehundredthousand_array)

with open('Scrambled Arrays/million.txt') as f:
    million_array = [int(x) for x in f.read().split()]
array_list.append(million_array)

total_arrays = len(array_list)
array_numbers = []
for arr in array_list:
    array_numbers.append(len(arr))
