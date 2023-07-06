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