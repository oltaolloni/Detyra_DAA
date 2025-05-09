# Duke pasur parasysh variablen formula - e tipit string, që përfaqëson një formulë kimike,
# ktheni numrin e secilit atom.
# Elementi atomik gjithmonë fillon me një karakter të madh,
# pastaj zero ose më shumë shkronja të vogla, që përfaqësojnë emrin. Një ose më shumë
# shifra që përfaqësojnë numërimin e atij elementi mund të pasojnë nëse numërimi është
# më i madh se 1. Nëse numërimi është 1, nuk do të ketë asnjë shifër.
# *Për shembull, "H2O" dhe "H2O2" janë të mundshme, ndërsa "H1O2" jo.
# Dy formula janë të lidhura së bashku për të prodhuar një formulë tjetër.
# *Për shembull, "H2O2He3Mg4" është gjithashtu formulë.
# Një formulë e vendosur në kllapa dhe një numërim (i shtuar opsionalisht) është gjithashtu
# një formulë.
# *Për shembull, "(H2O2)" and "(H2O2)3" jane formula.
# Ktheni numrin e të gjithë elementëve si string në formën e mëposhtme: emrin e parë (i
# sortuar), i ndjekur nga numri i tij (nëse ai numër është më i madh se 1), i ndjekur nga
# emri i dytë (i sortuar), i ndjekur nga numërimi (count) i tij (nëse ai numër është më i
# madh se 1), e kështu me radhë.
# Shembull:
# Hyrja: formula = "K4(ON(SO3)2)2"
# Dalja: "K4N2O14S4"
# Shpjegim: Numri i elementeve është: {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Kufizimet:
# - 1 <= formula.length <= 1000
# - formula përbëhet nga shkronja, numra, '(', dhe ')'.
# - Formula është gjithmonë valide.

import re
from collections import defaultdict

def count_atoms(formula):
    def parse_formula(formula):
        stack = []
        current = defaultdict(int)
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(current)
                current = defaultdict(int)
                i += 1
            elif formula[i] == ')':
                i += 1
                num_str = ''
                while i < n and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                multiplier = int(num_str) if num_str else 1
                prev = stack.pop()
                for key in current:
                    prev[key] += current[key] * multiplier
                current = prev
            else:
                element = re.match(r'([A-Z][a-z]*)', formula[i:]).group(1)
                i += len(element)
                num_str = ''
                while i < n and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                count = int(num_str) if num_str else 1
                current[element] += count

        return current

    atoms = parse_formula(formula)

    sorted_atoms = sorted(atoms.items())
    
    result = ''
    for element, count in sorted_atoms:
        result += element
        if count > 1:
            result += str(count)

    return result


# Shembuj përdorimi
print(count_atoms("H2O"))  # Output: "H2O"
print(count_atoms("Mg(OH)2"))  # Output: "H2MgO2"
print(count_atoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"