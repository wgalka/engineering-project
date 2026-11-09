---
title: Harmonogram, narzędzia i diagramy projektu
permalink: /2026-2027/narzedzia/
---

# Przewodnik: harmonogram Gantta i dobór diagramów projektowych

**Pełna instrukcja laboratoryjna: [Diagram Gantta krok po kroku](../lab4/gantt-krok-po-kroku.md)** — planowanie pracy, model referencyjny z obliczeniami, instrukcje dla programów GanttProject, ProjectLibre, Mermaid i Asana, kontrola obciążenia, analiza ryzyk, raportowanie dwutygodniowe oraz przykłady wzorcowych i błędnych wykresów. Poniżej znajduje się podsumowanie zasad oraz przewodnik doboru dodatkowych diagramów projektowych.

Raport postępu i aktualizacja dokumentacji obowiązują na każdym laboratorium; szczegółowy układ rozdziałów znajduje się w [przewodniku dokumentacji i raportowania](../dokumentacja/).

## Cel

Przygotowanie realistycznego planu prac oraz dobór diagramów wyjaśniających budowę i działanie projektowanego systemu. Wykres Gantta określa kolejność i terminy zadań zespołu, natomiast diagramy analityczne i projektowe opisują wymagania, dane, zachowanie i architekturę rozwiązania.

## Zasady przygotowania harmonogramu Gantta

### 1. Określenie rezultatów projektu

W pierwszej kolejności należy zdefiniować produkt końcowy oraz rezultaty pośrednie: zatwierdzony zakres, makiety, działający główny scenariusz (pierwszy przyrost), wersję zintegrowaną, testy, dokumentację oraz prezentację. Dopiero na tej podstawie definiowane są zadania prowadzące do poszczególnych rezultatów.

### 2. Podział pracy na zadania (WBS)

Zadania należy pogrupować w etapy: analiza, projekt, pierwszy przyrost, rozbudowa, integracja i testy, dokumentacja i oddanie. Nazwa każdego zadania powinna wskazywać czynność i sprawdzalny rezultat (np. *„Zaimplementować wyszukiwanie sal po parametrach”* zamiast *„Programowanie”*). Zadania powinny mieć szczegółowość pozwalającą na ocenę postępu w cyklu dwutygodniowym.

Każde zadanie musi posiadać nazwę, oczekiwany rezultat, nakład pracy w godzinach, czas trwania w dniach, przypisaną osobę odpowiedzialną, poprzedniki oraz sprawdzalne kryterium ukończenia. Czas trwania oznacza czas kalendarzowy realizacji zadania przy dostępności danego wykonawcy, a nie sumę roboczogodzin zespołu.

### 3. Zależności i kamienie milowe

Przykładowy ciąg zależności: doprecyzowanie wymagań → model danych → implementacja zapisu i odczytu → integracja → test głównego scenariusza. Relacja koniec–początek (`FS`) oznacza, że zadanie następne rozpoczyna się po ukończeniu poprzednika. Nie należy łączyć wszystkich zadań w jeden szeregowy łańcuch, jeżeli część prac może przebiegać równolegle.

Kamień milowy jest punktem kontrolnym o zerowym czasie trwania (`0 dni`), np. *„M1: Zatwierdzony zakres i ERD”*, *„M2: Pierwszy przyrost zintegrowany”* lub *„M3: Gotowość do obrony”*. W harmonogramie należy uwzględnić integrację, testy, poprawki, dokumentację oraz rezerwę na ryzyka.

### 4. Weryfikacja wykonalności planu

- Zastosować rzeczywiste daty semestru, przerw świątecznych i kolokwiów.
- Uwzględnić tygodniową dostępność godzinową każdego członka zespołu.
- Zweryfikować obciążenie zasobów — suma godzin zadań przypisanych jednej osobie w danym tygodniu nie może przekraczać jej dostępności.
- Dodać uzasadnioną rezerwę czasową przed kluczowymi kamieniami milowymi.
- Zaplanować pierwszy działający przyrost odpowiednio wcześnie przed końcem semestru.

### 5. Zapis planu bazowego i aktualizacje dwutygodniowe

Po zatwierdzeniu harmonogramu należy zapisać wersję bazową (*Baseline*). Po Laboratorium 4 aktualizacje postępu wykonywane są co dwa tygodnie aż do końca roku akademickiego 2026/2027 (również po Laboratorium 5). W każdym przeglądzie należy porównać stan rzeczywisty z planem bazowym, udokumentować wykonane prace, zapisać przyczyny odchyleń oraz zaktualizować dziennik raportów i rozdział 4.3 dokumentacji LaTeX.

## Przykładowy układ etapów WBS

| Etap | Przykładowe zadania | Rezultat / zależność |
|---|---|---|
| Analiza | Analiza źródeł, doprecyzowanie wymagań i kryteriów odbioru | Zatwierdzony zakres MVP i lista wymagań |
| Projekt | Makiety interfejsu, przypadki użycia, model danych ERD, architektura | Dane wejściowe do implementacji; prace mogą iść równolegle |
| Pierwszy przyrost | Główny scenariusz od interfejsu przez API do bazy danych | Wczesna weryfikacja działania systemu |
| Rozbudowa | Pozostałe wymagania funkcjonalne, walidacja, obsługa błędów | Funkcje powiązane z identyfikatorami wymagań |
| Integracja i testy | Testy scenariuszy użycia, testy niefunkcjonalne, poprawki błędów | Zweryfikowana wersja systemu |
| Oddanie | Dokumentacja LaTeX (rozdz. 4.1–4.5), instrukcja uruchomienia, prezentacja | Kompletny i odtwarzalny pakiet końcowy |

