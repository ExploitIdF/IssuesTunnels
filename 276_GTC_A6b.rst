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









