# BLOC 4 — « Manager les équipes et la transformation du SI » (cas Torpier)
# Plan des 2 présentations — Individuelle & Collective

> **Objectif : viser la note maximale (A = 16-20).** Ce document construit les deux trames
> **critère par critère** sur les grilles d'évaluation officielles, en gardant une **cohérence totale**
> entre les deux soutenances.
>
> **Décisions retenues :** axe focus individuel = **Optimisation du SI** · référentiel retenu = **ITIL** ·
> comparaison des 3 référentiels (collectif) = **ITIL vs COBIT vs Scrum/Agile** · méthode de conduite du
> changement = **ADKAR** ou **Kotter** (à arbitrer) · format = présentation orale 20 min + 15 min Q/R.

---

## 1. Rappel des barèmes (là où sont les points)

### Présentation INDIVIDUELLE — /20 (A ≥ 16)

| Thème | Critère | Pts |
|---|---|---|
| Modéliser | Présentation entreprise + activité **exhaustive/claire**, intègre **processus + workflows des flux d'info** | **3** |
| Modéliser | **SI existant clair et représenté GRAPHIQUEMENT** (topologies réseau, systèmes, données, applications) | **4** |
| Modéliser | **≥ 5 axes d'amélioration des FLUX du SI** (applicatif, réseau, stockage, hébergement, accès users) | **2** |
| Encadrer | Responsabilités/affectations équipe projet claires + cohérentes tâches & **compétences individuelles** | **1** |
| Encadrer | **Organigramme équipe projet** + affectation pertinente + **type de management adapté** + **outils de suivi** | **3** |
| Encadrer | Fournisseurs/sous-traitants identifiés + **plan de communication** (outils collaboratifs accessibles) | **2** |
| Changement | **Méthode + leviers** de motivation/engagement cohérents, **arguments convaincants** | **2** |
| Changement | **Acteurs clés listés** + moyens de communication adaptés aux parties prenantes | **1** |
| Qualité | Oral fluide/dynamique, prend en compte l'auditoire, vocabulaire précis, structuré | **1** |
| Qualité | Support pro, **schémas/tableaux lisibles et commentés** | **1** |
| | **TOTAL** | **20** |

### Présentation COLLECTIVE — Collective /20 + Individuelle /12

**Collective (/20) :** SWOT **1** · processus métiers + tâches + acteurs **2** · applis ↔ fonctions
métiers **2** · infra technique ↔ applis supportées **2** · 5 axes d'amélioration SI **1** ·
**comparaison des 3 référentiels montrant l'intérêt de CHACUN pour Torpier 2** · organisation des
équipes (hiérarchique + transversal) **2** · **matrice des responsabilités (RACI) parties prenantes 2** ·
outils de suivi projets **1** · outils de pilotage du changement **1** · **pitch d'adhésion direction 2** ·
présentation du groupe + **bilan points forts / axes d'amélioration du groupe 1** · oral fluide +
support pro IT **1**.

**Individuelle (/12, dans le projet collectif) :** participation individuelle & efficacité **2** ·
**maîtrise des outils 3** · **RÉACTION FACE À UN IMPRÉVU 4** · animation / prise en compte de
l'auditoire **2** · **réponses aux questions argumentées 1**.

