# Jepet një string s që përmban vetëm karakteret '(', ')', '{', '}', '[' dhe ']',
# përcaktoni nëse stringu i hyrjes është i vlefshëm.
# Një string hyrës është i vlefshëm nëse:
# 	a. Kllapat e hapura duhet të mbyllen me të njëjtin lloj kllapash.
# 	b. Kllapat e hapura duhet të mbyllen në rendin e duhur.
#
# Çdo kllapë mbyllëse ka një kllapë të hapur përkatëse të të njëjtit lloj.
# Shembull 1: Hyrja: s = "()", Dalja: true
# Shembull 2: Hyrja: s = "()[]{}", Dalja: true
# Shembull 3: Hyrja: s = "(]", Dalja: false
# Shembull 4: Hyrja: s = "([])", Dalja: true

def isValid(vargu):
    # Përdorim një listë si stack për të mbajtur kllapat e hapura.
    stack = []
    # Dictionary qe mapon cdo kllape mbyllese me kllapen hyrese perkatese
    mapping = {')': '(', '}': '{', ']': '['}

    for char in vargu:
        if char in mapping:  # Nëse është një kllapë mbyllëse
            # Nxirre elementin e fundit nga stack ose një vlerë dummy nëse stack është bosh
            top_element = stack.pop() if stack else '#'
            # Kontrollo nëse kllapa mbyllëse përputhet me kllapën e hapur
            if mapping[char] != top_element:
                return False
        else:  # Nëse është një kllapë hapëse
            stack.append(char)

    # Nëse stack është bosh kthehet true
    return not stack


# Shembuj të përdorimit
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
print(isValid("([])"))  # Output: True