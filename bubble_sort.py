# Der Bubble Sort

def bubble_sort(liste):
    n = len(liste)
    for i in range(n-1):  # Durchlaufe die Liste n-1 Mal
        for j in range(0, n-i-1):  # Durchlaufe die unsortierten Elemente
            if liste[j] > liste[j+1]:  # Wenn das aktuelle Element größer als das nächste Element ist
                liste[j], liste[j+1] = liste[j+1], liste[j]  # Tausche die beiden Elemente

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90] # Liste definieren
bubble_sort(arr) # Sortieren
print("Sortierte Liste: ", arr) # Liste in der Konsole ausgeben