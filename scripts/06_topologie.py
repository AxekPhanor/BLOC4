"""Produit la topologie reseau multi-sites Torpier.

Sortie : 06-Topologie-Reseau.png
Sites : Nanterre (siege + DSI) / Arras (usine FR) / Finlande / Bureaux EU (DE, IT, ES)
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUT = Path('/home/user/BLOC4/Livrables/00-Base-Commune')

fig, ax = plt.subplots(figsize=(22, 14))
ax.set_xlim(0, 22)
ax.set_ylim(0, 14)
ax.axis("off")

ax.text(11, 13.4, "Topologie reseau - Groupe Torpier",
        ha="center", fontsize=24, fontweight="bold", color="#1B3A5B")
ax.text(11, 12.9, "Interconnexion multi-sites via VPN IPSec (Fortinet)",
        ha="center", fontsize=12, color="#555", style="italic")

# --- Internet / cloud tiers (haut) ---
def cloud(x, y, w, h, label, bg="#E3F2FD", edge="#1565C0"):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h,
                                         boxstyle="round,pad=0.15",
                                         linewidth=1.5, edgecolor=edge,
                                         facecolor=bg))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="#1B3A5B")

cloud(0.5, 11.2, 3.5, 1.0, "Cloud Azure\n(Microsoft Dynamics)")
cloud(4.5, 11.2, 3.5, 1.0, "Cloud OVH\n(PrestaShop)")
cloud(8.5, 11.2, 3.5, 1.0, "Cloud Atlassian\n(Jira Service Management)")
cloud(13.5, 11.2, 3.5, 1.0, "Microsoft 365\n(migration en cours)")
cloud(17.5, 11.2, 4.0, 1.0, "INTERNET",
      bg="#FFEBEE", edge="#C62828")

# --- Bandeau firewall Nanterre ---
ax.add_patch(patches.FancyBboxPatch((7.5, 9.2), 7.0, 1.2,
                                     boxstyle="round,pad=0.1",
                                     linewidth=2, edgecolor="#C62828",
                                     facecolor="#FFF3E0"))
ax.text(11, 9.95, "FortiGate 200E + Proxy (Nanterre)",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color="#C62828")
ax.text(11, 9.45, "Firewall / IPS / Terminaison VPN / Filtrage Internet",
        ha="center", va="center", fontsize=9.5, color="#555",
        style="italic")

# Liens internet -> firewall
for x_cloud in [2.25, 6.25, 10.25, 15.25, 19.5]:
    ax.plot([x_cloud, 11], [11.2, 10.4], color="#888", lw=1.2, linestyle=":")

# --- Site Nanterre (siege) ---
def site(x, y, w, h, title, vlans, color, subtitle=""):
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h,
                                         boxstyle="round,pad=0.1",
                                         linewidth=2, edgecolor=color,
                                         facecolor="white"))
    # bandeau titre
    ax.add_patch(patches.Rectangle((x, y + h - 0.6), w, 0.6,
                                    linewidth=0, facecolor=color))
    ax.text(x + w / 2, y + h - 0.3, title, ha="center", va="center",
            fontsize=12, fontweight="bold", color="white")
    if subtitle:
        ax.text(x + w / 2, y + h - 0.85, subtitle, ha="center", va="center",
                fontsize=9, color="#555", style="italic")
    # VLAN / composants
    nlines = len(vlans)
    yy_top = y + h - 1.2
    dy = (h - 1.4) / max(nlines, 1)
    for i, vlan in enumerate(vlans):
        yy = yy_top - i * dy - dy / 2
        ax.add_patch(patches.FancyBboxPatch((x + 0.2, yy - dy / 2 + 0.05),
                                             w - 0.4, dy - 0.1,
                                             boxstyle="round,pad=0.02",
                                             linewidth=0.7, edgecolor=color,
                                             facecolor="#F8F9FA"))
        ax.text(x + w / 2, yy, vlan, ha="center", va="center",
                fontsize=9, color="#222222")

# NANTERRE (siege + DSI)
site(6.0, 5.0, 10.0, 4.0, "NANTERRE - Siege (DG + DSI + Services)",
     [
         "VLAN 10 - Direction Generale",
         "VLAN 20 - DSI postes (GitLab, poste test)",
         "VLAN 21 - DSI serveurs (Hyper-V, SQL cluster, AD DS, DFS, Veeam, WSUS, RDS, Exchange)",
         "VLAN 30 - Administratif & RH (SAGE Compta/Paie, DocuFlow)",
         "VLAN 40 - Commercial & Marketing (Dynamics, PrestaShop admin)",
         "Switches Cisco Catalyst (coeur) + SG (acces) | Routeur Cisco ISR 4000",
     ],
     "#1B3A5B")

# ARRAS (usine FR)
site(0.5, 1.0, 6.5, 3.6, "ARRAS - Usine FR",
     [
         "VLAN 50 - Production & Conception",
         "GesProd (serveur metier)",
         "Qualeval",
         "Postes PC Windows 11 (artisans)",
         "Postes conception (Revit + MacBook ArchiCAD)",
         "Replica AD DS (secondaire)",
         "Imprimantes (3) + switches SG",
     ],
     "#2E7D32", subtitle="Conception + R&D + Fabrication structures/mobiliers")

# FINLANDE
site(8.5, 1.0, 6.5, 3.6, "FINLANDE - Usine bois",
     [
         "VLAN 60 - Usine finlandaise",
         "Acces aux applis via VPN IPSec",
         "GesProd (acces distant)",
         "Qualeval (acces distant)",
         "Postes PC Windows 11 (artisans)",
         "PAS de replica AD DS (point de vigilance)",
         "Switches SG + imprimantes (3)",
     ],
     "#EF6C00", subtitle="Fabrication - 11 artisans (Sofia Jansson)")

# BUREAUX EU (DE/IT/ES)
site(16.5, 1.0, 5.0, 3.6, "BUREAUX EU",
     [
         "Allemagne (DE) - 1 commercial + 1 gerant",
         "Italie (IT) - 1 commercial + 1 gerant",
         "Espagne (ES) - 1 commercial + 1 gerant",
         "Acces VPN client -> Nanterre",
         "Applis utilisees : Dynamics, Teams/Exchange",
         "Postes PC portables Windows 11",
     ],
     "#6A1B9A", subtitle="Bureaux commerciaux ouverts en 2023")

# --- Liens VPN IPSec ---
# Nanterre <-> Arras
ax.annotate("", xy=(6.0, 3.9), xytext=(8.0, 5.0),
            arrowprops=dict(arrowstyle="<->", lw=2.2, color="#1565C0"))
ax.text(5.8, 4.85, "VPN IPSec\nSite-to-Site", ha="center", va="center",
        fontsize=9, color="#1565C0", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#1565C0"))

# Nanterre <-> Finlande (lien vertical simple puisque directement en-dessous)
ax.annotate("", xy=(11, 4.3), xytext=(11, 5.0),
            arrowprops=dict(arrowstyle="<->", lw=2.2, color="#1565C0"))
ax.text(12.8, 4.7, "VPN IPSec\nSite-to-Site", ha="center", va="center",
        fontsize=9, color="#1565C0", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#1565C0"))

# Nanterre <-> Bureaux EU
ax.annotate("", xy=(17.0, 3.9), xytext=(15.0, 5.0),
            arrowprops=dict(arrowstyle="<->", lw=2.2, color="#6A1B9A"))
ax.text(16.9, 4.85, "VPN client\n(Fortinet)", ha="center", va="center",
        fontsize=9, color="#6A1B9A", fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#6A1B9A"))

# Lien Nanterre -> firewall
ax.plot([11, 11], [9.2, 9.0], color="#C62828", lw=2)

# Legende
ax.text(0.5, 0.45, "Legende :", fontsize=10, fontweight="bold", color="#222")
ax.plot([2.2, 3.5], [0.5, 0.5], color="#1565C0", lw=2.2)
ax.text(3.7, 0.5, "VPN IPSec Site-to-Site (Fortinet)", fontsize=9, va="center",
        color="#222")
ax.plot([9.6, 10.8], [0.5, 0.5], color="#6A1B9A", lw=2.2)
ax.text(11.0, 0.5, "VPN client (teletravail / bureaux EU)", fontsize=9,
        va="center", color="#222")
ax.plot([16.3, 17.5], [0.5, 0.5], color="#888", lw=1.2, linestyle=":")
ax.text(17.7, 0.5, "Liens Internet / cloud tiers", fontsize=9, va="center",
        color="#222")

png_path = OUT / "06-Topologie-Reseau.png"
plt.tight_layout()
plt.savefig(png_path, dpi=200, bbox_inches="tight", facecolor="white")
plt.close()
print(f"OK PNG : {png_path}")
