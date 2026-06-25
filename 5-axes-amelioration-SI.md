# 5 axes d'amélioration du SI Torpier

> **Usage** : données de base communes au plan **COLLECTIF** (D7 — points forts/faibles SI → 5 axes) et au plan **INDIVIDUEL** (D6 — 5 axes + 1 indicateur de valeur par axe ; D7 — focus sur 1 axe ; D8 — 5 projets opérationnels de l'axe).
> Les axes sont **globaux** (thèmes de transformation) : chacun se décline ensuite en projets opérationnels.
> Chaque axe est rattaché à des **points faibles constatés** dans l'état des lieux et à la **stratégie 2026-2029** (diversification clients · développement durable · industrie 4.0 · optimisation du SI).

## Vue d'ensemble

| # | Axe global | Enjeu / points faibles Torpier | Stratégie servie | Référentiel pivot | Indicateur de valeur |
|---|-----------|--------------------------------|------------------|-------------------|----------------------|
| 1 | **Uniformiser & urbaniser le SI** | Silos applicatifs (échanges **CSV** GesProd↔Dynamics, BI sur **Excel**), e-commerce OVH non relié, pratiques FR/Finlande/bureaux Europe hétérogènes | Optimisation SI · Diversification (e-commerce) | COBIT / urbanisation (TOGAF) | % de flux inter-applications automatisés (vs CSV/Excel) |
| 2 | **Migrer vers un cloud hybride (Move to Cloud)** | Quasi-tout **on-premise à Nanterre** (site unique), Exchange en migration, résilience faible, élasticité nulle | Optimisation SI (**résilience & agilité**) | ITIL + gouvernance cloud | RTO/RPO ; % de services en haute dispo |
| 3 | **Définir un référentiel unique de gouvernance** | Pilotage des projets SI **« en construction »**, PMO naissant, pas de cadre commun de décision/données | Optimisation SI · Développement durable (traçabilité) | COBIT (gouvernance) + PMO | % de projets cadrés/suivis dans le référentiel |
| 4 | **Industrialiser la gestion des services & incidents IT** | Support utilisateur et maintenance peu outillés au-delà de Jira, pas de SLA/supervision formalisés | Optimisation SI (qualité de service) | ITIL (gestion des services) | délai moyen de résolution (MTTR) ; taux de respect des SLA |
| 5 | **Renforcer la sécurité & la conformité** | IAM à consolider (pas de SSO/MFA), télétravail/mobilité via RDS, **RGPD multi-pays** (expansion UE), PRA à fiabiliser | Optimisation SI · Diversification (mobilité) | ISO 27001 / RGPD / Zero Trust | taux de comptes sous MFA ; nb d'incidents de sécurité ; conformité RGPD des sites |

## Déclinaison en projets (pistes — à formaliser en D8)

**Axe 1 — Uniformiser & urbaniser le SI**
- Mettre en place un bus d'intégration / API (remplacer les échanges CSV par des flux temps réel)
- Relier l'e-commerce PrestaShop au SI interne (commandes → GesProd → production)
- Construire un entrepôt de données + référentiel unique pour fiabiliser Power BI
- Harmoniser les applications et pratiques entre usines FR et Finlande
- Intégrer les bureaux européens (DE/IT/ES) au SI

**Axe 2 — Move to Cloud (hybride)**
- Finaliser la migration messagerie vers une solution unifiée (M365)
- Plan de migration sélectif vers Azure (apps éligibles)
- Architecture hybride + PRA cloud (sortir du site unique Nanterre)
- Modernisation des accès distants (remplacer/sécuriser le RDS)
- FinOps : pilotage des coûts et de l'élasticité

**Axe 3 — Référentiel unique de gouvernance**
- Industrialiser le processus de pilotage des projets SI (cadrage, portefeuille)
- Outiller et étendre le PMO (uniformiser les pratiques projet)
- Gouvernance de la donnée (qualité, propriété, traçabilité matières — DD)
- Cartographie SI maintenue + comité d'architecture
- Tableau de bord de pilotage SI pour la direction

**Axe 4 — Gestion des services & incidents**
- Déployer pleinement ITIL sur Jira Service Management (catalogue, SLA)
- Mettre en place une supervision / monitoring de l'infra et des apps
- Base de connaissances + self-service utilisateurs
- Processus de gestion des changements et des problèmes
- Maintenance prédictive (lien industrie 4.0 / IoT)

**Axe 5 — Sécurité & conformité**
- Mise en place d'un IAM avec SSO + MFA
- Démarche Zero Trust / segmentation (dont réseau OT pour l'IoT)
- Mise en conformité RGPD multi-pays (sites européens)
- Fiabilisation du PRA et tests de reprise
- Sécurisation du télétravail et de la mobilité commerciale

## Notes de cohérence
- **Mêmes 5 axes** pour le collectif (D7) et l'individuel (D6) → garde-fou des deux plans.
- Un **indicateur de valeur** par axe (requis en D6 individuel) figure dans le tableau.
- Pour le **focus individuel (D7)**, l'axe au plus fort effet de levier sur l'adhésion direction est le **n°2 (Move to Cloud)** ou le **n°1 (uniformiser le SI)** : ils portent directement « l'optimisation du SI » revendiquée par la DG et conditionnent les autres axes.
- Chaque projet s'argumente via un référentiel (ITIL exploitation/services · COBIT gouvernance · Scrum/Agile développements).
