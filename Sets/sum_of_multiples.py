def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    union = set()
    for multiple in multiples:
        union = union | get_multiples(multiple, limit)
    return sum(union)

def get_multiples(num: int, limit: int) -> set[int]:
    return {i for i in range(num, limit, num)} if num > 0 else set()

# print(get_multiples(5, 15))
# print(sum_of_multiples(20, [3, 5]))
print(sum_of_multiples(1, [0]))