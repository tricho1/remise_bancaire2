# Modificateur de fichier MT101

Ce script Python permet de modifier un fichier bancaire au format MT101 en ajoutant des caractères ASCII spécifiques au début et à la fin du fichier.

## Utilisation

1. Placez votre fichier MT101 dans le même répertoire que le script
2. Modifiez les variables `input_file` et `output_file` dans le script selon vos besoins
3. Exécutez le script avec Python

## Caractères ASCII ajoutés

- Début du fichier : `SOH` (Start of Heading)
- Fin du fichier : `STX` (Start of Text)

## Exemple d'utilisation

```python
python mt101_modifier.py
```

Le script créera un nouveau fichier avec les caractères ASCII ajoutés.
