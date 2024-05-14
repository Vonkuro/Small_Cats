#!/bin/bash

# Chemin vers le fichier texte contenant le numéro de version
version_file="version.txt"

# Fonction pour incrémenter le numéro de version
increment_version() {
    # Vérifie si le fichier existe
    if [ ! -f "$version_file" ]; then
        # Si le fichier n'existe pas, créez-le avec la valeur 0.0.0.0
        echo "0.0.0.0" > "$version_file"
    fi

    # Lit la valeur actuelle du numéro de version depuis le fichier
    current_version=$(<"$version_file")

    # Décompose le numéro de version en ses parties X, Y, Z et W
    IFS='.' read -ra version_parts <<< "$current_version"
    X=${version_parts[0]}
    Y=${version_parts[1]}
    Z=${version_parts[2]}
    W=${version_parts[3]}

    # Incrémente la partie correspondant à la branche actuelle
    case "$current_branch" in
        "master")
            ((X++))
            ;;
        "preprod")
            ((Y++))
            ;;
        "recette")
            ((Z++))
            ;;
        "develop")
            ((W++))
            ;;
        *)
    esac

    # Réassemble le numéro de version mis à jour
    updated_version="$X.$Y.$Z.$W"

    # Écrit la nouvelle valeur du numéro de version dans le fichier
    echo "$updated_version" > "$version_file"

    # Affiche un message
    echo "Numéro de version incrémenté à $updated_version"
}

# Récupère le nom de la branche actuelle
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Incrémente le numéro de version en fonction de la branche actuelle
increment_version