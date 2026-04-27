# Synthese du projet - Manager les equipes et la transformation du SI

> Document de reference pour cadrer le travail. A lire avant chaque session.

---

## 1. Le projet en 1 minute

Le module "Manager les equipes et la transformation du SI" se compose de **2 evaluations** distinctes mais articulees autour du **meme cas d'entreprise** (Groupe Torpier) :

| Volet | Posture | Format | Note |
|---|---|---|---|
| **Projet collaboratif** (3-5 membres) | Equipe DSI de Torpier | PPT + soutenance 20 min + 15 min Q/R | /20 collective + /12 individuelle |
| **Evaluation individuelle (Bloc)** | Nouveau responsable du SI | PPT + soutenance 20 min + 15 min Q/R | /20 |

**Objectif vise : A sur les deux** (>= 16/20 collectif, >= 10/12 individuel-collab, >= 16/20 individuel-bloc).

---

## 2. Contexte Torpier (resume)

### Activite et histoire
- **Groupe familial** de structures (pergolas, abris-bus) et mobiliers (tables, bars exterieurs) **en bois** pour espaces publics et prives.
- Origine : 1862 (charpenterie Dordogne). Forme actuelle pilotee par **Sophie Crelin** (DG fondatrice) et **Luc Ciel-Marchand** (DAF).
- 2020-2022 : crise des matieres premieres -> virage **e-commerce** (PrestaShop + bots SAV).
- 2023-2025 : **+30 % de CA**, expansion europeenne, digitalisation acceleree, hausse du teletravail.

### Implantations
| Site | Role |
|---|---|
| Nanterre (siege) | DG, DSI, Marketing/Commercial, Admin/Compta/RH, SAV |
| Arras (usine FR) | Conception + R&D, fabrication structures et mobiliers |
| Finlande (usine) | Fabrication, 11 artisans (Sofia Jansson) |
| Bureaux EU | Allemagne, Italie, Espagne (ouverts en 2023) |

