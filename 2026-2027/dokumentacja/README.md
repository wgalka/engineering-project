---
title: Dokumentacja projektu i raportowanie postępów
permalink: /2026-2027/dokumentacja/
---

# Dokumentacja projektu i raportowanie postępów

Dokumentacja ma powstawać równolegle z projektem. Każdy zespół raportuje postęp na początku **każdego laboratorium**, a po zajęciach aktualizuje zmienione części dokumentacji i dopisuje datowany wpis do dziennika. Nie odkładajcie całego opisu na ostatnie spotkanie.

## Co zawiera szablon UR

W dostarczonym PDF rozdział 4 przedstawia strukturę pracy projektowej. Warto zachować tę kolejność i rozwijać ją podczas kolejnych zajęć:

Rozdziały 1–3 tego PDF-a są przede wszystkim instruktażem LaTeX i przykładami elementów składu (list, tabel, rysunków, bibliografii). Część opisująca właściwą dokumentację projektu zaczyna się w rozdziale 4.

| Rozdział szablonu | Co zespół opisuje | Kiedy powstaje |
|---|---|---|
| **4.1 Opis założeń projektu** | Problem i jego źródła, dowody potrzeby, cel, proponowane rozwiązanie i zakres; przegląd istniejących rozwiązań; wymagania funkcjonalne i niefunkcjonalne; aktorów, przypadki użycia i scenariusze. | Laboratoria 1–3, później poprawiany po informacji zwrotnej. |
| **4.2 Opis struktury projektu** | Architekturę i główne elementy rozwiązania, użyte technologie, dane/bazę danych, uzasadnione diagramy, sposób uruchomienia i wymagania środowiskowe. | Szkic od laboratorium 3, rozwijany wraz z projektem. |
| **4.3 Harmonogram realizacji projektu** | Diagram Gantta i jego opis, repozytorium oraz kontrolę wersji; regularne porównanie planu z wykonaniem, problemy, decyzje i zmiany terminów. | Plan bazowy na laboratorium 4; aktualizacja na każdym późniejszym przeglądzie. |
| **4.4 Prezentacja warstwy użytkowej** | Opis najważniejszych widoków i scenariuszy oraz czytelne zrzuty ekranu/obrazy z podpisami i odwołaniami. | Gdy dostępny jest prototyp lub działający przyrost; domknięcie przed prezentacją. |
| **4.5 Podsumowanie** | Co zrealizowano, co potwierdzają testy, jakie są ograniczenia i co można rozwijać dalej. | Wersja robocza na laboratorium 5, uzupełniana po końcowej weryfikacji. |
| **4.6 Oświadczenie o samodzielności** | W PDF szablonu występuje osobne oświadczenie studenta; należy je dołączać tylko w formie i zakresie wymaganym przez prowadzącego. | Końcowe składanie dokumentu, jeśli ma zastosowanie. |

Praca zawiera też streszczenia, bibliografię i automatyczne spisy elementów, jeśli wymaga ich przekazany wariant szablonu. Rysunki, tabele i diagramy powinny mieć podpisy, odwołania w tekście i podane źródła.

## Jak wykorzystać pracę Jopeka

Praca Jopeka dostarcza wzoru treści dla trzech części, które trzeba włączyć do rozdziału 4.1 szablonu UR:

- **§1.3 — przegląd istniejących rozwiązań:** porównanie, kryteria i wniosek o luce lub wartości dodanej projektu;
- **§2.1 — wymagania:** uporządkowane wymagania funkcjonalne i niefunkcjonalne, możliwe do sprawdzenia;
- **§2.2 — przypadki użycia:** aktorzy, granica systemu, diagram oraz scenariusze kluczowych przypadków.

Nie przenoście numeracji 1.3, 2.1 i 2.2 jako numerów rozdziałów do dokumentacji UR. To numery części pracy referencyjnej; w szablonie UR treść należy umieścić w odpowiednich podrozdziałach **4.1 Opis założeń projektu**. Własną strukturę i decyzje techniczne rozwijajcie dalej w 4.2.

## Stały raport na laboratorium

Na początku każdego laboratorium każdy zespół przedstawia około **2–3 minut** raportu. Na pierwszym spotkaniu jest to raport bazowy: skład, wybrany problem i pierwszy plan. Po laboratorium, na którym tworzycie Gantta, obowiązuje dodatkowo krótki raport pisemny **co dwa tygodnie do końca roku akademickiego 2026/2027** — również wtedy, gdy w danym okresie nie ma laboratorium. Raport odpowiada na pytania:

1. Co zespół planował od poprzedniego spotkania i co rzeczywiście ukończył? Pokażcie dowód: dokument, diagram, commit, prototyp, wynik testu lub inne sprawdzalne artefakty.
2. Co pozostało w toku albo nie zostało wykonane i dlaczego?
3. Które części dokumentacji i harmonogramu zmieniono? Czy zmienił się zakres, termin, odpowiedzialność lub założenie?
4. Jakie są blokery, ryzyka albo decyzje potrzebne od prowadzącego?
5. Jakie są następne zadania, kto za nie odpowiada i do kiedy?

Po każdym laboratorium zespół uzupełnia dziennik postępów, aktualizuje dotknięte rozdziały i harmonogram, a zmiany zapisuje w repozytorium. W okresie po stworzeniu Gantta ten sam przegląd wykonuje co dwa tygodnie: porównuje postęp z planem bazowym, zapisuje odchylenia i przyczyny, aktualizuje terminy oraz wskazuje następny kamień milowy. Raporty trwają do końca roku akademickiego, nie kończą się na ostatnim laboratorium. Wzór do skopiowania: [szablon raportu postępu](szablon-raportu.md).

## Uwaga techniczna do plików w archiwum szablonu LaTeX

Podglądowy plik PDF dołączony do archiwum szablonu prezentuje w rozdziale 4 właściwą strukturę projektową **4.1–4.5** opisaną w tabeli powyżej (w tym rozdział 4.3 na diagram Gantta, repozytorium i kontrolę wersji). Zwróćcie jednak uwagę, że plik źródłowy `chapters/chapter004.tex` w archiwum ZIP może zawierać przykładową treść dotyczącą dokumentowania promptów AI, przez co po pierwszej kompilacji w Overleaf układ podrozdziałów będzie różnił się od podglądowego PDF.

Podczas pisania dokumentacji **zawsze stosujcie strukturę podrozdziałów 4.1–4.5 z tabeli powyżej**: zastąpcie demonstracyjną zawartość pliku `chapters/chapter004.tex` sekcjami odpowiadającymi kolejnym częściom Waszego projektu (4.1 Założenia, 4.2 Struktura, 4.3 Harmonogram, 4.4 Warstwa użytkowa, 4.5 Podsumowanie) i po kompilacji sprawdźcie, czy spis treści generuje się poprawnie.
