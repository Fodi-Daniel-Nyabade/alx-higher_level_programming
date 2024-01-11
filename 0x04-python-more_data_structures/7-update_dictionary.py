def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): Input dictionary.
        key: Key to be added or replaced.
        value: Value to be associated with the key.

    Returns:
        dict: Updated dictionary.

    """
    a_dictionary[key] = value
    return a_dictionary
