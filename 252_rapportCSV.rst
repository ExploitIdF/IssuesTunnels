Spécification du format des rapports pour les visites bimestrielles et les interventions de maintenance annuelle dans les issues.
**************************************************************************************************************************************
La spécification des actions à mener et du contenu des rapports doit être réalisée par ailleurs. 
Dans cette page, on utilisera une hypothèse sur la nature des informations demandées; 
cette hypothèse a été construite sur la base du modèle de rapport annexé au CCTP de 2020.
Les points qui auront été décidés viendront plus tard remplacer l'hypothèse utilisée ici.

Le modèle de rapport prévoit que le prestataire renseigne 80 champs pour chaque issue, sans compter les 
champs de commentaires que le prestataire devrait remplir quand l'évaluation est mauvaise. La liste de ces champs est fournie ci-dessous avec un code à 5 caractère.

Le modèle comporte 3 types de champs :

* Evaluation réalisée de jour (23)
* Evaluation réalisée de nuit (9)
* Constat de la réalisation d'actions de maintenance (47: contrôle, réglage, nettoyage, graissage ...)

Les évaluations prennent les 5 valeurs :

.. csv-table::
   :header: Valeur,Code
   :widths: 30,10
   :width: 40%

     OK,  1
     Défaut mineur, 0.5
     Défaut majeur,	0
     Non équipé, NE
     Non verifié, NV

Les constats prennent les 3 valeurs :

.. csv-table::
   :header: Valeur,Code
   :widths: 30,10
   :width: 40%

      L’intervenant n’a pas encore effectué l’action d’entretien,**A faire**	
      L’intervenant n’a pas pu effectuer l’action d’entretien,**Pas fait**
      L’intervenant a effectué l’action d’entretien,**Fait**

Le fichier CSV de reporting comporte les champs suivants :

.. csv-table::
   :header: Valeur,Code,Contrôle
   :widths: 40,10,20
   :width: 60%

      Code de l'issue (ISNNN | ISNNNA) , CodeIssue,Prend d'une des 290 valeurs possibles
      Horodate de la saisie de l'information sur le terrain, Horodate,Respect du format "%Y/%M/%D %H:%M:%S"
      Code du champ considéré,CodeChamp, Prend l'une des 79 valeurs possibles
      Valeur du champ  considéré,Valeur,Prend l'une des 3 ou 5 valeurs possibles selon le champs
      Commentaire en texte libre en cas d'anomlie,Commentaire,Texte libre compatible avec le format CSV
      Nom et prénom de la personne qui réalise l'observation ou l'acton, NomTech,Respect du format texte avec au moins 2 mots


**Liste des champs figurant dans le modèle de rapport du marché Batiment 2020, avec les codes qui ont été associés pour identifier les champs dans le fichier CSV.**


