# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.5. - Visualisierung der Daten


|                                |  Erklärung                                                                                                                                         |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Name und Identifikationsnummer | UC 2.5. - Visualisierung der Daten                                                                                                                |
| Beschreibung                   |Nach Abschluss des Testes kann der Diagnostiker das Ergebnis visuell abfragen und relevante Informationen herauslesen. Die Auswertung kann dem Probanden zu Verfügung gestellt werden.   |
| Beteiligte Akteure            | Diagnostiker:in; Proband:in                                                                                                                    |
| Status                           | In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle                                                                                   | UC 2.1, UC 2.2, UC 2.3, UC 2.4, UC 2.6, UC 2.6                                                                                                          |
| Auslöser                              | Nachbereitung einer Leistungsdiagnose durch Diagnostiker:in                                                                                           |
| Vorbedingungen                 |  Daten sind vollständig vorhanden (UC 1.0)                                                                                                                                            |
| Invarianten                    | Alle Bedingungen, die innerhalb und durch den Anwendungsfall nicht verändert werden dürfen, also auch in einem Misserfolgs- oder Fehlerszenario immer noch gewährleistet werden müssen. | Originial-Aufzeichnung bleiben vorhanden, bis verarbeitete Daten gespeichert werden                                                                        |
| Nachbedingung/Ergebnis         | Der Zustand, der nach einem erfolgreichen Durchlauf des Anwendungsfalls erwartet wird.                                                                                                  | Grafiken und Auswertungen sind gespeichert. Eingangsordner ist leer.                                                                    |
| Standardablauf                 | Alle Leistungsstufen werden nacheinander durchlaufen. Überprüfung, ob Widerstandswerte eingehalten. Daten werden gespeichert.                     |
| Alternative Ablaufschritte     | Diagnostiker:in erkennt Abbruchgrund und gibt diesen ein. Eingabe wird dokumentiert und mit Daten gespeichert. Somit kommt es zu keiner Visualisierung der Daten.                                                                         |
| Hinweise                       |  Die Visualisierung sorgt für die Darstellung der aufgenommenen Daten. Visualisierung kann nur erfolgen wenn der Versuch erfolgreich abgelaufen ist.                                                                                                                                             |
| Änderungsgeschichte            |18.03.022 Antonia Bleckenwegner & Jannik Auer                                                                                                                 |
|                                                                                                                                                                                                                   |                                                                                                                                                  |
