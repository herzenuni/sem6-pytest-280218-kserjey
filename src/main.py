def create_dict(keys, values):
    if not isinstance(keys, list) or not isinstance(values, list):
        raise TypeError('Arguments should be lists')

    if len(keys) > len(values):
        diff = len(keys) - len(values)
        values = values + ([None] * diff)

    return dict(zip(keys, values))
