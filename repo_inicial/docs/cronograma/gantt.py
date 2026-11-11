# -*- coding: utf-8 -*-
"""Genera el diagrama de Gantt a partir de tareas.csv.
Uso: python gantt.py  ->  gantt.png
Para actualizar el cronograma, edita las fechas o las horas en tareas.csv y vuelve a ejecutarlo."""
import json, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch

import csv
tasks = []
for r in csv.DictReader(open("tareas.csv", encoding="utf8")):
    tasks.append({"id": r["id"], "corto": r["corto"], "fase": r["fase"], "inicio": r["inicio"], "fin": r["fin"], "horas": r["horas"]})
P = lambda s: dt.date.fromisoformat(s)
FASES = [
 ("F3", "Fase 3 · Planificación", "#7F7F7F"),
 ("F4", "Fase 4 · Diseño de la interfaz", "#2F5496"),
 ("EX", "Exámenes 1ª evaluación (tarea ligera)", "#BF9000"),
 ("F5", "Fase 5 · Desarrollo cliente", "#548235"),
 ("F6", "Fase 6 · Desarrollo servidor y persistencia", "#C55A11"),
 ("F7", "Fase 7 · Despliegue, pruebas, digitalización y sostenibilidad", "#7030A0"),
 ("F8", "Fase 8 · Cierre y defensa", "#C00000"),
]
color = {k: c for k, _, c in FASES}
title = {k: t for k, t, _ in FASES}

rows = []   # (tipo, datos)
for k, t, c in FASES:
    rows.append(("h", k))
    for tk in tasks:
        if tk["fase"] == k: rows.append(("t", tk))
n = len(rows)
fig, ax = plt.subplots(figsize=(11.2, 7.0), dpi=200)
ypos = {}
for i, (kind, d) in enumerate(rows):
    y = n - i
    if kind == "h":
        ax.text(dt.date(2026, 10, 31), y, title[d], fontsize=6.6, fontweight="bold", color=color[d], va="center", ha="left", zorder=5,
                transform=ax.get_yaxis_transform() if False else ax.transData)
        ax.axhspan(y - 0.5, y + 0.5, color=color[d], alpha=0.07, zorder=0)
    else:
        s, e = P(d["inicio"]), P(d["fin"]) + dt.timedelta(days=1)
        ax.barh(y, (e - s).days, left=s, height=0.62, color=color[d["fase"]], zorder=3)
        ax.text(e + dt.timedelta(days=0.6), y, f'{d["horas"]} h', fontsize=5.6, va="center", color="#333333", zorder=4)
        ypos[d["id"]] = (y, s, e)

# etiquetas de tareas a la izquierda (fuera del eje de fechas) 
ax.set_yticks([n - i for i, (k, d) in enumerate(rows)])
ax.set_yticklabels([("" if k == "h" else f'{d["id"]}  {d["corto"]}') for k, d in rows], fontsize=5.8)
ax.tick_params(axis="y", length=0)

# periodos especiales
ax.axvspan(dt.date(2026, 11, 23), dt.date(2026, 12, 7), color="#FFD966", alpha=0.35, zorder=1)
ax.axvspan(dt.date(2026, 12, 21), dt.date(2027, 1, 11), color="#9DC3E6", alpha=0.30, zorder=1)
ax.text(dt.date(2026, 11, 30), n + 1.6, "Exámenes\n1ª evaluación", fontsize=5.6, ha="center", va="bottom", color="#7F6000")
ax.text(dt.date(2026, 12, 31), n + 1.6, "Navidad\n(menos horas)", fontsize=5.6, ha="center", va="bottom", color="#1F4E79")

# hitos / entregas
hitos = [(dt.date(2026, 11, 8), "Entrega\nFase 3"), (dt.date(2026, 11, 22), "Entrega\nFase 4"),
         (dt.date(2026, 12, 20), "Entrega\nFase 5"), (dt.date(2027, 1, 10), "Entrega\nFase 6"),
         (dt.date(2027, 1, 24), "Entrega\nFase 7"), (dt.date(2027, 2, 7), "Entrega F8\ny exposición")]
for d_, t_ in hitos:
    ax.axvline(d_ + dt.timedelta(days=1), color="#222222", lw=0.6, ls=":", zorder=2)
    ax.plot([d_ + dt.timedelta(days=1)], [n + 0.9], marker="D", color="#222222", ms=4, zorder=6, clip_on=False)
    ax.text(d_ + dt.timedelta(days=1), n + 1.6, t_, fontsize=5.6, ha="center", va="bottom", fontweight="bold")
ax.text(dt.date(2027, 2, 19), n + 1.6, "Prácticas FE\n(mediados\nde febrero)", fontsize=5.4, ha="center", va="bottom", color="#555555")

# dependencias principales
deps = [("T05","T10"),("T06","T10"),("T07","T11"),("T10","T14"),("T11","T13"),("T10","T16"),("T13","T17"),("T16","T17"),
        ("T17","T18"),("T18","T19"),("T16","T20"),("T20","T21"),("T19","T22"),("T21","T22"),("T19","T23"),("T21","T23"),("T23","T24"),
        ("T24","T29"),("T29","T30"),("T30","T31"),("T29","T32")]
for a, b in deps:
    ya, sa, ea = ypos[a]; yb, sb, eb = ypos[b]
    x1 = ea; x2 = sb
    ax.annotate("", xy=(x2, yb + 0.31 if yb < ya else yb - 0.31), xytext=(x1, ya),
                arrowprops=dict(arrowstyle="-|>", lw=0.5, color="#555555", alpha=0.75, shrinkA=0, shrinkB=0,
                                connectionstyle="angle,angleA=0,angleB=90,rad=0"), zorder=4)

ax.set_xlim(dt.date(2026, 11, 1), dt.date(2027, 2, 24))
ax.set_ylim(0.2, n + 1.2)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
plt.setp(ax.get_xticklabels(), fontsize=5.4, rotation=90)
ax.grid(axis="x", color="#BBBBBB", lw=0.3, zorder=0)
for s_ in ("top", "right", "left"): ax.spines[s_].set_visible(False)
ax.set_title("Diagrama de Gantt · Sistema de Gestión de Huertos Urbanos Municipales (semanas que empiezan en lunes; las flechas marcan las dependencias principales)",
             fontsize=7, loc="left", pad=34)
leg = [Patch(color=c, label=t) for k, t, c in FASES]
fig.legend(handles=leg, loc="lower center", ncol=4, fontsize=5.6, frameon=False, bbox_to_anchor=(0.55, 0.0))
plt.subplots_adjust(left=0.185, right=0.985, top=0.9, bottom=0.115)
fig.savefig("gantt.png")
print("gantt ok", n, "filas")
