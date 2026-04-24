"""Architecture du SI Torpier - 4 strates - version pro."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

from charte import (Charte, setup_figure, add_header, add_footer,
                    shadow, save, wrap)
import matplotlib.patches as patches

OUT = Path('/home/user/BLOC4/Livrables/00-Base-Commune')

STRATES = [
    {
        "titre": "Processus",
        "sous_titre": "Ce que l'entreprise fait",
        "color": Charte.PRIMARY,
        "soft": "#E5ECF4",
        "items": [
            "Gouvernance", "Pilotage projets SI",
            "Commerce et relation client", "Conception et R&D",
            "Approvisionnement et fabrication",
            "Livraison et SAV", "RH et paie",
            "Comptabilite et facturation", "Reporting",
            "Support IT", "Securite et conformite",
        ],
    },
    {
        "titre": "Fonctions",
        "sous_titre": "Capacites que le SI doit offrir",
        "color": Charte.SECONDARY,
        "soft": "#DCEFEE",
        "items": [
            "CRM / Ventes", "Commandes et devis",
            "Gestion production", "Stocks et approvisionnement",
            "Qualite et conformite", "CAO / BIM",
            "Comptabilite", "Paie et RH", "E-commerce B2C/B2B",
            "GED", "Reporting / BI",
            "ITSM (support)", "Messagerie et collaboration",
            "IAM / Securite",
        ],
    },
    {
        "titre": "Applications",
        "sous_titre": "Logiciels qui realisent les fonctions",
        "color": Charte.VIOLET,
        "soft": Charte.VIOLET_SOFT,
        "items": [
            "Microsoft Dynamics", "GesProd", "SAGE Compta",
            "SAGE Paie", "Qualeval", "ArchiCAD", "Revit",
            "PrestaShop", "DocuFlow", "MS Project", "Power BI",
            "Jira Service Management", "Exchange (migration)",
            "GitLab", "Active Directory",
        ],
    },
    {
        "titre": "Infrastructure",
        "sous_titre": "Serveurs, reseau, postes, cloud",
        "color": Charte.ACCENT,
        "soft": Charte.ACCENT_LIGHT,
        "items": [
            "Serveurs Windows 2019 / 2022 (Hyper-V)",
            "Cluster SQL AlwaysOn",
            "AD DS (Nanterre + replica Arras)",
            "GitLab (Ubuntu 22.04)",
            "Veeam (sauvegarde)", "WSUS", "RDS",
            "FortiGate 200E + Proxy",
            "VPN IPSec Fortinet",
            "Switches Cisco Catalyst + SG",
            "Routeurs Cisco ISR 4000",
            "PC Windows 11 + MacBook Pro",
            "Cloud Azure (Dynamics)",
            "Cloud OVH (PrestaShop)",
            "Cloud Atlassian (Jira)",
        ],
    },
]


def render() -> Path:
    fig, ax, W, H = setup_figure()
    add_header(
        ax,
        title="Architecture du SI Torpier - 4 strates",
        subtitle="Alignement vertical : processus > fonctions > applications > infrastructure",
        width=W, height=H,
        kicker="Phase 1 - Cartographie",
    )

    # Zone utile (sous le header, au-dessus du footer)
    zone_top = H - 8
    zone_bot = 4
    zone_left = Charte.MARGIN_X + 3.5  # bande gauche pour la fleche
    zone_right = W - Charte.MARGIN_X

    n_strates = len(STRATES)
    gap = 0.9
    total_h = zone_top - zone_bot - gap * (n_strates - 1)
    strate_h = total_h / n_strates

    # Fleche verticale a gauche ("alignement strategique")
    arrow_x = Charte.MARGIN_X + 0.9
    ax.annotate("", xy=(arrow_x, zone_bot), xytext=(arrow_x, zone_top),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5",
                                lw=2, color=Charte.MUTED))
    ax.text(arrow_x - 0.9, (zone_top + zone_bot) / 2,
            "Alignement strategique",
            rotation=90, ha="center", va="center",
            fontsize=11, color=Charte.MUTED, family=Charte.FONT,
            fontweight="bold")

    for idx, strate in enumerate(STRATES):
        y_top = zone_top - idx * (strate_h + gap)
        y = y_top - strate_h
        x = zone_left
        w = zone_right - zone_left
        band_w = 16
        items_x0 = x + band_w + 1.2
        items_x1 = x + w - 0.8

        # ombre sur toute la carte
        shadow(ax, x, y, w, strate_h)

        # bandeau gauche colore (rectangle simple, coins nets)
        ax.add_patch(patches.Rectangle(
            (x, y), band_w, strate_h,
            linewidth=0, facecolor=strate["color"], zorder=2))

        # zone items (blanche)
        ax.add_patch(patches.Rectangle(
            (x + band_w, y), w - band_w, strate_h,
            linewidth=0, facecolor="white", zorder=2))

        # contour global arrondi (au-dessus)
        ax.add_patch(patches.FancyBboxPatch(
            (x, y), w, strate_h,
            boxstyle="round,pad=0.02,rounding_size=0.4",
            linewidth=0.9, edgecolor=Charte.LINE,
            facecolor="none", zorder=5))

        # numero de strate (pastille)
        num_cx = x + 1.7
        num_cy = y + strate_h - 1.4
        ax.add_patch(patches.Circle((num_cx, num_cy), 0.95,
                                    facecolor="white", alpha=0.15,
                                    zorder=4))
        ax.text(num_cx, num_cy, f"{idx + 1}",
                ha="center", va="center",
                fontsize=16, fontweight="bold", color="white",
                zorder=5, family=Charte.FONT)

        # titre de strate
        ax.text(x + 3.2, y + strate_h - 1.3, strate["titre"].upper(),
                ha="left", va="center",
                fontsize=13, fontweight="bold", color="white",
                zorder=5, family=Charte.FONT)
        # sous-titre
        ax.text(x + 3.2, y + strate_h - 2.3,
                strate["sous_titre"],
                ha="left", va="center",
                fontsize=9.5, color="white", alpha=0.9,
                zorder=5, family=Charte.FONT, style="italic")
        # compteur d'items
        ax.text(x + 1.2, y + 0.9,
                f"{len(strate['items'])} elements",
                ha="left", va="center",
                fontsize=9, color="white", alpha=0.85,
                zorder=5, family=Charte.FONT)

        # items dans la zone droite, grille
        zone_iy0 = y + 0.5
        zone_iy1 = y + strate_h - 0.5
        items = strate["items"]
        ncols = 5
        nrows = (len(items) + ncols - 1) // ncols
        cell_w = (items_x1 - items_x0) / ncols
        cell_h = (zone_iy1 - zone_iy0) / nrows
        for i, item in enumerate(items):
            r = i // ncols
            c = i % ncols
            cx = items_x0 + c * cell_w + cell_w / 2
            cy = zone_iy1 - r * cell_h - cell_h / 2
            # pilule
            bw = cell_w * 0.92
            bh = cell_h * 0.78
            ax.add_patch(patches.FancyBboxPatch(
                (cx - bw / 2, cy - bh / 2), bw, bh,
                boxstyle="round,pad=0.02,rounding_size=0.25",
                linewidth=0.7, edgecolor=strate["color"],
                facecolor=strate["soft"], zorder=4))
            ax.text(cx, cy, item,
                    ha="center", va="center",
                    fontsize=8.8, color=Charte.INK,
                    family=Charte.FONT, zorder=5)

    add_footer(ax, page_label="Fiche 05 - Architecture SI (4 strates)",
               width=W, height=H)

    out = OUT / "05-Strates-SI.png"
    save(fig, out)
    return out


if __name__ == "__main__":
    p = render()
    print(f"OK PNG : {p}")
