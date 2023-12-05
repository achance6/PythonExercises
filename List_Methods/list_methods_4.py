def commands(binary_str: str) -> str:
    output = []
    if binary_str[4] == '1':
        output.append('wink')
    
    if binary_str[3] == '1':
        output.append('double blink')

    if binary_str[2] == '1':
        output.append('close your eyes')
    
    if binary_str[1] == '1':
        output.append('jump')
    
    if binary_str[0] == '1':
        output.reverse()

    return output

# print(commands('10101'))