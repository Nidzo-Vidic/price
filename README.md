# Price

CLI-Tool, das den momentanen Sprit Preis in der gewählten Stadt angbit.

## Installation

```bash
pip3 install --user --editable .
```
## Beispiel

```bash
~ price --help
Usage: price [OPTIONS]

Options:
  -r, --radius INTEGER  Radius der Tankstellen
  -c, --city TEXT       Radius der Tankstellen  [required]
  -t, --type TEXT       Diesel, E10, E5, SuperPlus und die kleingeschriebenen
                        Varianten  [required]
```

```bash
$ price -c ulm -t diesel
-----------------------------------------------------------------------------------------------
Preis  | Tankstelle       | Stadt                   | Straße                         | Radius
-----------------------------------------------------------------------------------------------
1.039  | Pinoil           | 89231 Neu-Ulm           | Memminger Str. 182             | 3.8 km
1.069  | AVIA             | 89079 Ulm               | Maybachstr. 13                 | 5.3 km
1.079  | Freie Tankstelle | 89231 Neu-Ulm           | Turmstr. 38                    | 1.2 km
1.079  | JET              | 89231 Neu-Ulm           | Memminger Str. 54              | 1.7 km
.
.
.
$ price -c "Esslingen am Neckar" -t diesel
-----------------------------------------------------------------------------------------------
Preis  | Tankstelle       | Stadt                   | Straße                         | Radius
-----------------------------------------------------------------------------------------------
1.029  | SB Tankstelle    | 73734 Esslingen         | Weilstr. 105                   | 1.7 km
1.029  | Supermarkt-Tanks | 73733 Esslingen         | Wannenrain 30                  | 2.6 km
1.029  | bft              | 73734 Esslingen         | Zollhausweg 37                 | 2.0 km
1.029  | Avanti           | 70329 Stuttgart         | Augsburgerstr. 740             | 3.0 km
.
.
.
```
