"""Generuje oba wzorcowe SVG i ich kopie z jednej sieci zadań.

Uruchomienie z dowolnego katalogu: python scripts/generuj_przyklady_gantta.py
Kalendarz przykładowych zespołów: pn.–pt., 11.11 i 6.01 wolne,
przerwa zespołu 22.12.2026–3.01.2027 (nie jest kalendarzem uczelni).
"""

from collections import defaultdict
from datetime import date, timedelta
from fractions import Fraction
from html import escape
from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
START = date(2026, 11, 2)
END = date(2027, 1, 18)
BREAK_START, BREAK_END = date(2026, 12, 22), date(2027, 1, 3)
HOLIDAYS = {date(2026, 11, 11), date(2027, 1, 6)}
CALENDAR = [START + timedelta(days=i) for i in range((END - START).days)]
WORKDAYS = [d for d in CALENDAR if d.weekday() < 5 and d not in HOLIDAYS
            and not BREAK_START <= d <= BREAK_END]
WIDTH, TIMELINE, DAY = 1700, 900, 10
CRITICAL, NORMAL, BUFFER, SPIKE = '#dc2626', '#2563eb', '#d97706', '#7c3aed'


def task(key, name, owner, work, duration, predecessors='', kind='task'):
    return dict(id=key, name=name, owner=owner, work=work, duration=duration,
                predecessors=predecessors.split(), kind=kind)


EXAMPLE_1 = [
    task('T01', 'Doprecyzować wymagania i kryteria RF-01…08', 'Ania', 6, 4),
    task('T02', 'Zaprojektować schemat bazy ERD i migracje', 'Bartek', 8, 6, 'T01'),
    task('T03', 'Przygotować makiety UI i kontrakt OpenAPI', 'Celina', 6, 5, 'T01'),
    task('M1', 'Architektura i ERD zatwierdzone', '—', 0, 0, 'T02 T03', 'milestone'),
    task('T04', 'Zaimplementować API slotów i blokady kolizji', 'Bartek', 12, 9, 'M1'),
    task('T05', 'Zbudować widok wyboru terminu i formularz', 'Celina', 10, 7, 'M1'),
    task('T06', 'Zintegrować formularz z API i przetestować E2E', 'Ania', 8, 4, 'T04 T05'),
    task('T07', 'Poprawić błędy z rezerwą przed demonstracją MVP', 'Ania', 4, 2, 'T06', 'buffer'),
    task('M2', 'Pierwszy przyrost MVP działa E2E', '—', 0, 0, 'T07', 'milestone'),
    task('T08', 'Zbudować panel dziekanatu: kolejka i status wizyty', 'Bartek', 12, 8, 'M2'),
    task('T09', 'Dodać powiadomienia e-mail i anulowanie rezerwacji', 'Celina', 10, 7, 'M2'),
    task('T10', 'Przetestować RF/RNF i poprawić wykryte błędy', 'Ania', 10, 6, 'T08 T09'),
    task('T11', 'Opracować rozdz. 4.2–4.5 LaTeX i instrukcję README', 'Celina', 6, 5, 'T08 T09'),
    task('T12', 'Przygotować demonstrację z rezerwą końcową', 'Ania', 4, 4, 'T10 T11', 'buffer'),
    task('M3', 'Projekt i dokumentacja gotowe do oddania', '—', 0, 0, 'T12', 'milestone'),
]
EXAMPLE_2 = [
    task('S01', 'Sprawdzić inferencję modelu YOLO na CPU (limit 4 h)', 'Dawid', 4, 3, kind='spike'),
    task('T01', 'Przygotować zbiór 300 zdjęć testowych i etykiety', 'Kasia', 8, 6),
    task('T02', 'Zdefiniować architekturę REST i kolejkę zadań', 'Marek', 6, 6, 'S01'),
    task('M1', 'Wykonalność potwierdzona, zbiór danych gotowy', '—', 0, 0, 'T01 T02', 'milestone'),
    task('T03', 'Dostroić model detekcji i wyeksportować ONNX', 'Dawid', 12, 10, 'M1'),
    task('T04', 'Zbudować serwis FastAPI i zapis wyników w PostgreSQL', 'Marek', 10, 8, 'M1'),
    task('T05', 'Zbudować panel operatora: podgląd klatek i alertów', 'Piotr', 10, 9, 'M1'),
    task('T06', 'Przygotować skrypt walidacji metryk Precision/Recall', 'Kasia', 6, 6, 'M1'),
    task('T07', 'Połączyć pipeline: Kamera → FastAPI → ONNX → UI', 'Marek', 8, 5, 'T03 T04 T05'),
    task('M2', 'Pierwszy przyrost detekcji na żywo gotowy', '—', 0, 0, 'T07', 'milestone'),
    task('T08', 'Zmierzyć czas odpowiedzi (RNF-01 < 500 ms) i zoptymalizować', 'Dawid', 8, 7, 'M2 T06'),
    task('T09', 'Przygotować Docker Compose i test na czystej maszynie', 'Piotr', 6, 6, 'M2'),
    task('T10', 'Opracować rozdz. 4.2–4.5: metryki, architektura i widoki', 'Kasia', 10, 8, 'T08 T09'),
    task('T11', 'Przygotować demonstrację z rezerwą na poprawki', 'Marek', 6, 4, 'T10', 'buffer'),
    task('M3', 'Projekt gotowy do oddania i obrony', '—', 0, 0, 'T11', 'milestone'),
]


