---
title: Plan laboratoriów 2026/2027
permalink: /2026-2027/
---

# Projekt inżynierski — plan laboratoriów

## Organizacja pracy w semestrze

Cykl laboratoryjny obejmuje **15 godzin kontaktowych (5 spotkań po 3 godziny lekcyjne)**. Jeśli plan zajęć danej grupy dzieli godziny na krótsze spotkania, realizujcie kolejne etapy zgodnie z porządkiem kamieni milowych opisanym poniżej.

Zespoły pracują nad projektem również między laboratoriami. **Każde laboratorium zaczyna się raportem postępu**: zespół porównuje wykonane prace z poprzednim planem, pokazuje dowód pracy, zgłasza przeszkody i podaje następne zadania z osobami odpowiedzialnymi i terminami. Po laboratorium, na którym powstaje Gantt, zespoły składają krótki raport pisemny **co dwa tygodnie aż do końca roku akademickiego 2026/2027**. Każdy raport aktualizuje dziennik i zmienione części dokumentacji, w tym plan bazowy oraz stan rzeczywisty harmonogramu.

## Przebieg semestru

| Laboratorium | Temat i stały raport | Aktualizowany fragment dokumentacji |
|---|---|---|
| [1 — Wybór problemu i zespołu](lab1/README.md) | Raport bazowy; wybór tematu i research. | Karta projektu; roboczy pakiet 4.1: materiał na podstawie §1.3, §2.1 i §2.2 pracy Jopeka. |
| [2 — Prezentacje koncepcji](lab2/README.md) | Raport z prac od laboratorium 1 i prezentacja wszystkich trzech części. | Poprawiony opis 4.1, wymagania, przypadki użycia i zapis decyzji/uwag. |
| [3 — Wymagania i przypadki użycia](lab3/README.md) | Raport z realizacji ustaleń i aktualizacja ryzyk. | Wymagania, diagram i scenariusze w 4.1; szkic struktury 4.2. |
| [4 — Harmonogram i diagramy](lab4/README.md) | Raport plan–wykonanie; ustalenie bazowego Gantta. | 4.2 struktura techniczna; 4.3 Gantt, repozytorium i dziennik przeglądów. Potem raport co 2 tygodnie do końca roku akademickiego. |
| [5 — Przegląd i prezentacja](lab5/README.md) | Raport stanu, dowody działania i odchylenia od planu. | 4.4 interfejs, 4.5 podsumowanie, testy i aktualizacja 4.3; raportowanie trwa dalej do końca roku akademickiego. |

Stały rytm pracy i wzory raportu opisano w [przewodniku dokumentacji](dokumentacja/README.md). Każdy zespół dopisuje raport do własnego repozytorium, np. do `dokumentacja/raporty/postepy.md`, i wykorzystuje go do aktualizacji rozdziału 4.3 oraz każdej części, której treść się zmieniła.

## Dokumentacja projektowa

Punktem odniesienia jest praca Tomasza Jopka, *Aplikacja mobilna: sklep z elektroniką*. Zespoły opracowują własne treści, korzystając ze struktury i sposobu argumentacji w następujących częściach:

- §1.3 — przegląd aktualnych rozwiązań;
- §2.1 — wymagania funkcjonalne i niefunkcjonalne;
- §2.2 — diagram przypadków użycia i opis scenariuszy.

Studenci korzystają z przekazanego szablonu LaTeX UR, zastępując demonstracyjne treści opisem własnego projektu. Strukturę dokumentu wyznaczają rozdziały 4.1–4.5 szablonu; treści z pracy Jopeka są wzorem dla researchu, wymagań i przypadków użycia, a nie numeracją rozdziałów do skopiowania. Szczegółowe mapowanie i zauważoną niespójność plików szablonu opisuje [przewodnik dokumentacji](dokumentacja/README.md). Nie kopiujcie tekstu, diagramów ani implementacji z pracy wzorcowej. [Praca Jopeka — PDF](https://staff-ksi.pwr.edu.pl/kopel/inz/2018.01_inz_Jopek.pdf).

## Materiały

- [Instrukcje laboratoryjne](../)
- [Przewodnik po harmonogramie, narzędziach i diagramach](narzedzia/README.md)
- [Dokumentacja projektu i raportowanie postępów](dokumentacja/README.md)
- Szablon LaTeX i instrukcja importu są materiałami kursowymi przechowywanymi lokalnie w `priv/` i przekazywanymi zespołom osobno.

## Kryteria przeglądu

- Research ma sprawdzalne źródła, porównuje rozwiązania według wspólnych kryteriów i uzasadnia wartość dodaną bez deklarowania nieudowodnionej „globalnej unikalności”.
- Wymagania są jednoznaczne i możliwe do zweryfikowania; kryteria jakościowe są mierzalne.
- Diagramy są czytelne, zgodne z zakresem i opisane w tekście.
- Harmonogram obejmuje analizę, projekt, implementację, integrację, testy, dokumentację i prezentację; zadania mają czas, zależności i odpowiedzialnych.
- Każde laboratorium ma datowany wpis postępu, dowody wykonanych prac, aktualny plan i zmienione fragmenty dokumentacji.
- Demonstracja odpowiada wymaganiom, a testy mają zapisany wynik.
