# Duke pasur parasysh një varg numrash të plotë, shkruani një funksion që gjen nënvargun e ngjitur me shumën më të madhe.
# Nënvargu duhet të jetë i ngjitur, që do të thotë se elementët duhet të jenë në një sekuencë dhe nuk mund të ndahen.
# Funksioni duhet të kthejë shumën e nënvargut.
# Për shembull, për vargun [-2, 1, -3, 4, -1, 2, 1, -5, 4], shuma maksimale e nënvargut është 6
# (nënvargu është [4, -1, 2, 1] ).

def shuma_maksimale_nenvargu(vargu):
    # Inicializo variablat
    shuma_maksimale = 0  # Shuma maksimale e gjetur deri më tani
    shuma_aktuale = 0                # Shuma e nënvargut aktual

    # Itero nëpër çdo element të vargut
    for numri in vargu:
        # Shto numrin aktual në shumën aktuale
        shuma_aktuale += numri

        # Nëse shuma aktuale është më e madhe se shuma maksimale, përditëso shumën maksimale
        if shuma_aktuale > shuma_maksimale:
            shuma_maksimale = shuma_aktuale

        # Nëse shuma aktuale bëhet negative, rivendosja në 0
        if shuma_aktuale < 0:
            shuma_aktuale = 0

    # Kthe shumën maksimale
    return shuma_maksimale

# Shembull përdorimi
vargu = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
rezultati = shuma_maksimale_nenvargu(vargu)
print("Shuma maksimale e nënvargut është:", rezultati)