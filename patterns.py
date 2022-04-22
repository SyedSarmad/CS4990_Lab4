import math
import copy
import collections

# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]

    # We compare everything to itemsets
    kitemsets = []
    elements = []
    visited = list()
    for item in itemsets:
        for element in item:
            if element not in visited:
                visited.append(element)
                counter = 0
                for sett in itemsets:
                    if element in sett:
                        counter += 1

                if counter/len(itemsets) >= threshold:
                    kitemsets.append(([element], round(counter/len(itemsets), 2)))
                    elements.append(element)
    print(elements)
    print(kitemsets)

    visited.clear()
    frequents = kitemsets.copy()

    # return []
    while True:
        tempk = list()
        print('Lenght of kitemsets is:', len(kitemsets[0][0]))
        for i in range(len(kitemsets)):

            for j in range(len(kitemsets[0][0]), len(elements)):
                #print('i is', i)
                # print('j is', j)
                joiner = kitemsets[i][0].copy()
                #print('Before adding, joiner is', joiner)
                if elements[j] not in joiner:
                    joiner.append(elements[j])
                    counter = 0
                    for sett in itemsets:
                        if set(joiner.copy()).issubset(sett):
                            counter += 1
                    #print('After adding, joiner is', joiner, ' with count', counter)
                    if counter/len(itemsets) >= threshold:
                        tempk.append((joiner.copy(), round(counter/len(itemsets), 2)))
                    #print(tempk)
                    joiner.clear()
        if len(tempk) == 0:
            return removeDupes(kitemsets)
        else:
            kitemsets = tempk.copy()

        # print('kitemsets is', kitemsets)
        # input('Continue')

"""This right here is some ugly-ass code. But I don't care. It's 3:22 AM and it works"""
def removeDupes(kitemsets):
    # return kitemsets
    temp = list()
    for l in kitemsets:
        l[0].sort()
        temp.append((tuple(l[0]), l[1]))
    # print(temp)
    # print(set(temp))
    return set(temp)




    
# DO NOT CHANGE THE FOLLOWING LINE
def association_rules(itemsets, frequent_itemsets, metric, metric_threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of triples: condition, effect, metric value 
    # Each entry (c,e,m) represents a rule c => e, with the matric value m
    # Rules should only be included if m is greater than the given threshold.    
    # e.g. [(set(condition),set(effect),0.45), ...]
    return []


def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1
