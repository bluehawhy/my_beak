import random
import sys
from itertools import permutations

def find_reasonable_value(weights,dict_max):
    #acceptable_list = []
    value = 0
    #여기서 DP를 사용해야 함.
    #모든 조합은 메모리나 시간초과에 많은 비용이 듬
    for i in range(len(dict_max.keys())):
        combi_weights = list(permutations(dict_max.keys(), i+1))
        print(combi_weights)
        for combi_weight in combi_weights:
            if sum(combi_weight) > weights:
                pass
            elif len(combi_weight) == 0:
                pass
            else:
                #print(combi_weight)
                temp_value = 0
                for i in list(combi_weight):
                    temp_value = temp_value + dict_max[i]
                    if temp_value > value:
                        value = temp_value
                        #acceptable_list = list(combi_weight)
    #print(acceptable_list)
    #print(value)
    return value


def get_list_wight_values():
    items,weights = map(int, sys.stdin.readline().split())
    dict_max = {}    
    for i in range(items):
        weight, value = map(int, sys.stdin.readline().split())
        #print(weight, value)
        #print(dict_max)
        if weight not in dict_max.keys():
            #print('weight not in dict')
            dict_max[weight]= value            
        else:
            #print('weight in dict')
            value_in_dict = dict_max[weight]
            if value >= value_in_dict:
                dict_max[weight] = value
    #print(dict_max)
    return weights, dict_max

def make_list_wight_values():
    weight_dicmax = get_list_wight_values()
    total_val = find_reasonable_value(weight_dicmax[0],weight_dicmax[1])
    print(total_val)
    return 0


#make_list_wight_values()

items = 3
weights = 2
dict_max = {}
for i in range(items):
    dict_max[i+1] = random.randint(0,100)
print(dict_max)
value = find_reasonable_value(weights, dict_max)
print(value)
#combi_weights = list(permutations(dict_max.keys(), 50))
#print(sys.getsizeof(combi_weights))
