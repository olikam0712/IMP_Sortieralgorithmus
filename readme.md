## Sortieralgorithmen
### 1. Bubble Sort
#### **Vorteile**:
 - **Einfache Implementierung**: Bubble Sort ist relativ einfach zu verstehen und zu implementieren. Es erfordert keine komplexen Datenstrukturen oder speziellen Algorithmen.
 - **Kein zusätzlicher Speicherbedarf**: Bubble Sort sortiert die Liste in-place, dh es werden keine zusätzlichen Datenstrukturen benötigt. Dies spart Speicherplatz.
 - **Gut für kleine Datenmengen**: Bubble Sort funktioniert gut für kleine Datenmengen oder bereits fast sortierte Listen. In solchen Fällen kann es eine effiziente Lösung sein.
#### **Nachteile**:
 - **Langsame Laufzeit**: Bubble Sort kann für die Sortierung großer Listen sehr viel zeit in Anspruch nehmen. Es ist nicht effizient für große Datenmengen.
 - **Ineffizienter Algorithmus**: Bubble Sort führt viele unnötige Vergleiche und Vertauschungen durch, auch wenn die Liste bereits sortiert ist. Dies macht den Algorithmus ineffizient im Vergleich zu anderen Sortieralgorithmen.
 - **Mangelnde Anpassungsfähigkeit**: Bubble Sort ist ein einfacher Algorithmus, der nicht besonders anpassungsfähig ist. Es gibt keine Möglichkeit, die Sortierung zu beschleunigen oder zu optimieren, abgesehen von kleinen Verbesserungen wie das Erkennen, dass die Liste bereits sortiert ist. Es gibt bessere Sortieralgorithmen, die in den meisten Fällen bevorzugt werden.
### 2. Insertion Sort
#### **Vorteile**:
 - **Einfache Implementierung**: Der Insertion Sort ist einfach zu verstehen und zu implementieren. Es erfordert keine komplexen Datenstrukturen oder speziellen Algorithmen.
 - **Effizient für kleine Datenmengen oder bereits fast sortierte Listen**: Der Insertion Sort ist effizient für kleine Datenmengen oder Listen, die bereits teilweise sortiert sind. In solchen Fällen kann er schneller sein als andere Sortieralgorithmen mit einer höheren Laufzeitkomplexität.
 - **Sortiert in-place**: Der Insertion Sort sortiert die Liste in-place, dh es werden keine zusätzlichen Datenstrukturen benötigt. Dies spart Speicherplatz.
#### **Nachteile**:
 - **Langsame Laufzeit für große Datenmengen**: Der Insertion Sort ist bei großen Datenmengen im Vergleich zu effizienteren Sortieralgorithmen langsam.
 - **Hoher Aufwand für das Einfügen von Elementen**: Beim Insertion Sort müssen Elemente an die richtige Position in der sortierten Teilmenge eingefügt werden. Dies erfordert einen großen Aufwand für das Verschieben der Elemente, was bei großen Listen zeitaufwändig sein kann.
 - **Nicht stabil**: Der Insertion Sort ist nicht stabil, was bedeutet, dass die Reihenfolge von Elementen mit demselben Schlüssel möglicherweise nicht beibehalten wird. Wenn Stabilität wichtig ist, müssen andere Sortieralgorithmen verwendet werden, die diese Eigenschaft garantieren können.
### 3. Selection Sort
#### **Vorteile**:
 - **Einfache Implementierung**: Der Selection Sort ist einfach zu verstehen und zu implementieren. Es erfordert keine komplexen Datenstrukturen oder speziellen Algorithmen.
 - **Sortiert in-place**: Der Selection Sort sortiert die Liste in-place, dh es werden keine zusätzlichen Datenstrukturen benötigt. Dies spart Speicherplatz.
 - **Wenige Vertauschungen**: Der Selection Sort führt nur eine begrenzte Anzahl von Vertauschungen durch, im Vergleich zu anderen Sortieralgorithmen wie dem Bubble Sort. Dies kann in bestimmten Situationen von Vorteil sein.
#### **Nachteile**:
 - **Langsame Laufzeit**: Der Selection Sort ist bei großen Datenmengen im Vergleich zu effizienteren Sortieralgorithmen langsam.
 - **Keine Anpassungsfähigkeit**: Der Selection Sort ist ein statischer Algorithmus, der nicht in der Lage ist, sich an bestimmte Muster oder Eigenschaften der Daten anzupassen. Er führt unabhängig von der Verteilung der Daten immer die gleiche Anzahl von Vergleichen und Vertauschungen durch.
 - **Nicht stabil**: Der Selection Sort ist nicht stabil, was bedeutet, dass die Reihenfolge von Elementen mit demselben Schlüsselwert möglicherweise nicht beibehalten wird. Wenn Stabilität wichtig ist, müssen andere Sortieralgorithmen verwendet werden, die diese Eigenschaft garantieren können.