## Narzędzia do harmonogramu (open source i komercyjne)

Szczegółowe porównanie oraz instrukcje krok po kroku dla poszczególnych narzędzi znajdują się w [Części III instrukcji laboratoryjnej](../lab4/gantt-krok-po-kroku.md#część-iii-wybór-narzędzia-i-wprowadzenie-harmonogramu-krok-7):

- **[GanttProject](https://www.ganttproject.biz/download) (Open Source, GPLv3)** — program desktopowy obsługujący hierarchię WBS, zależności, kamienie milowe, wykres obciążenia zasobów, ścieżkę krytyczną, linie bazowe i eksport PDF/PNG (Windows, macOS, Linux).
- **[ProjectLibre Desktop](https://projectlibre.com/projectlibre-desktop/) (Open Source, CPAL)** — program desktopowy rozróżniający nakład godzinowy (*Work*) i czas trwania (*Duration*), wyposażony w sieć PERT/CPM, wyliczanie zapasów czasu (*Slack*) i bazę porównawczą; [dokumentacja](https://projectlibre.com/projectlibre-documentation/).
- **[Mermaid.js](https://mermaid.js.org/syntax/gantt.html) (Open Source, MIT)** — tekstowy zapis wykresu Gantta w repozytorium Git (uzupełnienie dokumentacji wymagające osobnej tabeli obciążenia zasobów).
- **Narzędzia komercyjne (Asana, Jira Timeline/Plans, MS Project, ClickUp)** — możliwe do wykorzystania przy posiadaniu aktywnego dostępu zespołowego, pod warunkiem zachowania pełnego eksportu danych oraz czytelnych wydruków PDF/PNG w repozytorium.

Należy wybrać jedną główną ścieżkę narzędziową i zachować plik źródłowy oraz eksport PDF/PNG z czytelnymi nazwami zadań, datami, strzałkami zależności, kamieniami milowymi i przypisanymi osobami.

## Dobór dodatkowych diagramów projektowych

Nie należy tworzyć wszystkich rodzajów diagramów. Należy wybrać diagramy odpowiadające na istotne pytania projektowe dla danego systemu.

| Diagram | Pytanie projektowe | Zastosowanie |
|---|---|---|
| Kontekstu / granicy systemu | Co należy do systemu, kto z niego korzysta i z jakimi usługami się komunikuje? | Gdy zakres systemu lub integracje zewnętrzne wymagają rozgraniczenia. |
| Przypadków użycia (UML) | Jakie cele realizują użytkownicy w systemie? | Wymagany w rozdziale 4.1; przedstawia aktorów i ich cele, bez szczegółów interfejsu. |
| Aktywności (UML) | Jak przebiega proces i w jakich punktach podejmowane są decyzje? | Dla złożonej logiki biznesowej lub wieloetapowego algorytmu. |
| Sekwencji (UML) | W jakiej kolejności komponenty wymieniają komunikaty? | Dla kluczowego scenariusza obejmującego kilka warstw systemu. |
| Klas (UML) lub ERD | Jakie encje, atrybuty i relacje występują w bazie danych? | Gdy aplikacja przetwarza i składuje powiązane dane. |
| Komponentów | Z jakich modułów składa się rozwiązanie i jakie mają interfejsy? | Gdy system dzieli się na frontend, API, bazę danych, moduł AI lub usługi zewnętrzne. |
| Wdrożenia (UML) | Na jakich węzłach i w jakich środowiskach uruchamiane są elementy systemu? | Gdy istotna jest konfiguracja serwerów, kontenerów lub urządzeń. |
| Stanów (UML) | Jak zmienia się stan wybranego obiektu w cyklu życia? | Dla obiektów o wielu stanach (np. rezerwacja, zamówienie, zgłoszenie). |

## Narzędzia do diagramów i dokumentacji

- [diagrams.net / draw.io](https://www.drawio.com/docs/integrations/) — edytor online oraz aplikacja desktopowa do pracy lokalnej; pliki źródłowe `.drawio` należy przechowywać w repozytorium.
- **Overleaf / LaTeX** — przygotowanie dokumentacji na podstawie szablonu UR.
- Dla każdego diagramu należy zachować plik edytowalny oraz eksport PDF/PNG i umieścić odwołanie wraz z opisem w tekście dokumentacji.

## Zakres przygotowania na Laboratorium 4

1. Harmonogram od bieżącej daty do końcowego oddania projektu.
2. Zadania z określonym nakładem pracy, czasem trwania, zależnościami, właścicielami i kryteriami ukończenia.
3. Co najmniej trzy kamienie milowe oraz zadania obejmujące integrację, testy, dokumentację i prezentację.
4. Co najmniej jeden dodatkowy diagram techniczny do rozdziału 4.2 wraz z uzasadnieniem wyboru.
5. Pliki źródłowe i eksporty diagramu oraz harmonogramu.
6. Minimum trzy ryzyka harmonogramowe, ich wpływ na plan oraz sposób reakcji.

## Materiał odniesienia

Strukturę opisu przeglądu rozwiązań, wymagań i przypadków użycia można przeanalizować w §1.3, §2.1 i §2.2 pracy Tomasza Jopka, *Aplikacja mobilna: sklep z elektroniką*: [PDF pracy](https://staff-ksi.pwr.edu.pl/kopel/inz/2018.01_inz_Jopek.pdf).
