# Rozkład jazdy

API rozkładu jazdy Brzesko-Tarnów

## Opis

API rozkładu jazdy dwóch lokalnych przwoźników Pławecki oraz Solak. Godziny przejazdów w przypadku Solaka są scrapowane
bezpośrednio z ich strony głównej. Dane pławeckiego zapisałem recznie w oparciu o Firebase'a.

## Endpointy

### Wszystkie kursy - Solak

```
127.0.0.1:8000/timetable/timetables/solak
```

```json
{
  "brzesko-tarnow": {
    "0": [
      "6:30",
      "6:50",
      "7:30",
      "8:20",
      "8:40",
      "9:30",
      "10:30",
      "10:40",
      "11:30..."
    ]
  }
}
```

### Wszystkie kursy - Plawecki

```
127.0.0.1:8000/timetable/timetables/plawecki
```

```json
[
  {
    "robocze": [
      "6:10",
      "7:15",
      "9:00",
      "9:40",
      "11:00",
      "11:40",
      "13:00",
      "13:40",
      "15:00",
      "15:40"
    ]
  }
]
```

### Kursy według kierunku - Solak

```
127.0.0.1:8000/timetable/timetables/solak/{direction}
127.0.0.1:8000/timetable/timetables/solak/brzesko-tarnow
```

```json
{
  "0": [
    "6:30",
    "6:50",
    "7:30",
    "8:20",
    "8:40",
    "9:30",
    "10:30",
    "10:40",
    "11:30",
    "12:30",
    "12:40"
  ]
}
```

### Kursy według kierunku - Plawecki

```
127.0.0.1:8000/timetable/timetables/solak/{direction}
127.0.0.1:8000/timetable/timetables/plawecki/1 //TODO
```

```json
{
  "robocze": [
    "5:15",
    "6:05",
    "7:00",
    "8:10",
    "8:40",
    "10:00",
    "10:40",
    "12:00",
    "12:40",
    "14:00",
    "14:50",
    "16:10",
    "16:50",
    "18:20",
    "19:05"
  ]
}
```

### Najbliższy kurs (tymczasowo dla Solaka)

```
127.0.0.1:8000/timetable/time/{time}/{direction}
127.0.0.1:8000/timetable/time/7:00/brzesko-tarnow
```
```json
{
  "will be soon": "..."
}
```
