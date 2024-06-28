Données GTC des portes en tunnel
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

La redondance des capteurs confère de la robustesse à l'information.

Les enregistrements dont var4 == 'ETA_ACCES_TUN', rendent compte:

* des ouvertures (Evenement == 'Transition à 1')
* des fermetures (Evenement == 'Transition à 0')
