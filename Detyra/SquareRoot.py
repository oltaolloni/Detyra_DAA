# Viti 2024: Duke pasur parasysh një numër të plotë jo negativ x,
# ktheni rrënjën katrore të x të rrumbullaksuar poshtë në numrin e plotë më të afërt.
# Numri i plotë i kthyer duhet të jetë gjithashtu jo negativ.
# Shembulli 1: Hyrja: x = 4, Dalja: 2 || Shpjegim: Rrënja katrore e 4 është 2, pra kthejmë 2.
# Shembulli 2: Hyrja: x = 8, Dalja: 2 || Shpjegim: Rrënja katrore e 8 është 2,82842..., dhe meqë e
# rrumbullakojmë në numrin e plotë më të afërt, kthehet 2.
# Nuk duhet të përdorni asnjë built-in funksion/metodë ose operator.

def square_root(x):
    left = 0
    right = x
    result = 0
    # Përdorim kërkimin binar për të gjetur rrënjën katrore.
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Shembull testimi
print(square_root(4))  # Dalja: 2
print(square_root(8))  # Dalja: 2
print(square_root(16))  # Dalja: 4
print(square_root(27))  # Dalja: 5