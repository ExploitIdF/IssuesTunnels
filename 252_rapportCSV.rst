Spécification du format des rapports pour les visites bimestrielles et les interventions de maintenance annuelle dans les issues.
**************************************************************************************************************************************
La spécification des actions à mener et du contenu des rapports doit être réalisée par ailleurs. 
Dans cette page, on utilisera une hypothèse sur la nature des informations demandées; 
cette hypothèse a été construite sur la base du modèle de rapport annexé au CCTP de 2020.
Les points qui auront été décidés viendront plus tard remplacer l'hypothèse utilisée ici.

Le modèle de rapport prévoit que le prestataire renseigne 80 champs pour chaque issue, sans compter les 
champs de commentaires que le prestataire devrait remplir quand l'évaluation est mauvaise.

Le modèle comporte 3 types de champs :

* Evaluation réalisée de jour (23)
* Evaluation réalisée de nuit (9)
* Constat de la réalisation d'actions de maintenance (47: contrôle, réglage, nettoyage, graissage ...)

Les évaluations prennent les valeurs :

.. csv-table::
   :header: Valeur,Code
   :widths: 30,10
   :width: 40%

     OK		,          1
     Défaut mineur,		0,5
     Défaut majeur,		0
     Non équipé		,  NE
     Non verifié	,  	NV

Les constats prennent les valeurs :

* **A faire**	l’intervenant n’a pas encore effectué l’action d’entretien
* **Pas fait**	l’intervenant n’a pas pu effectuer l’action d’entretien
* **Fait**	l’intervenant a effectué l’action d’entretien















