Analyse des données GTC AEV A6b (Bicêtre & Italie)
****************************************************
Mise à jour : mai 2024

Pour explorer l'utilité d'exploiter les données de la GTC AEV des tunnels, le cas A6b a été choisi comme exemple. 
Les données du journal des consignations ont été extraites sur la période mai/2023 - avril/2024 (180 000 lignes). 
On rend compte ici des traitements réalisés.

Variables prises en compte
==========================

Le fichier contient les variables suivantes :
'name', 'value', 'ts', 'domain', 'nature', 'description', 'alarmlevel','equipement', 'utilisateur', 'evenement', 'etat'.

Les variables identifiées comme utiles sont les suivantes :
'type', 'dt',  'description',    'equipement',   'evenement'

On décrit ci-dessous chacune de ces variables.

Variable type
--------------

On construit la variable **type** en décomposant la variable **name** en 5 parties séparées par des point ".". Par exemple :
name : **A6B_TU.AE001.AE600007.TS.ETA_MA_SURP** -> type : **ETA_MA_SURP**.

La variable type prend 151 valeurs.
On a supprimé les enregistrements dont la variable type a moins de 20 occurences (39 valeurs).

On peut classer les valeurs de la variable type selon ses 3 premières lettres

On indique les nombres d'occurences des 6 groupes ainsi définis :  

      * ETA    140721  
      * DEF     30598  
      * MOD      7001  
      * CDE      1207  
      * ETL       256  
      * CLI        50 

Dans la suite, on s'interessera aux 4 premiers groupes.

Variable equipement
-----------------------

La variable **equipement** prend 35 valeurs que l'on peut classer en 4 groupes :

