Niches de sécurité
#######################
Définition
*************
Les niches de sécurité et les niches incendie sont des lieux situés dans les tunnels où sont placés les équipements suivants :

* Postes d'appel d'urgence (PAU)
* Extincteurs
* Hydrants : bornese ou poteaux incendie ou nourisses ou arivées de colonnes sèches
* Prises pompier
* Pictogrammes lumineux de signalisation des niches.

Dans CosWin, il est donné le nom de niche à un *local* avec ou sans porte, mais aussi à un simple emplacement au sol, 
parfois en dehors du tunnel comme aux entrées et sorties, parfois dans une issue de secours.

CosWin contient 437 équipements dont le champ **Type Famille** prend la valeur **LOCAL-NICHE** et qui sont liés à un tunnel géré par le STT.
(Les tunnels exclus du périmètre sont : 'LA_JONCHERE',  'COUV._BLANC-MESNIL', 'ORLEANS', 'COUV._BAGNOLET', 'COUV._MOZART', 'COUV._A-FRANCE').

Niches *Sécurité* ou  niches *Incendie* ?
******************************************
Selon le champ **Description**, on a :

* 374 niches Sécurité
* 55 niches Incendie
* 8 niches Inspection

On trouve des niches *Sécurité* dans tous les tunnels, mais seulement certains tunnels ont des niches *Incendie*.

Une niche *Sécurité* comporte un PAU, 2 extincteurs, un pictogrammes et une borne incendie quand celle-ci ne se trouve pas dans une niches incendie à proximité.

Une niche *Incendie* comporte généralement une borne incendie et parfois des extincteurs ou un pictogramme.

CosWin référence 334 bornes incendie en exploitation dans le périmètre du STT.

CosWin ne connait aucune borne pour le tunnel de Bicêtre et seulement 8 pour le tunnel de Champigny. 
Ces tunnels sont équipés de colonnes sèches qui s'appuient sur des bornes gérées par des tiers.

Les niches *Inspection* (Boissy) ne concernent pas la sécurité des tunnels et ne seront pas prises en compte dans la suite.

CosWin associe au moins un pictogramme à 377 niches.

Le fichier ci-dessous indique, pour les 437 niches identifiées dans CosWin, les nombres de bornes incendie, de pictogrammes et d'extincteurs associés dans CosWin.

`Table des niches <https://raw.githubusercontent.com/ExploitIdF/IssuesTunnels/main/_static/nichesBrExPc.csv>`_ 