.. csv-table::
   :header: Code,Type,Famille,Item
   :widths: 10,20,20,50
   :width: 90%      
      
      EVJ01,Evaluation Jour,Huisseries,Porte Tunnel
      EVJ02,Evaluation Jour,Huisseries,Porte SAS
      EVJ03,Evaluation Jour,Huisseries,Porte Haute
      EVJ04,Evaluation Jour,Huisseries,Portail ou portillon Extérieure
      EVJ05,Evaluation Jour,Eclairage et Alimentation,Eclairage permanent (LED)
      EVJ06,Evaluation Jour,Eclairage et Alimentation,Eclairage renforcé (fluo)
      EVJ07,Evaluation Jour,Eclairage et Alimentation,Eclairage extérieur
      EVJ08,Evaluation Jour,Eclairage et Alimentation,Pictogramme CE30
      EVJ09,Evaluation Jour,Accessibilité et Sécurité,Accessibilité extérieure
      EVJ10,Evaluation Jour,Accessibilité et Sécurité,Signalisation extérieure de l’issue
      EVJ11,Evaluation Jour,Accessibilité et Sécurité,Vacuité dans l’issue
      EVJ12,Evaluation Jour,Accessibilité et Sécurité,Propreté de l’issue
      EVJ13,Evaluation Jour,Accessibilité et Sécurité,Visibilité de la statique (main courante et panneaux)
      EVJ14,Evaluation Jour,Accessibilité et Sécurité,Surpression (si issue équipée)
      EVJ15,Evaluation Jour,Accessibilité et Sécurité,Dégradation et accessibilité des PST
      EVJ16,Evaluation Jour,Capteurs – Communication,Téléphone de SEcurité
      EVJ17,Evaluation Jour,Capteurs – Communication,Caméra dans l’issue
      EVJ18,Evaluation Jour,Capteurs – Communication,Détecteurs de présence
      EVJ19,Evaluation Jour,GTC,Remontée GTC Ouverture porte (Tunnel)
      EVJ20,Evaluation Jour,GTC,Remontée GTC Intrusion en issue (Haute)
      EVJ21,Evaluation Jour,GTC,Remontée GTC Détection de présence en IS
      EVJ22,Evaluation Jour,GTC,Remontée GTC Visualisation de la caméra en IS
      EVJ23,Evaluation Jour,GTC,Défaut(s) présent(s) à la GTC
      ACT01,Action,Huisseries Porte Tunnel,"Fonctionnement des portes coupe-feu, avec réglage de fermeture"
      ACT02,Action,Huisseries Porte Tunnel,Vérification de l’état des différents éléments constitutifs (panneaux et calfeutrements)
      ACT03,Action,Huisseries Porte Tunnel,nettoyage des parements inox des vantaux effectué avec un chiffon doux imbibé d’un produit non corrosif
      ACT04,Action,Huisseries Porte Tunnel,"graissage des gonds, serrures et toutes les parties métalliques en mouvement"
      ACT05,Action,Huisseries Porte Tunnel,Essais des organes de commande sensibles aux manifestations d’incendie
      ACT06,Action,Huisseries Porte Tunnel,Établissement d’un rapport relatif aux anomalies qui auraient pu être décelées
      ACT07,Action,Huisseries Porte Tunnel,"Vérification de l’état mécanique (corrosion, chocs éventuels, serrage…) des pièces suivantes : pivot, roulement, ferme-porte et bras, serrures, sélecteurs de vantaux…"
      ACT08,Action,Huisseries Porte Tunnel,Vérification du système de détection et de déclenchement
      ACT09,Action,Huisseries Porte Tunnel,Vérification la présence et l’état des liaisons électriques et détecteurs et des déclencheurs
      ACT10,Action,Huisseries Porte Tunnel,Test de fonctionnement par détection et déclenchement automatique
      ACT11,Action,Huisseries Porte Tunnel,Contrôle de l’alignement du capteur avec la porte et le cadre
      ACT12,Action,Huisseries Porte Tunnel,Vérification temps de fermetures de la porte en moins de 30 secondes
      ACT13,Action,Huisseries Porte Extérieur,"Fonctionnement des portes coupe-feu, avec réglage de fermeture"
      ACT14,Action,Huisseries Porte Extérieur,Vérification de l’état des différents éléments constitutifs (panneaux et calfeutrements)
      ACT15,Action,Huisseries Porte Extérieur,nettoyage des parements inox des vantaux effectué avec un chiffon doux imbibé d’un produit non corrosif
      ACT16,Action,Huisseries Porte Extérieur,"graissage des gonds, serrures et toutes les parties métalliques en mouvement"
      ACT17,Action,Huisseries Porte Extérieur,Essais des organes de commande sensibles aux manifestations d’incendie
      ACT18,Action,Huisseries Porte Extérieur,Établissement d’un rapport relatif aux anomalies qui auraient pu être décelées
      ACT19,Action,Huisseries Porte Extérieur,"Vérification de l’état mécanique (corrosion, chocs éventuels, serrage…) des pièces suivantes : pivot, roulement, ferme-porte et bras, serrures, sélecteurs de vantaux…"
      ACT20,Action,Huisseries Porte Extérieur,Vérification du système de détection et de déclenchement
      ACT21,Action,Huisseries Porte Extérieur,Vérification la présence et l’état des liaisons électriques et détecteurs et des déclencheurs
      ACT22,Action,Huisseries Porte Extérieur,Test de fonctionnement par détection et déclenchement automatique
      ACT23,Action,Huisseries Porte Extérieur,Contrôle de l’alignement du capteur avec la porte et le cadre
      ACT24,Action,Huisseries Porte Extérieur,Vérification temps de fermetures de la porte en moins de 30 secondes
      ACT25,Action,Huisseries Porte Sas,"Fonctionnement des portes coupe-feu, avec réglage de fermeture"
      ACT26,Action,Huisseries Porte Sas,Vérification de l’état des différents éléments constitutifs (panneaux et calfeutrements)
      ACT27,Action,Huisseries Porte Sas,nettoyage des parements inox des vantaux effectué avec un chiffon doux imbibé d’un produit non corrosif
      ACT28,Action,Huisseries Porte Sas,"graissage des gonds, serrures et toutes les parties métalliques en mouvement"
      ACT29,Action,Huisseries Porte Sas,Essais des organes de commande sensibles aux manifestations d’incendie
      ACT30,Action,Huisseries Porte Sas,Établissement d’un rapport relatif aux anomalies qui auraient pu être décelées
      ACT31,Action,Huisseries Porte Sas,"Vérification de l’état mécanique (corrosion, chocs éventuels, serrage…) des pièces suivantes : pivot, roulement, ferme-porte et bras, serrures, sélecteurs de vantaux…"
      ACT32,Action,Huisseries Porte Sas,Vérification du système de détection et de déclenchement
      ACT33,Action,Huisseries Porte Sas,Vérification la présence et l’état des liaisons électriques et détecteurs et des déclencheurs
      ACT34,Action,Huisseries Porte Sas,Test de fonctionnement par détection et déclenchement automatique
      ACT35,Action,Huisseries Porte Sas,Contrôle de l’alignement du capteur avec la porte et le cadre
      ACT36,Action,Huisseries Porte Sas,Vérification temps de fermetures de la porte en moins de 30 secondes
      ACT37,Action,Eclairage et Alimentation,contrôle de l’éclairage normal et de sécurité
      ACT38,Action,Eclairage et Alimentation,contrôle et essai de l’éclairage de sécurité
      ACT39,Action,Accessibilité et Sécurité,vérification de la vacuité de l’issue
      ACT40,Action,Accessibilité et Sécurité,Vérification de la présence des panneaux d’évacuation
      ACT41,Action,Accessibilité et Sécurité,contrôle main courante
      ACT42,Action,Accessibilité et Sécurité,contrôle de l’état extérieur des armoires électriques
      ACT43,Action,Accessibilité et Sécurité,contrôle de fonctionnement de la surpression
      ACT44,Action,Capteurs – Communication,contrôle et essai du téléphone de sécurité
      ACT45,Action,Capteurs – Communication,contrôle du fonctionnement du capteur de présence
      ACT46,Action,Capteurs – Communication,contrôle de fonctionnement de la caméra
      ACT47,Action,GTC,"Vérification des remontées d’information vers le PCTT (capteurs de portes, fonctionnement surpression, présence, caméra, téléphone de sécurité)"
      EVN01,Evaluation Nuit,Signalisation,Plots de jalonnement
      EVN02,Evaluation Nuit,Signalisation,Chevrons
      EVN03,Evaluation Nuit,Signalisation,Capotage + tri-flash
      EVN04,Evaluation Nuit,Signalisation,CE30
      EVN05,Evaluation Nuit,Signalisation,"Présence et visibilité de la statique (DP2a/b, issue en face)"
      EVN06,Evaluation Nuit,Signalisation,Défaut(s) présent(s) à la GTC
      EVN07,Evaluation Nuit,Sonorisation,Sirene
      EVN08,Evaluation Nuit,Sonorisation,Balises sonores
      EVN09,Evaluation Nuit,PST en Tunnel,Dégradation et accessibilité des PST












