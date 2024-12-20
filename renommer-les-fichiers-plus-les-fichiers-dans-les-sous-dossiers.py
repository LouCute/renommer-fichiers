import os
import random
import string
from pathlib import Path
import urllib.parse

# Configuration
ROOT_FOLDER = "./Base"  # Dossier racine contenant les fichiers à renommer
EXCLUDED_EXTENSIONS = {".py", ".png"}  # Extensions de fichiers à exclure du renommage
LOG_FILE = "rename_log.md"  # Nom du fichier de log

# Fonction pour générer un nom aléatoire
def generate_random_name(extension):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + extension

# Fonction pour convertir un chemin Windows en URI cliquable
def path_to_uri(path):
    resolved_path = str(path.resolve()).replace("\\", "/")  # Corrige les barres obliques
    return f"file:///{urllib.parse.quote(resolved_path)}"



# Fonction pour écrire les logs dans un fichier Markdown avec mise en forme
def log_action(message, code_block=False):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        if code_block:
            log_file.write(f"```\n{message}\n```\n")
        else:
            log_file.write(message + "\n")

# Fonction pour renommer les fichiers
def rename_files(root_folder, excluded_extensions):
    # Effacer le fichier de log précédent si nécessaire
    if Path(LOG_FILE).exists():
        Path(LOG_FILE).unlink()
    
    # Écrire un titre dans le fichier de log
    log_action("# Journal de renommage des fichiers\n", code_block=False)

    for root, _, files in os.walk(root_folder):
        for file in files:
            file_path = Path(root) / file
            # Vérifier si l'extension du fichier est dans la liste des exclusions
            if file_path.suffix.lower() in excluded_extensions:
                message = f"- **Exclu du renommage** : [{file_path.name}]({path_to_uri(file_path)}) (extension `{file_path.suffix}`)"
                print(message)
                log_action(message, code_block=False)
                continue

            # Obtenir l'extension du fichier
            extension = file_path.suffix.lower()
            new_name = generate_random_name(extension)
            new_file_path = file_path.with_name(new_name)
            
            # Vérifier si le nouveau nom existe déjà
            if new_file_path.exists():
                message = f"- ⚠️ Le nom `{new_name}` existe déjà, passage au suivant."
                print(message)
                log_action(message, code_block=True)
                continue
            
            # Renommer le fichier
            file_path.rename(new_file_path)
            message = f"- ✅ Renommé : [{file_path.name}]({path_to_uri(file_path)}) → [{new_file_path.name}]({path_to_uri(new_file_path)})"
            print(message)
            log_action(message, code_block=False)

if __name__ == "__main__":
    rename_files(ROOT_FOLDER, EXCLUDED_EXTENSIONS)
