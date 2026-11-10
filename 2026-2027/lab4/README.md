---
title: Laboratorium 4 — harmonogram i diagramy
permalink: /2026-2027/lab4/
---

# Laboratorium 4: harmonogram Gantta i diagramy rozwiązania

**Główna instrukcja laboratoryjna krok po kroku: [Planowanie prac i budowa diagramu Gantta krok po kroku]({{ '/2026-2027/lab4/gantt/' | relative_url }}).**

Przed zajęciami należy opracować w zespole **Część I (Kroki 1–5)** instrukcji: określić zakres minimalny (MVP) i pierwszy przyrost, podzielić pracę na 12–20 zadań WBS, ustalić dostępność godzinową w tygodniach semestru, oszacować czas trwania zadań oraz określić zależności i kamienie milowe. Na laboratorium realizowane są kolejne części instrukcji: przeliczenie modelu referencyjnego (**Część II**), budowa harmonogramu w wybranym narzędziu open source lub komercyjnym (**Część III**), analiza ścieżki krytycznej, symulacja opóźnienia i dodanie rezerwy czasowej (**Część IV**) oraz eksport planu bazowego do dokumentacji LaTeX (**Część V**). Zakup płatnej licencji nie jest wymagany.

## Cel zajęć

Przygotowanie wykonalnego harmonogramu prac do końca projektu oraz dobór diagramów technicznych wyjaśniających budowę systemu. Zajęcia rozpoczynają się raportem postępu nr 4 obejmującym planowane i wykonane zadania, dowody wykonania oraz wpływ zmian na dalsze prace.

## Przygotowanie przed zajęciami

1. Zapoznać się z [instrukcją krok po kroku do diagramu Gantta]({{ '/2026-2027/lab4/gantt/' | relative_url }}) oraz [przewodnikiem doboru diagramów projektowych]({{ '/2026-2027/narzedzia/' | relative_url }}).
2. Przygotować zakres MVP, tabelę zadań WBS z szacunkami i poprzednikami, tabelę dostępności członków zespołu, kalendarz semestru oraz kamienie milowe (Kroki 1–5 z instrukcji głównej).
3. Zainstalować wybrane narzędzie open source (**GanttProject** lub **ProjectLibre Desktop**) albo skonfigurować wspólny projekt w wybranym narzędziu online (**Asana**, **Jira**, **MS Project**).

## Przebieg pracy na laboratorium

1. **Raport postępu nr 4 (15 min):** dopisać raport do dziennika zespołu według [wspólnego szablonu]({{ '/2026-2027/dokumentacja/szablon-raportu/' | relative_url }}) i przedstawić aktualny stan artefaktów oraz dokumentacji.
2. **Weryfikacja WBS, dostępności i szacunków (25 min):** zweryfikować kompletność zadań (analiza, projekt, pierwszy przyrost, rozbudowa, integracja, testy, dokumentacja, oddanie), właścicieli, nakład godzinowy względem czasu trwania oraz kryteria ukończenia.
3. **Ćwiczenie na modelu referencyjnym (25 min):** wprowadzić wspólny przykład (zadania A–H i kamień milowy M1) do wybranego narzędzia i potwierdzić wyliczenie 12 dni roboczych oraz ścieżki krytycznej.
4. **Budowa harmonogramu projektu zespołu (35 min):** wprowadzić strukturę WBS, połączyć zadania relacjami zależności (`FS`, `SS`, `FF`), dodać minimum 3 kamienie milowe, przypisać członków zespołu i wyeliminować przeciążenia zasobów.
5. **Analiza ścieżki krytycznej, symulacja opóźnienia i ryzyka (20 min):** wyznaczyć ścieżkę krytyczną, przeprowadzić symulację wydłużenia zadania krytycznego oraz skrócenia gałęzi równoległej, uzupełnić rejestr minimum 3 ryzyk i dodać rezerwę czasową.
6. **Wzajemny przegląd i eksport (15 min):** zapisać plan bazowy (*Baseline*), wyeksportować czytelny wykres PDF/PNG i zweryfikować jego czytelność z sąsiednim zespołem według listy kontrolnej z Kroku 12.

**Praca własna po zajęciach (poza powyższymi 135 minutami):** dobrać i przygotować co najmniej jeden dodatkowy diagram techniczny do rozdziału 4.2 (np. ERD dla danych, sekwencji/aktywności dla zachowania lub komponentów dla architektury), uzupełnić opis harmonogramu i skompilować dokumentację LaTeX.

**Do uzupełnienia w dokumentacji i repozytorium po zajęciach:** rozdział **4.2** (struktura techniczna z dodatkowym diagramem), rozdział **4.3** (opis organizacji pracy, repozytorium Git, tabela etapów, wyeksportowany bazowy diagram Gantta, analiza ścieżki krytycznej i rejestr ryzyk), wpis raportu nr 4 oraz pliki źródłowe i eksporty wszystkich diagramów zgodnie z listą oddania w [Kroku 12 instrukcji]({{ '/2026-2027/lab4/gantt/' | relative_url }}#krok-12-wzajemny-przegląd-lista-samokontroli-i-oddanie-pracy).

## Raportowanie po utworzeniu Gantta

Od tego laboratorium aż do końca roku akademickiego 2026/2027 raporty postępu składane są **co dwa tygodnie**, również między zajęciami i po laboratorium 5. W każdym wpisie należy porównać postęp z planem bazowym, przedstawić dowody wykonania, zapisać odchylenia i ich przyczyny, zaktualizować roboczy plik Gantta oraz odpowiednie części dokumentacji i wskazać zadania na następny okres. Należy stosować [szablon raportu]({{ '/2026-2027/dokumentacja/szablon-raportu/' | relative_url }}) z zachowaniem wcześniejszych wpisów.
