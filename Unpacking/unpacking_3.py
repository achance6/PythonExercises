def transpose(lines: str) -> str:
    lines_list = lines.split('\n')
    max_len = len(max(lines_list, key = len))
    for i, line in enumerate(lines_list):
        line_len = len(line)
        if line_len < max_len:
            lines_list[i] += ' ' * (max_len - line_len)

    zipped = zip(lines_list)
    res = ''
    for line in zipped:
        res += tuple_to_string(line)
        res += '\n'
    res = res[:-1]
    print(res)
    return res

def tuple_to_string(tup: tuple[str, ...]) -> str:
    res = ''
    for letter in tup:
        res += letter
    return res.rstrip()

# transpose('\n'.join(['A1', 'B2', 'C3']))
# transpose('\n'.join(['ABC', 'DEF']))
# transpose('\n'.join(['ABC', 'DE']))
# transpose('\n'.join(['The fourth line.', 'The fifth line.']))
# 'TT\nhh\nee\n  \nff\noi\nuf\nrt\nth\nh \n l\nli\nin\nne\ne.\n. ' 
# 'TT\nhh\nee\n  \nff\noi\nuf\nrt\nth\nh \n l\nli\nin\nne\ne.\n.'
# transpose('\n'.join(["The longest line.", "A long line.", "A longer line.", "A line."]))
# transpose('\n'.join(["Single line."]))

# 'S\ni\nn\ng\nl\ne\n\nl\ni\nn\ne\n.'
# 'S\ni\nn\ng\nl\ne\n \nl\ni\nn\ne\n.'