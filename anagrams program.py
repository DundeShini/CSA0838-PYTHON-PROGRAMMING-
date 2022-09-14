def groupAnagrams(words):
    anagrams = []
    if not words:
        return anagrams
    nums = [''.join(sorted(word)) for word in words]
    d = {}
    for i, e in enumerate(nums):
        d.setdefault(e, []).append(i)
    for index in d.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
    return anagrams
if _name== 'main_':
    words = ["eat","ate","tan","tea","nat","bat"]
 
    anagrams = groupAnagrams(words)
    for anagram in anagrams:
        print(anagram)
