# Duke pasur parasysh një varg Vargu, renditni atë në rend zbritës bazuar në frekuencën e karaktereve.
# Frekuenca e një karakteri është numri i herëve që shfaqet në varg.
# Ktheni vargun e renditur.
# Nëse ka më shumë se një përgjigje, ktheni njërën prej tyre.
#
# Shembulli 1:
# Hyrja: Vargu = "tree"
# Dalja: "eert"
# Shpjegim: 'e' paraqitet dy herë , ndërsa 'r' dhe 't' paraqiten nga një herë .
#
# Shembulli 2:
# Hyrja: Vargu = "cccaaa"
# Dalja: "aaaccc"
# Shpjegim: 'c' dhe 'a' paraqiten tri herë, kështu që "cccaaa" and "aaaccc" janë përgjigje të sakta.
# KUJDES: "cacaca" është përgjigje e pasaktë, sepse karakteret e njëjta duhet të shfaqen bashkë.

def sortByFrequency(vargu):
    frequency = {}  # dictionary to store character frequencies
    for char in vargu:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Sort characters first by frequency (descending) and then alphabetically
    sorted_chars = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))

    result = []
    for char in sorted_chars:
        result.append(char * frequency[char])

    return ''.join(result)  # Return the sorted string

# Test the function
print(sortByFrequency("tree"))  # Output: "eetr" or "eert" depending on sorting