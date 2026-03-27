import json
import os

# Fichier pour la mémoire
MEMORY_FILE = "memory.json"

# Charger la mémoire si elle existe
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Sauvegarder la mémoire
def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)

# Fonction principale du chatbot
def chatbot():
    print("🤖 Mini-IA activée ! (tape 'quit' pour sortir)\n")
    memory = load_memory()

    while True:
        user_input = input("👤 Toi : ").strip().lower()

        if user_input == "quit":
            print("🤖 IA : À bientôt !")
            save_memory(memory)
            break

        # Exemple : IA se souvient du nom
        if "je m'appelle" in user_input:
            name = user_input.replace("je m'appelle", "").strip()
            memory["name"] = name
            print(f"🤖 IA : Enchanté {name} ! Je m'en souviendrai.")
            continue

        # l'IA répond si elle connaît le nom
        if "mon nom" in user_input or "qui suis-je" in user_input:
            if "name" in memory:
                print(f"🤖 IA : Tu t'appelles {memory['name']} 😎")
            else:
                print("🤖 IA : Tu ne m’as pas encore dit ton nom.")
            continue

        # Réponses simples par mots-clés
        if "bonjour" in user_input:
            print("🤖 IA : Bonjour ! Comment ça va ?")
        elif "ça va" in user_input:
            print("🤖 IA : Moi aussi ça va bien 😁")
        elif "merci" in user_input:
            print("🤖 IA : Avec plaisir !")
        elif "tu fais quoi" in user_input:
            print("🤖 IA : Je discute avec toi et j’apprends 😎")
        elif "au revoir" in user_input:
            print("🤖 IA : À bientôt ! 👋")
        elif "tu fais quoi" in user_input:
            print("🤖 IA : Je discute avec toi et j’apprends 😎")
        elif "au revoir" in user_input:
            print("🤖 IA : À bientôt ! 👋")
        else:
            print("🤖 IA : Je n'ai pas encore appris à répondre à ça...")
        
        # Sauvegarder la mémoire à chaque échange
        save_memory(memory)


if __name__ == "__main__":
    chatbot()
