"""Produit le schema des 4 strates de l'architecture du SI Torpier.

Strates (de haut en bas) :
1. Processus metiers (ce que l'entreprise fait)
2. Fonctions metiers (ce que le SI supporte)
3. Applications (ce qui realise les fonctions)
4. Infrastructure (ce sur quoi ca tourne)

Sortie : 05-Strates-SI.png
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT = Path('/home/user/BLOC4/Livrables/00-Base-Commune')

STRATES = [
    {
        "titre": "PROCESSUS METIERS",
        "sous_titre": "Pilotage | Metiers coeur | Supports",
        "color": "#1B3A5B",
        "bg": "#E8EEF5",
        "items": [
            "Gouvernance", "Pilotage projets SI",
            "Commerce & relation client", "Conception & R&D",
            "Approvisionnement & fabrication", "Livraison & SAV",
            "RH & paie", "Comptabilite & facturation",
            "Reporting", "Support IT", "Securite & conformite",
        ],
    },
    {
        "titre": "FONCTIONS METIERS",
        "sous_titre": "Capacites que le SI doit offrir",
        "color": "#2E7D32",
        "bg": "#E8F5E9",
        "items": [
            "CRM / Ventes", "Commandes & devis",
            "Gestion production", "Stocks & approvisionnement",
            "Qualite & conformite", "CAO / BIM",
            "Comptabilite", "Paie & RH",
            "E-commerce B2C/B2B", "GED", "Reporting / BI",
            "ITSM (support)", "Messagerie & collaboration",
            "IAM / Securite",
        ],
    },
    {
        "titre": "APPLICATIONS",
        "sous_titre": "Logiciels qui realisent les fonctions",
        "color": "#6A1B9A",
        "bg": "#F3E5F5",
        "items": [
            "Microsoft Dynamics", "GesProd", "SAGE Compta", "SAGE Paie",
            "Qualeval", "ArchiCAD", "Revit", "PrestaShop",
            "DocuFlow", "MS Project", "Power BI",
            "Jira Service Management", "Exchange (migration)",
            "GitLab", "Active Directory",
        ],
    },
    {
        "titre": "INFRASTRUCTURE",
        "sous_titre": "Serveurs - reseau - postes - cloud",
        "color": "#EF6C00",
        "bg": "#FFF3E0",
        "items": [
            "Serveurs Windows 2019/2022 (Hyper-V)", "Cluster SQL AlwaysOn",
            "AD DS (Nanterre + replica Arras)", "GitLab (Ubuntu 22.04)",
            "Veeam (sauvegarde)", "WSUS", "RDS",
            "FortiGate 200E + Proxy", "VPN IPSec Fortinet",
            "Switches Cisco Catalyst + SG", "Routeurs Cisco ISR 4000",
            "PC Windows 11 + MacBook Pro", "Cloud Azure (Dynamics)",
            "Cloud OVH (PrestaShop)", "Cloud Atlassian (Jira)",
        ],
    },
]

fig, ax = plt.subplots(figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis("off")

# Titre
ax.text(10, 13.4, "Architecture du SI Torpier - 4 strates",
        ha="center", fontsize=24, fontweight="bold", color="#1B3A5B")

# Fleche verticale a gauche pour montrer l'alignement
ax.annotate("", xy=(0.8, 1.0), xytext=(0.8, 12.3),
            arrowprops=dict(arrowstyle="->", lw=2, color="#555"))
ax.text(0.3, 6.7, "Alignement du SI", rotation=90, ha="center", va="center",
        fontsize=11, fontweight="bold", color="#555")

# strates
strate_height = 2.5
for idx, strate in enumerate(STRATES):
    y = 10.8 - idx * (strate_height + 0.3)
    # fond de la strate
    ax.add_patch(patches.FancyBboxPatch((1.8, y), 17.8, strate_height,
                                         boxstyle="round,pad=0.03",
                                         linewidth=1.5,
                                         edgecolor=strate["color"],
                                         facecolor=strate["bg"]))
    # bandeau titre a gauche
    ax.add_patch(patches.Rectangle((1.8, y), 4.0, strate_height,
                                    linewidth=0,
                                    facecolor=strate["color"]))
    ax.text(3.8, y + strate_height / 2 + 0.3, strate["titre"],
            ha="center", va="center", fontsize=14,
            fontweight="bold", color="white")
    ax.text(3.8, y + strate_height / 2 - 0.4, strate["sous_titre"],
            ha="center", va="center", fontsize=9.5,
            color="white", style="italic")
    # items dans la zone droite, distribues en grille
    zone_x0, zone_x1 = 6.2, 19.4
    zone_y0 = y + 0.25
    zone_y1 = y + strate_height - 0.25
    items = strate["items"]
    # grille : 5 colonnes, lignes variables
    ncols = 5
    nrows = (len(items) + ncols - 1) // ncols
    cell_w = (zone_x1 - zone_x0) / ncols
    cell_h = (zone_y1 - zone_y0) / nrows
    for i, item in enumerate(items):
        r = i // ncols
        c = i % ncols
        cx = zone_x0 + c * cell_w + cell_w / 2
        cy = zone_y1 - r * cell_h - cell_h / 2
        # bulle de l'item
        box_w = cell_w * 0.9
        box_h = cell_h * 0.78
        ax.add_patch(patches.FancyBboxPatch((cx - box_w / 2, cy - box_h / 2),
                                             box_w, box_h,
                                             boxstyle="round,pad=0.02",
                                             linewidth=0.8,
                                             edgecolor=strate["color"],
                                             facecolor="white"))
        ax.text(cx, cy, item, ha="center", va="center",
                fontsize=9, color="#222222", wrap=True)

png_path = OUT / "05-Strates-SI.png"
plt.tight_layout()
plt.savefig(png_path, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"OK PNG : {png_path}")
