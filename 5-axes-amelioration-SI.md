# 5 axes d'amélioration du SI Torpier

> **Usage** : données de base communes au plan **COLLECTIF** (D7 — points forts/faibles SI → 5 axes) et au plan **INDIVIDUEL** (D6 — 5 axes + 1 indicateur de valeur par axe ; D7 — focus sur 1 axe).
> Chaque axe est rattaché à un **point faible constaté** dans l'état des lieux et à un **axe de la stratégie 2026-2029** (diversification clients · développement durable · industrie 4.0 · optimisation du SI).

| # | Axe (catégorie) | Point faible constaté | Lien stratégie | Indicateur de valeur |
|---|-----------------|-----------------------|----------------|----------------------|
| 1 | **Applicatif** — urbanisation & intégration | Silos applicatifs : échange GesProd ↔ Dynamics par **fichiers CSV**, Power BI alimenté par des **fichiers Excel**, e-commerce PrestaShop (OVH) non relié au SI interne | Optimisation du SI · Diversification clients (e-commerce) | % de flux inter-applications automatisés (vs CSV/Excel manuels) ; délai de propagation d'une commande e-commerce → production |
| 2 | **Réseau** — segmentation & interconnexion multi-sites | VLAN 50 **commun production + conception** (segmentation insuffisante) ; interconnexion VPN IPSec site-à-site sans SD-WAN ; bureaux Europe (DE/IT/ES) mal intégrés ; pas de réseau OT pour l'IoT | Optimisation du SI (interconnexion, résilience) · Industrie 4.0 (IoT) | Disponibilité du lien inter-sites (%) ; latence/QoS sur les flux critiques ; nb de segments OT/IoT isolés |
| 3 | **Stockage & données** — gouvernance et valorisation | Données dispersées (« spécialistes Excel »), pas de **référentiel unique** ni d'entrepôt de données, BI non fiabilisée, pas d'outil de traçabilité matières | Développement durable (**traçabilité** des matières premières) · Optimisation du SI | % de décisions appuyées sur une donnée unique/fiable ; taux de traçabilité des lots de bois ; délai de production d'un reporting |
| 4 | **Hébergement** — trajectoire cloud hybride & résilience | Quasi-tout **on-premise à Nanterre** (serveurs applicatifs, BDD, AD) → site unique = résilience faible ; Exchange en migration ; PRA à consolider | Optimisation du SI (**résilience et agilité**) | RTO/RPO (objectifs de reprise) ; taux de services en haute dispo ; coût/élasticité des ressources |
| 5 | **Accès & sécurité** — IAM, mobilité & conformité | Gestion des identités/accès à renforcer (pas de SSO/MFA mentionné) ; télétravail + mobilité commerciale via RDS ; expansion européenne = **RGPD multi-pays** | Optimisation du SI (agilité, sécurité) · Diversification (mobilité commerciale) | Taux de comptes sous MFA/SSO ; nb d'incidents d'accès ; conformité RGPD des sites européens |

## Notes de cohérence
- Les **mêmes 5 axes** servent au collectif et à l'individuel (garde-fou des deux plans).
- Pour l'individuel, l'axe avec le plus fort **effet de levier sur l'adhésion direction** est le n°4 (hébergement / résilience cloud hybride) ou le n°1 (intégration applicative) : tous deux servent directement « l'optimisation du SI » revendiquée par la DG et débloquent les autres axes.
- Chaque proposition s'argumente via les bonnes pratiques et un référentiel (ITIL pour l'exploitation/résilience, COBIT pour la gouvernance de la donnée, Scrum/Agile pour les développements applicatifs).
