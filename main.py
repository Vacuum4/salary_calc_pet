def dict_names(list1: list) -> dict:
    result_dict = {}
    for i in list1:
        if i not in result_dict:
            result_dict[i] = 1
        else:
            result_dict[i] += 1
    return result_dict


print(dict_names(['a', 'b', '1', 'tt', 'a', 'a']))
