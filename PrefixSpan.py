from collections import defaultdict

def frequent_rec(patt, mdb):
    """
    Fonction récursive pour explorer les motifs fréquents.
    :param patt: Le motif courant.
    :param mdb: La base de motifs courante.
    """
    # Exclure le motif vide des résultats
    if patt:
        results.append((len(mdb), patt))

    # Initialiser un dictionnaire pour enregistrer les occurrences des éléments
    occurs = defaultdict(list)
    
    # Parcourir la base de motifs courante
    for (i, startpos) in mdb:
        seq = db[i]
        # Parcourir la séquence à partir de la position suivante
        for j in range(startpos + 1, len(seq)):
            l = occurs[seq[j]]
            # Vérifier si le motif courant est déjà apparu dans cette séquence
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j))

    # Explorer les motifs fréquents pour chaque nouvel élément
    for (c, newmdb) in occurs.items():
        # Vérifier si le motif a un support suffisant
        if len(newmdb) >= minsup:
            frequent_rec(patt + [c], newmdb)

# Données séquentielles d'exemple
db = [
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2],
]

# Support minimum requis pour qu'un motif soit considéré comme fréquent
minsup = 3

# Liste pour stocker les motifs fréquents
results = []

# Appel initial à la fonction récursive avec le motif vide
frequent_rec([], [(i, -1) for i in range(len(db))])

# Affichage des motifs fréquents
print("Motifs fréquents:")
for support, pattern in results:
    print(f"Motif: {pattern}, Support: {support}")
