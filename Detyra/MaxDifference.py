# Të shkruhet kodi që e zgjidh problemin në vijim duke përdorur algoritmin më të përshtatshëm!
# Arsyeto pse keni zgjedhur të përdorni X algoritmin për të zgjidhur këtë problem.
# Duke pasur parasysh një varg të numrave të plotë, ktheni diferencën maksimale midis dy elementeve
# të njëpasnjëshme në formën e tyre të sortuar. Nëse grupi përmban më pak se dy elemente, ktheni 0.
# Shembull: Hyrja: vargu = [9,18,27,3]
# Dalja: 9
# Sqarim: Vargu i sortuar është [3,9,18,27],
# dhe çiftet (9,18) dhe (18,27) kanë diferencën më të madhe 9

# Zgjidhja me Radix Sort, i cili perdor Buckets:

def radix_sort(nums):
    if len(nums) == 0:
        return []

    max_num = max(nums)
    exp = 1

    while max_num // exp > 0:
        # Krijojmë 10 buckets (nga 0 në 9)
        buckets = [[] for _ in range(10)]

        # Hedhim numrat në bucket sipas shifrës në pozitën exp
        for num in nums:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        # Bashkojmë të gjithë bucket-at në një listë të vetme
        nums = [num for bucket in buckets for num in bucket]

        exp *= 10

    return nums


def max_difference(nums):
    if len(nums) < 2:
        return 0

    # nums.sort() - me funksion te gatshem

    radix_sort(nums)

    # Gjejmë diferencën maksimale midis elementeve të njëpasnjëshme
    max_diff = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff > max_diff:
            max_diff = diff

    return max_diff


# Shembull i përdorimit
vargu = [9, 18, 27, 3]
print(max_difference(vargu))  # Output: 9