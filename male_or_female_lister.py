# -*- coding: utf-8 -*-
"""
Author: Rohan Soni

Converts attributes labels from ALL attributes list to a single text file containing specific attribute.
This case uses male and female labels for 60000 different images (samples).
"""
ATTR_PATH = "C:/Desktop/Rohan/Python Programs/MIT Internship/CelebA Dataset (MINE)/"
num_samples = 60000

import math
def entropy(probs):
    err = 0.01
    if abs(sum(probs)-1) >= err:
        print("ERROR: Total probability does not equal 1.")
        
    final_entropy = 0
    for i in probs:
        if i == 0:
            final_entropy += 0
        else:
            final_entropy += (-1) * i * math.log(i,math.e)
    return final_entropy

attributes_path = open(ATTR_PATH + "list_attr_celeba.txt", "r")
attributes_lines = attributes_path.readlines()

male_or_female = open(ATTR_PATH + "male_or_female.txt", "w")

male_or_female_list = []
samples = num_samples
for i in range(2, samples+2):
    bit = attributes_lines[i].split()[21]
    
    #0 for females, 1 for males (converted from -1 for females and 1 for males)
    #because it's generally been in 0 and 1 for MINE before
    if bit == "-1":
        male_or_female_list.append(0)
    else:
        male_or_female_list.append(1)
        
females = male_or_female_list.count(0)
males = male_or_female_list.count(1)

fm_entropy = entropy([males / (samples), females / (samples)])
print(f"Males in the first {samples} samples: {males}")
print(f"Females in the first {samples} samples: {females}")
print(f"Entropy of first {samples} samples: {fm_entropy}") #used to check accuracy of MINE results

for j in male_or_female_list:
    male_or_female.write(str(j) + "\n")

male_or_female.close()
attributes_path.close()