Camera dans les issues et les galeries
****************************************

Dans CosWin, le champs **Type Famille**  comporte 2 valeurs qui peuvent correspondre aux caméras liées aux issues
et aux galeries d'évacuation.

* CAMERA-IS
* CAMERA-VIDEO

CAMERA-IS
===========
Il y a 264 équipements dont le **Type Famille** est **CAMERA-IS**. 

Leur Code exploitant est de la forme CAM/ISNNN pour la caméra de l'issue ISNNN,
et toutes les caméras peuvent être associées à une issue existante de cette manière.

L'issue IS421 a 3 caméras dans CosWin : CAM/IS421, CAM/IS421a, CAM/IS421b

Les issues IS228, IS103, IS237, IS224, IS238 ont chacune 2caméras dans CosWin CAM/ISNNN & CAM/ISNNNa

En revanche, 33 issues ne sont pas associées à l'une des caméras identifiées dans CosWin 
par la valeur  **CAMERA-IS** du champs **Type Famille**.


.. csv-table::
   :header: Tunnel,Issue
   :widths: 35, 15
   :width: 50%
    
    AMBROISE_PARE,IS431
    AMBROISE_PARE,IS433
    AMBROISE_PARE,IS434
    AMBROISE_PARE,IS436
    AMBROISE_PARE,IS439
    AMBROISE_PARE,IS441
    AMBROISE_PARE,IS443
    AMBROISE_PARE,IS445
    ANTONY,IS316
    BOBIGNY,IS224A
    BOBIGNY,IS228A
    BOBIGNY,IS237A
    BOBIGNY,IS238A
    CHAMPIGNY,IS382
    CHAMPIGNY,IS383
    ECHANGEUR_NANTERRE,IS120
    ECHANGEUR_NANTERRE,IS136
    FONTENAY,IS421A
    FONTENAY,IS421B
    FONTENAY,IS423
    FONTENAY,IS423A
    FONTENAY,IS423B
    FONTENAY,IS424
    GUY-MOQUET,IS271
    GUY-MOQUET,IS280
    LA_DEFENSE,IS103A
    LUMEN_NORTON,IS212
    MOULIN,IS286
    MOULIN,IS287
    SEVINES,IS513
    SEVINES,IS514
    TAVERNY,IS471
    TAVERNY,IS476

CAMERA-VIDEO
=============
Comme on va le voir, le **Type Famille** qui prend la valeur **CAMERA-VIDEO** contient des caméras de nature très différentes.

On explique ci-dessous comment on arrive, par éliminiations successives, aux 53 caméras en issues qui sont classées dans ce **Type Famille** .

Il y a au total 926 équipements dont le champ **Type Famille** prend la valeur **CAMERA-VIDEO** et 
dont le champ **Etat** prend la valeur **EXPLOITATION**.

Parmi ces équipements, 278 ont une valeur du champ **Tunnel** qui est l'un des 25 noms de tunnels exploités par le DETT.

Parmi ces équipements 118 ont un champ **Local** qui est vide. Il s'agit de caméras qui ont une valeur
du champ **Description** de la forme : **Caméra DAI/Non DAI sur ANN**. 

Ces caméras sont semble-t-il orientées vers la route et n'ont pas de lien direct avec les issues.

Il reste 160 équipements qui sont identifiées à la fois par leur champs **Description** et par 
leur champs **Code Exploitant** comme des caméras **Anti intrustion**.

* 104 ont une description qui commence par : Caméra anti-intrusion du LTU
* 46 ont une description qui commence par : Caméra anti-intrusion de l'Issue de secours n°
* 7 ont une description qui commence par : Caméra anti-intrusion de la Galerie évacuation (Cette dernière catégorie correspond à des caméras situées dans les galeries du tunnel de Saint Cloud.)

On a identifié par ce moyen 46+7=53 caméras en issues (y.c. galeries). 
Pour 46 d'entre-elles, l'issue correspondante peut être identifiées en supprimant les dix premiers caractères ("CAM-INTRU/") du champs "Code Exploitant".

Pour les 7 autres cas, il s'agit : 

* soit d'issues avec plusieurs caméras (IS460-1,IS460-2), 
* soit d'un codage inhabituel (PARIS-1,PARIS-2,PARIS-3, ici le champ description indique l'issue IS451)
* soit d'un codage qui fait référence à l'IS430 du  tunnel de Bobigny qui a été récemment rebaptisée (Il y aurait lieu de modifier dans CosWin le code exploitant de ces caméras).

Le fruit de ce traitement est une table des caméras du **Type Famille**  **CAMERA-VIDEO** : 
`coswin-camera-video-issues.csv
<https://raw.githubusercontent.com/ExploitIdF/IssuesTunnels/main/_static/camera/coswin-camera-video-issues.csv>`_














