#1 Zodziai prasidedantys didzaja raide
# \b[A-Z]\w*\b

#2 Zodziai kurie is visu didz raidziu + skaiciai
# \b[A-Z][A-Z0-9]+\b

#3 Parašykite šabloną trumpąjam telefono numeriui (nereikia idealaus, tiesiog išrinkite 1884 ir 1663)
# \b1\d{3}\b

#4 Parašykite šabloną ilgąjam telefono numeriui
# \+370\s\d{1,2}\s\d{3}\s\d{4}

#5 Parašykite šabloną fakso numeriui
#  \(\d\s\d{1,2}\)\s\d{3}\s\d{4}

#6 Parašykite šabloną, kuris tiktų ir ilgąjam telefono numeriui, ir faksui (naudokite '|' ir grupavimą
# (\+370\s\d{1,2}\s\d{3}\s\d{4}|\(\d\s\d{1,2}\)\s\d{3}\s\d{4})

#7 Pagauti banko saskaita
# \bLT\d{2} \d{4} \d{4} \d{4} \d{4}\b

#8 Pagauti PVM koda
# \bLT\d{9}\b

#9 Pagauti zodis pries:
# \b\w+\b(?=:)

#10 Paprasta uzklausa emailui
# \b\w+@\w+\.\w+\b

import re

text = "Telefonai:\n1884 arba +370 5 268 4444 (Privatiems klientams)\n1633 arba +370 5 268 4422 (Verslo klientams)"
pattern = r"\b1\d{3}\b"
matches = re.findall(pattern, text)

print(matches)

text = "Telefonai:\n1884 arba +370 5 268 4444 (Privatiems klientams)\n1633 arba +370 5 268 4422 (Verslo klientams)\nFaksas: (8 5) 258 2700"

pattern = r"(\+370\s\d{1,2}\s\d{3}\s\d{4}|\(\d\s\d{1,2}\)\s\d{3}\s\d{4})"
matches = re.findall(pattern, text)

print(matches)