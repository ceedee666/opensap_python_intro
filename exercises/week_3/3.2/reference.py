en_de = { "red" : "rot", "blue" : "blau", "green" : "grün", "pink" : "rosa"}
color = input("Which color should be translated? ")

if color in en_de:
     print("Die Übersetzung von", color, "ist", en_de[color])
else:
     print("Die Übersetzung von", color, "ist leider nicht bekannt")