Données de la GTC
******************
.. toctree::
   :hidden:
   :maxdepth: 3

   271_porteT
   273_surpression


Accès aux données
=================
La GTC des tunnels enregistre des événements liés au issues. Les données sont accessibles par l'application JASPER disponible sur le réseau technique du STT.

Il faut choisir dans une requette sur le *"journal des ocnsignations"* :

* une période, 
* un tunnel et 
* le métier *Autoévacuation*.

Les requettes avec une période de plus d'une semaine ont échoué 3 fois sur 4 lors des essais réalisés. En une heure et demi, on est parvenu à extraire quelques jours de données sur 6 tunnels, soit 50 000 *évènements*.
Il n'est donc pas possible par ce moyen de faire des analyses systématiques pour une période de plusieurs mois.

La table ci-dessous présente, pour chacun des 6 tunnels :

* le nombre de jours pour lesquelles des données ont été recueillies
* le nombre d'issues qui apparaissent dans les données

Par exemple, pour le Landy, avec un seul jour de donnée, moins de la moitié des issues ont été à l'origine d'évènements enregistrés par la GTC.

.. csv-table::
   :header: Tunnel ,Nombre de jours, Nombre d'issues
   :widths: 30, 40,40
   :width: 60%

    BAP,4,15
    BDR,1,19
    DEF,4,29
    LAN,1,7
    RUE,9,10
    SCL,9,13


Certains événements apparaissent de nombreuses fois sur une même journée ce qui correspond sans doute à un défaut de capteur.
On a trouvé 5 événements qui sont intervenus plus de 2000 fois:

* IS 337 Discord contacts pte extérieure	
* IS 337   Contact 2 ouv. porte extérieure
* IS150 Défaut téléphone de sécurité HS
* IS460 Défaut téléphone de sécurité HS
* E73.809T détection de fumée impossible	

Le champ *Variable* de la GTC se décompose en 5 parties séparées par des points (**'.'**).
La dernière partie du champ *Variable*, que l'on a notée *var4*, prend 80 valeurs sur l'échantillon récolté. Cette *var4* constituent une typologie des événements.

Quels événements sont enregistrés dans la GTC.
===============================================
Ouverture de portes en tunnel
"""""""""""""""""""""""""""""
Les ouvertures de portes en tunnel sont détectées par 2 capteurs. La GTC fait un contrôle de cohérence.

L'analyse des données permet de détecter les situations suivantes :

* un nombre d'ouvertures anormalement élevé, 
* un temps entre l'ouverture et la fermeture anormal,
* une absence d'utilisation prolongée (à consition de disposer de données sur une longue période)

De manière globale, il serait interessant d'observer la distribution des fréquences d'ouvertures et d'identifier une typologie des issues selon cete distribution.

:doc:`Lien vers l'analyse détaillée des données d'ouvertures de portes en tunnels<271_porteT>`

Activation de la surpression
""""""""""""""""""""""""""""""
La mise en marche et l'arrêt de la surpression sont détectés par la GTC.

L'analyse des données permet de détecter les situations suivantes sur une issue :

* un nombre d'activations anormalement élevé, 
* un temps d'activation anormal,
* une absence d'activation prolongée (à condition de disposer de données sur une longue période)

Il faudrait également vérifier la cohérence entre les activations de la GTC et les autres événements tels que les ouvertures de portes.






