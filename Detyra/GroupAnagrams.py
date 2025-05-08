# Duke pasur parasysh një varg stringjesh strs, gruponi anagramet së bashku.
# Ju mund ta ktheni përgjigjen në çdo mënyrë.
#
# Shembull 1:
# Hyrja: strs = ["eat","tea","tan","ate","nat","bat"]
# Dalja: [["bat"],["nat","tan"],["ate","eat","tea"]]


from collections import defaultdict

# Funksion që bën renditjen me Bubble Sort për karakteret e një stringu
def bubble_sort_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chars[j] > chars[j + 1]:
                chars[j], chars[j + 1] = chars[j + 1], chars[j]
    return ''.join(chars)

def groupAnagrams(strs):
    # Krijon një fjalor ku çdo çelës i ri automatikisht inicializohet me një listë të zbrazët.
    anagrams = defaultdict(list)

    for s in strs:
        # Rendit shkronjat e stringut alfabetikisht dhe përdor si çelës
        sorted_str = bubble_sort_string(s)
        # Shto stringun në listën e anagramave për këtë çelës
        anagrams[sorted_str].append(s)

    # Kthe listën e vlerave të fjalorit (listat e anagramave)
    return list(anagrams.values())


# Shembuj të përdorimit
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""]))  # Output: [[""]]
print(groupAnagrams(["a"]))  # Output: [["a"]]