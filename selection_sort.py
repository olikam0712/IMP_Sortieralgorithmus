# Der Selection Sort

def selection_sort(liste):
    for i in range(len(liste)): # Jedes Element der Liste durchgehen
        min_idx = i  # Index des kleinsten Elements definieren
        for j in range(i+1, len(liste)): # Den Rest der Liste durchgehen
            if liste[j] < liste[min_idx]:  # Das kleinste Element im Rest der Liste finden
                min_idx = j # Das kleinste Element ändern
        liste[i], liste[min_idx] = liste[min_idx], liste[i]  # Das aktuelle Element mit dem kleinsten Element tauschen

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90] # Liste definieren
selection_sort(arr) # Sortieren
print("Sortierte Liste: ", arr) # Liste in der Konsole ausgeben