## Projekt Hintergründe

### Zweck des Projekts
Das Projekt soll die Erhebung und Auswertung von Leistungsdaten an einem Fahrradergometer ermöglichen.


### Ziel des Projekts
Die Software zielt darauf ab, den Prozess der Leistungsdiagnostik zu vereinfachen und zu automatisieren.
Dabei soll der aktuelle Gesundheitszustand, die Belastbarkeit und der Leistungszustand von Sportler:innen effizient untersucht werden.


### Hintergrundinformation
- Der Auftraggeber verfügt bereits über Ergometer, die die erforderlichen Daten aufzeichnen können. 
- Beim Leistungstest handelt es sich um einen 3 Minuten Test in dem ein bestimmtes Leistungsziel vorgegeben ist
- Vom Ergometer werden Puls und Leistung als Zeitreihe erfasst und gespeichert



## Perspektiven
### Wer benutzt das System?
Das System ist vorwiegend für den professionellen Gebrauch in sportmedizinischen Einrichtungen entworfen.
Grundsätzlich dient die Software dem Leistungsdiagnostiker als Tool, Leistungsdaten seiner Probanden effizient auswerten zu können.
Dabei sollte der Diagnostiker jedoch nichtsdestotrotz fähig sein, diverse Gründe zum Abbruch begutachten und manuell vermerken zu können.



### Wer sorgt für Input?
Die Software kann mit dem Input von Probanden sämtlichen Alters und gesundheitlichen Zustandes arbeiten. 
Dabei wird es sich größtenteils um Input von Personen handeln, die eine Leistungsdiagnostik bei einem Experten durchführen lassen.



## Projekt Zielsetzung
### Bekannte Geschäftsregeln
Da es sich um ein medizinisches-Gerät handelt, muss vor jeglichem Gebrauch auf Risiken und Nebenwirkungen aufmerksam gemacht werden. 
Weiters wird das System vor der Veröffentlichung mehrere Prüfverfahren durchlaufen.
NOTE-JHU: Passt. Auch hierutner würde z.B. der Ablauf fallen: Erst wird der Test durchgeführt, dann von einer Expert:in mittels Software ausgewertet.

### System Informationen und Diagramme
Die Software liefert als Ergebnis der Leistungsdiagnostik unter anderem einen Plot, der die Herzrate und die Leistung über einen bestimmten Zeitraum darstellt.


Beispiel von aufgezeichneten EKG Daten aus dem die Software dann zum Beispiel die Herzfrequenz bestimmt:
![](ekg_example.png)



### Annahmen und Abhängigkeiten
Grundsätzlich ist jeder Druchlauf als gültig anzusehen, solange kein Abbruchskriterium erfüllt wird.
Sollte die Software jedoch zum Beispiel eine bedenkliche Herzfrequenz erkennen, ist die Auswertung der Software ungültig und somit auch nicht verwendbar.

ecg_data_subject:

subject_1:
Es handelt sich um eine json Datei, die flgende Inforationen über den Probanden enthält:
- subject id: Identifikationsnummer des Probande
- test_power_w: maximal getretene Wattanzahl
- birth year: Geburtsjahr
- test_ duration_s: dauer in sekunden




### Design und Implementation
Die Software läuft auf einem Computer, welcher mit dem Ergometer verbunden ist und wird nach jetzigem Stand über eine Kommandozeile bedient.


## Risiken
Sollte der Proband auf einen Abbruch des Leistungstests bei zum Beispiel einer Überschreitung von 90% der maximalen Herzfrequenz nicht reagieren, kann es zu ernsthaften Herz-Kreislauf Problemen kommen. Weiters könnten falsch ausgewerterte Daten den Probanden falsche Schlüsse ziehen lassen und somit seine Gesundheit gefährden.



## Bekannte Zukunftsverbesserungen
Das Tool wird zunächst mit einer Kommandozeile bedient, allerdings könnte bei Bedarf ein Nutzerinterface integriert werden.
Weiters wird auf sämtliche Bugs und weitere Probleme der Software immer sofort mit einer Überarbeitung reagiert.

## Referenzen

- [Link zur Aufgabenstellung](tbd)

## Offene, ungelöste TBD Probleme
Derzeit sind noch keine Probleme bekannt.
