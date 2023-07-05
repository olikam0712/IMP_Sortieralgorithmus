def bubble_sort(liste):
    n = len(liste)
    for i in range(n-1):  # Durchlaufe die Liste n-1 Mal
        for j in range(0, n-i-1):  # Durchlaufe die unsortierten Elemente
            if liste[j] > liste[j+1]:  # Wenn das aktuelle Element größer als das nächste Element ist
                liste[j], liste[j+1] = liste[j+1], liste[j]  # Tausche die beiden Elemente

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sortierte Liste: ", arr)


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


def selection_sort(liste):
    for i in range(len(liste)):
        min_idx = i  # Index des kleinsten Elements
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_idx]:  # Finde das kleinste Element im Rest der Liste
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]  # Tausche das aktuelle Element mit dem kleinsten Element

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sortierte Liste: ", arr)


arr = [64, 34, 25, 12, 22, 11, 90]
arr.sort()
print("Sortierte Liste: ", arr)

