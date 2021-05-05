from . import calc_general_config
def calc_general_index(**kwargs):
    list_to_sum = []
    total_coefficient = 0
    for key, value in kwargs.items():
        coefficient = calc_general_config.config.get(key,1)
        total_coefficient += coefficient
        list_to_sum.append(value*coefficient)
    result = sum(list_to_sum)/total_coefficient
    return int(result)
    