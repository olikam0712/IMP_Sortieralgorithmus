def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # Durchlaufe die Liste n-1 Mal
        for j in range(0, n-i-1):  # Durchlaufe die unsortierten Elemente
            if arr[j] > arr[j+1]:  # Wenn das aktuelle Element größer als das nächste Element ist
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Tausche die beiden Elemente

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sortierte Liste: ", arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Aktuelles Element, das verglichen wird
        j = i-1
        while j >= 0 and arr[j] > key:  # Verschiebe Elemente nach rechts, um Platz für das aktuelle Element zu schaffen
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  # Setze das aktuelle Element an die richtige Position

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sortierte Liste: ", arr)


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i  # Index des kleinsten Elements
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:  # Finde das kleinste Element im Rest der Liste
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Tausche das aktuelle Element mit dem kleinsten Element

# Beispielverwendung:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sortierte Liste: ", arr)