### Strategie 2026-2029 (4 axes)
1. **Diversification clients** -> B2B prive (promoteurs immobiliers)
2. **Developpement durable** -> tracabilite bois, certification fournisseurs
3. **Industrie 4.0** -> IoT, automatisation, maintenance predictive
4. **Optimisation du SI** -> interconnexion, resilience, agilite (= **axe focus** de l'eval indiv)

### SI existant en 1 coup d'oeil
- **11 applications** : Microsoft Dynamics (CRM), GesProd (production), SAGE Compta/Paie, Qualeval, MS Project, Power BI, PrestaShop, DocuFlow, Jira Service Management, ArchiCAD/Revit + Exchange (en migration).
- **Infra** : Windows Server 2019/2022 sous Hyper-V, cluster SQL AlwaysOn, AD DS (Nanterre + replica Arras, **pas Finlande**), Veeam, FortiGate 200E, VPN IPSec Fortinet.
- **Reseau** : 6 VLANs, interconnexion Nanterre <-> Arras <-> Finlande via VPN IPSec.
- **DSI** : 5 permanents (Ludovic Besnier DSI, Aurelie Duchamp Infra/Securite, Tiffany Valentia PMO PMP+Scrum Master, Laurent Vigne Applicatif) + 4 techniciens/devs + freelances.

### Points faibles cles (leviers de transformation)
- **Aucun PRA / PCA** documente (incendie -> 150 KEUR de perte)
- Echanges **CSV** fragiles entre GesProd et Dynamics
- **Workflow Excel** pour les commandes production
- **Pas de replica AD DS** sur l'usine finlandaise
- Migration Exchange non finalisee
- Processus ITIL immatures (problemes, changements, connaissance)
- Absence de MFA / SSO face au teletravail
- Processus de pilotage des projets SI **en construction**

---

## 3. Projet collaboratif (groupe)

### Posture
> **Vous etes la DSI de Torpier.** Le DSI vous mandate pour realiser une **etude preliminaire d'evolution du SI** (= ebauche de schema directeur) afin que le SI reste aligne sur la strategie d'entreprise.

### Livrables attendus (PPT)
**Partie 1 - Analyse de l'existant**
- SWOT de l'entreprise
- Cartographie des processus metiers (taches + acteurs)
- Tableau des applications x fonctions metiers
- Tableau des composants techniques x applications supportees
- 5 axes d'amelioration / evolutions du SI
- Comparaison de **3 referentiels** de gouvernance SI

**Partie 2 - Gestion des equipes et du changement**
- Organisation globale (hierarchique + transversale) des equipes SI
- Matrice **RACI** avec parties prenantes cles
- Outils de suivi des projets et du changement
- **Pitch** pour faire adherer la direction a la conduite du changement

**Partie 3 - Bilan**
- Roles et responsabilites de chaque membre du groupe
- Bilan du travail effectue (points forts + axes d'amelioration)

### Grille d'evaluation collective (/20)
| Theme | Critere | Pts |
|---|---|---|
| Modeliser flux et ressources | SWOT distinguant les 4 quadrants | 1 |
|  | Processus + taches + acteurs | 2 |
|  | Applications + fonctions metiers | 2 |
|  | Infrastructure + applications supportees | 2 |
|  | 5 axes d'amelioration coherents | 1 |
|  | Comparaison 3 referentiels argumentee | 2 |
| Encadrer les equipes | Organisation hierarchique + transversale | 2 |
|  | Matrice RACI claire avec parties prenantes | 2 |
| Conduire le changement | Outils de suivi des projets | 1 |
|  | Outils de pilotage du changement | 1 |
|  | Pitch convaincant pour la direction | 2 |
| Presentation orale | Bilan groupe + organisation | 1 |
|  | Support PPT pro et prestation fluide | 1 |
| **Total** |  | **20** |

**Bareme : A 16-20  /  B 12-15.99  /  C 8-11.99  /  D 0-7.99**

### Grille d'evaluation individuelle dans le collab (/12)
| Theme | Critere | Pts |
|---|---|---|
| Competences techniques | Participation et efficacite | 2 |
|  | Maitrise des outils | 3 |
|  | Reaction face a un imprevu | 4 |
| Qualite oral | Animation, prise en compte de l'auditoire | 2 |
|  | Reponses aux questions argumentees | 1 |
| **Total** |  | **12** |

**Bareme : A 10-12  /  B 7-9.99  /  C 5-6.99  /  D 0-4.99**

---

## 4. Evaluation individuelle de Bloc (solo)

### Posture
> **Vous etes le nouveau responsable du SI.** Premier objectif : **ameliorer l'alignement du SI avec la strategie** d'entreprise (= accroitre la valeur ajoutee du SI). Vous presentez **la trajectoire du SI** a la direction pour la convaincre.

### Livrables attendus (PPT)

**Bloc 1 - Modeliser les flux metiers et les ressources techniques**
- Comprehension synthetique de la strategie d'entreprise
- Representation schematique des **4 strates** : processus, fonctions, applications, infrastructure
- 5 ameliorations argumentees avec **indicateur de la valeur** apportee
- **Focus sur 1 des 5 axes** (= "Optimisation du SI" pour nous)
- Description de **5 projets operationnels** (titre, perimetre, objectifs, **referentiel de gouvernance** + processus/methode preconisee)

**Bloc 2 - Encadrer les equipes**
- Roles et responsabilites couvrant les 5 projets (en accord avec competences et aspirations)
- Type de management adapte aux referentiels utilises
- **Organigramme equipe projet** coherent avec le management et les responsabilites
- **Identification des besoins externes** (fournisseurs, sous-traitants) avec justification
- **Plan de communication** : actions, ressources, canaux, indicateurs d'evaluation
- **Outil(s) collaboratif(s)** facilitant la relation avec les externes ET le pilotage interne via KPIs

**Bloc 3 - Conduire le changement**
- **Leviers d'engagement** (ce qui entraine l'adhesion)
- **Methode de changement** activant ces leviers
- 1-2 **arguments d'adhesion** coherents avec l'axe choisi
- Liste des **acteurs impactes** + acteurs a engager
- Vision macroscopique des **processus de communication** autour du changement

### Grille d'evaluation individuelle (/20)
| Theme | Critere | Pts |
|---|---|---|
| Modeliser flux et ressources | Presentation entreprise + processus + workflows | 3 |
|  | SI existant avec **topologies graphiques** | **4** |
|  | 5 axes d'amelioration repondant aux enjeux | 2 |
| Encadrer les equipes | Responsabilites coherentes avec competences | 1 |
|  | Organigramme + management + outils de suivi | **3** |
|  | Fournisseurs + plan de com collaboratif | 2 |
| Conduire le changement | Methode + leviers + arguments d'adhesion | 2 |
|  | Acteurs cles + moyens de communication | 1 |
| Qualite presentation | Prestation orale fluide et structuree | 1 |
|  | Support pro avec schemas lisibles | 1 |
| **Total** |  | **20** |

**Bareme : A 16-20  /  B 12-15.99  /  C 8-11.99  /  D 0-7.99**

---

## 5. Articulation collaboratif -> individuel

| Element produit en collab | Reutilisable en indiv ? | Adaptations |
|---|---|---|
| SWOT | Oui | Tel quel |
| Cartographie des processus | Oui | Tel quel |
| Tableau applications x fonctions | Oui | Tel quel |
| Tableau infrastructure x applications | Oui | Tel quel |
| Schema des 4 strates SI | Oui (obligatoire indiv) | Tel quel |
| Topologie reseau | Oui (obligatoire indiv) | Tel quel |
| 5 axes d'amelioration SI | Oui | + focus approfondi sur 1 axe |
| Comparaison 3 referentiels | Oui | + 1 referentiel applique aux 5 projets |
| Organigramme DSI globale | Partiel | Indiv = organigramme **equipe projet operationnelle** (different) |
| RACI globale transformation | Partiel | Indiv = RACI du **programme des 5 projets** |
| Outils collab + pitch changement | Partiel | A approfondir cote indiv (CDC + plan de com) |

**Specifique a l'individuel (a creer en plus)** :
- Description detaillee des 5 projets operationnels (referentiel + processus)
- Organigramme equipe projet + type de management justifie
- Plan de com prestataires + outils collaboratifs avec KPIs
- Methode de conduite du changement + leviers + acteurs

---

## 6. Choix deja figes

| Decision | Choix |
|---|---|
| Axe focus individuel | **Optimisation du SI** |
| Composition groupe | 3 personnes |
| **5 projets de l'axe Optim. SI** | P1 Migration Exchange -> M365 + Annuaire unifie  /  P2 SD-WAN multi-sites  /  P3 PRA/PCA  /  P4 IAM/SSO/MFA + ITSM ITIL  /  P5 Integration GesProd<->Dynamics + Pilotage KPI |
| Referentiels | A arbitrer (default : ITIL v4 + COBIT 2019 + ISO 27001) |
| Methode de conduite du changement | A arbitrer (default : Kotter + ADKAR) |

---

## 7. Conseils CESI a garder en tete

- **Sujet ouvert** : on peut ajouter des informations tant qu'elles ne contredisent pas le contexte.
- **Argumentation = point central** pour convaincre la DSI / la direction.
- **Forme irreprochable** : on presente devant la direction.
- Avancer **par iterations** : trame globale d'abord, detail ensuite.
- **Mettre l'accent sur le pourquoi** plus que sur le comment.

---

*Document de cadrage - Groupe Torpier | SDSI 2026-2029 - DSI Torpier - v1.0*