def schedule(source, overrides=None):
    result = {}
    for original in source:
        t = dict(original)
        t['duration'] = (overrides or {}).get(t['id'], t['duration'])
        t['start'] = max((result[p]['end'] for p in t['predecessors']), default=0)
        t['end'] = t['start'] + t['duration']
        result[t['id']] = t
    finish = max(t['end'] for t in result.values())
    for key, t in reversed(list(result.items())):
        successors = [s for s in result.values() if key in s['predecessors']]
        t['late_start'] = min((s['late_start'] for s in successors), default=finish) - t['duration']
        t['slack'] = t['late_start'] - t['start']
    return result


def load_by_week(tasks):
    loads = defaultdict(lambda: [Fraction(0) for _ in range(11)])
    daily = defaultdict(Fraction)
    for t in tasks.values():
        if t['duration']:
            for d in WORKDAYS[t['start']:t['end']]:
                effort = Fraction(t['work'], t['duration'])
                loads[t['owner']][(d - START).days // 7] += effort
                daily[t['owner'], d] += effort
    # Oba przykładowe zespoły deklarują do 2 h na osobę w każdym dniu roboczym.
    assert all(hours <= 2 for hours in daily.values()), 'Przeciążenie osoby'
    assert sum(map(sum, loads.values())) == sum(t['work'] for t in tasks.values())
    return dict(sorted(loads.items()))


def x(d):
    return TIMELINE + (d - START).days * DAY


def ends(t):
    finish = x(WORKDAYS[t['end'] - 1] + timedelta(days=1))
    return (x(WORKDAYS[t['start']]), finish) if t['duration'] else (finish, finish)


def chunks(t):
    groups = []
    for d in WORKDAYS[t['start']:t['end']]:
        if groups and d == groups[-1][-1] + timedelta(days=1):
            groups[-1].append(d)
        else:
            groups.append([d])
    return [(x(g[0]), len(g) * DAY) for g in groups]


def color(t):
    return {'buffer': BUFFER, 'spike': SPIKE}.get(t['kind'], CRITICAL if t['slack'] == 0 else NORMAL)


def draw(number, source, titles, starts, baseline_overrides=None):
    tasks = schedule(source)
    baseline = schedule(source, baseline_overrides) if baseline_overrides else None
    loads = load_by_week(tasks)
    if baseline:
        load_by_week(baseline)
        assert all(tasks[k]['end'] == baseline[k]['end'] for k in ('M1', 'M2', 'M3'))
    if number == 2:
        assert tasks['T01']['slack'] == 3
    rows, groups, y = {}, [], 138
    for t in tasks.values():
        if t['id'] in starts:
            group_index = starts.index(t['id'])
            groups.append((y, group_index))
            y += 34
        rows[t['id']] = y
        y += 42
    bottom = y
    resource_top = bottom + 38
    legend_top = resource_top + (len(loads) + 1) * 28 + 24
    height = legend_top + 134
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="title desc" font-family="Segoe UI, Arial, sans-serif">',
           f'<title id="title">Poprawny harmonogram — przykład {number}, rok 2026/2027</title>',
           '<desc id="desc">Zadania, daty, zależności FS, ścieżka krytyczna i tygodniowe obciążenie każdej osoby. Szare pola to dni wolne. Nakład rozłożono równomiernie po dniach roboczych.</desc>',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10" fill="#64748b"/></marker></defs>']

    def rect(px, py, w, h, fill, extra=''):
        out.append(f'<rect x="{px}" y="{py}" width="{w}" height="{h}" fill="{fill}" {extra}/>')

    def text(px, py, content, size=13, fill='#1e293b', extra=''):
        out.append(f'<text x="{px}" y="{py}" font-size="{size}" fill="{fill}" {extra}>{escape(str(content))}</text>')

    def line(x1, y1, x2, y2, stroke='#e2e8f0', extra=''):
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" {extra}/>')

    def diamond(px, py, fill):
        out.append(f'<path d="M{px} {py-7} l7 7 l-7 7 l-7 -7 Z" fill="{fill}"/>')

    rect(0, 0, WIDTH, height, '#ffffff')
    rect(0, 0, WIDTH, 70, '#0f172a')
    title = 'System rezerwacji wizyt w dziekanacie' if number == 1 else 'System detekcji usterek z kamer przemysłowych'
    text(22, 29, f'PRZYKŁAD {number} · {title}', 20, '#ffffff', 'font-weight="700"')
    text(22, 53, 'Rok 2026/2027 · zależności FS · dni robocze pn.–pt. · dostępność każdej osoby: 2 h / dzień roboczy', 13, '#cbd5e1')
    text(22, 90, 'Wspólne dni wolne: 11.11.2026, 22.12.2026–03.01.2027 (przerwa zespołu), 06.01.2027. Weekendy zaznaczono na szaro.', 13)
    rect(0, 102, WIDTH, 36, '#f1f5f9')
    for px, label in [(22, 'ID / zadanie i rezultat'), (480, 'Właściciel'), (570, '[h]'), (632, '[dni]'), (700, 'Start – koniec'), (811, 'Poprzedniki')]:
        text(px, 125, label, 12, extra='font-weight="700"')
    for i in range(11):
        monday = START + timedelta(weeks=i)
        sunday = monday + timedelta(days=6)
        px = x(monday)
        text(px + 35, 115, f'T{i+1}', 11, extra='text-anchor="middle" font-weight="700"')
        span = f'{monday:%d}–{sunday:%d.%m}' if monday.month == sunday.month else f'{monday:%d.%m}–{sunday:%d.%m}'
        text(px + 35, 131, span, 9, extra='text-anchor="middle"')
        line(px, 102, px, legend_top - 12)
    for d in CALENDAR:
        if d not in WORKDAYS:
            rect(x(d), 138, DAY, bottom - 138, '#fef3c7' if BREAK_START <= d <= BREAK_END or d in HOLIDAYS else '#f1f5f9')
    for py, group_index in groups:
        start_index = list(tasks).index(starts[group_index])
        stop_index = list(tasks).index(starts[group_index + 1]) if group_index + 1 < len(starts) else len(tasks)
        members = list(tasks.values())[start_index:stop_index]
        rect(0, py, TIMELINE, 34, '#e8edf4')
        text(16, py + 22, titles[group_index], 14, extra='font-weight="700"')
        text(570, py + 22, sum(t['work'] for t in members), 13, extra='font-weight="700"')
        text(632, py + 22, max(t['end'] for t in members) - min(t['start'] for t in members), 13, extra='font-weight="700"')
        left, right = min(ends(t)[0] for t in members), max(ends(t)[1] for t in members)
        rect(left, py + 15, right - left, 5, '#0f172a')
    for t in tasks.values():
        tx, _ = ends(t)
        ty = rows[t['id']] + 17
        for p in t['predecessors']:
            _, px = ends(tasks[p])
            py = rows[p] + 17
            bend = max(px + 3, tx - 5)
            out.append(f'<path d="M{px} {py} H{bend} V{ty} H{tx}" fill="none" stroke="#64748b" stroke-width="1" marker-end="url(#arrow)"/>')
    for t in tasks.values():
        py = rows[t['id']]
        line(0, py + 42, WIDTH, py + 42)
        label = f"{t['id']}. {t['name']}"
        wrapped = textwrap.wrap(label, width=62, break_long_words=False)
        assert len(wrapped) <= 2, label
        for j, part in enumerate(wrapped):
            text(22, py + (19 if len(wrapped) == 1 else 15) + j * 16, part, 13,
                 CRITICAL if t['kind'] == 'milestone' else '#1e293b',
                 'font-weight="600"' if t['kind'] == 'milestone' else '')
        text(480, py + 22, t['owner'])
        text(570, py + 22, t['work'])
        text(632, py + 22, t['duration'])
        dates = f"{WORKDAYS[t['start']]:%d.%m}–{WORKDAYS[t['end']-1]:%d.%m}" if t['duration'] else f"{WORKDAYS[t['end']-1]:%d.%m} (koniec)"
        text(700, py + 22, dates, 11)
        text(811, py + 22, ','.join(t['predecessors']) or '—', 11)
        left, right = ends(t)
        if not t['duration']:
            diamond(right, py + 17, CRITICAL if t['slack'] == 0 else NORMAL)
        else:
            line(left, py + 17, right, py + 17, color(t), 'stroke-dasharray="2 3"')
            for bx, w in chunks(t):
                rect(bx, py + 10, w, 14, color(t), 'rx="2"')
            if number == 1:
                progress = 1 if t['id'] in ('T01', 'T02', 'T03') else {'T04': .55, 'T05': .6}.get(t['id'], 0)
                remaining = t['duration'] * DAY * progress
                for bx, w in chunks(t):
                    filled = min(w, remaining)
                    if filled > 0:
                        rect(bx, py + 16, filled, 4, '#15803d')
                    remaining -= filled
            if t['slack'] and number == 2 and t['id'] == 'T01':
                text(right + 8, py + 21, '+3 dni zapasu', 11, NORMAL)
            if baseline:
                for bx, w in chunks(baseline[t['id']]):
                    rect(bx, py + 29, w, 3, '#94a3b8')
    for px in (468, 558, 620, 690, 800, TIMELINE):
        line(px, 102, px, bottom, '#cbd5e1')
    if number == 1:
        sx = x(date(2026, 11, 24))
        line(sx, 138, sx, bottom, SPIKE, 'stroke-dasharray="5 4" stroke-width="2"')
        rect(sx - 71, 140, 142, 19, SPIKE, 'rx="3"')
        text(sx, 154, 'Status: 24.11.2026', 11, '#ffffff', 'text-anchor="middle"')
    text(22, bottom + 25, 'Kontrola obciążenia: zaplanowane h / dostępne h w tygodniu. Nakład rozłożony równomiernie po dniach roboczych; liczby zaokrąglone do 0,1 h.', 13)
    available = [2 * sum((d - START).days // 7 == i for d in WORKDAYS) for i in range(11)]
    all_loads = list(loads.items()) + [('Suma zespołu', [sum(v[i] for v in loads.values()) for i in range(11)])]
    for j, (owner, hours) in enumerate(all_loads):
        py = resource_top + j * 28
        rect(0, py, WIDTH, 28, '#f0fdf4' if j % 2 == 0 else '#f8fafc')
        total = sum(hours)
        text(22, py + 19, f'{owner} · łącznie {total} h', 13, '#166534', 'font-weight="600"')
        for i, effort in enumerate(hours):
            capacity = available[i] * (len(loads) if owner == 'Suma zespołu' else 1)
            assert effort <= capacity
            value = f'{float(effort):.1f}'.replace('.', ',')
            text(TIMELINE + i * 70 + 35, py + 19, f'{value} / {capacity}', 10, '#166534', 'text-anchor="middle"')
    rect(0, legend_top, WIDTH, 134, '#f1f5f9')
    for px, fill, label in [(22, CRITICAL, 'Zadanie krytyczne: zapas 0 dni'), (340, NORMAL, 'Zadanie niekrytyczne'), (610, BUFFER, 'Poprawki / demonstracja z rezerwą'), (1000, SPIKE, 'Data statusu' if baseline else 'Eksperyment (spike)'), (1260, '#94a3b8', 'Plan bazowy' if baseline else 'Dni wolne: pola szare i żółte')]:
        rect(px, legend_top + 17, 20, 12, fill)
        text(px + 28, legend_top + 28, label, 12)
    critical = ' → '.join(t['id'] for t in tasks.values() if t['slack'] == 0)
    text(22, legend_top + 54, f'Ścieżka krytyczna (przy zachowaniu zaplanowanych rezerw): {critical}', 13, extra='font-weight="600"')
    if baseline:
        text(22, legend_top + 78, 'T04: plan bazowy 7 dni → aktualnie 9 dni (+2). T07: 4 dni → 2 dni; nadal przewidziano 4 h na poprawki. M2 pozostaje 07.12.2026.', 13)
        text(22, legend_top + 100, 'Zielone linie oznaczają wykonany zakres; nie wynikają z upływu czasu. Pozostałą rezerwę skrócono świadomie po aktualizacji planu.', 13)
    else:
        text(22, legend_top + 78, 'T01 ma 3 dni zapasu: M1 czeka na dłuższą gałąź S01 → T02. Eksperyment S01 jest krytyczny, choć wyróżniono go fioletem.', 13)
        text(22, legend_top + 100, 'Cztery osoby pracują równolegle przy T03–T06. Integracja T07 czeka na T03, T04 i T05; T08 wymaga także T06.', 13)
    text(22, legend_top + 122, 'Opracowanie dydaktyczne. Rezerwy obejmują wskazany nakład pracy; ich skrócenie wymaga sprawdzenia dostępności wykonawcy.', 12, '#475569')
    out.append('</svg>')
    svg = '\n'.join(out) + '\n'
    filename = f'gantt-dobry-przyklad-{number}.svg'
    for directory in ('2026-2027/lab4/img', '2026-2027/lab4/gantt/img', 'img'):
        (ROOT / directory / filename).write_text(svg, encoding='utf-8', newline='\n')
    print(f'{filename}: {sum(t["work"] for t in tasks.values())} h, {max(t["end"] for t in tasks.values())} dni roboczych; koniec {WORKDAYS[max(t["end"] for t in tasks.values())-1]}')


if __name__ == '__main__':
    draw(1, EXAMPLE_1, ['1. Analiza i projekt architektury', '2. Pierwszy działający przyrost MVP', '3. Rozbudowa, testy i dokumentacja'], ['T01', 'T04', 'T08'], {'T04': 7, 'T07': 4})
    draw(2, EXAMPLE_2, ['1. Eksperyment i specyfikacja', '2. Równoległa budowa komponentów', '3. Weryfikacja, dokumentacja i oddanie'], ['S01', 'T03', 'T08'])
