import os
import random
import string
from pathlib import Path

# Configuration
ROOT_FOLDER = "./Base"  # Dossier racine contenant les fichiers à renommer
EXCLUDED_EXTENSIONS = {".jpg", ".png"}  # Extensions de fichiers à exclure du renommage
LOG_FILE = "rename_log.md"  # Nom du fichier de log

# Fonction pour générer un nom aléatoire
def generate_random_name(extension):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + extension

# Fonction pour écrire les logs dans un fichier
def log_action(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

# Fonction pour renommer les fichiers dans le dossier racine uniquement
def rename_files_in_root(root_folder, excluded_extensions):
    root_path = Path(root_folder)
    if not root_path.is_dir():
        error_message = f"Le dossier racine {root_folder} n'existe pas ou n'est pas un dossier valide."
        print(error_message)
        log_action(error_message)
        return

    # Effacer le fichier de log précédent si nécessaire
    if Path(LOG_FILE).exists():
        Path(LOG_FILE).unlink()

    log_action("# Journal de renommage des fichiers\n")

    for file in root_path.iterdir():
        # Vérifier si c'est un fichier (ignorer les dossiers)
        if file.is_file():
            # Vérifier si l'extension du fichier est dans la liste des exclusions
            if file.suffix.lower() in excluded_extensions:
                message = f"Exclu du renommage (extension {file.suffix}): {file}"
                print(message)
                log_action(f"- {message}")
                continue

            # Obtenir l'extension du fichier
            extension = file.suffix.lower()
            new_name = generate_random_name(extension)
            new_file_path = file.with_name(new_name)

            # Vérifier si le nouveau nom existe déjà
            if new_file_path.exists():
                message = f"Le nom {new_name} existe déjà, passage au suivant."
                print(message)
                log_action(f"- {message}")
                continue

            # Renommer le fichier
            file.rename(new_file_path)
            message = f"Renommé {file} en {new_file_path}"
            print(message)
            log_action(f"- {message}")
        else:
            message = f"Ignoré (pas un fichier): {file}"
            print(message)
            log_action(f"- {message}")

if __name__ == "__main__":
    rename_files_in_root(ROOT_FOLDER, EXCLUDED_EXTENSIONS)
