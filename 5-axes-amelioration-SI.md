# 5 axes d'amélioration du SI Torpier

> **Usage** : données de base communes au plan **COLLECTIF** (D7) et au plan **INDIVIDUEL** (D6/D7/D8).
> **Formulation par aspect technique** pour coller au libellé exact des grilles :
> - *Individuel (2 pts)* : « Au moins 5 axes d'amélioration possibles **des flux du SI** sont identifiés sur les aspects **applicatifs, réseau, stockage, hébergement, accès utilisateurs, etc.** Ils répondent aux enjeux de l'entreprise. »
> - *Collectif (1 pt)* : « 5 axes d'amélioration SI sont proposés. Ils sont cohérents avec le contexte. »
> Stratégie 2026-2029 : diversification clients · développement durable · industrie 4.0 · optimisation du SI.

## Hiérarchie (macro → micro)
- **5 axes** (D6) = niveau **macro**, un par aspect technique → tous présentés.
- **1 axe choisi** (D7) = **Applicatif** → décomposé en **5 projets opérationnels** (D8, niveau **micro**).
- Les 5 projets ne sont **pas** « 1 par axe » : ce sont les 5 déclinaisons du **seul** axe focus.
- **Mêmes 5 axes** au collectif et à l'individuel (garde-fou des deux plans).

---

## A. Les 5 axes (par aspect technique)

| # | Axe (aspect) | Enjeu / points faibles Torpier | Enjeu stratégique servi | Indicateur de valeur |
|---|--------------|--------------------------------|-------------------------|----------------------|
| 1 | **Applicatif** | Silos : échanges **CSV** GesProd↔Dynamics, Power BI alimenté par **Excel**, e-commerce PrestaShop (OVH) non relié au SI | Optimisation SI · Diversification (e-commerce) | % de flux inter-applications automatisés ; délai de traitement d'une commande de bout en bout |
| 2 | **Réseau** | VLAN 50 **production + conception confondus**, VPN IPSec multi-sites sans SD-WAN, bureaux Europe (DE/IT/ES) mal intégrés, pas de réseau OT pour l'IoT | Optimisation SI · Industrie 4.0 | Disponibilité du lien inter-sites (%) ; latence / QoS des flux critiques |
| 3 | **Stockage & données** | Données éparpillées (« spécialistes Excel »), pas de référentiel unique, traçabilité matières absente, sauvegardes Veeam à fiabiliser | Développement durable (traçabilité) · Optimisation SI | RPO ; taux de traçabilité des lots de bois ; % de données fiabilisées |
| 4 | **Hébergement** | Quasi-tout **on-premise à Nanterre** (site unique), Exchange en migration, résilience faible, élasticité nulle | Optimisation SI (résilience & agilité) | RTO / RPO ; % de services en haute disponibilité |
| 5 | **Accès utilisateurs** | IAM à consolider (pas de SSO/MFA), télétravail + mobilité commerciale via RDS, **RGPD multi-pays** (expansion UE) | Optimisation SI · Diversification (mobilité) | Taux de comptes sous MFA ; nb d'incidents d'accès ; conformité RGPD des sites |

---

## B. Focus individuel : axe **Applicatif** (justification — D7)

L'axe applicatif est le **socle** de l'« optimisation du SI » et de la « diversification clients » (e-commerce). Casser les silos applicatifs **débloque les autres axes** : donnée fiable pour la BI (axe stockage), traçabilité des matières (développement durable), interconnexion des sites (axe réseau). Le ROI est **immédiatement lisible par la direction** (fin des ressaisies CSV/Excel, données fiables pour décider, commandes traitées de bout en bout) → c'est le plus fort **levier d'adhésion** de la DG.

---

## C. 5 projets opérationnels de l'axe Applicatif (D8)

> Chaque projet : **titre explicite · périmètre · objectifs · référentiel de gouvernance + processus/méthode préconisé**.

### Projet 1 — Plateforme d'intégration & API Management
- **Périmètre** : remplacer les échanges de fichiers (CSV GesProd↔Dynamics, sources Excel) par un bus d'intégration / API ; connecteurs Dynamics, GesProd, SAGE, Qualéval.
- **Objectifs** : flux temps réel, fin des ressaisies, fiabilité des données partagées.
- **Référentiel & méthode** : **TOGAF** (urbanisation — méthode **ADM**) pour le cadrage d'architecture + **Scrum** (sprints, incréments) pour la réalisation.

### Projet 2 — Intégration e-commerce ↔ SI
- **Périmètre** : synchroniser commandes, stocks et livraison entre PrestaShop (OVH), Microsoft Dynamics et GesProd.
- **Objectifs** : parcours commande de bout en bout, support de la diversification vers les clients privés.
- **Référentiel & méthode** : **Scrum / Agile** (backlog produit, sprints, revues de sprint).

### Projet 3 — Entrepôt de données & fiabilisation décisionnelle (BI)
- **Périmètre** : datawarehouse alimenté par les applications (au lieu d'Excel), refonte des tableaux de bord Power BI.
- **Objectifs** : donnée unique et fiable pour le pilotage de la DG ; socle de la traçabilité des matières (développement durable).
- **Référentiel & méthode** : **COBIT** (gouvernance et qualité de la donnée — domaine **APO**, « gérer les données »).

### Projet 4 — Urbanisation & cartographie applicative
- **Périmètre** : référentiel d'architecture, cartographie des applications et des flux, comité d'architecture, rationalisation du parc applicatif.
- **Objectifs** : cohérence globale du SI (feuille de route du DSI), maîtrise de la dette technique.
- **Référentiel & méthode** : **TOGAF / COBIT** (gouvernance d'architecture, processus de revue d'architecture).

### Projet 5 — Industrialisation du cycle de vie des applications internes (DevOps)
- **Périmètre** : GesProd, Qualéval, DocuFlow — CI/CD sur l'instance **GitLab** existante, tests automatisés, mises en production maîtrisées.
- **Objectifs** : qualité logicielle, réduction des incidents post-déploiement, capacité à absorber la charge (renforts freelances).
- **Référentiel & méthode** : **ITIL** (gestion des **mises en production et déploiements** + gestion des **changements**) couplé à une démarche **DevOps**.

---

## D. Notes de cohérence
- **Mêmes 5 axes** au collectif (D7) et à l'individuel (D6).
- **1 indicateur de valeur** par axe (exigé en D6 individuel) — colonne dédiée du tableau A.
- Tout l'aval individuel (équipes, externes, conduite du changement) porte sur l'axe **Applicatif**.
- Argumentation par référentiel : **ITIL** (exploitation / services), **COBIT** (gouvernance / donnée), **Scrum / TOGAF** (développements / urbanisation).
