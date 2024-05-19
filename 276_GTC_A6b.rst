Analyse des données GTC AEV A6b (Bicêtre & Italie)
****************************************************
Pour explorer l'utiliter d'exploiter les données de la GTC AEV des tunnels, le cas A6b a été choisi comme exemple. 
Les données du journal des consignations ont été extraites sur la période mai/2023 - avril/2024 (180 000 lignes). 
On rend compte ici des traitements réalisés.

Variables prises en compte
==========================
Le fichier contient les variables suivantes :
'name', 'value', 'ts', 'domain', 'nature', 'description', 'alarmlevel','equipement', 'utilisateur', 'evenement', 'etat'.

Les variables exploitées sont les suivantes :
'type', 'dt',  'description',    'equipement',   'evenement'

type
^^^^^^
On construit la variable **type** en décomposant la variable **name** en 5 parties séparées par des point ".". Par exemple :
name : **A6B_TU.AE001.AE600007.TS.ETA_MA_SURP** -> type : **ETA_MA_SURP**.

La variable type prend 151 valeurs.
On a supprimé les enregistrements dont la variable type a moins de 20 occurences (39 valeurs).

On peut classer les valeurs de la variable type selon ses 3 premières lettres :  

      * ETA    140721  
      * DEF     30598  
      * MOD      7001  
      * CDE      1207  
      * ETL       256  
      * CLI        50 

Dans la suite, on s'interessera aux 4 premiers groupes.

equipement
^^^^^^^^^^
Le champ **equipement** prend 35 valeurs que l'on peut classer en 3 groupes :

**'Auto Evacuation A6b'** : valeur utilisée uniquement pour le déclenchement de la surpression dans les issues, toutes les 3 heures pendant 15 minutes. 

A chaque fois que cette valeur apparait, on observe également des événements de type pour les équipements suivants : 'SENS W NS01 / NS03 / NS05 / NS07',
       'SENS W NS09 / NS11', 'SENS W NS13', 'SENS W NS15',
       'SENS W NS17 / NS19 / NS21', 'SENS W SB00X',
       'SENS Y NS02 / NS04 / NS06 / NS08', 'SENS Y NS10 / NS12', 'SENS Y NS14',
       'SENS Y NS16', 'SENS Y NS18 / NS20 / NS22', 'SENS Y SB00A / SB00B',
       'SENS Y SB00C', 'SENS Y SB00D', 'SENS Y SB00E'

'PAU niche NS1 - IP=\t30.8.36.34','PAU niche NS2 - IP=\t30.8.36.35', 'PAU niche NS3 - IP=\t30.8.36.36',
'PAU niche NS4 - IP=\t30.8.36.37', 'PAU niche NS5 - IP=\t30.8.36.38','PAU niche NS6 IP=\t30.8.36.39', 
'SENS W NS01 / NS03 / NS05 / NS07',

'SENS W NS09 / NS11', 'SENS W NS13', 'SENS W NS15','SENS W NS17 / NS19 / NS21', 
'SENS Y NS02 / NS04 / NS06 / NS08', 'SENS Y NS10 / NS12', 'SENS Y NS14','SENS Y NS16', 'SENS Y NS18 / NS20 / NS22',

'SENS W SB00X','SENS Y SB00A / SB00B','SENS Y SB00C', 'SENS Y SB00D', 'SENS Y SB00E',

'TSE issue 401 IP=30.8.36.31', 'TSE issue 402 IP=30.8.36.32',
'TSE issue 403 IP=30.8.36.33', 'TSE issue 404 IP=30.8.36.11',
'TSE issue 405 IP=30.8.36.12', 'TSE issue 406 IP=30.8.36.13',
'TSE issue 407 IP=30.8.36.14', 'TSE issue 408 IP=30.8.36.15',
'TSE issue 409 IP=30.8.36.20', 'TSE issue 410 IP=30.8.36.19',
'TSE issue 411 IP=30.8.36.18', 'TSE issue 412 IP=30.8.36.17',
'TSE issue 413 IP=30.8.36.16'








