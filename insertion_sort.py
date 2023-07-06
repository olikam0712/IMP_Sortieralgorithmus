# Der Insertion Sort

def insertion_sort(liste):
    for i in range(1, len(liste)): # Alle Elemente außer das Erste durchlaufen
        aktuell = liste[i]  # Aktuelles Element, das verglichen wird definieren
        j = i-1 # Index des vorherigen Elements definieren
        while j >= 0 and liste[j] > aktuell:  # Verschiebe Elemente nach rechts, um Platz für das aktuelle Element zu schaffen
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = aktuell  # Setze das aktuelle Element an die richtige Position

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90] # Liste definieren
insertion_sort(arr) # Sortieren
print("Sortierte Liste: ", arr) # Liste in der Konsole ausgeben