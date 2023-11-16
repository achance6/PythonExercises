def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    res = {}
    for value, letters in legacy_data.items():
        for letter in letters:
            res[letter.lower()] = value
    return res

