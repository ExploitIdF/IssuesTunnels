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

On peut classer les valeurs de la variable type selon ses 3 premières lettres, nombre d'occurences des 6 groupes ainsi définis :  

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








