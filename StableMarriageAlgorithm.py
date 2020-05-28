
#list of men
#list of women

#dictionary
# {man1 :[pref 1, pref2, pref3]}, {man2 : [pref1, pref2, pref3] ...}

men = ["Andrew", "Bernie", "Charlie"]
women = ["Annie", "Bessy", "Cynthia"]

preferences = {"Andrew": ["Bessy", "Cynthia", "Annie"],
               "Bernie": ["Annie", "Bessy", "Cynthia"],
               "Charlie": ["Bessy", "Annie", "Cynthia"],
               "Annie": ["Andrew", "Bernie", "Charlie"],
               "Bessy": ["Andrew", "Bernie", "Charlie"],
               "Cynthia": ["Andrew", "Bernie", "Charlie"]}

"""
How Stable Marriage algorithm works. 
Each man and woman has a preference list of all of the other gender
Day 1: 
    Each woman proposes to their #1 choice, each man rejects all but their top suitor (this is tentative)
Day 2-N: 
    Each rejected woman proposes to her next best man (regardless if he's single or tanken)
    Each man rejects all but top suitor
Algorithm ends when there are no single women left or when there is no change after a day 
    (second one happens when number of men < number of women) 
"""

def SMA(men, women, preferences, optimal):
    #if optimal is 0, it is male optimal, meaning that the single set is the women
    #if optimal is 1, it si female optimal, meaning that the single set is the men

    if optimal is 0:
        singles = women.copy()
    else:
        singles = men.copy()
    change = 1
    day = 0
    pairings = {}
    while len(singles) != 0 or change == 0:
        day += 1
        change = 0
        for suitor in singles:
            print(suitor)
            curr_prefs = preferences[suitor]
            suited = curr_prefs[0]
            #if the woman's top choice doesn't already have a match, set the match to the woman
            #otherwise compere the rankings of the current match and the woman, and set the match to the higher ranked.
            if suited not in pairings:
                pairings[suited] = suitor
                change = 1
            else:
                curr_match = pairings[suited]
                curr_match_rank = preferences[suited].index(curr_match)
                suitor_rank = preferences[suited].index(suitor)
                if suitor_rank < curr_match_rank:
                    change = 1
                    pairings[suited] = suitor
            curr_prefs.remove(suited)

        for suited, suitor in pairings.items():
            if suitor in singles:
                singles.remove(suitor)

        print(pairings)
    return pairings




print()
print(SMA(men, women, preferences, 0))





























