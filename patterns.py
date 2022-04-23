import math
import copy
import collections

# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]

    print(itemsets)

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
        print('Length of kitemsets is:', len(kitemsets[0][0]))
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
    metric = "all"
    print(frequent_itemsets)

    print("TESTING PHASE...")
    print(len(frequent_itemsets))
    frequent_itemsets_with_powersets = []
    for item in frequent_itemsets:
        print("item[0] for this instance...")
        print(item[0])
        powerset_item = powerset(item[0])
        setsWithCounts = list()
        for item2 in powerset_item:
            temp = set(item2)
            #if len(temp) != 0 and temp != set(item[0]):
            if len(temp) != 0 and temp != set(item[0]):
                count = 0
                # print('temp is', temp)
                for sett in itemsets:
                    if temp.issubset(sett):
                        count += 1
                setsWithCounts.append((temp, count))
        print(setsWithCounts)
        frequent_itemsets_with_powersets.append(setsWithCounts)
        print("frequent_itemsets_with_powersets...")
        print(frequent_itemsets_with_powersets)

        #print("IN HERE")
        #print(powerset_item)
        #print("after")
        #remove_unwanted(powerset_item)
        #print(powerset_item)

        #for item_instance in powerset_item:
           # if len(item_instance) <= 1:
            #    powerset_item.remove(item_instance)

    #support is given, which is p(t)
    if metric == "lift":
        # lift = A=>B = P(T) / (P(A) * P(B) = P(B|A) / P(B) = CONF(A=>B) / SUPP(B)
        pass
    elif metric == 'all':
        # all_conf(A=>B) = MIN(P(A|B), P(B|A))
        count = 0
        print("TESTING the all.....")
        for item in frequent_itemsets:
            # gets the powerset for the nth instance of the frequent itemset
            frequent_itemsets_instance = frequent_itemsets_with_powersets[count]

            # gets all the values that should be in the frequent itemset
            # we will use this to get the consequence
            set_to_get_b = item[0]
            print("frequent_itemsets_instance...") #for testing, can delete later
            print(frequent_itemsets_instance) #for testing, can delete later
            print("set_to_get_b") #for testing, can delete later
            print(set_to_get_b) #for testing, can delete later

            for antecedent_set in frequent_itemsets_instance:
                antecedent_value = antecedent_set[0]
                consequence_set = getConsequence(antecedent_value, set_to_get_b)
                find_count(antecedent_value, setsWithCounts)





            #put the A and B into a set
            #calc the equation
            #put that into the set as well
            #move on to the next instance
            #for antecedent in frequent_itemsets_instance:
            count = count + 1

            #pass
    elif metric == 'max':
        # MAX_conf(A=>B) = MAX(P(A|B), P(B|A)
        pass
    elif metric == 'kulczynski':
        # KULC(A=>B) = (P(A|B) + P(B|A)) / 2
        pass
    elif metric == 'cosine':
        # COS(A=>B) = SQRT(P(A|B) * P(B|A))
        pass


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

def powerset(s):
    list = []
    x = len(s)
    for i in range(1 << x):
        list.append([s[j] for j in range(x) if (i & (1 << j))])
    return list

def remove_unwanted(powerset):

    #for item in powerset:
        #print(item)
        #if len(item) < 1:
            #powerset.remove(item)
    powerset.pop(0)
    powerset.pop(len(powerset) - 1)


def getConsequence(antecedent_value, set_to_get_b):
    b = copy.deepcopy(set_to_get_b)
    for value in b:
        if antecedent_value == value:
            b.remove(value)
    return b

def find_count(a,setsWithCounts):
    for value in setsWithCounts:
        if value[0] == a:
            return value[1]