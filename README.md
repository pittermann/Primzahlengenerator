# Primzahlengenerator
Das in Python geschriebene Programm dient zur Erforschung von Primzahlen. Das Tool ist sehr flexibel gehalten. Es steht ein interaktiver Modus zur Verfügung. Die Steuerung kann auch über die Kommandozeile erfolgen.

![Mit dem Parameter "-h" bekommt man Hilfe angezeigt](https://github.com/pittermann/Primzahlengenerator/blob/master/images/primzahlen_help.jpg)

Getestet wurde das Programm unter Kali Linux, Python Version 3.6.5, und unter Windows 10, Python Version 3.7.3.

Um im den interaktiven Modus zu gelangen, genügt die Eingabe von: python primzahlen.py.
Hilfe bekommt man mit python primzahlen.py -h


Möchte man es über die Kommandozeile aufrufen, stehen acht Parameter zur Verfügung:
1. Parameter
Die Zahl, bis zu der Primzahlen gesucht werden sollen

2. Parameter
	0 = Es erfolgt keine grafische Ausgabe der gefundenen Zahlen, 
	1 = die Primzahlen sollen grafisch dargestellt werden

3. Parameter
Sollen die gefundenen Primzahlen angezeigt werden, oder nur das Endergebnis.1 = Anzeigen aller ermittelter Primzahlen

4. Parameter
| = Trennzeichen

5. Parameter
10 = Anzahl der Ausgabespalten

6. Parameter
1 = Anzeige fuehrender Nullen

7. Parameter
1 = Leerzeichen (0 = Nullen)
                                       
8. Parameter																			 
0: Bildschirmausgabe
1: primzahlen.dat im akt.Verzeichnis anlegen

## Grafische Anzeige
Python bietet extrem mächtige Befehle zur Erzeugung von Visualisierungen. Deswegen war es keine Kunst, zur Ausgabe der Werte auch die grafische Darstellung der Fundstellen zu schreiben.
![Die Visualisierung ist ruckzuck geschrieben](https://github.com/pittermann/Primzahlengenerator/blob/master/images/primzahlen_graphic.jpg)

