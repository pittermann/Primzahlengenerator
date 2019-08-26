import os, sys, math, time
import matplotlib.pyplot as plt

from itertools import cycle

# Farbige Ausgabe auf dem Bildschirm mit print
class c:
    PURPLE = '\033[95m'
    PURPLEBOLD = '\033[95m\033[1m'
    CYAN = '\033[96m'
    CYANBOLD = '\033[96m\033[1m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    BLUEBOLD = '\033[94m\033[1m'
    GREEN = '\033[92m'
    GREENBOLD = '\033[92m\033[1m'
    YELLOW ='\033[93m'
    YELLBOLD = '\033[1m\033[93m'
    RED = '\033[91m'
    REDBOLD = '\033[1m\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALIC = '\33[3m'

# Quersumme anzeigen
def quersumme(value):
    value = str(value)
    while len(value) > 1:
        value = str(sum(int(digit) for digit in value))
    return value



# Tausender Trennzeichen ausgeben
def format_int(i, sep='.'):
    cyc = cycle(['', '', sep])
    s = str(i)
    last = len(s) - 1
    formatted = [(next(cyc) if idx != last else '') + char
                 for idx, char in enumerate(reversed(s))]
    return ''.join(reversed(formatted))

# Fuehrende Leerstellen statt Nullen wie bei zfill(x) ausgeben
def fuell_auf(a, b):
    tempvar = 0;
    leerzeichen = '';
    for tempvar in range(len(a), b):
         leerzeichen = leerzeichen + ' '
    return leerzeichen



# Handelt es sich um einen Integer?
def is_int(mytest):
    return(isinstance(mytest, int))

# Ausgabe der Ergebnisse
def ausgabe_ergebnis():
    ergebnis = c.CYAN
    ohnefarbe = c.END

    printf( '\n\nListe der natuerlichen Zahlen bis: \t ' + ergebnis + '%s\n' + ohnefarbe, format_int(hoechstwert))
    printf( 'Gefundene Primzahlen: \t\t\t ' + ergebnis + '%d\n' + ohnefarbe, (menge - 1))
    printf( 'Es ist jede \t\t\t\t ' + ergebnis + "%2f" + ohnefarbe + ' Zahl eine Primzahl\n', float(hoechstwert) / float(menge))
    printf( 'Dauer der Untersuchung: \t\t ' + ergebnis + '%.4f ' + ohnefarbe + 'Sekunden\n', float(endezeit - startzeit))

# 'Clearen' des Bildschirms
def clear():
    if os.name == 'nt':
         clearme = lambda: os.system('cls')
         clearme()
    else:
         os.system('clear')

# Formatierte Zeichenausgabe
def printf(format, *args):
    sys.stdout.write(format % args)

def printprime():
    printf(c.CYAN)
    printf("     ##### \n")
    printf(c.GREEN)
    printf("   ####   ##*\n")
    printf(c.CYAN)
    printf("  #  ##     ##\n")
    printf(c.GREEN)
    printf("     ##      ##\n")
    printf(c.CYAN)
    printf("     ##      ##\n")
    printf(c.GREEN)
    printf("     ##     ##     +#\n")
    printf(c.CYAN)
    printf("     ##  ###*      #+\n")
    printf(c.GREEN)
    printf("     #####\n")
    printf(c.CYAN)
    printf("     ##    *#####  ## -## ## ##*   *####*\n")
    printf(c.GREEN)
    printf("     ##    ###++## ##   ### ## ##  ##   ##\n")
    printf(c.CYAN)
    printf("     ##    ##      ##   ##  ## ##  ######*\n")
    printf(c.GREEN)
    printf("     ##    ##      ##   ##  ## ##  ##\n")
    printf(c.CYAN)
    printf("     ##    ##      ##   ##  ## ##  ##\n")
    printf(c.GREEN)
    printf("     ##    ##      ##   ##  ## ##  *##**-\n\n\n")
    printf(c.END)

def abbruch():
    printprime()
    printf(c.CYANBOLD)
    printf("primzahl.py")
    printf(c.END)
    printf(" ist ein Hilfsprogramm zur Untersuchung von Primzahlen.\n")
    printf("Das Programm kann in zwei Modi verwendet werden:\n\n")
    printf("\t- interaktiv")
    printf(c.BOLD)
    printf(" und\n")
    printf(c.END)
    printf("\t- ueber die Kommandozeile\n\n")
    printf("Um im den interaktiven Modus zu gelangen, genuegt die Eingabe von:\n")
    printf(c.CYAN)
    printf("\tpython primzahl.py\n\n\n")
    printf(c.END)
    printf(c.BOLD)
    printf("Beispiel fuer den Kommandozeilenmodus:\n\n")
    printf(c.END)
    printf(c.CYAN)
    printf("python primzahl.py 1000 0 1 \"|\" 10 1 1 0 0 \n")
    printf(c.END)
    printf(c.ITALIC)
    printf("                   1000 Anzahl der Primzahlen bis n [pi(n)]\n")
    printf("                        0 = Keine grafische Ausgabe\n")
    printf("                          1 = Anzeigen aller ermittelter Primzahlen\n")
    printf("                             | = Trennzeichen\n")
    printf("                                10 = Anzahl der Ausgabespalten\n")
    printf("                                   1 = Anzeige fuehrender Nullen\n")
    printf("                                     1 = Leerzeichen (0 = Nullen)\n")
    printf("                                       0: Bildschirmausgabe\n")
    printf("                                       1: primzahlen.dat im akt.\n")
    printf("                                          Verzeichnis anlegen\n)")
    printf("                                           0 = Quersumme nicht anzeigen (1 = anzeigen)\n)")
    printf(c.END)


# Los geht's
def main():
    global menge, hoechstwert, startzeit, endezeit, dauer
    menge = 1
    querSum = ''
    schreibindatei = False
    zeigQuersumme = False
    trennzeichen = ''
    blockgroesse = 10
    # Nur wenn alle Argumente uebergeben werden
    #print "This is the name of the script: ", sys.argv[0]
    #print "Number of arguments: ", len(sys.argv)
    #print "The arguments are: " , str(sys.argv)
    hilfe = str(sys.argv[1:])
    if (hilfe.find('-h') > 0) or (hilfe.find('--h') > 0):
        clear()
        abbruch()
        sys.exit(0)

    if len(sys.argv) == 10:
        try:
            hoechstwert = int(sys.argv[1])      # Zahl

            zeigegrafik = int(sys.argv[2])      # Bool
            if zeigegrafik == 1:
                zeigegrafik = True
            else:
                zeigegrafik = False

            zeigeprim = int(sys.argv[3])        # Bool
            if zeigeprim == 1:
                zeigeprim = True
            else:
                zeigeprim = False

            trennzeichen = sys.argv[4]          # Zeichen

            blockgroesse = int(sys.argv[5])     # Zahl

            zeigenullen = int(sys.argv[6])      # Bool
            if zeigenullen == 1:
                zeigenullen = True
            else:
                zeigenullen = False

            zeigleer = int(sys.argv[7])         # Bool
            if zeigleer == 1:
                zeigleer = True
            else:
                zeigleer = False

            schreibindatei = int(sys.argv[8])   # Bool
            if schreibindatei == 1:
                schreibindatei = True
                zeigeprim = True
            else:
                schreibindatei = False

            zeigQuersumme = int(sys.argv[9])         # Bool
            if zeigQuersumme == 1:
                zeigQuersumme = True
            else:
                zeigQuersumme = False

            # Den eingegebenen Hoechstwert in eine Zeichenkette umwandeln und die Laenge des Strings merken
            hoechstwertlaenge = len(str(hoechstwert))

        except Exception:
            clear()
            abbruch()
            sys.exit(0)
    else:
        ################################################################################################
        # los geht's mit der Abfrage ...
        ################################################################################################
        if len(sys.argv) > 1:
            clear()
            print(c.REDBOLD)
            print("Fehler!")
            print(c.END)
            printf("Anzahl der Parameter ist fehlerhaft. Aufruf der Hilfe mit \"python primzahl.py -h\". ")
            repeat = input("Start im interaktiven Modus (J/n)?")
            if repeat.upper() == "N":
                sys.exit()
        clear()
        menge = 1              # Bis zum Zeitpunkt x gefundene Primzahlen
        hoechstwertlaenge = 0  # Die Anzahl Zeichen des, vom Anwender eingegebenen Hoechstwert speichern
        nullen = 'j'           # Fuehrende Nullen anzeigen 'j' als Defaultwert
        schreiben = 'n'        # Nicht in Datei schreiben per Default

        printf( c.BOLD + c.CYAN)
        printf('Primzahlen berechnen\n')
        printf('--------------------\n')
        printf( c.END)

        # Frage nach einem Hoechstwert bis zu dem gesucht werden soll
        try:
            hoechstwert = int(input('\nBis zu welcher natuerlichen Zahl sollen die Primzahlen errechnet werden (default: 1000)? '))
        except ValueError:
            hoechstwert = 1000

        # Soll eine grafische Anzeige der gefundenen Primzahlen erfolgen? Das dauert aber zigfach laenger.
        info = input('\nGrafik anzeigen? Das Programm arbeitet durch die grafische Ausgabe deutlich laenger. (j/N)?')
        if info in ['j', 'J', 'y', 'Y']:
            zeigegrafik = True
        else:
            zeigegrafik = False

        # Soll nur das Ergebnis angezeigt werden, oder jede gefundene zahl?
        info = input('\nJede gefundene Primzahl ausgeben? (J/n)?')
        if (info in ['j', 'J']) or (len(info) == 0):
            zeigeprim = True

            # Mit welchem Zeichen sollen die ermittelten Primzahlen getrennt werden?
            trennzeichen = input('\nWelches Trennzeichen soll verwendet werden (default: |)?')
            if len(trennzeichen) > 0:
                trennzeichen = trennzeichen[0]
            else:
                trennzeichen = '|'

            # Sollen die gefundenen Primzahlen in Bloecken zu x Zeichen ausgegeben werden?
            blockgroesse = input('\nNach wievielen Primzahlen soll ein Zeilenumbruch erfolgen (default: 10)?')
            try:
                blockgroesse = int(blockgroesse)
                if blockgroesse == 0:
                    blockgroesse = 1
            except:
                blockgroesse = 10

            nullen = input('\nFuehrende Nullen ausgeben? (J/n)?')
            if nullen in ['n', 'N']:
                zeigenullen = False
            else:
                zeigenullen = True
                null_leer = input('\nTatsaechlich fuehrende Nullen oder lieber ein Leerzeichen ausgeben? (J=0/n=Leerzeichen)?')
                if null_leer in ['n', 'N']:
                    zeigleer = True
                else:
                    zeigleer = False


            schreiben = input('\nDie Primzahlen in eine Datei schreiben statt auf dem Bildschirm auszugeben? (j/N)?')
            if schreiben in ['j', 'j', 'y', 'Y']:
                schreibindatei = True
            else:
                schreibindatei = False
            # Den eingegebenen Hoechstwert in eine Zeichenkette umwandeln und die Laenge des Strings merken
            hoechstwertlaenge = len(str(hoechstwert))

        else:
            zeigeprim = False



    ################################################################################################
    # Ende des Abfrageblocks
    ################################################################################################

    # Bildschirm leeren - sieht schicker aus
    clear()

    # Falls das Ergebnis in eine Datei geschrieben werden soll
    if schreibindatei == True:
        f = open("primzahlen.dat","w")

    # Einige Vorarbeiten, wenn die grafische Ausgabe gewuenscht wird
    if zeigegrafik == True:
        # Fenstertitel anzeigen
        fig = plt.figure()
        # ... und beschriften
        fig.canvas.set_window_title('Primzahlen mit Python berechnen und anzeigen ...')
        # Subplot fuer die Beschriftung
        ax = fig.add_subplot(111)
        # Titel der Primzahlberechnung
        plt.title('Primzahlberechnungen', fontsize=24, color='black')

    # Bildschirm 'leeren' und Startzeit merken
    clear()
    startzeit = time.time()

    printf( c.BOLD + c.CYAN)
    printf('Ergebnis der Primzahlberechnungen\n')
    printf('---------------------------------\n')
    printf( c.END)


    ################################################################################################
    # Ab hier beginnt die eigentliche Berechnung
    ################################################################################################

    # Jede Zahl zwischen 1 und hoechstwert wird zuerst als Primzahl angenommen
    # und der Wert mit True vorbelegt. Da zahlen[0] die 0 und zahlen[1] die 1 repraesentiert
    # und somit per se keine Primzahlen sind, werden die mit False vorbelegt
    zahlen = [True]*(hoechstwert+1)
    zahlen[0] = False
    zahlen[1] = False

    if zeigQuersumme == True:
        # Wenn die Quersumme angezeigt werden soll, muss auch die Primzahl ausgegeben werden
        zeigeprim = True

    # ... also geht es bei der '2' erst los
    i = 2

    # Durchlaufe die Routine nur, wenn 'i*1' kleiner oder gleich dem Hoechstwert (hoechstwert) ist
    while i*i <= hoechstwert:
        if zahlen[i] == True:

            # Streiche alle Vielfachen von i
            for k in range(i*i,hoechstwert+1,i):
                zahlen[k] = False

        # Die Laufvariable 'i' um 1 hochzaehlen
        i = i+1

    # Ausgabe aller gefundenen Primzahlen
    for i, v in enumerate(zahlen):
        if v == True:
            # Wenn die gefundenen Primzahlen ausgegeben werden sollen
            if zeigeprim == True:
                if zeigQuersumme == True:
                    querSum = ' (' + str(quersumme(i)) + ') '
                else:
                    querSum = ''

                # Wenn fuehrende Nullen mit ausgegeben werden sollen
                if zeigenullen == True:
                    if schreibindatei == False:
                        # Wenn fuehrende Nullen statt Leerzeichen auf dem Bildschirm gewollt sind
                        if zeigleer == False:
                            printf(str(i).zfill(hoechstwertlaenge) + querSum + trennzeichen)
                        else:
                            printf(fuell_auf(str(i), hoechstwertlaenge) + str(i) + querSum + trennzeichen)
                    else:
                        # Und das Ganze nun auch wenn in die Datei geschrieben wird
                        if zeigleer == False:
                            f.write(str(i).zfill(hoechstwertlaenge) + querSum + trennzeichen)
                        else:
                            f.write(fuell_auf(str(i), hoechstwertlaenge) + str(i) + querSum + trennzeichen)
            else:
                if schreibindatei == False:
                    printf(str(i) + querSum + trennzeichen)
                else:
                    f.write(str(i) + querSum + trennzeichen)

                # Zeilenumbruch nach x Ausgaben
                if (blockgroesse <= menge):
                    if (menge % blockgroesse) == 0:
                        if schreibindatei == False:
                            printf('\n')
                        else:
                            f.write('\n')


            # Wenn Grafik gewuenscht wird ...
            if zeigegrafik == True:
                plt.plot( i, menge, color='green', linestyle='', marker='o')
                ax.annotate('%s' %i, xy=(i,menge))

            # menge speichert die Anzahl der gefundenen Primzahlen
            menge = menge + 1

    ################################################################################################
    # Hier endet die eigentliche Berechnung
    ################################################################################################

    # Falls die Datei geoeffnet ist, wieder schliessen
    if schreibindatei == True:
        f.close()

    # Merke dir das Ende der Berechnung
    endezeit = time.time()

    # Ausgabe der Ergenisse
    ausgabe_ergebnis()

    # Wenn Grafik gewuenscht wird ...
    if zeigegrafik == True:
        # Label der y-Achse
        plt.ylabel('Gefundene Primzahlen: ' + str(menge), fontsize=18, color = 'blue')
        # Achsenbereich festlegen xMin, xMax, yMin, yMax
        plt.xlabel('Eingegebener Hoechstwert: ' + str(hoechstwert), fontsize = 18, color='blue')
        #plt.axis([0, hoechstwert, 0, menge])
        plt.axis([0, hoechstwert, 0, hoechstwert])

        plt.grid(True)
        plt.show()
    return 0

if __name__ == '__main__':
    main()
