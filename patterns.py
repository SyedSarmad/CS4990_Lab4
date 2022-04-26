import math
import copy
import collections

# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]

    # print(itemsets)

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
    # print(elements)
    # print(kitemsets)

    visited.clear()
    frequents = kitemsets.copy()

    # return []
    while True:
        tempk = list()
        #print('Length of kitemsets is:', len(kitemsets[0][0]))
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
    #metric = "all"

    #print("frequent_itemsets (came from result of apriori)")
    #print(frequent_itemsets)

    setsWithCounts = list()
    #print("TESTING PHASE...")
    #print(len(frequent_itemsets))
    frequent_itemsets_with_powersets = []
    for item in frequent_itemsets:
        # print("item[0] for this instance...")
        # print(item[0])
        powerset_item = powerset(item[0]).copy()
        setsWithCounts.clear()
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
        # print("printing sets with counts...")
        # print(setsWithCounts)
        frequent_itemsets_with_powersets.append(setsWithCounts.copy())
        # print("frequent_itemsets_with_powersets...")
        # print(frequent_itemsets_with_powersets)


    #support is given, which is p(t)
    if metric == "lift":
        # lift = A=>B = P(T) / (P(A) * P(B) = P(B|A) / P(B) = CONF(A=>B) / SUPP(B)
        metric_info = calculations_for_metrics(frequent_itemsets, itemsets, frequent_itemsets_with_powersets, setsWithCounts)
        print("Result of the \"all\" metric...")
        result = []
        for instance in metric_info:
            print(instance)
            temp_list = [instance[0], instance[1], instance[5]/instance[3]]
            if temp_list[2] < metric_threshold:
                pass
            else:
                result.append(temp_list)

        print_result(result)
        return result

    elif metric == 'all':

        metric_info = calculations_for_metrics(frequent_itemsets, itemsets, frequent_itemsets_with_powersets, setsWithCounts)
        print("Result of the \"all\" metric...")
        result = []
        for instance in metric_info:
            temp_list = [instance[0], instance[1], min(instance[2], instance[3])]
            if temp_list[2] < metric_threshold:
                pass
            else:
                result.append(temp_list)

            print_result(result)
            result.append(temp_list)
        return result

    elif metric == 'max':
        # MAX_conf(A=>B) = MAX(P(A|B), P(B|A)
        metric_info = calculations_for_metrics(frequent_itemsets, itemsets, frequent_itemsets_with_powersets, setsWithCounts)
        print("Result of the \"max\" metric...")
        result = []
        for instance in metric_info:
            temp_list = [instance[0], instance[1], max(instance[2], instance[3])]
            result.append(temp_list)
        print_result(result)
        return result

    elif metric == 'kulczynski':
        # KULC(A=>B) = (P(A|B) + P(B|A)) / 2
        metric_info = calculations_for_metrics(frequent_itemsets, itemsets, frequent_itemsets_with_powersets, setsWithCounts)
        print("Result of the \"kulczynski\" metric...")
        result = []
        for instance in metric_info:
            temp_list = [instance[0], instance[1], ((instance[2] + instance[3]) / 2)]
            result.append(temp_list)
        print_result(result)
        return result

    elif metric == 'cosine':
        # COS(A=>B) = SQRT(P(A|B) * P(B|A))
        metric_info = calculations_for_metrics(frequent_itemsets, itemsets, frequent_itemsets_with_powersets,setsWithCounts)
        print("Result of the \"cosine\" metric...")
        result = []
        for instance in metric_info:
            temp_list = [instance[0], instance[1], (math.sqrt((instance[2] * instance[3])))]
            result.append(temp_list)
        print_result(result)
        return result


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
    b = []
    #print("in get consequence....")
    #print(antecedent_value)
    #print(set_to_get_b)
    # {i,0}
    antecedent_set_turned_to_list = copy.deepcopy(antecedent_value)
    antecedent_set_turned_to_list = list(antecedent_set_turned_to_list)
    list_set_to_get_b = copy.deepcopy(set_to_get_b)
    list_set_to_get_b = list(list_set_to_get_b)
    for value in set_to_get_b:
            if value not in antecedent_set_turned_to_list:
                b.append(value)

    #print(b)
    return b

