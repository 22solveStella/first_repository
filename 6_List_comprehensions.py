old_string = "se#%c&,r!_e?*@t^"
new_string = ""

for obj in old_string: # die FOR Schleife geht den string old_string, zeichen für zeichen durch (se#%c&,r!_e?*@t^)
    if obj.isalnum(): #method bezogen auf objekt, braucht keine Parameter hier, die method liefert true oder false , weil if frage
        new_string = new_string + obj #wenn true,dann macht er was in condition steht, nämlich diese Zeile
print(new_string)
#die if abfrage fragt ob ein character entweder ein buchstabe oder ein ziffer ist, wenn ja dann hängt sie an den string new_string den character an