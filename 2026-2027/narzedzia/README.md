---
title: Harmonogram, narzędzia i diagramy projektu
permalink: /2026-2027/narzedzia/
---

# Praca domowa: harmonogram Gantta i diagramy projektu

**Pełne laboratorium: [Diagram Gantta krok po kroku](../lab4/gantt-krok-po-kroku.md)** — planowanie pracy, przykład z obliczeniami, ścieżki w GanttProject i Asana, obciążenie, ryzyka, raportowanie i kryteria oddania. Zacznijcie od tej instrukcji. Poniżej znajdziecie skrót zasad oraz przewodnik po dodatkowych diagramach.

Ten przewodnik dotyczy laboratorium 4. Sam raport postępu i aktualizacja dokumentacji są wymagane na **każdym** laboratorium; zobacz [strukturę dokumentacji i wzór raportu](../dokumentacja/).

## Cel

Przed laboratorium 4 przygotujcie realistyczny plan prac i wybierzcie diagramy, które wyjaśniają wasz system. Gantt pokazuje kolejność i terminy zadań; diagramy analityczne i projektowe pomagają zrozumieć wymagania, dane, zachowanie i budowę rozwiązania.

## Jak przygotować dobry harmonogram Gantta

### 1. Zacznijcie od rezultatów

Ustalcie, co będzie gotowe na koniec projektu i jakie rezultaty pośrednie są potrzebne: zaakceptowany zakres, makieta, działający główny scenariusz, zintegrowana wersja, testy, dokumentacja i prezentacja. Dopiero potem rozpiszcie prace prowadzące do tych rezultatów.

### 2. Podzielcie pracę na zadania

Pogrupujcie zadania, np. analiza, projekt, implementacja, integracja, testy, dokumentacja i prezentacja. Nazwa powinna opisywać konkretną pracę oraz wynik: „Zaimplementować wyszukiwanie po nazwie” zamiast „Programowanie”. Nie rozpisujcie każdej drobnej czynności; zadania mają być na tyle małe, by dało się regularnie ocenić postęp.

Każde zadanie powinno mieć nazwę, oczekiwany rezultat, czas trwania, osobę odpowiedzialną, poprzedniki i sprawdzalne kryterium ukończenia. Czas trwania zadania to czas kalendarzowy planowanej pracy, a nie suma roboczogodzin całego zespołu.

### 3. Pokażcie zależności i kamienie milowe

Przykładowy łańcuch: doprecyzowanie wymagań → model danych → implementacja zapisu i odczytu → integracja → test głównego scenariusza. Zależność koniec–początek oznacza, że następne zadanie rusza po zakończeniu poprzedniego. Nie łączcie wszystkich zadań w jeden łańcuch, jeśli część prac może być wykonana równolegle.

Kamień milowy jest punktem kontrolnym bez czasu trwania, np. „zaakceptowany zakres”, „pierwsza zintegrowana wersja” lub „gotowość do prezentacji”. Uwzględnijcie integrację, testy, poprawki, dokumentację i rezerwę na ryzyka. Harmonogram, w którym cały semestr zajmuje tylko programowanie, jest niekompletny.

### 4. Sprawdźcie realizm

- Użyjcie rzeczywistych dat semestru i terminów spotkań.
- Uwzględnijcie zajęcia, egzaminy, dostępność członków zespołu i zależności zewnętrzne.
- Porównajcie obciążenie osób; kluczowe prace nie powinny zależeć wyłącznie od jednej osoby.
- Zostawcie uzasadnioną rezerwę na ryzyka i poprawki.
- Podzielcie długie prace na przyrosty, które można wcześnie zademonstrować.

### 5. Zapiszcie plan bazowy i aktualizujcie go

Po uzgodnieniu planu zachowajcie wersję bazową. Na początku każdego laboratorium raportujcie, co ukończono, co się przesunęło i jaki wpływ ma zmiana na kolejne zadania; po zajęciach dopiszcie tę informację do dziennika i rozdziału 4.3 dokumentacji. Po laboratorium 4 składajcie takie aktualizacje co dwa tygodnie aż do końca roku akademickiego 2026/2027, również po laboratorium 5. Nie przesuwajcie po cichu starych dat, żeby plan wyglądał na wykonany; zapiszcie aktualizację i przyczynę.

## Przykładowy szkielet

To punkt wyjścia, nie gotowy harmonogram do skopiowania.

| Etap | Przykładowe zadania | Rezultat / zależność |
|---|---|---|
| Analiza | Research, rozmowy z użytkownikami, wymagania | Zatwierdzony zakres i kryteria sukcesu |
| Projekt | Makieta, przypadki użycia, model danych, decyzje architektoniczne | Gotowe wejście do implementacji; część prac może iść równolegle |
| Pierwszy przyrost | Jeden główny scenariusz od interfejsu do danych | Wczesna demonstracja i informacja zwrotna |
| Rozbudowa | Kolejne funkcje, obsługa błędów, integracje | Funkcje powiązane z wymaganiami |
| Integracja i testy | Testy scenariuszy, poprawki, wymagania jakościowe | Wersja gotowa do oceny |
| Oddanie | Dokumentacja, instrukcja uruchomienia, prezentacja | Kompletne i odtwarzalne oddanie |

## Narzędzia do harmonogramu (Open Source i komercyjne)

