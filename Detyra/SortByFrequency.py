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
    frequency = {}  # dictionary per te ruajtur key,value (char, numri i paraqitjes)
    for char in vargu:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # lista e krijuar prej elementeve (karakter, frekuence)
    lista = [(char, frequency) for char, frequency in frequency.items()]

    n = len(lista)

    # bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][1] < lista[j+1][1]: #krahasojme elementet ngjitur
                lista[j], lista[j+1] = lista[j+1], lista[j] #swap

    rezultati = ""
    for char, frequency in lista:
        rezultati += char*frequency

    return rezultati

# Test the function
print(sortByFrequency("tree"))  # Output: "eetr" or "eert" depending on sorting