Rapport des visites bimestrielles des issues de secours 
#############################################################
Objectifs
*************************
Pour les visites bimestrielles des issues de secours qui sont une nouvelle prestation introduite dans le marché Bâtiment, le DETT a choisi de demander au prestataire 
de produire *en temps réel* un rapport dématérialisé pour chaque issue visitée.

Pour le succès de cet objectif, il faut examiner les implications pour les parties concernées et prévoir plusieurs actions :

* Rédaction (dans le CCTP) des spécifications des rapports demandés, de leur mode de production et de transmission
* Rédaction dans le RdC de ce que les candidats doivent indiquer dans leur offre à ce sujet
* Elaboration des outils pour la formation des TDM
* Développement par le DETT du SI pour l’acquisition des rapports, le traitement des données et leur restitution pour les PCTT.
* Developpement par le titulaire de l'application de saisie des informations nécessaires et de transmission. L'application fonctionnera sur un terminal mobile (Smartphone ou tablette) dont seront équipés les intervenants.

Spécification du reporting
****************************
Saisie et transmission
=======================
Pour la saisie des données alimentant le reporting, l'intervenant qui effectue la visite d'une issue sera muni d'un terminal informatique (smartphone ou tablette). 
Si plusieurs agents visitent parallèlement des issues de la même fermeture, chacun de ces agents devra être équipé d'un terminal pour que les saisies soient réalisées in-situ.

Pour chaque issue, un rapport sera enregistré par l'agent et transmis par l'application, dès la fin de la visite de l'issue. 

Le serveur DiRIF fera un enregistrement du rapport et enverra un accusé de réception dans lequel seront mentionnés les résultats des contrôles effectués.

Si l'accusé de réception signale une anomalie que l'agent peut corriger, celui-ci pourra envoyer un nouveau rapport corrigé.

Information à enregistrer lors de la visite
=============================================
Un fichier est produit pour chaque issue visitée.

Le rapport porte sur les 6 éléments suivants :

* Porte Tunnel (Première porte depuis le tunnel vers l'issue) 
* Porte Extérieure (Porte de l'issue vers l'extérieur c'est à dire à l'air libre)
* Porte Intérieure (La ou les portes intermédiaires)
* Proprete (Il s'agit de signaler la présence initiale de détritus ou de salissures notables et de mentionner, si le défaut a pu être corrigé pendant la visite, les actions réalisées par l'intervenant et les actions éventuellement nécessaire pour corriger le défaut)
* Vacuite (Il s'agit de signaler si des objets gênent le passage, si le défaut a pu être corrigé pendant la visite, les actions réalisées par l'intervenant et les actions éventuellement nécessaire pour corriger le défaut)
* Eclairage (Etat de fonctionnement des dispositifs d'éclairage à l'intérieur de l'issue)

Pour chaque élément, une note est attribuée : 0(HS) ,1 (Défaut mineur) ,2(OK)

La note 0 doit être donnée si un défaut constaté supprime une fonction essentielle de l'élément et si l'agent n'a pas pu rétablir la fonction pendant la visite.
Cette note signifie qu'une action corrective devra être programmée à court terme.

La note 1 doit être donnée si un défaut notable a été constaté et si l'agent a pu rétablir pendant la visite les fonctions essentielles éventuellement altérées.

La note 2 doit être donnée si aucun défaut notable n'a été constaté.

Pour chaque élément, un commentaire est enregistré pour expliquer les notes 0 ou 1.

Le commentaire décrit le défaut constaté, il indique les actions réalisées par l'agent pendant la visite et il décrit l'état de l'élément suite à la visite.

Format du fichier transmis
===========================
La syntaxe exacte est décrite ci-dessous. 
La conformité à cette spécification sera vérifiée et conditionnera le constat de la prestation.

.. code-block:: 

  {
    "horodate":"<yy/mm/dd HH:MM>",
    "OT":"NNNNN",
    "Tatouage":"ISNNNX",
    "nom_intervenant":"<nom_intervenant>"
    "PorteTunnelNote":"N" , 
    "PorteExterieureNote":"N", 
    "PorteInterieureNote":"N", 
    "PropreteNote":"N", 
    "VacuiteNote":"N" , 
    "EclairageNote":"N"
    "PorteTunnelCom":"<Commentaire (<1000 caractères)>",
    "PorteExterieureCom":"<Commentaire (<1000 caractères)>",
    "PorteInterieureCom":"<Commentaire (<1000 caractères)>",
    "PropreteCom":"<Commentaire (<1000 caractères)>",
    "VacuiteCom":"<Commentaire (<1000 caractères)>",
    "EclairageCom":"<Commentaire (<1000 caractères)>"
  }

Confirmation du serveur
========================
Suite à la réception du fichier, le serveur envoie un message  a une adresse fournie par le prestataire pour confirmer la réception d'un fichier conforme ou pour signaler une anomalie dans le format du fichier.



Rédaction dans le RdC de ce que les candidats doivent indiquer dans leur offre
================================================================================
Pour démontrer leur capacité à répondre à l'attente de la DIRIF les candidats devront développer les points suivants dans leur offre:

* Description de la mise en oeuvre d'applications mobiles dans le cadre de prestations, matériels et outils logiciels utilisés, 
* Formation des agents envisagée,
* Risques anticipés et mesures de réduction des risques

Elaboration des outils pour la formation des TDM
================================================
Les TDM sont en première ligne, au contact des intervenants qui doivent produire les rapports. 
Ils doivent être en mesure d'expliquer et de justifier la nouvelle pratique.

Un guide de la mise en oeuvre des visites bimestrielles doit être rédigé à l'intention des TDM et des intervenants de l'entreprise.
Une esquisse de ce guide sera annexée au CCTP et devra être finalisé par le titulaire dans la phase d'initialisation.
Le guide développera les étapes suivantes :

* Commande des prestations par le PCTT
* Proposition par le titulaire des dates d'intervention, sur la base du calendrier des fermetures annuelles
* Validation du calendrier par le PCTT
* Information du titulaire sur les évolutions du calendrier
* Confirmation de l'intervention 15(??) jours avant
* Réalisation des visites
* Contrôle par le TDM des rapports et information du titulaire sur les anomalies éventuelles
* Transmission par le titulaire des rapports corrigés
* Validation du service fait avec éventuelles réfactions en cas d'anomalies majeures












