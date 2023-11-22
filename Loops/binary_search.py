def find(search_list: list[int], value: int) -> int:
    low = 0
    high = len(search_list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
        else:
            return mid
    raise ValueError("value not in array")
