Actions d'amélioration
************************
.. toctree::
   :hidden:
   :maxdepth: 3

   51_objectifs
   53_actions



Les pages précédentes sont descriptives. 
Elles comportent des constats de lacunes et des pistes d'améliorations mais qui sont dispersées.
Cette partie vise à faire la liste des actions d'amélioration pour les expliciter, les évaluer et retenir les plus pertinentes.

Dans un premier temps, on fera la synthèse des :doc:`objectifs poursuivis par les améliorations.<51_objectifs>`

On fera ensuite la :doc:`liste des actions d'amélioration qui répondent à ces objectifs<53_actions>`.


Actions proposées
============================
Réorganisation des marchés intervenant sur les issues.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
On a vu que les prestations concernant les issues sont réparties entre 2 marchés différents et que le principal prix concerne la maintenance d'une issue alors que les interventions sont faites pour l'ensemble des issues et des niches d'un tube.

On pourrait regrouper toutes la maintenance préventive annuelle d'un tube dans un seul prix du BPU. 
Cela comporterait une maintenance annuelle de chaque issue et 5 visites pour réaliser des essais fonctionnels. 
Les interventions devraient être réparties dans l'année pour qu'il n'y ait jamais 3 mois sans qu'une issue soit contrôlée.

Le prix d'une visite suplémentaire pourrait être au BPU et servir également pour calculer, lors du constat, 
la réfection quand le prestataire n'a pas fait les 5 visites prévues.

Dans le cas où les inspections bimestrielles sont réalisées en régie, on utiliserait un prix 
pour une unique action préventive sur toutes les issues et les niches d'un tube.

Explicitation des exigences pour les missions préventives
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Actuellement, la consistance exacte des tâches à réaliser n'est pas précisement définie et les TDM n'ont pas tous la même conception sur certaines d'entre-elles. 

Que veut dire par exemple vérifier le bon fonctionnement de la surpression ? 
  * A) Le ventilateur démarre quand on ouvre la porte.
  * B)  A) & le niveau de bruit émis par les organes concernés correspond à ce à quoi on a l'habitude.
  * C)  B) & la pression sur la porte de la rend pas trop difficule à ouvrir.
  * D) on mesure par une procédure déterminée le niveau de la surpression pour vérifier qu'il est conforme à une fourchette de valeurs acceptables.

Il faudrait faire une description exhaustive des tâches pour la maintenance annuelle et pour les essais fonctionnels. En parallèle, il faut concevoir les modalités de reporting associées. Le résultat de ce travail figurera dans le CCTP du marché.

Les documents produit devront être soumis aux TDM concernés pourqu'ils s'assurent qu'ils comprennent tous la même chose et qu'ils sont en mesure de faire appliquer et de contrôler la réalisation des spécifications ainsi définies.


Etablir un format de fichiers pour importer le réporting du prestataire dans une base CosWin
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Pour que les données des rapports soient rassemblées dans une base unique, il faut que les prerstataires
disposent d'une application sur le terrain pour enregistrer ce qu'ils ont constaté et ce qu'ils ont fait.
Il faut ensuite que des fichiers exploitables soient transmis à la DIRIF.

Les entreprises compétentes disposent d'outils de saisie des données qu'elles connaissent et 
leur personnel est équipé de terminaux compatibles.
Les entreprises peuvent concevoir les modules de collecte de données et les convertions de fichiers pour communiquer 
les rapports à la DIRIF dans un format imposé.

Il faut donc définir une liste de champs et pour chaque champ le type de données attendues. 
Pour certains champ, la liste des choix possibles fera partie de la spécification.


Exploiter les données de la GTC sur les ouvertures de portes et les détections d'événements dans les issues.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
La GTC conserve pendant 12 mois les événements détectés par les capteurs présents dans les issues. 
Cela permet par exemple de calculer, pour chaque tunnel, combien de portes ont été ouvertes pendant les deux derniers mois.
Le fait qu'une porte ait été ouverte donne une indication sur le fonctionnement de cette porte.
Le fait qu'une issues ait été visité par quelqu'un suggère qu'elle est opérationnelle dans la mesure où la personne aurait signalé un désordre majeur qu'il aurait constaté.

Pour faire cette exploitation, il faut extraire globalement les données correspondantes sur un an. 
L'outil Jasper n'est pas adpaté à ce type de requête.

A terme, il faudrait que les données utiles de la GTC soient mises à disposition sur une base accessible à l'extérieur du réseau technique. En attendant, on pourrait demander à Actémium de faire une extraction particulière.

Mettre à disposition des TDM une application pour le reporting des visites en régie
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le reporting des actions faites en régie est également nécessaire. 
Dans ce cas, c'est au DETT de fournir la solution aux TDM.

Cette application pourrait dans un premier temps ne porter que sur les 3 éléments des CME des issues :
  * ouverture de la porte du tunnel
  * cheminement aisé dans l'issue
  * éclairage de sécurité







