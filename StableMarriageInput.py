import sys
import os
import StableMarriageAlgorithm as SM

#get the men's names
male_count = 0
man = input("What is the name of male number " + str(male_count + 1) + ". Type \'end\' to move on to females: ")
men = []
while(man != "end"):
    men += [man]
    male_count += 1
    man = input("What is the name of male number " + str(male_count + 1) + ". Type \'end\' to move on to females: ")

#get the women's names
female_count = 0
woman = input("What is the name of female number " + str(male_count + 1) + ". Type \'end\' to move on to pairings: ")
women = []
while(woman != "end"):
    women += [woman]
    female_count += 1
    woman = input("What is the name of female number " + str(male_count + 1) + ". Type \'end\' to move on to pairings: ")

#is this male optimal or female optimal
optimal = -1
while optimal < 0:
    inp = input("Is this male-optimal or female optimal? Typle \'male\' or \'female\'")
    if(inp == 'male'):
        optimal = 0
    elif(inp == 'female'):
        optimal = 1

#find the men's preferences
for man in men:
    prefs = []
    count = 0
    while len(prefs) != female_count:
        pref = input("Who is " + man + "'s preference number " + (count + 1))
        if pref in women:
            count += 1
            prefs += [pref]





