# Duke pasur parasysh detyrat e një grupi karakteresh, që përfaqësojnë detyrat që duhet të bëjë një CPU,
# ku çdo shkronjë përfaqëson një detyrë të ndryshme. Detyrat mund të kryheshin në çdo mënyrë.
# Çdo detyrë kryhet në një njësi të kohës. Për çdo njësi të kohës, CPU mund të kryejë ose një detyrë ose thjesht të jetë boshe.
# Sidoqoftë, ekziston një numër i plotë jo negativ n që përfaqëson periudhën e cooldown midis dy detyrave të njëjta (e njëjta shkronjë në grup),
# domethënë duhet të ketë të paktën n njësi kohore midis çdo dy detyrash të njëjta.
# Ktheni numrin më të vogël të njësive të kohës që CPU-ja do të marrë për të përfunduar të gjitha detyrat e dhëna.
# Shembull: Input: tasks = ["A","A","A","B","B","B"], n = 2 Output: 8
# Shpjegim: A-> B -> idle ->A-> B -> idle ->A-> B
# Ka të paktën 2 njësi kohore ndërmjet çdo dy detyrash të njëjta.

from collections import Counter
def least_interval(tasks, n):
    # Numëro frekuencën e secilës detyrë
    freq = Counter(tasks)

    # Gjej frekuencën maksimale
    max_freq = max(freq.values())

    # Numëro sa detyra kanë frekuencën maksimale
    num_max_freq = list(freq.values()).count(max_freq)

    # Llogarit numrin minimal të njësive kohore
    min_time = (max_freq - 1) * (n + 1) + num_max_freq

    # Kthe maksimumin midis min_time dhe gjatësisë së detyrave
    return max(min_time, len(tasks))


# Shembull përdorimi
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(least_interval(tasks, n))  # Output: 8