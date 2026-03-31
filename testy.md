# Testowanie Aplikacji

## Test 1 - Wyczyść rzędu pełnego płytek

Kroki:
* Uruchamiam aplikację
* Przechodzę przez Menu do Gry
* Ustawiam bloki, tak aby jeden rząd był pełen płytek z bloków (brak pustych)

Rezultat:
* Rząd od razu się usuwa
* Bloki przesuwają się o liczbę usuniętych rzędów w dół
* Ilość punktów zostaje dodana do wyniku (w zależności od ilości wyczyszczonych rzędów w jednym ruchu)

## Test 2 - Zakończenie gry poprzez układanie wieży z bloków do sufitu siatki

Kroki:
* Uruchamiam aplikację
* Przechodzę przez Menu do Gry
* Ustawiam bloki, tak aby jeden po drugim tworzyły wieżę dotykającą sufitu

Rezultat:
* Gra przestaje wyrzucać nowe bloki
* Pokazuje się napis "GAME OVER"
* Po kliknięciu dowolnego przycisku, gra się resetuje (wynik też)

## Test 3 - Wykonanie zdjęcia okna aplikacji po zakończeniu gry

Kroki:
* Uruchamiam aplikację
* Przechodzę przez Menu do Gry
* Ustawiam bloki pod rząd, tak aby dotknęły sufit siatki
* Aktywuje się koniec gry
* Klikam klawisz 'p', aby zrobić screenshot

Rezultat:
* Zostaje zapisany plik `screenshot.png` w folderze
* (Jeśli ten plik był wcześniej, zostaje zastąpiony)

## Test 4 - Agresywna rotacja i poruszanie się bloku przez użytkownika

Kroki:
* Uruchamiam aplikację
* Przechodzę przez Menu do Gry
* Agresywnie klikam spację i strzałki, przez co agresywnie porusza się cały blok
* Robię to tak, aż blok dojdzie do dołu siatki

Rezultat:
    * Bez używania dolnej strzałki, gra działa w porządku
W innym przypadku:
    * Gra zatrzymuje się
    * Wyskakuje błąd, w którym blok jest poza indexem listy (czyli naszej siatki)
LUB
    * Gra aktywuje koniec gry

## Test 5 - Obracanie bloku przy lewej i prawej granicy siatki

Kroki:
* Uruchamiam aplikację
* Przechodzę przez Menu do Gry
* Kieruje blok do jednego z granic i zaczynam obracać blok kilka razy

Rezultat:
    Prawa granica:
        * Blok przestaje się obracać
    Lewa granica:
        * Blok przestaje się obracać
