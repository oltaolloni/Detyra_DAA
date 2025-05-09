# Të shkruhet kodi i cili përmes inputit të userit krijon vargun vargu me n elemente numra të plotë.
# Të kontrollohet nëse ekziston modeli (ang. Pattern) 132 i tre numrave të plotëvargu[i], vargu[j] dhe vargu[k],
# ashtu që të vlej kushti: i<j<k dhe vargu[i]<vargu[k]<vargu[j].
# Shfaq true nëse ekziston 132 modeli ne atë varg, përndryshe shfaq false.
# Shembull:
# a) Hyrja: vargu[3,1,4,2]  Dalja: true
# b) Hyrja: vargu[1,2,3,4]  Dalja: false

def find_132_pattern(vargu):
    n = len(vargu)
    if n < 3:
        return False

    # Përdorim një stack për të ruajtur elementet e mundshme për vargu[k]
    stack = []
    # Ruajmë vlerën minimale të mundshme për vargu[i]
    min_i = 0

    for j in range(n - 1, -1, -1):
        if vargu[j] < min_i:
            return True
        while stack and vargu[j] > stack[-1]:
            min_i = stack.pop()
        stack.append(vargu[j])

    return False


# Marrim inputin nga useri
user_input = input("Shkruani numrat e vargut të ndarë me hapësira: ")
vargu = list(map(int, user_input.split()))

# Shfaqim rezultatin
print(find_132_pattern(vargu))