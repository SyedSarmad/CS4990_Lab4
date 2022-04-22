import math
import copy

# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]

    kitemsets = []
    for item in itemsets:
        # print("ITEM: ", end=" ")
        # print(item, end="")
        occurrences = itemsets.count(item)
        # print(" COUNT: ", end=" ")
        # print(occurrences)
        if occurrences / len(itemsets) >= threshold:
            print("ITEM: ", end=" ")
            print(item, end="")
            print(" COUNT: ", end=" ")
            print(occurrences)
            kitemsets.append(item)
    print(kitemsets)
    # removing the duplicates
    remove_dup(kitemsets)
    print(kitemsets)
    two_itemset = []
    for i in range(len(kitemsets)):
        temp_list = []
        temp_list.append(kitemsets[i])
        #print("temp_list (outer): ", end=" ")
        #print(temp_list)
        for val in kitemsets:
            if kitemsets[i] != val:
                #print("two_itemset (outer): ", end=" ")
                #print(two_itemset)
                #print("val: ", end=" ")
                #print(val)
                temp_list.append(val)
                copy_of_temp = copy.deepcopy(temp_list)
                #print("temp_list (inner): ",end=" ")
                #print(temp_list)
                two_itemset.append(copy_of_temp)
                #print("two_itemset (inner): ", end=" ")
                #print(two_itemset)
                temp_list.pop()
            else:
                continue
    print(two_itemset)
    # now compare this with the orignal paired one



    return []

    
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
