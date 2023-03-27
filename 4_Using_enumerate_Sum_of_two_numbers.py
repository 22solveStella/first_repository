def sum_current_previous(lst): #beide fkt machen das selbe, diese fkt bekommt ein argument, eine liste und die fkt aus, nicht die liste mi
    prev = 0
    for n in lst: #mit zahlen, sondern immer die summe des aktuellen listenelements und des vorhergehenden listenelements
        print(n + prev) #Ausgabe: Summe vom aktuellen listenelement und den vorhergehende
        prev = n  #variable prev, die merkt sich immer für den nächsten schleifendurchlauf, den vorhergehenden wert


def sum_current_previous_enu(lst): #Geht Liste durch und gibt die Summe des aktuellen Listenelements und des vorgehende Element aus
    prev = 0
    for i, n in enumerate(lst): # for schleife mit enumerate
        print(f"Index: {i}, Sum: {n + prev}") #index plus listenelementausgabe
        prev = n


sum_current_previous([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) #aufruf fkt

sum_current_previous_enu([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])