Groupe :'Auto Evacuation A6b'
"""""""""""""""""""""""""""""""""""

Une seule valeur : **Auto Evacuation A6b**

La  valeur **'Auto Evacuation A6b'**  est utilisée uniquement pour le déclenchement de la surpression dans les issues, toutes les 3 heures pendant 15 minutes. 

A chaque fois que cette valeur apparait, on observe également des événements de type **ETA_MA_SURPVENT** 
pour les équipements suivants : 'SENS W NS01 / NS03 / NS05 / NS07',  'SENS W NS09 / NS11', 'SENS W NS13', 
'SENS W NS15', 'SENS W NS17 / NS19 / NS21',
'SENS W SB00X','SENS Y NS02 / NS04 / NS06 / NS08', 'SENS Y NS10 / NS12','SENS Y NS14', 'SENS Y NS16', 
'SENS Y NS18 / NS20 / NS22', 'SENS Y SB00A / SB00B', 'SENS Y SB00C', 'SENS Y SB00D', 'SENS Y SB00E'

On observe également des événements de type **DEF_DISC_SURP, ETA_MA_SURP & ETA_RM_SURP** pour les seuls équipements suivants :	
'SENS W NS15', 'SENS Y NS16',  'SENS Y SB00C'

Groupe : Niches de sécurité du tunnel de Bicêtre NS1 à NS22
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Les valeurs de la variable, pour ce groupe, font référence aux niches du tunnel de Bicêtre, regroupées en fonction de l'issue à laquelle elles sont associées.

10 valeurs prises :
'SENS W NS01 / NS03 / NS05 / NS07','SENS W NS09 / NS11', 'SENS W NS13', 'SENS W NS15','SENS W NS17 / NS19 / NS21', 
'SENS Y NS02 / NS04 / NS06 / NS08', 'SENS Y NS10 / NS12', 'SENS Y NS14','SENS Y NS16', 'SENS Y NS18 / NS20 / NS22'

De nombreux enregistrements qui contiennent ces valeurs font référence à l'issue et non aux niches (Surpression, détection de présence, ouvertures de portes ...). L'information sur l'issue est par ailleurs comprise dans la variable **description**.


Groupe : Niches de sécurité SB00A à SB00E et SB00X
""""""""""""""""""""""""""""""""""""""""""""""""""

Les valeurs de la variable, pour ce groupe, font référence aux niches du tunnel Italie, regroupées en fonction de l'issue à laquelle elles sont associées. 

'SENS W SB00X','SENS Y SB00A / SB00B','SENS Y SB00C', 'SENS Y SB00D', 'SENS Y SB00E',

Les cas des valeurs 'SENS Y SB00E','SENS Y SB00X' sont spécifiques. Les codes SB00X & SB00X prennent la place des codes IS40N dans la variable déscription. Ils sont alors associés au PAU NS5 et NS6 ...

Groupe : PAU et TSE avec leur adresse IP
""""""""""""""""""""""""""""""""""""""""""""""""""

Il s'agit ici des PAU et TSE. 

Les codes NS1-NS6 semblent faire référence à des niches, mais ils ne correspondent pas aux codes NS01-NS22 rencontrés plus haut.

'PAU niche NS1 - IP=\t30.8.36.34','PAU niche NS2 - IP=\t30.8.36.35', 'PAU niche NS3 - IP=\t30.8.36.36',
'PAU niche NS4 - IP=\t30.8.36.37', 'PAU niche NS5 - IP=\t30.8.36.38','PAU niche NS6 IP=\t30.8.36.39',

'TSE issue 401 IP=30.8.36.31', 'TSE issue 402 IP=30.8.36.32','TSE issue 403 IP=30.8.36.33', 'TSE issue 404 IP=30.8.36.11',
'TSE issue 405 IP=30.8.36.12', 'TSE issue 406 IP=30.8.36.13','TSE issue 407 IP=30.8.36.14', 'TSE issue 408 IP=30.8.36.15',
'TSE issue 409 IP=30.8.36.20', 'TSE issue 410 IP=30.8.36.19','TSE issue 411 IP=30.8.36.18', 'TSE issue 412 IP=30.8.36.17',
'TSE issue 413 IP=30.8.36.16'

Déclenchement périodique de la surpression des issues
========================================================
Toutes les 3 heures, sont enregistrés l'activation des surpressions dans les issues. 

15 minutes plus tard, sont enregistrés les désactivations de ces surpressions.

Pour toutes les issues, figure un enregistrement de la forme :

         * type : ETA_MA_SURPVENT	
         * equipement : SENS Y SB00
         * description : IS403 Marche surpression ventilation

Pour les issues IS402 et IS407 s'ajoute un enregistrement de la forme :

         * type : ETA_RM_SURP
         * equipement : SENS Y SB00C	
         * description : IS402 Retour marche surpression

et

         * type : ETA_MA_SURP
         * equipement : SENS Y SB00C	
         * description : IS402 Marche surpression*


Nuits de fermetures et autres jours exceptionnels
==================================================
Lors des nuits de fermeture, les équipes chargées de la maintenance sont amenées à pénétrer dans les issues et ainsi à déclencher les enregistrements d'ouverture de portes et de détection de présence.

Pour détecter ces périodes, on a procédé en plusieurs étapes :

Sélection des enregistrement de type :

* Accès depuis tunnel       ETA_ACCES_TUN      3637
* Détection de présence      ETA_CPT_MVT_ON     2452
* Marche éclairage renforcé  ETA_MA_ECL_RENF    1236

Sélection des heures pour lesquelles au moins 3 issues différentes font l'objet par un enregistrement sélectionné.

A partir de cette sélection, sélection des jours pour lesquels la somme sur les heures des nombres d'issues visitées est supérieure à 8.

Ce tri conduit à retenir les jours et heures suivants :

.. csv-table::
   :header:     Date,Heure,Nombre d'issues
   :widths: 30, 30,30
   :width: 100%
    		
		2023-05-10,23,5
		2023-05-10,22,13
		2023-05-10,21,4
		2023-05-11,20,10
		2023-05-11,0,3
		2023-05-11,21,4
		2023-05-11,23,5
		2023-06-27,21,10
		2023-06-27,22,7
		2023-06-28,22,9
		2023-06-28,21,7
		2023-06-28,23,6
		2023-07-12,0,8
		2023-07-12,23,3
		2023-07-12,1,3
		2023-07-30,15,11
		2023-07-30,16,4
		2023-07-30,17,8
		2023-08-22,22,4
		2023-08-22,23,10
		2023-09-20,22,6
		2023-09-20,2,5
		2023-09-20,23,5
		2023-09-21,1,6
		2023-09-21,2,5
		2023-10-18,0,5
		2023-10-18,2,13
		2023-10-18,1,6
		2024-01-16,23,10
		2024-01-17,0,12
		2024-01-17,1,4
		2024-01-17,2,3
		2024-02-14,0,4
		2024-02-14,3,4
		2024-02-14,23,7
		2024-02-15,0,5
		2024-02-15,2,6
		2024-02-15,3,3
		2024-03-14,1,7
		2024-03-14,2,5
		2024-03-14,22,3
		2024-03-14,23,8
		2024-03-14,0,11
		2024-03-15,0,5
		2024-03-15,1,8
		2024-03-15,2,6
		2024-03-15,3,4







Incendie du 17 février 2024 dans le tunnel Italie Y
=====================================================
Un incendie est survenu dans le début du tube nord le 17 février 2024 à 9h38. La fiche CETU rapporte une interuption du trafic de 140 minutes, soit jusqu'à 12h. 

Les données GTC correspondantes sont disponibles  :doc:`ICI :<2762_GTC240217>`

Les observations suivantes montrent des anomalies sur la détection de la mise en marche de la surpression des issues et de l'éclairage renforcé.

     Dans l'issues IS401, l' *accès tunnel* et la *détection de présence* sont enregistrés à 9h55.
     Il y a par la suite 38 enregistrements de *détection de présence* mais aucun autre accès.
     
     Dans l'issues IS402, l'*accès tunnel* et la *détection de présence* sont enregistrés une première fois à 10h15.
     Il y a par la suite  4 enregistrements d'*accès tunnel* mais pas d'autre *détection de présence*. 
     
     Dans cette issue, à la différence de l'issue IS401 sont enregistrées en outre 2 *Alarme Intrusion en issue*. 
     La  *Marche surpression ventilation* est enregistrée mais pas la *Marche éclairage renforcé*.
     
     Dans l'issues IS403, l'accès tunnel et la détection de présence sont enregistrés une première fois à 10h17.
     Il y a par la suite  2 enregistrements d'accès tunnel mais pas d'autre détection de présence. 
     
     Dans cette issue, comme dans l'issue IS401 il n'y a pas d'*Alarme Intrusion en issue*. 
     La *Marche éclairage renforcé* est enregistrée simultanément mais pas la *Marche surpression ventilation*.









