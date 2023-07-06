def insertion_sort(liste):
    for i in range(1, len(liste)):
        aktuell = liste[i]  # Aktuelles Element, das verglichen wird
        j = i-1
        while j >= 0 and liste[j] > aktuell:  # Verschiebe Elemente nach rechts, um Platz für das aktuelle Element zu schaffen
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = aktuell  # Setze das aktuelle Element an die richtige Position

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sortierte Liste: ", arr)