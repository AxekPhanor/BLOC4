"""Produit le SWOT Torpier en Excel (format 2x2) + PNG lisible."""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

OUT = Path('/home/user/BLOC4/Livrables/00-Base-Commune')
OUT.mkdir(parents=True, exist_ok=True)

# --- Contenu SWOT ---
STRENGTHS = [
    "Notoriete et heritage (entreprise familiale depuis 1862)",
    "Croissance soutenue : +30 % de CA entre 2023 et 2025",
    "Expertise bois + design ecoresponsable (Sophie Crelin, Samir Oufrani)",
    "Virage e-commerce reussi (PrestaShop + bots SAV)",
    "DSI structuree : DSI, Infra/Securite, PMO, Applicatif + devs",
    "Tiffany Valentia (PMP + Scrum Master) porte la cellule PMO",
    "Socle technique solide : cluster SQL AlwaysOn, Veeam, AD DS, GitLab",
    "Jira Service Management deploye (base ITIL)",
    "Culture SI presente chez les utilisateurs",
    "Direction fortement impliquee dans la strategie SI",
]

WEAKNESSES = [
    "Pas de PRA / PCA formalise (incendie -> 150 K EUR de perte)",
    "Echanges CSV fragiles entre GesProd et Dynamics",
    "Workflow de commandes via mail + Excel (atelier fabrication)",
    "Pas de replique AD DS en Finlande",
    "VLAN unique Production + Conception (cloisonnement insuffisant)",
    "Migration Exchange non finalisee",
    "Processus ITIL immatures (problemes, changement, connaissance)",
    "Absence de MFA / SSO central face au teletravail croissant",
    "VPN IPSec vieillissant pour 5+ sites europeens",
    "Serveurs Windows Server 2019 en fin de vie",
    "Processus de pilotage des projets SI en construction",
    "Aucun tableau de bord d'usage / service IT pour les metiers",
    "Barriere linguistique et culturelle avec l'usine finlandaise",
]

OPPORTUNITIES = [
    "Expansion europeenne : Allemagne, Italie, Espagne, Finlande",
    "Marche B2B prive (promoteurs immobiliers) en croissance",
    "Demande clients pour des produits ecoresponsables et traces",
    "Industrie 4.0 : IoT, maintenance predictive, automatisation",
    "Maturite du cloud (M365, Azure, iPaaS)",
    "Cadres reglementaires (RGPD, CSRD) valorisant la conformite",
    "Ecosystemes d'API et de donnees ouvertes (integration facilitee)",
    "Disponibilite de freelances pour absorber les pics de charge",
]

THREATS = [
    "Cybermenaces croissantes (ransomware, phishing) amplifiees par le teletravail",
    "Pression reglementaire : RGPD, NIS 2, CSRD",
    "Obsolescence technologique (Windows 2019, Exchange on-prem, VPN)",
    "Dependance a des applications internes vieillissantes (GesProd, DocuFlow)",
    "Penurie de competences IT et industrielles sur le marche",
    "Volatilite des cours du bois et tensions d'approvisionnement",
    "Concurrence europeenne accrue (entree sur de nouveaux marches)",
    "Risque d'incident physique (incendie, sinistre site)",
]

# --- Generation Excel ---
wb = Workbook()
ws = wb.active
ws.title = "SWOT Torpier"

THIN = Side(border_style="thin", color="AAAAAA")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
TITLE_FONT = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
SUB_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
BODY_FONT = Font(name="Calibri", size=10, color="222222")
FILL_S = PatternFill("solid", fgColor="2E7D32")  # vert - forces
FILL_W = PatternFill("solid", fgColor="C62828")  # rouge - faiblesses
FILL_O = PatternFill("solid", fgColor="1565C0")  # bleu - opportunites
FILL_T = PatternFill("solid", fgColor="EF6C00")  # orange - menaces
BG_S = PatternFill("solid", fgColor="E8F5E9")
BG_W = PatternFill("solid", fgColor="FFEBEE")
BG_O = PatternFill("solid", fgColor="E3F2FD")
BG_T = PatternFill("solid", fgColor="FFF3E0")

ws["A1"] = "SWOT - Groupe Torpier"
ws["A1"].font = Font(name="Calibri", size=20, bold=True, color="1B3A5B")
ws.merge_cells("A1:D1")
ws.row_dimensions[1].height = 32

# quadrants : titres en ligne 3, listes en colonne
def write_quadrant(col, fill_title, bg, title, items):
    c = ws.cell(row=3, column=col, value=title)
    c.font = SUB_FONT
    c.fill = fill_title
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = BORDER
    for i, item in enumerate(items, start=4):
        cell = ws.cell(row=i, column=col, value=f"- {item}")
        cell.font = BODY_FONT
        cell.fill = bg
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = BORDER

write_quadrant(1, FILL_S, BG_S, "Forces (Strengths)", STRENGTHS)
write_quadrant(2, FILL_W, BG_W, "Faiblesses (Weaknesses)", WEAKNESSES)
write_quadrant(3, FILL_O, BG_O, "Opportunites (Opportunities)", OPPORTUNITIES)
write_quadrant(4, FILL_T, BG_T, "Menaces (Threats)", THREATS)

for col_letter in "ABCD":
    ws.column_dimensions[col_letter].width = 45

max_rows = max(len(STRENGTHS), len(WEAKNESSES), len(OPPORTUNITIES), len(THREATS))
for r in range(4, 4 + max_rows):
    ws.row_dimensions[r].height = 30

ws.row_dimensions[3].height = 26

xlsx_path = OUT / "01-SWOT.xlsx"
wb.save(xlsx_path)
print(f"OK Excel : {xlsx_path}")

# --- Generation PNG lisible ---
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Titre
ax.text(5, 9.6, "SWOT - Groupe Torpier", ha="center", fontsize=22, fontweight="bold",
        color="#1B3A5B")

quadrants = [
    ("Forces", STRENGTHS, 0.2, 5, "#2E7D32", "#E8F5E9"),
    ("Faiblesses", WEAKNESSES, 5.2, 5, "#C62828", "#FFEBEE"),
    ("Opportunites", OPPORTUNITIES, 0.2, 0.2, "#1565C0", "#E3F2FD"),
    ("Menaces", THREATS, 5.2, 0.2, "#EF6C00", "#FFF3E0"),
]

for title, items, x, y, color_strong, color_soft in quadrants:
    # fond
    ax.add_patch(patches.FancyBboxPatch((x, y), 4.6, 4.3, boxstyle="round,pad=0.02",
                                        linewidth=1, edgecolor=color_strong,
                                        facecolor=color_soft))
    # bandeau titre
    ax.add_patch(patches.Rectangle((x, y + 3.8), 4.6, 0.5,
                                   linewidth=0, facecolor=color_strong))
    ax.text(x + 2.3, y + 4.05, title, ha="center", va="center",
            fontsize=14, fontweight="bold", color="white")
    # items
    text = "\n".join([f"- {it}" for it in items])
    ax.text(x + 0.15, y + 3.6, text, ha="left", va="top",
            fontsize=9, color="#222222", wrap=True)

png_path = OUT / "01-SWOT.png"
plt.tight_layout()
plt.savefig(png_path, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"OK PNG   : {png_path}")
