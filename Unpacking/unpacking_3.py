import itertools

def transpose(lines: str) -> str:
    """Transposes strings separated by newlines"""
    lines_list = lines.split('\n')
    zipped = itertools.zip_longest(*lines_list, fillvalue='@')
    res = ''

    for line in zipped:
        # Only padding to the left with @'s to be replaced with spaces
        # @'s are only used to fill when the inputs are mismatched
        res += tuple_to_string(line).rstrip('@').replace('@', ' ')
        res += '\n'

    # remove final newline
    res = res[:-1] 
    return res

def tuple_to_string(tup: tuple[str, ...]) -> str:
    """Concatenates all strings in a tuples to a string"""
    res = ''
    for letter in tup:
        res += letter
    return res

# transpose('\n'.join(['A1']))
# transpose('\n'.join(['A1', 'B2', 'C3']))
# transpose('\n'.join(['ABC', 'DEF']))
# transpose('\n'.join(['ABC', 'DE']))
# transpose('\n'.join(['The fourth line.', 'The fifth line.']))
# transpose('\n'.join(['The first line.', 'The second line.']))
# transpose('\n'.join(["The longest line.", "A long line.", "A longer line.", "A line."]))
# transpose('\n'.join(["Single line."]))