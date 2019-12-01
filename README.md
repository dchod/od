# Optimo Development

1. Uzyty system wyszukiwania pełnotekstowego to ElasticSearch (katalog search_indexes) - na pewno mozna usprawnić ten kod.

2. z pakietów nie jest wyciągany email, imię oraz nazwisko osoby utrymującej pakiet poniewaz nie nnalałem do tego łatwego dostępu.

3. Tak samo nie są pobierane słowa kluczowe. Gdyby były mozna - w modelu uzyć pola 'JSONField' jezeli mamy dostęp do Postgresa (uzyty jest zwykły SQLite)

4. Funkcja pobierające dane uruchamiana jest komendą: > python manage.py get_packages Jeżeli miało by to działać bez crontaba - mozna dodać Celery

5. W przypadku uzycia serwera deweloperskiego mozna w środowisku ustawić liczbę wyników dla 1 strony paginacji w ten sposób: 
> PER_PAGE=3 python manage.py runserver
Jezeli tak się nie stanie - defaultowo ta wartość ostanie ustawiona na '2' (plik settings.py)

6. API jest dołączone z pomocą DRF

7. HTML jest baaardzo prosty - prosty szablon w Bootstrap + SCSS

8. Panel admina został wyłączony

9. została dodatkowo uzyta biblioteka 'tqdm'. Dzięki niej podcasz pobierania informacji o pakietach w komendzie jest wyświetlany pasek postępu

10. Przepraszam za ewentualne literówki - nie działa mi na klawiaturze kilka przycisków ;)
