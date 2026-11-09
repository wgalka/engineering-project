---
title: Laboratorium 4 — harmonogram i diagramy
permalink: /2026-2027/lab4/
---

# Laboratorium 4: harmonogram Gantta i diagramy rozwiązania

**Główna instrukcja laboratoryjna krok po kroku: [Planowanie prac i budowa diagramu Gantta krok po kroku](gantt-krok-po-kroku.md).**

Przed zajęciami wykonajcie w zespole **Część I (Kroki 1–5)** instrukcji: określcie zakres minimalny (MVP) i pierwszy przyrost, rozbijcie pracę na 12–20 zadań WBS, ustalcie realną dostępność godzinową w tygodniach semestru oraz oszacujcie czas trwania zadań. Na laboratorium przećwiczycie model referencyjny (**Część II**), zbudujecie własny harmonogram w wybranym narzędziu open source lub komercyjnym (**Część III**), przeanalizujecie ścieżkę krytyczną, przeprowadzicie symulację opóźnienia i dodacie bufory ryzyka (**Część IV**), a na koniec wyeksportujecie plan bazowy do dokumentacji LaTeX (**Część V**). Zakup żadnej płatnej licencji nie jest wymagany.

## Cel zajęć

Przygotujecie wykonalny, policzalny plan prac do końca projektu i dobierzecie diagramy techniczne wyjaśniające budowę Waszego systemu. Zajęcia zaczynają się od raportu postępu nr 4: co zaplanowaliście na ostatni okres, co wykonaliście, jakie macie dowody i jaki jest wpływ na dalsze prace.

## Przygotowanie przed zajęciami

1. Przeczytajcie [instrukcję krok po kroku do diagramu Gantta](gantt-krok-po-kroku.md) oraz [przewodnik doboru diagramów projektowych](../narzedzia/).
2. Przygotujcie tabelę zadań WBS, tabelę dostępności członków zespołu oraz kalendarz semestru (Kroki 1–4 z instrukcji głównej).
3. Zainstalujcie wybrane narzędzie open source (**GanttProject** lub **ProjectLibre Desktop**) albo skonfigurujcie wspólny projekt w wybranym narzędziu online (**Asana**, **Jira**, **MS Project**).

## Przebieg pracy na laboratorium

1. **Raport postępu nr 4 (15 min):** dopiszcie raport do dziennika zespołu według [wspólnego szablonu](../dokumentacja/szablon-raportu.md) i przedstawcie aktualny stan artefaktów oraz dokumentacji.
2. **Weryfikacja WBS, dostępności i szacunków (25 min):** sprawdźcie kompletność zadań (analiza, projekt, pierwszy przyrost, rozbudowa, integracja, testy, dokumentacja, oddanie), właścicieli, nakład godzinowy vs czas trwania oraz kryteria ukończenia (DoD).
3. **Ćwiczenie na modelu referencyjnym (25 min):** wprowadźcie wspólny przykład (zadania A–H i kamień milowy M1) do wybranego narzędzia i potwierdźcie wyliczenie 12 dni roboczych oraz ścieżki krytycznej.
4. **Budowa harmonogramu własnego projektu (35 min):** wprowadźcie strukturę WBS, połączcie zadania relacjami zależności (`FS`, `SS`, `FF`), dodajcie minimum 3 kamienie milowe, przypiszcie członków zespołu i usuńcie wszystkie przeciążenia zasobów.
5. **Analiza ścieżki krytycznej, symulacja opóźnienia i ryzyka (20 min):** wyznaczcie ścieżkę krytyczną, przeprowadźcie eksperyment wydłużenia zadania krytycznego oraz skrócenia gałęzi równoległej, dodajcie rejestr minimum 3 ryzyk i jawny bufor czasowy.
6. **Wzajemny przegląd (Peer Review) i eksport (15 min):** zapiszcie plan bazowy (*Baseline*), wyeksportujcie czytelny wykres PDF/PNG i przetestujcie jego czytelność z sąsiednim zespołem według listy kontrolnej z Kroku 12.
7. **Dodatkowy diagram techniczny:** dobierzcie co najmniej jeden diagram do rozdziału 4.2 (np. ERD dla danych, sekwencji/aktywności dla zachowania lub komponentów dla architektury).

**Do uzupełnienia w dokumentacji i repozytorium po zajęciach:** rozdział **4.2** (struktura techniczna z dodatkowym diagramem), rozdział **4.3** (opis organizacji pracy, repozytorium Git, tabela etapów, wyeksportowany bazowy diagram Gantta, analiza ścieżki krytycznej i rejestr ryzyk), wpis raportu nr 4 oraz pliki źródłowe i eksporty wszystkich diagramów zgodnie z listą oddania w [Kroku 12 instrukcji](gantt-krok-po-kroku.md#krok-12-wzajemny-przegląd-lista-samokontroli-i-oddanie-pracy).

## Raportowanie po utworzeniu Gantta

Od tego laboratorium aż do końca roku akademickiego 2026/2027 raportujcie postępy **co dwa tygodnie**, także między zajęciami i po laboratorium 5. W każdym wpisie porównajcie postęp z planem bazowym, pokażcie dowody wykonania, zapiszcie odchylenia i ich przyczyny, zaktualizujcie roboczy plik Gantta oraz odpowiednie części dokumentacji i wskażcie zadania na następny okres. Używajcie [szablonu raportu](../dokumentacja/szablon-raportu.md) i zachowujcie poprzednie wpisy.
