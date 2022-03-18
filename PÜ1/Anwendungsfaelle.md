# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.5. - Visualisierung der Daten


|                                |                                                                                                                                         |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Name und Identifikationsnummer | UC 2.5. - Visualisierung der Daten                                                                                                                |
| Beschreibung                   |Nach Abschluss des Testes kann der Diagnostiker das Ergebnis visuell abfragen und relevante Informationen herauslesen. Die Auswertung kann dann zusätzlich auch dem Probanden zu Verfügung gestellt werden.   |
| Beteiligte Akteure            | Diagnostiker:in; Proband:in                                                                                                                    |
| Status                           | In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle                                                                                   | UC 2.1, UC 2.2, UC 2.3, UC 2.4, UC 2.6, UC 2.6                                                                                                          |
| Auslöser                              | Übersichtliche Darstellung der Daten für effizientere Datenauswertung durch Diagnostiker:in                                                                                           |
| Vorbedingungen                 |  Daten sind vollständig vorhanden (UC 1.0), Daten werden korrekt von der Software ausgewertet (UC 2.0)                                                                                                                                           |
| Invarianten                    | Verarbeitete Daten bleiben vorhanden, auch nachdem sie ins Diagramm integriert wurden | Originial-Aufzeichnung bleiben vorhanden, bis verarbeitete Daten gespeichert werden                                                                        |
| Nachbedingung/Ergebnis         | Grafiken und Auswertungen sind gespeichert. Eingangsordner ist leer.                                                                                                  | Grafiken und Auswertungen sind gespeichert. Eingangsordner ist leer.                                                                    |
| Standardablauf                 | Durchlauf aller Leistungstufen. Überprüfung der Einhaltung aller Wiserstandswerte. Speicherung der Daten.                   |
| Alternative Ablaufschritte     | Diagnostiker:in erkennt Abbruchgrund und gibt diesen ein. Eingabe wird dokumentiert und mit Daten gespeichert. Somit kommt es zu keiner Visualisierung der Daten.                                                                         |
| Hinweise                       |  Die Visualisierung sorgt für die Darstellung der aufgenommenen Daten. Visualisierung kann nur erfolgen wenn der Versuch erfolgreich abgelaufen ist.                                                                                                                                             |
| Änderungsgeschichte            |18.03.2022; Antonia Bleckenwegner & Jannik Auer                                                                                                                 |
|                                                                                                                                                                                                                   |                                                                                                                                                  |
