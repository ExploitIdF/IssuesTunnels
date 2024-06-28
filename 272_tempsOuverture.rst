Temps de fermeture d'une porte tunnel
##########################################
mise à jour 28/06/2024

Une extraction des données GTC pour le métier **Autoévacuation** a été réalisée sur la période de 5/2023 à 5/2024, 
pour tous les tunnels sauf 3  (A14, Echangeur A14/A86 et Fontenay le F.).  

Les données ne sont pas absolument complètes, mais les données manquantes représentent moins de 10 jours par tunnel.
On considèrera donc qu'on dispose de données pour une période d'une année entière.

Pour 5 tunnels, (Nanterre, Neuilly, Belle-Rive, Saint-Cloud & Sévines) l'horodatage est arrondi à la minute 
ce qui ne permet pas d'analyser le temps de fermeture des portes qui se compte en seconde.

Les 16 tunnels pour lesquelles un horodatage à la seconde est disponible sont : 
'A6B', 'ANT', 'BAP', 'BDR', 'BOI', 'CHA', 'CRN', 'FRE', 'GMO', 'LAN','LUM', 'MOU', 'NOG', 'ORL', 'PON', 'TAV'.

Ces 16 tunnels représentent 160 issues sur 290. Ils constituent le périmètre des traitements que l'on présente ci-dessous.

On peut calculer le nombre d'ouvertures détectées dans l'année :

* 90% des issues ont été ouverte plus de  37 fois dans l'année.
* 80% des issues ont été ouverte plus de  52 fois dans l'année.
* 50% des issues ont été ouverte plus de  84 fois dans l'année.
* 20% des issues ont été ouverte plus de  195 fois  dans l'année.
* 10% des issues ont été ouverte plus de  256 fois dans l'année.

5 issues remontent des valeurs suppérieures à 500 ouvertures dans l'année. Ces valeurs extrêmes sont liées à des pics qui ne durent que quelques jours. Il s'agit en fait de "bagotements" qu'il faut traiter comme tels. Il ne sont pas neutralisés dans la présente analyse car ils ne concerne qu'un petit nombre d'issues.

Pour chaque issue, on peut calculer la distribution des temps de fermeture 
et en particulier la valeur médiane des temps de fermeture :

* Pour 30% des issues cette valeur médiane est de 6 secondes. Deux issues ont une valeurs médiane inférieure (4 secondes).
* 50% des issues ont une valeur médiane des temps de fermeture inférieure à 8 secondes.
* 80% des issues ont une valeur médiane des temps de fermeture inférieure à 11 secondes.
* 90% des issues ont une valeur médiane des temps de fermeture inférieure à 14 secondes.
* 5 issues ont une valeur médiane des temps de fermeturesuppérieure à 30 secondes.

Par ailleurs les issues du tunnels de Champigny (IS383 & IS387) remontent des informations incohérentes qui ne permettent pas de connaitre leurs temps de fermeture.

Pour terminer,on fournit dans le tableau ci-dessous la liste des 160 issues du  périmètre mentionné ci-dessus.
Pour chaque issue, le tableau fournit le nombre d'ouverture dans l'année et les deuxième, cinquième et huitième
déciles du temps de fermeture de la porte tunnel de l'issue.


