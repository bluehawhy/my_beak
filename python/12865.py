from itertools import permutations

def make_dict_by_max_value(weight_list,value_list):
    dict_max = {}
    for i in range(len(weight_list)):
        weight = weight_list[i]
        value = value_list[i]
        if weight in dict_max:
            value_in_dict = dict_max[weight]
            if value_in_dict < value:
                dict_max[weight] = value
        else:
            dict_max[weight] = value
    return dict_max

def find_reasonable_value(weights,weight_list,dict_max):
    acceptable_list = []
    weight_list.sort()
    value = 0
    for i in range(len(weight_list)):
        combi_weights = list(permutations(weight_list, i))
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
                        acceptable_list = list(combi_weight)
    #print(acceptable_list)
    #print(value)
    return value


def make_list_wight_values():
    input_count = input()
    items,weights = map(int, input_count.split())
    weight_list = [] #무게들을 조합
    value_list = []
    for i in range(items):
        weight, value = map(int, input().split())
        weight_list.append(weight)
        value_list.append(value)
    #print(weight_list,value_list)
    total_val = find_reasonable_value(weights,weight_list,make_dict_by_max_value(weight_list,value_list))
    print(total_val)
    return 0


make_list_wight_values()
