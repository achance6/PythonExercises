def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    union = set()
    for multiple in multiples:
        union | get_multiples(multiple, limit)
    return sum(union)

def get_multiples(num: int, limit: int) -> set[int]:
    multiples = set()
    i = 1
    while (i * num) < limit:
        multiples.add(i * num)
        i += 1
    return multiples

print(get_multiples(5, 15))