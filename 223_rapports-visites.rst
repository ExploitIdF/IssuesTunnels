Rapport des visites bimestrielles des issues de secours 
#############################################################
Objectifs
*************************
Pour cette nouvelle prestation, le DETT a choisi de demander au prestataire un rapport dématérialisé.

Pour le succés de cet objectif, il faut prévoir plusieurs actions :

* Rédaction (dans le CCTP) des spécifications des rapports demandés, de leur mode de production et de transmission
* Rédaction dans le RdC de ce que les candidats doivent indiquer dans leur offre à ce sujet
* Developpement par le DETT du SI pour l'aquisition des rapports, le traitement des données et leur restitution pour les PCTT.
* Developpement par le titulaire de l'application de saisie des informations nécessaires et de transmission. L'application fonctionnera sur un terminal mobile (Smartphone ou tablette) dont seront équipés les intervenants.

Spécification du reporting
****************************
Saisie et transmission
=======================
Pour la saisie des données alimentant le reporting, l'intervenant qui effectue la visite d'une issue sera muni d'un terminal informatique. Si plusieurs agents visitent parallèlement des issues de la même fermeture, chacun de ces agents devra être équipé d'un terminal pour que les saisies soient réalisées in-situ.

Pour chaque issue, un rapport sera enregistré par l'agent et transmis par l'application, dès la fin de la visite de l'issue. 

Le serveur DiRIF fera un enregistrement du rapport et enverra un accusé de réception dans lequel seront mentionnés les résultats des contrôles effectués.

Si l'accusé de réception signale une anomalie que l'agent peut corriger, celui-ci pourra envoyer un nouveau rapport corrigé.

Information à enregistrer
===========================
Un rapport est produit pour chaque issue visitée.

Le rapport porte sur les 6 éléments suivants :

* Porte Tunnel (Première porte depuis le tunnel vers l'issue) 
* Porte Exterieure (Porte de l'issue vers l'extérieur c'est à dire à l'air libre)
* PorteInterieure (La ou les portes intermédiaires)
* Proprete (Il s'agit de signaler la présence initiale de détritus ou de salissures notables et de mentionner, si le défaut a pu être corrigé pendant la visite, les actions réalisées par l'intervenant et les actions éventuellement nécessaire pour corriger le défaut)
* Vacuite (Il s'agit de signaler si des objets gênent le passage, si le défaut a pu être corrigé pendant la visite, les actions réalisées par l'intervenant et les actions éventuellement nécessaire pour corriger le défaut)
* Eclairage (Etat de fonctionnement des dispositifs d'éclairage à l'intérieur de l'issue)

Pour chaque élément, une note est attribuée : 0(HS) ,1 (Défaut) ,2(OK)

La note 0 doit être donnée si le défaut supprime une fonction essentielle de l'élément et si l'agent n'a pas pu rétablir la fonction pendant la visite.
Cette note signifie qu'une action corrective devra être programmée à court terme.

La note 1 doit être donnée si un défaut notable a été constaté et l'agent a pu rétablir pendant la visite les fonctions essentielles éventuellement altérées.

La note 2 doit être donnée si aucun défaut notable n'a été constaté.

Pour chaque élément, un commentaire est enregistré pour expliquer les notes 0 ou 1.

Le commentaire décrit le défaut constaté, il indique les actions réalisées par l'agent pendant la visite et il décrit l'état de l'élément suite à la visite.

Format du fichier transmis
===========================
la syntaxe exacte est décrite ci-dessous. 
La conformité à cette spécification sera vérifiée et conditionnera le constat de la prestation.

.. code-block:: 

  {
    "horodate":"<yy/mm/dd HH:MM>",
    "code_issue":"ISNNNX",
    "nom_intervenant":"<nom_intervenant>"
    "PorteTunnelNote":"N" , "PorteExterieureNote":"N", "PorteInterieureNote":"N", "PropreteNote":"N", "VacuiteNote":"N" , "EclairageNote":"N"
    "PorteTunnelCom":"<Commentaire (<1000 caractères)>",
    "PorteExterieureCom":"<Commentaire (<1000 caractères)>",
    "PorteInterieureCom":"<Commentaire (<1000 caractères)>",
    "PropreteCom":"<Commentaire (<1000 caractères)>",
    "VacuiteCom":"<Commentaire (<1000 caractères)>",
    "EclairageCom":"<Commentaire (<1000 caractères)>"
  }












