values = [1, 2, '3', 'forth', 'end', 99, True, None]

change_int_to_str = lambda item: str(item) if isinstance(item, int) and not isinstance(item, bool) else item 
change_values = list(map(change_int_to_str, values))

print(change_values)


