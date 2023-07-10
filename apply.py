from collections import OrderedDict


def apply_func_to_values(ordered_dict, func):
    new_ordered_dict = OrderedDict()
    for key, value in ordered_dict.items():
        if isinstance(value, dict):
            new_ordered_dict[key] = apply_func_to_values(value, func)
        else:
            new_ordered_dict[key] = func(value)
    return new_ordered_dict