.. csv-table::
   :header: PC,Tunnel,Issue,Nombre ,déc2,déc5,déc8
   :width: 80%
    
    PCE,BOISSY,IS521,74,6,6,12
    PCE,BOISSY,IS522,47,4,6,8
    PCE,BOISSY,IS523,58,6,8,15
    PCE,BOISSY,IS524,54,4,8,30
    PCE,BOISSY,IS525,80,6,8,14
    PCE,BOISSY,IS526,102,4,6,12
    PCE,BOISSY,IS527,95,6,6,14
    PCE,BOISSY,IS528,77,6,7,10
    PCE,CHAMPIGNY,IS381,53,6,12,47
    PCE,CHAMPIGNY,IS382,52,7,19,1451
    PCE,CHAMPIGNY,IS383,4,13200,1768556,5383204
    PCE,CHAMPIGNY,IS384,54,6,8,12
    PCE,CHAMPIGNY,IS385,84,6,10,44
    PCE,CHAMPIGNY,IS386,38,6,10,54
    PCE,CHAMPIGNY,IS387,7,46362,284199,2761374
    PCE,CHAMPIGNY,IS388,102,6,8,19
    PCE,CHAMPIGNY,IS389,68,4,8,16
    PCE,CHAMPIGNY,IS390,145,4,6,12
    PCE,CHAMPIGNY,IS391,109,6,8,16
    PCE,CHAMPIGNY,IS392,136,4,6,18
    PCE,CHAMPIGNY,IS393,105,6,8,18
    PCE,GUY-MOQUET,IS272,64,4,6,20
    PCE,GUY-MOQUET,IS273,138,4,9,35
    PCE,GUY-MOQUET,IS274,519,6,13,28
    PCE,GUY-MOQUET,IS275,70,9,12,29
    PCE,GUY-MOQUET,IS276,20,8,11,14
    PCE,GUY-MOQUET,IS277,76,6,8,21
    PCE,GUY-MOQUET,IS278,85,8,18,167
    PCE,GUY-MOQUET,IS280,156,6,8,30
    PCE,MOULIN,IS282,8,18,44,108
    PCE,MOULIN,IS283,32,4,10,50
    PCE,MOULIN,IS284,41,6,9,35
    PCE,MOULIN,IS285,55,6,7,54
    PCE,MOULIN,IS289,31,8,12,26
    PCE,MOULIN,IS290,33,6,8,20
    PCE,MOULIN,IS291,32,8,12,27
    PCE,MOULIN,IS292,62,6,11,28
    PCE,MOULIN,IS293,24,6,12,22
    PCE,MOULIN,IS294,52,6,10,48
    PCE,MOULIN,IS295,56,8,16,131
    PCE,MOULIN,IS296,50,6,8,28
    PCE,NOGENT,IS251,128,6,10,28
    PCE,NOGENT,IS252,195,4,6,18
    PCE,NOGENT,IS253,92,4,6,26
    PCE,NOGENT,IS254,198,6,7,14
    PCE,NOGENT,IS255,120,6,8,18
    PCE,NOGENT,IS256,104,6,6,12
    PCE,NOGENT,IS257,177,6,8,20
    PCE,NOGENT,IS258,108,6,13,87
    PCE,NOGENT,IS259,79,6,8,57
    PCE,NOGENT,IS260,215,4,6,12
    PCE,NOGENT,IS261,109,10,32,219
    PCE,NOGENT,IS262,42,6,8,26
    PCE,NOGENT,IS263,149,8,10,28
    PCE,NOGENT,IS264,176,4,8,222
    PCE,NOGENT,IS265,228,4,6,16
    PCE,NOGENT,IS266,276,6,8,20
    PCE,NOGENT,IS267,161,6,14,126
    PCE,NOGENT,IS268,262,4,6,20
    PCE,NOGENT,IS269,181,6,10,38
    PCN,BOBIGNY,IS221,78,6,10,26
    PCN,BOBIGNY,IS222,79,6,7,16
    PCN,BOBIGNY,IS223,24,6,6,8
    PCN,BOBIGNY,IS224,72,6,8,14
    PCN,BOBIGNY,IS225,214,4,12,16
    PCN,BOBIGNY,IS226,75,4,6,8
    PCN,BOBIGNY,IS227,65,6,32,120
    PCN,BOBIGNY,IS228,30,4,6,13
    PCN,BOBIGNY,IS229,91,6,8,14
    PCN,BOBIGNY,IS230,60,5,8,22
    PCN,BOBIGNY,IS228A,77,6,8,13
    PCN,BOBIGNY,IS232,130,6,8,19
    PCN,BOBIGNY,IS237A,91,4,6,12
    PCN,BOBIGNY,IS234,56,6,8,18
    PCN,BOBIGNY,IS235,70,6,8,18
    PCN,BOBIGNY,IS236,112,8,12,21
    PCN,BOBIGNY,IS237,70,6,6,12
    PCN,BOBIGNY,IS238,171,8,22,666
    PCN,BOBIGNY,IS239,186,6,8,16
    PCN,BOBIGNY,IS240,61,6,8,12
    PCN,BOBIGNY,IS241,81,6,8,17
    PCN,BOBIGNY,IS238A,199,6,8,12
    PCN,BOBIGNY,IS243,45,4,8,20
    PCN,BOBIGNY,IS224A,40,6,7,14
    PCN,BOBIGNY,IS245,101,6,6,22
    PCN,LANDY,IS351,269,10,12,20
    PCN,LANDY,IS352,183,6,8,22
    PCN,LANDY,IS353,69,6,8,14
    PCN,LANDY,IS354,293,6,8,12
    PCN,LANDY,IS355,54,8,9,27
    PCN,LANDY,IS356,84,6,8,22
    PCN,LANDY,IS357,251,6,8,18
    PCN,LANDY,IS358,87,6,8,30
    PCN,LANDY,IS359,147,8,18,58
    PCN,LANDY,IS360,5151,4,7,18
    PCN,LANDY,IS361,195,8,30,1393
    PCN,LANDY,IS362,186,6,8,20
    PCN,LANDY,IS363,213,6,10,30
    PCN,LANDY,IS364,309,6,8,20
    PCN,LANDY,IS365,184,6,8,23
    PCN,LANDY,IS366,130,6,8,18
    PCN,LANDY,IS367,236,6,8,20
    PCN,LANDY,IS368,80,8,12,149
    PCN,LANDY,IS369,461,6,8,10
    PCN,LANDY,IS370,333,6,8,22
    PCN,LA_COURNEUVE,IS201,55,6,14,55
    PCN,LA_COURNEUVE,IS202,74,8,32,102
    PCN,LA_COURNEUVE,IS203,61,8,18,71
    PCN,LA_COURNEUVE,IS204,104,6,8,24
    PCN,LUMEN_NORTON,IS211,617,4,12,36
    PCN,LUMEN_NORTON,IS212,3417,5,6,46
    PCN,LUMEN_NORTON,IS213,39,8,34,183
    PCN,LUMEN_NORTON,IS214,29,6,14,86
    PCN,TAVERNY,IS472,58,8,8,23
    PCN,TAVERNY,IS473,59,6,10,39
    PCN,TAVERNY,IS474,36,8,8,30
    PCN,TAVERNY,IS475,43,8,8,17
    PCO,AMBROISE_PARE,IS431,73,6,8,19
    PCO,AMBROISE_PARE,IS432,59,4,6,10
    PCO,AMBROISE_PARE,IS433,27,4,6,13
    PCO,AMBROISE_PARE,IS434,16,4,8,12
    PCO,AMBROISE_PARE,IS435,40,6,8,16
    PCO,AMBROISE_PARE,IS436,38,6,6,12
    PCO,AMBROISE_PARE,IS437,45,6,8,14
    PCO,AMBROISE_PARE,IS438,62,4,6,10
    PCO,AMBROISE_PARE,IS439,35,8,10,14
    PCO,AMBROISE_PARE,IS440,69,5,6,12
    PCO,AMBROISE_PARE,IS441,58,4,6,10
    PCO,AMBROISE_PARE,IS442,37,6,6,10
    PCO,AMBROISE_PARE,IS443,48,6,6,16
    PCO,AMBROISE_PARE,IS444,80,6,8,14
    PCO,AMBROISE_PARE,IS445,49,4,6,10
    PCO,CHENNEVIERES,IS492,64,4,8,14
    PCO,CHENNEVIERES,IS493,62,6,8,14
    PCS,ANTONY,IS311,102,6,24,680
    PCS,ANTONY,IS312,163,6,8,16
    PCS,ANTONY,IS313,256,4,6,14
    PCS,ANTONY,IS314,178,6,6,14
    PCS,ANTONY,IS315,350,4,6,14
    PCS,ANTONY,IS317,244,4,6,10
    PCS,ANTONY,IS318,206,5,8,14
    PCS,ANTONY,IS319,198,4,6,12
    PCS,ANTONY,IS320,1507,4,12,43
    PCS,BICETRE,IS404,245,4,4,14
    PCS,BICETRE,IS405,186,4,6,10
    PCS,BICETRE,IS406,237,6,6,20
    PCS,BICETRE,IS407,106,4,6,13
    PCS,BICETRE,IS408,237,4,6,11
    PCS,BICETRE,IS409,311,4,6,10
    PCS,BICETRE,IS410,152,4,6,8
    PCS,BICETRE,IS411,104,4,6,82
    PCS,BICETRE,IS412,212,4,6,8
    PCS,BICETRE,IS413,270,4,4,6
    PCS,FRESNES,IS301,169,6,10,20
    PCS,FRESNES,IS302,297,6,10,22
    PCS,ITALIE,IS401,140,6,6,12
    PCS,ITALIE,IS402,80,6,8,10
    PCS,ITALIE,IS403,145,6,8,12
    PCS,ORLY,IS481,65,6,8,12
    PCS,ORLY,IS482,63,6,8,14









