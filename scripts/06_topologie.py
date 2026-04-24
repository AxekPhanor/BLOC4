"""Topologie reseau multi-sites Torpier - version pro."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))

from charte import (Charte, setup_figure, add_header, add_footer,
                    shadow, save)
import matplotlib.patches as patches

OUT = Path('/home/user/BLOC4/Livrables/00-Base-Commune')


def site_card(ax, x, y, w, h, title, subtitle, items, color, soft,
              badge_text=None):
    """Dessine une carte de site avec bandeau colore et items."""
    # ombre
    shadow(ax, x, y, w, h)
    # fond blanc + contour
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        linewidth=0.9, edgecolor=Charte.LINE,
        facecolor="white", zorder=2))
    # bandeau colore en haut
    band_h = 2.4
    ax.add_patch(patches.Rectangle(
        (x, y + h - band_h), w, band_h,
        linewidth=0, facecolor=color, zorder=3))
    # contour arrondi global
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        linewidth=0.9, edgecolor=Charte.LINE,
        facecolor="none", zorder=5))
    # titre
    ax.text(x + 0.9, y + h - 0.9, title,
            ha="left", va="center",
            fontsize=12, fontweight="bold", color="white",
            zorder=4, family=Charte.FONT)
    # sous-titre
    if subtitle:
        ax.text(x + 0.9, y + h - 1.9, subtitle,
                ha="left", va="center",
                fontsize=8.8, color="white", alpha=0.9,
                zorder=4, family=Charte.FONT, style="italic")
    # badge (optionnel) en haut a droite
    if badge_text:
        bw, bh = 4.0, 0.9
        bx, by = x + w - bw - 0.5, y + h - band_h + 0.55
        ax.add_patch(patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.02,rounding_size=0.2",
            linewidth=0, facecolor="white", alpha=0.2, zorder=4))
        ax.text(bx + bw / 2, by + bh / 2, badge_text,
                ha="center", va="center",
                fontsize=8, color="white", fontweight="bold",
                zorder=5, family=Charte.FONT)
    # items (lignes avec puce)
    item_y_top = y + h - band_h - 0.6
    item_y_bot = y + 0.5
    n = len(items)
    line_spacing = (item_y_top - item_y_bot) / max(n, 1)
    for i, (item, is_warning) in enumerate(items):
        yy = item_y_top - i * line_spacing - line_spacing / 2
        # puce
        ax.add_patch(patches.Circle((x + 0.75, yy), 0.11,
                                    facecolor=Charte.DANGER if is_warning else color,
                                    zorder=4))
        ax.text(x + 1.2, yy, item,
                ha="left", va="center",
                fontsize=8.5,
                color=Charte.DANGER if is_warning else Charte.INK,
                fontweight="bold" if is_warning else "normal",
                family=Charte.FONT, zorder=4)


def cloud_pill(ax, x, y, w, h, label):
    """Pilule cloud tiers (style neutre)."""
    ax.add_patch(patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.45",
        linewidth=1, edgecolor=Charte.INFO,
        facecolor=Charte.INFO_SOFT, zorder=2))
    ax.text(x + w / 2, y + h / 2, label,
            ha="center", va="center",
            fontsize=9, color=Charte.PRIMARY,
            family=Charte.FONT, fontweight="bold",
            zorder=3)


def render() -> Path:
    fig, ax, W, H = setup_figure()
    add_header(
        ax,
        title="Topologie reseau - Groupe Torpier",
        subtitle="Interconnexion multi-sites via VPN IPSec (Fortinet) - sites FR, Finlande, bureaux EU",
        width=W, height=H,
        kicker="Phase 1 - Cartographie",
    )

    # ===== 1. Zone Cloud & Internet (haut) =====
    cloud_y = H - 12
    cloud_h = 1.8
    cloud_items = [
        ("Cloud Azure\n(Microsoft Dynamics)", Charte.INFO),
        ("Cloud OVH\n(PrestaShop)", Charte.INFO),
        ("Cloud Atlassian\n(Jira Service)", Charte.INFO),
        ("Microsoft 365\n(en migration)", Charte.INFO),
    ]
    internet_w = 6
    total_cloud_w = (W - 2 * Charte.MARGIN_X - internet_w - 1.5)
    cloud_w = (total_cloud_w - 3 * 0.8) / 4
    cx = Charte.MARGIN_X
    for label, _ in cloud_items:
        ax.add_patch(patches.FancyBboxPatch(
            (cx, cloud_y), cloud_w, cloud_h,
            boxstyle="round,pad=0.02,rounding_size=0.35",
            linewidth=1, edgecolor=Charte.INFO,
            facecolor=Charte.INFO_SOFT, zorder=2))
        ax.text(cx + cloud_w / 2, cloud_y + cloud_h / 2, label,
                ha="center", va="center",
                fontsize=9, color=Charte.PRIMARY,
                family=Charte.FONT, fontweight="bold",
                zorder=3)
        cx += cloud_w + 0.8
    # Internet
    ix = W - Charte.MARGIN_X - internet_w
    ax.add_patch(patches.FancyBboxPatch(
        (ix, cloud_y), internet_w, cloud_h,
        boxstyle="round,pad=0.02,rounding_size=0.35",
        linewidth=1, edgecolor=Charte.DANGER,
        facecolor=Charte.DANGER_SOFT, zorder=2))
    ax.text(ix + internet_w / 2, cloud_y + cloud_h / 2, "INTERNET",
            ha="center", va="center",
            fontsize=11, color=Charte.DANGER,
            family=Charte.FONT, fontweight="bold",
            zorder=3)

    # ===== 2. FortiGate + Proxy (dessus du siege) =====
    fg_y = cloud_y - 3.5
    fg_h = 2.2
    fg_w = 38
    fg_x = (W - fg_w) / 2
    shadow(ax, fg_x, fg_y, fg_w, fg_h)
    ax.add_patch(patches.FancyBboxPatch(
        (fg_x, fg_y), fg_w, fg_h,
        boxstyle="round,pad=0.02,rounding_size=0.4",
        linewidth=1.2, edgecolor=Charte.DANGER,
        facecolor="white", zorder=3))
    # bande rouge gauche
    ax.add_patch(patches.Rectangle(
        (fg_x, fg_y), 0.9, fg_h,
        linewidth=0, facecolor=Charte.DANGER, zorder=4))
    ax.text(fg_x + 2, fg_y + fg_h / 2 + 0.25,
            "FortiGate 200E + Proxy (Nanterre)",
            ha="left", va="center",
            fontsize=12, fontweight="bold", color=Charte.DANGER,
            zorder=5, family=Charte.FONT)
    ax.text(fg_x + 2, fg_y + fg_h / 2 - 0.55,
            "Firewall / IPS / Terminaison VPN / Filtrage Internet",
            ha="left", va="center",
            fontsize=9, color=Charte.INK_SOFT, style="italic",
            zorder=5, family=Charte.FONT)

    # Liens Internet / clouds -> Firewall
    fg_mid_x = fg_x + fg_w / 2
    for base_x in [Charte.MARGIN_X + cloud_w / 2,
                   Charte.MARGIN_X + cloud_w * 1.5 + 0.8,
                   Charte.MARGIN_X + cloud_w * 2.5 + 1.6,
                   Charte.MARGIN_X + cloud_w * 3.5 + 2.4,
                   ix + internet_w / 2]:
        ax.plot([base_x, fg_mid_x], [cloud_y, fg_y + fg_h],
                color=Charte.MUTED, lw=0.9, linestyle=":", zorder=1)

    # ===== 3. Nanterre (siege) =====
    nan_y = fg_y - 14
    nan_h = 12.5
    nan_w = 38
    nan_x = fg_x
    nanterre_items = [
        ("VLAN 10 - Direction generale", False),
        ("VLAN 20 - DSI postes (GitLab, poste test)", False),
        ("VLAN 21 - DSI serveurs (SQL, AD DS, DFS, Veeam, RDS, Exchange)", False),
        ("VLAN 30 - Administratif & RH (SAGE, DocuFlow)", False),
        ("VLAN 40 - Commercial & Marketing (Dynamics)", False),
        ("Cisco Catalyst (coeur) + SG (acces)", False),
        ("Routeurs Cisco ISR 4000", False),
    ]
    site_card(ax, nan_x, nan_y, nan_w, nan_h,
              "NANTERRE - Siege",
              "DG + DSI + Services centraux",
              nanterre_items,
              Charte.PRIMARY, Charte.BG_SOFT,
              badge_text="Site principal")
    # lien firewall -> Nanterre
    ax.plot([fg_mid_x, nan_x + nan_w / 2], [fg_y, nan_y + nan_h],
            color=Charte.DANGER, lw=2, zorder=1)

    # ===== 4. Sites distants (bas) =====
    sites_y = 4.5
    sites_h = 14.5
    site_w = (W - 2 * Charte.MARGIN_X - 2 * 1.2) / 3

    # ARRAS
    arras_items = [
        ("VLAN 50 - Production & Conception", False),
        ("GesProd (serveur metier)", False),
        ("Qualeval (qualite)", False),
        ("Replica AD DS secondaire", False),
        ("Postes Windows 11 (artisans)", False),
        ("Postes conception (Revit + MacBook ArchiCAD)", False),
        ("Switches Cisco SG + 3 imprimantes", False),
    ]
    site_card(ax, Charte.MARGIN_X, sites_y, site_w, sites_h,
              "ARRAS - Usine France",
              "Conception + R&D + Fabrication",
              arras_items,
              Charte.SUCCESS, Charte.SUCCESS_SOFT,
              badge_text="VPN IPSec")

    # FINLANDE
    fi_x = Charte.MARGIN_X + site_w + 1.2
    finlande_items = [
        ("VLAN 60 - Usine finlandaise", False),
        ("Acces applis via VPN IPSec", False),
        ("GesProd (acces distant)", False),
        ("Qualeval (acces distant)", False),
        ("Postes Windows 11 (artisans)", False),
        ("PAS de replica AD DS", True),
        ("Switches SG + 3 imprimantes", False),
    ]
    site_card(ax, fi_x, sites_y, site_w, sites_h,
              "FINLANDE - Usine bois",
              "Fabrication - 11 artisans (Sofia Jansson)",
              finlande_items,
              Charte.ACCENT, Charte.ACCENT_LIGHT,
              badge_text="VPN IPSec")

    # BUREAUX EU
    eu_x = Charte.MARGIN_X + 2 * (site_w + 1.2)
    eu_items = [
        ("Allemagne (DE) - 1 commercial + 1 gerant", False),
        ("Italie (IT) - 1 commercial + 1 gerant", False),
        ("Espagne (ES) - 1 commercial + 1 gerant", False),
        ("Acces VPN client (Fortinet) -> Nanterre", False),
        ("Applis : Dynamics, Teams, Exchange", False),
        ("Postes PC portables Windows 11", False),
    ]
    site_card(ax, eu_x, sites_y, site_w, sites_h,
              "BUREAUX EU",
              "3 bureaux commerciaux (ouverts en 2023)",
              eu_items,
              Charte.VIOLET, Charte.VIOLET_SOFT,
              badge_text="VPN client")

    # ===== 5. Liens VPN =====
    nan_mid_x = nan_x + nan_w / 2

    # Arras
    arras_top_x = Charte.MARGIN_X + site_w / 2
    ax.plot([arras_top_x, nan_mid_x - 8],
            [sites_y + sites_h, nan_y],
            color=Charte.INFO, lw=2, zorder=1)
    ax.add_patch(patches.FancyBboxPatch(
        (nan_mid_x - 16, nan_y - 1.6), 7, 1.2,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        linewidth=1, edgecolor=Charte.INFO,
        facecolor="white", zorder=3))
    ax.text(nan_mid_x - 12.5, nan_y - 1, "VPN IPSec S2S",
            ha="center", va="center",
            fontsize=8.5, color=Charte.INFO, fontweight="bold",
            zorder=4, family=Charte.FONT)

    # Finlande
    fi_top_x = fi_x + site_w / 2
    ax.plot([fi_top_x, nan_mid_x],
            [sites_y + sites_h, nan_y],
            color=Charte.INFO, lw=2, zorder=1)
    ax.add_patch(patches.FancyBboxPatch(
        (nan_mid_x - 3.5, nan_y - 1.6), 7, 1.2,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        linewidth=1, edgecolor=Charte.INFO,
        facecolor="white", zorder=3))
    ax.text(nan_mid_x, nan_y - 1, "VPN IPSec S2S",
            ha="center", va="center",
            fontsize=8.5, color=Charte.INFO, fontweight="bold",
            zorder=4, family=Charte.FONT)

    # Bureaux EU
    eu_top_x = eu_x + site_w / 2
    ax.plot([eu_top_x, nan_mid_x + 8],
            [sites_y + sites_h, nan_y],
            color=Charte.VIOLET, lw=2, zorder=1)
    ax.add_patch(patches.FancyBboxPatch(
        (nan_mid_x + 9, nan_y - 1.6), 7, 1.2,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        linewidth=1, edgecolor=Charte.VIOLET,
        facecolor="white", zorder=3))
    ax.text(nan_mid_x + 12.5, nan_y - 1, "VPN client",
            ha="center", va="center",
            fontsize=8.5, color=Charte.VIOLET, fontweight="bold",
            zorder=4, family=Charte.FONT)

    add_footer(ax, page_label="Fiche 06 - Topologie reseau",
               width=W, height=H)

    out = OUT / "06-Topologie-Reseau.png"
    save(fig, out)
    return out


if __name__ == "__main__":
    p = render()
    print(f"OK PNG : {p}")
