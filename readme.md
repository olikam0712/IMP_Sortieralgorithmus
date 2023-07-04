## 1.  Bubble Sort:
    
    -   Bubble Sort vergleicht benachbarte Elemente und tauscht sie, wenn sie in der falschen Reihenfolge sind. Dabei wird das größte Element nach jedem Durchlauf an das Ende der Liste "aufsteigen". Dieser Vorgang wird wiederholt, bis die gesamte Liste sortiert ist.
    -   In jedem Durchlauf werden zwei aufeinanderfolgende Elemente verglichen und gegebenenfalls vertauscht. Das größte Element "blubbert" (engl. "bubble") dabei nach oben.
    -   Bubble Sort hat eine Zeitkomplexität von O(n^2) im schlechtesten und durchschnittlichen Fall, da jeder einzelne Durchlauf die Größe der unsortierten Teilmenge um eins reduziert.
## 2.  Insertion Sort:
    
    -   Insertion Sort baut die sortierte Liste schrittweise auf, indem es jedes Element an der richtigen Position in die bereits sortierten Elemente einfügt.
    -   Der Algorithmus beginnt mit dem zweiten Element und vergleicht es mit dem vorherigen Element. Falls das aktuelle Element kleiner ist, wird es nach links verschoben, bis es an der richtigen Position steht. Dieser Vorgang wird für jedes Element in der Liste wiederholt.
    -   Insertion Sort hat ebenfalls eine Zeitkomplexität von O(n^2) im schlechtesten und durchschnittlichen Fall. Allerdings ist es effizienter als Bubble Sort in praktischen Anwendungen, insbesondere wenn die Liste bereits teilweise sortiert ist.
## 3.  Selection Sort:
    
    -   Selection Sort teilt die Liste in einen sortierten und einen unsortierten Teil auf. In jedem Durchlauf wird das kleinste Element aus dem unsortierten Teil ausgewählt und an die richtige Position im sortierten Teil platziert.
    -   Der Algorithmus durchläuft die Liste und sucht das kleinste Element. Sobald es gefunden wird, wird es mit dem ersten Element des unsortierten Teils getauscht. Dadurch wächst der sortierte Teil Schritt für Schritt an.
    -   Selection Sort hat ebenfalls eine Zeitkomplexität von O(n^2) im schlechtesten und durchschnittlichen Fall, da in jedem Durchlauf das kleinste Element gesucht werden muss. Es ist jedoch schneller als Bubble Sort, da die Anzahl der Vertauschungen geringer ist.
