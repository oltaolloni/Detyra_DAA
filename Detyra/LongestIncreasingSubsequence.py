# Duke pasur parasysh një varg numrash të plotë, shkruani një funksion që gjen gjatësinë e nënrenditjes më të gjatë në rritje.
# Një nënsekuencë është një sekuencë elementësh që shfaqen në të njëjtin rend në vargun origjinal, por jo domosdoshmërisht në mënyrë të njëpasnjëshme.
# Funksioni duhet të kthejë gjatësinë e nënsekuencës më të gjatë në rritje. Për shembull, për vargun [10, 9, 2, 3, 7, 101, 18], nënsekuenca më e gjatë në rritje është [2, 3, 7, 101] dhe gjatësia e saj është 4.

# Zgjidhja me Dynamic Programming
def gjatesia_LIS(vargu):
    n = len(vargu)
    if n == 0:
        return 0

    # Inicializo vargun dp me 1
    dp = [1] * n

    # Për çdo element i
    for i in range(1, n):
        # Për çdo element j para i
        for j in range(i):
            if vargu[j] < vargu[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Kthe maksimumin e vargut dp
    return max(dp)

vargu = [10, 9, 2, 3, 7, 101, 18]
rezultati = gjatesia_LIS(vargu)
print("Gjatësia e nënsekuencës më të gjatë në rritje është:", rezultati)

# Zgjidhja me binary search