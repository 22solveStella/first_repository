#Sinn der Function is_first_and_last_same ist die Überprüfung, ob in einer Liste das erste und das letzte Element den selben Wert haben
#Beim Aufruf der function gibt man als argument eine Liste mit
#Die function liefert dann entweder True oder False zurück

def is_first_and_last_same(lst):#es geht darum den ersten und den letzten Wert zu überprüfen
    first = lst[0]#erster Wert      --> Zuerst wird den Variablen first und last der erste und der letzte Wert der Liste zugewiesen
    last = lst[-1]#letzer Wert list
    if first == last:   # Dann wird geprüft, ob beide den selben Wert haben
        return True     # Ist das der Fall, liefert die function True
    else:
        return False    # ansonsten liefert sie False


my_list = [10, 20, 30, 40, 6] # Hier wird die Liste definiert, die geprüft werden soll
print("First and last values are the same:", is_first_and_last_same(my_list)) #Hier wird ausgegben, ob bei der Prüfung der Liste True oder False rauskommt