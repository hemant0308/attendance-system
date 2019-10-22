def to_camel_case(kebab_case):
    if kebab_case is not None:
        words = kebab_case.split("_")
        return words[0]+"".join([word.title() for word in words[1:]])
    return None

def to_snake_case(camel_case):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def change_dict_keys(input_dict, method):
    if isinstance(input_dict, dict):
        keys = list(input_dict.keys())
        for key in keys:
            new_key = method(key)
            value = input_dict[key]
            change_dict_keys(value, method)
            del input_dict[key]
            input_dict[new_key] = value
    elif isinstance(input_dict,list):
        for el in input_dict:
            change_dict_keys(el, method)
    else:
        return
