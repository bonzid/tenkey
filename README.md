 # T9 text converter

Ce script Python convertit un texte en séquence de touches T9 (clavier de téléphone) et inversement.

## Fonctionnalités

- `txt_to_tenkey(text)` : convertit une chaîne de texte (sans accents ni majuscules) en une séquence T9
- `tenkey_to_text(sequence)` : convertit une séquence T9 en texte lisible
- Gestion automatique des accents et caractères spéciaux

## Exemple d'utilisation

```python
txt="Qui me reflète sinon toi-même"
encoded=txt_to_tenkey(txt)
decoded=tenkey_to_text(encoded)

print(f"Original : {txt}")
print(f"Encoded : {encoded}")
print(f"Decoded : {decoded}")
```

Résultats attendus :

```
Original : Qui me reflète sinon toi-même
Encoded : 7777 88 444 0 6 33 0 777 33 333 8 0 7777 66 7777 33 0 8 666 444 0 6 33 7777 63
Decoded : qui me reflete sinon toi-meme
```
