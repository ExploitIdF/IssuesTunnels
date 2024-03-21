Données GTC des ouvertures de portes en tunnel
*********************************************

Les ouvertures de portes en tunnel sont détectées par 2 capteurs. Les valeurs correspondantes de va4 sont :

* 'ETA_C1_PTUN_OUV',
* 'ETA_C2_PTUN_OUV'
* 'ETA_ACCES_TUN',
* 'DEF_BGT_C2_PTUN',
* 'DEF_DISC_PTUN',

'ETA_C1_PTUN_OUV' & 'ETA_C2_PTUN_OUV' sont les évènements émis par chacun des détecteurs 1 & 2.

'ETA_ACCES_TUN' est l'évènement de synthèse calculé par la GTC.

'DEF_DISC_PTUN' & 'DEF_BGT_C2_PTUN' signalent des anomalies telles que le fait que les deux détecteurs ne remontent pas la même donnée.

La table suivante indique pour chaque issue, le nombre d'ouvertures observées, l'heure pour laquelle le plus grand nombre d'ouvertures ont été observées 
et les 2ème,5ème et 9ème déciles du temps d'ouverture de la porte.

.. csv-table::
   :header: Tunnels ,Issues, Nombre d'ouvertures,Heure la plus fréquente,secondes (2ème décile),secondes (5ème décile),secondes (9ème décile)
   :widths: 10, 10,15,15,15,15,15
   :width: 90%

      BAP,IS431,32,22,6,9,28
      BAP,IS432,10,0,6,9,95
      BAP,IS433,6,0,8,19,99
      BAP,IS434,5,23,7,10,174
      BAP,IS435,6,0,6,8,97
      BAP,IS436,11,0,6,8,16
      BAP,IS437,2,2,54,106,175
      BAP,IS440,5,22,8,8,14
      BAP,IS441,5,23,4,6,7
      BAP,IS443,4,22,6,13,36
      BAP,IS444,25,22,6,8,12
      BAP,IS445,12,22,4,6,9
      BDR,IS221,3,21,8,8,1044
      BDR,IS223,16,1,6,7,15
      BDR,IS224,8,21,6,8,23
      BDR,IS224A,2,22,6,7,7
      BDR,IS225,1,21,144,144,144
      BDR,IS226,1,22,4,4,4
      BDR,IS227,11,21,6,8,10
      BDR,IS228,6,22,4,4,6
      BDR,IS228A,6,22,4,4,6
      BDR,IS229,32,23,4,6,13
      BDR,IS230,2,22,5,7,9
      BDR,IS232,14,22,7,8,15
      BDR,IS236,17,21,8,10,12
      BDR,IS239,2,8,4,4,4
      BDR,IS240,8,21,4,6,6
      BDR,IS241,4,20,6,7,8
      DEF,IS102,3,12,5,7,7
      DEF,IS103A,3,17,42,57,2382
      DEF,IS140,9,6,6,8,17
      DEF,IS147,28,8,621,806,2282
      DEF,IS148,1,20,2,2,2
      DEF,IS157,2,7,46,48,51
      LAN,IS370,1,14,6,6,6
      RUE,IS331,5,1,3,8,30
      RUE,IS338,1,1,948,948,948
      RUE,IS341,1,1,4,4,4
      RUE,IS343,3,1,4,6,6
      RUE,IS345,2,1,6,7,7
      SCL,IS451,5,22,7,20,175
      SCL,IS452,4,2,13,20,152
      SCL,IS453,24,2,8,9,30
      SCL,IS454,28,2,4,8,94
      SCL,IS455,11,2,6,6,92
      SCL,IS456,15,23,4,8,23
      SCL,IS457,4,1,6,7,9
      SCL,IS458,7,0,4,6,8
      SCL,IS459,9,1,6,8,16
      SCL,IS460,25,5,6,6,14
      SCL,IS461,4,1,6,6,7
      SCL,IS462,4,1,5,6,6
      SCL,IS463,5,1,6,10,61