> **3 conséquences majeures pour la note :**
> 1. Soigner **+++** les **schémas** : le SI graphique = **4 pts** en individuel ; les 3 tableaux de
>    cartographie = **6 pts** en collectif. → des visuels, pas du texte.
> 2. En collectif, la note individuelle se joue surtout sur **« réaction face à un imprévu » (4/12)** et
>    la **maîtrise des outils (3/12)** → **répéter le Q/R de 15 min** et que chacun maîtrise Jira/Power BI/ITIL/RACI.
> 3. Ne pas oublier le **bilan réflexif du groupe** (points forts / axes d'amélioration).

---

## 2. Socle commun (réutilisé dans les 2 présentations)

**Stratégie Torpier 2026-2029 (4 axes) :** diversification clients privés/promoteurs · développement
durable (traçabilité bois) · industrie 4.0 / IoT · **optimisation du SI** (interconnexion, résilience, agilité).

**Faiblesses du SI (matière des axes d'amélioration) :** silos applicatifs (GesProd ↔ Dynamics par
fichiers **CSV**) · Exchange en migration · processus de pilotage des projets SI « en construction » ·
hétérogénéité FR / Finlande · interconnexion VPN à fiabiliser · support outillé (Jira) mais **sans cadre
ITIL** · accès distants (RDS) à sécuriser.

### Les 5 axes d'amélioration du SI — LISTE UNIQUE, partagée par les 2 présentations

> Le collectif les **identifie tous les 5** ; l'individuel les **reprend à l'identique** puis **zoome
> sur les axes 1 & 2** (= l'axe stratégique « Optimisation du SI »).

| # | Axe | Contenu | Indicateur de valeur |
|---|---|---|---|
| 1 | **Applicatif / urbanisation** | Casser les silos (GesProd↔Dynamics en CSV) via API/ESB, urbaniser le SI | Nb d'interfaces manuelles supprimées |
| 2 | **Réseau / interconnexion & résilience** | Fiabiliser/sécuriser l'interconnexion multi-sites (VPN, QoS), PRA | Taux de disponibilité inter-sites |
| 3 | **Stockage / données & BI** | Consolidation & qualité des données, sauvegarde/PRA, décisionnel (Power BI) | RTO / RPO |
| 4 | **Hébergement / cloud hybride** | Exchange → M365, scalabilité e-commerce (PrestaShop/OVH) | Coût/perf, élasticité |
| 5 | **Accès utilisateurs / sécurité** | IAM, RGPD, sécurisation des accès distants (RDS, MFA) | Nb d'incidents de sécurité |

→ **Axe focus individuel = « Optimisation du SI »**, incarné concrètement par les **axes 1 & 2**
(urbanisation + interconnexion/résilience), qui appellent naturellement **ITIL** (gestion des
changements / incidents / niveaux de service pour fiabiliser le *run* multi-sites).

### Comparaison des 3 référentiels (montrer l'intérêt de CHACUN pour Torpier)

| Référentiel | Rôle | Intérêt pour Torpier | Limite | 
|---|---|---|---|
| **ITIL** *(retenu)* | Gestion des **services / run** (incident, problème, changement, niveaux de service) | Fiabilise le support & l'exploitation multi-sites, cadre le run aujourd'hui informel (Jira sans process) | Peu orienté gouvernance stratégique / projets |
| **COBIT** | **Gouvernance** SI (alignement SI/stratégie, KPIs, risques, RGPD) | Chapeau directionnel, conformité RGPD | Lourd pour une PME, peu opérationnel au quotidien |
| **Scrum / Agile** | **Build** : projets de dev itératifs | Adapté aux dev internes (PrestaShop, GesProd) ; porté par Tiffany (Scrum Master) & cellule PMO | Ne couvre ni le run ni la gouvernance |

**Conclusion :** **ITIL pour le run** + **Scrum/Agile pour le build** des projets, **COBIT en chapeau**
gouvernance/alignement. → choix **ITIL** comme fil conducteur, repris tel quel dans l'individuel.

### Modèles du cours CESI « Posture du Manager » à mobiliser

Style de management **participatif / collaboratif** (équipe DSI experte et autonome) avec touches
**directives** sur la sécurité/conformité (cohérent ITIL) · **Mintzberg / Laloux** (organisation « orange »
→ plus participative) · **autorité** statutaire/auteur/capacité · objectifs **SMART** + **cascade des
objectifs** + **Hoshin Kanri** · **RACI** · **First 100 Days (Gartner)** · conduite du changement =
**leviers de motivation + Mission-Vision-Valeurs + exemplarité du manager + plan de communication**,
méthode structurante **ADKAR** ou **8 étapes de Kotter**.

---

## 3. Présentation COLLECTIVE — étude préliminaire / ébauche de schéma directeur (20 min)

| # | Partie | Contenu (→ critère noté / points) | ~min |
|---|--------|-----------------------------------|------|
| 0 | Ouverture | Contexte Torpier + objectif de l'étude + **organisation du groupe** (qui fait quoi) → *présentation groupe (1)* | 1,5 |
| 1 | SWOT | Forces / faiblesses / menaces / opportunités nettement distingués → *SWOT (1)* | 2 |
| 2 | Processus métiers SI | Liste des processus + **tâches principales + acteurs** (visuel BPMN/schéma) → *processus (2)* | 2,5 |
| 3 | Tableau applicatif | Applis recensées **↔ fonctions métiers** (Dynamics, GesProd, SAGE, Qualéval, PrestaShop, Jira, Power BI, DocuFlow…) → *applis (2)* | 2 |
| 4 | Tableau infra technique | Serveurs / réseau **↔ applications supportées** (Hyper-V, SQL AlwaysOn, AD, VPN Fortinet, VLAN) → *infra (2)* | 2 |
| 5 | 5 axes d'amélioration SI | **La liste UNIQUE des 5 axes** (§2) → *5 axes (1)* | 1,5 |
| 6 | **Comparaison 3 référentiels** | **ITIL vs COBIT vs Scrum/Agile** : tableau avantages/limites + **intérêt de CHACUN** pour Torpier, puis **choix ITIL** (repris dans l'individuel) → *comparaison (2)* | 2,5 |
| 7 | Organisation des équipes SI | Schéma **hiérarchique + transversal** (run/build, PMO) + style de management → *organisation (2)* | 1,5 |
| 8 | **Matrice RACI** + outils | RACI des parties prenantes clés + **outils de suivi projets** (Jira, MS Project, Power BI) et **de pilotage du changement** (Teams, enquêtes, indicateurs d'adhésion) → *RACI (2) + outils suivi (1) + outils changement (1)* | 1,5 |
| 9 | **Pitch conduite du changement** | Argumentaire percutant « adopter une politique de conduite du changement » → *pitch adhésion (2)* | 1,5 |
| 10 | Rôles des membres + **bilan groupe** | Rôle de chacun + **bilan : points forts & axes d'amélioration du groupe** + conclusion → *présentation groupe (1)* | 1,5 |

**Note individuelle /12 (transverse, à préparer en amont) :** chaque membre **participe activement**,
**maîtrise les outils présentés** (Jira / Power BI / RACI / ITIL), **anime** et **répond aux questions de
façon argumentée**. Surtout : **s'entraîner à l'imprévu (4 pts)** = simuler les questions pièges du jury.

---

## 4. Présentation INDIVIDUELLE — trajectoire du SI, focus « Optimisation du SI » (20 min)

| # | Partie | Contenu (→ critère noté / points) | ~min |
|---|--------|-----------------------------------|------|
| 0 | Accroche direction | Posture de nouveau responsable SI + promesse : aligner SI ↔ stratégie / créer de la valeur (le **POURQUOI**) | 1 |
| 1 | Entreprise, activité & **processus/workflows** | Présentation **exhaustive et claire** : activité, organisation, **processus + workflows des flux d'information** + stratégie 2026-2029 → *entreprise + processus (3)* | 3 |
| 2 | **SI existant — schémas graphiques** | **4 strates + topologie réseau** (systèmes, données, applications, VLAN, VPN, serveurs) — pièce maîtresse visuelle → *SI graphique (4)* | 3,5 |
| 3 | **≥ 5 axes d'amélioration des flux du SI** | **La même liste UNIQUE des 5 axes** (§2) + **indicateur de valeur** pour chacun → *5 axes (2)* | 2,5 |
| 4 | **Focus axe : Optimisation du SI** | Zoom sur **axes 1 & 2** (urbanisation + interconnexion/résilience) ; justifie résilience/agilité + fiabilisation du run via **ITIL** (choix issu de la comparaison du collectif) + bénéfices direction | 1,5 |
| 5 | 5 projets opérationnels | Titre / périmètre / objectifs **rattachés à l'axe focus** + référentiel **ITIL** (gestion des changements / incidents / niveaux de service) ; Scrum/Agile pour les projets de dev | 2,5 |
| 6 | Équipe projet + **organigramme** + management | Rôles/responsabilités **cohérents avec compétences & aspirations** (Aurélie infra/sécu, Laurent applicatif, Tiffany PMO agile…) + **organigramme équipe projet** + **type de management adapté** (ITIL → participatif / directif sécu) + **outils de suivi** → *responsabilités (1) + organigramme/management/outils (3)* | 2,5 |
| 7 | Externes & **plan de communication** | Justifier les besoins externes (freelances dev, intégrateurs) + **plan de communication prestataires** (actions, ressources, canaux, indicateurs) avec **outils collaboratifs accessibles** → *fournisseurs + plan com (2)* | 1,5 |
| 8 | Outil(s) collaboratif(s) | Choix argumenté : relation externes + pilotage interne par KPI (Teams + Jira + Power BI) | 1 |
| 9 | Conduite du changement | **Leviers d'engagement + méthode (ADKAR/Kotter) + 1-2 arguments d'adhésion convaincants** + **acteurs clés listés** + moyens de communication par partie prenante → *méthode/leviers (2) + acteurs (1)* | 1,5 |

**Qualité (2 pts, transverse) :** support pro, **schémas/tableaux lisibles et COMMENTÉS** ; oral fluide,
structuré, vocabulaire précis, orienté **POURQUOI** (adhésion direction). Préparer le **Q/R de 15 min**.

---

## 5. Cohérence COLLECTIF ↔ INDIVIDUEL (fil narratif unique)

Le jury doit percevoir que l'individuel **prolonge** le collectif (même cas, même base, montée en altitude).
On garde **identiques** dans les 2 présentations :

| Élément | Collectif | Individuel | Invariant à respecter |
|---|---|---|---|
| Données Torpier | SWOT + cartographies | Schémas SI | Mêmes chiffres, applis, serveurs, VLAN, personas |
| Cartographie | 3 tableaux (processus / applis / infra) | 4 strates + topologie | Même contenu, mise en forme différente |
| **5 axes d'amélioration** | les 5 listés | les 5 repris **à l'identique** | **Liste UNIQUE (§2)** — aucune divergence |
| **Référentiel** | compare ITIL/COBIT/Scrum → **choisit ITIL** | **applique ITIL** aux 5 projets | Le choix individuel **découle** de la comparaison collective |
| Organisation / équipe | organisation SI + **RACI** | **organigramme équipe projet** + management | Mêmes personas/responsabilités ; l'organigramme projet est un sous-ensemble de l'organisation SI |
| Conduite du changement | pitch d'adhésion | méthode + leviers + acteurs | **Même méthode** (ITIL + ADKAR ou Kotter) et mêmes leviers |
| Outils | suivi projets + pilotage changement | outils collaboratifs / KPI | Même boîte à outils (Jira, MS Project, Power BI, Teams) |

**Différence d'altitude assumée :** collectif = *étude préliminaire / panorama du SI + choix de
gouvernance* (les 5 axes, sans focus) ; individuel = *trajectoire du SI avec focus sur 1 axe* (zoom
opérationnel : 5 projets, équipe projet, conduite du changement de l'axe « Optimisation du SI »).

---

## 6. Leviers « note max » (ce qui fait la différence A vs B)

1. **Visuels** : le SI graphique (4 pts indiv) et les 3 tableaux de cartographie (6 pts collectif)
   doivent être nets, légendés, commentés — pas du texte. Schémas : topologie réseau, BPMN, tableaux
   croisés applis ↔ fonctions ↔ infra.
2. **Exhaustivité ancrée Torpier** : citer les vrais éléments du contexte (Dynamics, GesProd/CSV,
   Fortinet, SQL AlwaysOn, VLAN 10-60, sites Nanterre/Arras/Finlande, personas Besnier/Duchamp/Vigne/
   Valentia…) → crédibilité et critère « cohérent avec le contexte ».
3. **3 référentiels** (collectif) : montrer l'intérêt **de chacun** pour Torpier (pas seulement ITIL).
4. **RACI + organigramme** lisibles, **responsabilités alignées aux compétences/aspirations** réelles
   des personas.
5. **Conduite du changement** : méthode nommée (ITIL + ADKAR/Kotter), leviers explicites, pitch percutant.
6. **Oral & Q/R** : répéter ; en collectif, **chacun maîtrise les outils** et **s'entraîne à l'imprévu**
   (4 pts/12) ; ne pas oublier le **bilan réflexif du groupe** (1 pt).
7. **Réutiliser le socle commun** entre les 2 présentations : cohérence garantie + gain de temps.

---

## 7. À arbitrer avant de construire les PPT

- Méthode de conduite du changement : **ADKAR** ou **8 étapes de Kotter**.
- Noms / rôles réels des membres du groupe collaboratif (sinon s'appuyer sur les personas DSI Torpier :
  Besnier DSI, Duchamp infra/sécu, Vigne applicatif, Valentia PMO/agile…).
