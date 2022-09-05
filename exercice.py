#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouveau_mot = ''
    for lettre in mot:
        lettre_ascii = ord(lettre)
        if 97 <= lettre_ascii <= 122 or 224 <= lettre_ascii <= 253:
            nouveau_mot += chr(lettre_ascii - 32)
        else:
            nouveau_mot += lettre
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
