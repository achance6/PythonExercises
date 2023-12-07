def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    res = []
    for candidate in candidates:
        tmp_word = word
        tmp_cand = candidate
        word = word.lower()
        candidate = candidate.lower()
        for letter in tmp_cand.lower():
            word = word.replace(letter, '', 1)
        for letter in tmp_word.lower():
            candidate = candidate.replace(letter, '', 1)
        if word == candidate and (tmp_word.lower() != tmp_cand.lower()): 
            res.append(tmp_cand)
        word = tmp_word
        candidate = tmp_cand
    return res

# candidates = ["dog", "goody"]
# print(find_anagrams('good', candidates))
# candidates = ["lemons", "cherry", "melons"]
# print(find_anagrams('solemn', candidates))
# candidates = ["Eons", "ONES"]
# print(find_anagrams('nose', candidates))