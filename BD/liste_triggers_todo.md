# Liste des triggers qu'il faut implémenter  
## Trigers ajoutés:
- Vérification de la double existance de la liaison musicale

## Trigers à implémenter:
- Vérification que le lieu du concert ne soit pas déjà utiliser (vérif heure_début et heure_fin (heure_début + durée) du concert not in between heure_début et heure_fin des concerts qui possède le même lieu)
- Même vérification qu'au dessus mais sur les disponibilités du groupe
- Vérification des pré-inscription, ne doit pas dépasser la capacité du lieu
- Vérification du nombre de billet (COMPLEXE à cause des tickets à plusieurs jours)
- D'autres sont sur le rendu 1 de la SAE (je crois)