def find_count(a,setsWithCounts):
    for value in setsWithCounts:
        #print("value...")
        #print(value)
        #temp = copy.deepcopy(value)
        value_as_list = value[0]
        a = set(a)
        #print('a is:', a)
        #print('value_as_list is:', value_as_list)

        if value_as_list == a:
            return value[1]



def calculations_for_metrics(frequent_itemsets,itemsets,frequent_itemsets_with_powersets,setsWithCounts):
    # print("\n\nIn calculations for metrics")
    result = []
    count = 0
    # print("TESTING the all.....")
    for item in frequent_itemsets:
        # print('Item is', item)
        # gets the powerset for the nth instance of the frequent itemset
        frequent_itemsets_instance = frequent_itemsets_with_powersets[count]
        # print('frequent_itemsets_instance:', frequent_itemsets_instance)

        # gets all the values that should be in the frequent itemset
        # we will use this to get the consequence
        set_to_get_b = item[0]
        count_of_all_items_for_this_instance = math.floor(item[1] * len(itemsets))
        # print("frequent_itemsets_instance...") #for testing, can delete later
        # print(frequent_itemsets_instance) #for testing, can delete later
        # print("count of all items") #for testing, can delete later
        # print(count_of_all_items_for_this_instance) #for testing, can delete later

        for antecedent_set in frequent_itemsets_instance:
            # a
            # testing stuff out
            temp_antecedent_set = copy.deepcopy(antecedent_set)
            antecedent_value_a = temp_antecedent_set[0]
            #print(antecedent_value_a)
            #antecedent_value_a = antecedent_value_a.pop()
            # print(antecedent_value_a)
            antecedent_value_a_count = antecedent_set[1]
            # b
            # print('antecedent_value_a', antecedent_value_a)
            antecedent_value_b = getConsequence(antecedent_value_a, set_to_get_b)
            # print("DEBUGGING....")
            # print(setsWithCounts) #debug

            # print('Antecedent_value_b:', antecedent_value_b)
            # print('frequent_itemsets_instance:', frequent_itemsets_instance)
            antecedent_value_b_count = find_count(antecedent_value_b, frequent_itemsets_instance)
            # print(antecedent_value_b_count)
            a = count_of_all_items_for_this_instance / antecedent_value_a_count
            b = count_of_all_items_for_this_instance / antecedent_value_b_count

            temp_result = (antecedent_value_a, antecedent_value_b, a,b)
            result.append(temp_result)

        # put the A and B into a set
        # calc the equation
        # put that into the set as well
        # move on to the next instance
        # for antecedent in frequent_itemsets_instance:
        count = count + 1

    return result

   # [('i', ['o', 's', 'u'], 0.5), ('o', ['i', 's', 'u'], 0.47619047619047616), ('o', ['i', 's', 'u'], 0.6666666666666666), ('s', ['i', 'o', 'u'], 0.5), ('s', ['i', 'o', 'u'], 0.6666666666666666), ('o', ['i', 's', 'u'], 0.625),
    # ('o', ['i', 's', 'u'], 0.8333333333333334), ('u', ['i', 'o', 's'], 0.5263157894736842),
    # ('u', ['i', 'o', 's'], 0.8333333333333334), ('o', ['i', 's', 'u'], 0.6666666666666666),
    # ('o', ['i', 's', 'u'], 0.8333333333333334), ('s', ['i', 'o', 'u'], 0.5882352941176471),
     #('s', ['i', 'o', 'u'], 0.8333333333333334), ('o', ['i', 's', 'u'], 0.7142857142857143)]


def print_result(result):
    index_count = 0

    for val in result:
        total_length = len(val[0]) - 1

        for a_val in val[0]:
            if (index_count == total_length):
                print(str(a_val), end="")
            else:
                print(str(a_val) + ",", end="")

            index_count = index_count + 1

        print(" =>", end=" ")
        index_count = 0
        total_length = len(val[1]) - 1

        for b_val in val[1]:
            if (index_count == total_length):
                print(str(b_val), end="")
            else:
                print(str(b_val) + ",", end="")
        print(":", end=" ")
        print(str(val[2]) + " ")
        index_count = 0