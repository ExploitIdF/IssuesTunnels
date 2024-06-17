Actions proposées
============================
Réorganisation des marchés intervenant sur les issues.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
On a vu que les prestations concernant les issues sont réparties entre 2 marchés différents et que le principal prix concerne la maintenance d'une issue, alors que les interventions sont faites pour l'ensemble des issues et des niches d'un tube.

On pourrait regrouper toutes la maintenance préventive annuelle d'un tube dans un seul prix du BPU. 
Cela comporterait une maintenance annuelle de chaque issue et 5 visites pour réaliser des essais fonctionnels. 
Les interventions devraient être réparties dans l'année pour qu'il n'y ait jamais 3 mois sans qu'une issue soit contrôlée.

Le prix d'une visite supplémentaire des issues d'un tube pourrait être au BPU et servir également pour calculer, lors du constat, 
la réfaction quand le prestataire n'a pas fait les 5 visites prévues.

Dans le cas où les inspections bimestrielles sont réalisées en régie par le PCTT, on utiliserait un prix 
pour une unique action préventive sur toutes les issues et les niches d'un tube.

Explicitation des exigences pour les missions préventives
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Actuellement, la consistance exacte des tâches à réaliser n'est pas précisément définie et les TDM n'ont pas tous la même conception sur certaines d'entre elles. 

Que veut dire par exemple vérifier le bon fonctionnement de la surpression ? 
  * A) = Le ventilateur démarre quand on ouvre la porte.
  * B)  = A) & le niveau de bruit émis par les organes concernés correspond à ce à quoi on a l'habitude.
  * C)  = B) & la pression sur la porte de la rend pas trop difficile à ouvrir.
  * D)  = On mesure par une procédure déterminée le niveau de la surpression pour vérifier qu'il est conforme à une fourchette de valeurs acceptables.

Il faudrait faire une description exhaustive des tâches pour la maintenance annuelle et pour les essais fonctionnels. 
En parallèle, il faut concevoir les modalités de reporting associées. 
Le résultat de ce travail figurera dans le CCTP du marché.

Les documents produits devront être soumis aux TDM concernés pour qu'ils s'assurent qu'ils comprennent tous la même chose et qu'ils sont en mesure de faire appliquer et de contrôler la réalisation des spécifications ainsi définies.


Etablir un format de fichiers pour importer le reporting du prestataire dans une base unique
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Pour que les données des rapports soient rassemblées dans une base unique, il faut que les équipes des prestataires
disposent d'une application sur le terrain pour enregistrer ce qu'ils ont constaté et ce qu'ils ont fait.
Il faut ensuite que des fichiers exploitables soient transmis à la DIRIF.

Les entreprises compétentes pour être titulaire du marché disposent d'outils de saisie des données qu'elles 
connaissent bien et leur personnel est équipé de terminaux compatibles.
Les entreprises peuvent concevoir les modules de collecte de données et les conversions de fichiers pour communiquer 
les rapports à la DIRIF dans un format imposé.

Il faut donc définir une liste de champs et pour chaque champ le type de données attendues. 
Pour certains champs, la liste des choix possibles fera partie de la spécification.
Cette spécification doit figurer dans le DCE du marché.


Exploiter les données de la GTC sur les ouvertures de portes et les détections d'événements dans les issues.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
La GTC conserve pendant 12 mois les événements détectés par les capteurs présents dans les issues. 
Cela permet par exemple de calculer, pour chaque tunnel, combien de portes ont été ouvertes pendant les deux derniers mois.
Le fait qu'une porte ait été ouverte donne une indication sur le fonctionnement de cette porte.
Le fait qu'une issue ait été visitée par quelqu'un suggère qu'elle est opérationnelle dans la mesure où le visiteur 
aurait signalé un désordre majeur qu'il aurait constaté.

Pour faire cette exploitation, il faut extraire globalement les données correspondantes sur un an. 
L'outil d'extraction existant, Jasper, n'est pas adapté à des requêtes de plus de quelques jours et sur un seul tunnel.

A terme, il faudrait que les données utiles de la GTC soient mises à disposition sur une base accessible à l'extérieur du réseau technique. 
En attendant, Actémium a fourni une extraction de mai 2023 à mai 2024, pour la plus grande partie des tunnels.

Le travail de mise en place des outils d'analyse des données, sur la base d'une spécification du DETT, pourrait être confié à un prestataire extérieur. 
Une fois la conception des programmes établie, leur utilisation et les adaptations nécessaires pourront être réalisées par les agents d'UPMM.

Mettre à disposition des TDM une application pour le reporting des visites en régie
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le reporting des actions faites en régie est également nécessaire. 
Dans ce cas, c'est au DETT de fournir la solution aux TDM.

Cette application pourrait dans un premier temps ne porter que sur les 3 éléments des CME des issues :
  * ouverture de la porte du tunnel
  * cheminement aisé dans l'issue
  * éclairage de sécurité