Szczegółowe porównanie oraz instrukcje krok po kroku dla każdego z narzędzi znajdziecie w [Części III instrukcji laboratoryjnej](../lab4/gantt-krok-po-kroku.md#część-iii-wybierzcie-narzędzie-i-wprowadźcie-harmonogram-krok-7):

- **[GanttProject](https://www.ganttproject.biz/download) (Open Source, GPLv3)** — rekomendowane narzędzie desktopowe z hierarchią WBS, zależnościami, kamieniami milowymi, wykresem obciążenia zasobów, ścieżką krytyczną, liniami bazowymi i eksportem PDF/PNG; działa lokalnie na Windows, macOS i Linux.
- **[ProjectLibre Desktop](https://projectlibre.com/projectlibre-desktop/) (Open Source, CPAL)** — zaawansowane narzędzie desktopowe rozróżniające nakład godzinowy (*Work*) i czas trwania (*Duration*), wyposażone w sieć PERT/CPM, zapasy czasu (*Slack*) i bazę porównawczą; [dokumentacja](https://projectlibre.com/projectlibre-documentation/).
- **[Mermaid.js](https://mermaid.js.org/syntax/gantt.html) (Open Source, MIT)** — definicja wykresu Gantta jako kodu tekstowego w repozytorium Git (świetne uzupełnienie do `README.md` i raportów, wymagające ręcznego pilnowania tabeli obciążenia zasobów).
- **Narzędzia komercyjne / chmurowe (Asana, Jira Timeline/Plans, MS Project, ClickUp)** — możecie z nich skorzystać, jeśli zespół ma aktywny dostęp (np. edukacyjny lub okres próbny), pod warunkiem zachowania pełnego eksportu danych oraz czytelnych wydruków PDF/PNG w repozytorium.

Wybierzcie jedną główną ścieżkę narzędziową i zachowajcie plik źródłowy oraz eksport PDF/PNG. Zadbajcie o to, aby na wyeksportowanym rysunku każdy czytelnik bez trudu odczytał nazwy zadań, daty, strzałki zależności, kamienie milowe i odpowiedzialności.

## Jak dobrać diagramy

Nie rysujcie wszystkich rodzajów diagramów. Wybierzcie diagramy, które odpowiadają na konkretne pytania projektowe.

| Diagram | Pytanie, na które odpowiada | Kiedy go wybrać |
|---|---|---|
| Kontekst / granica systemu | Co należy do systemu, kto z niego korzysta i z czym się komunikuje? | Gdy zakres lub integracje są niejasne. |
| Przypadków użycia (UML) | Jakie cele użytkownicy realizują w systemie? | Wymagany w §2.2; pokazuje aktorów i cele, nie szczegóły ekranów. |
| Aktywności (UML) | Jak przebiega proces i gdzie są decyzje? | Dla złożonej logiki lub procesu biznesowego. |
| Sekwencji (UML) | Kto z kim i w jakiej kolejności wymienia komunikaty? | Dla jednego ważnego scenariusza. |
| Klas (UML) lub ERD | Jakie pojęcia, dane i relacje występują w systemie? | Gdy aplikacja przechowuje powiązane dane. ERD pokazuje dane, nie przepływ ekranów. |
| Komponentów | Z jakich większych części składa się rozwiązanie i jakie mają interfejsy? | Gdy są np. frontend, API, baza, model AI lub usługi zewnętrzne. |
| Wdrożenia (UML) | Gdzie działają elementy i jak są połączone? | Gdy istotne są urządzenia, serwery lub środowiska. |
| Stanów (UML) | Jak zmienia się stan konkretnego obiektu? | Dla cyklu życia zamówienia, zgłoszenia lub zadania. |

Na początek zwykle wystarczą przypadki użycia, model danych jeśli projekt przechowuje dane oraz diagram aktywności albo sekwencji dla głównego scenariusza. Diagram architektury lub wdrożenia dodajcie, gdy wyjaśnia istotną decyzję. Gantt opisuje terminy prac i nie zastępuje diagramu procesu ani UML.

## Narzędzia do diagramów i dokumentacji

- [diagrams.net / draw.io](https://www.drawio.com/docs/integrations/) — edytor online oraz aplikacja desktopowa do pracy offline; pliki można zachować w repozytorium.
- **Overleaf** — edycja i kompilacja LaTeX w przeglądarce; skorzystajcie z przekazanego ZIP-a szablonu UR.
- Zachowujcie format edytowalny (np. `.drawio`) oraz eksport czytelny w PDF. Każdy diagram opiszcie w tekście.

## Zadanie do oddania

Przed laboratorium 4 przygotujcie:

1. harmonogram od aktualnej daty do oddania projektu;
2. zadania z czasem, zależnościami, odpowiedzialnymi i sprawdzalnymi rezultatami;
3. co najmniej trzy kamienie milowe oraz zadania na testy, integrację, dokumentację i prezentację;
4. co najmniej jeden dodatkowy diagram wraz z krótkim uzasadnieniem jego wyboru;
5. pliki źródłowe i eksport diagramu oraz harmonogramu;
6. dwa najważniejsze ryzyka, ich wpływ na plan i sposób reakcji.

## Materiał odniesienia

Strukturę opisu researchu, wymagań i przypadków użycia można przeanalizować w §1.3, §2.1 i §2.2 pracy Tomasza Jopka, *Aplikacja mobilna: sklep z elektroniką*: [PDF pracy](https://staff-ksi.pwr.edu.pl/kopel/inz/2018.01_inz_Jopek.pdf). Korzystajcie z niej jako wzoru struktury i poziomu konkretu, cytując źródła i pisząc własnymi słowami.
