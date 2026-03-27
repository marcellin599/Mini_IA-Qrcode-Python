import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

# Charger la mémoire
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
    else:
        memory = {}

    # S’assurer que les clés existent
    if "tasks" not in memory:
        memory["tasks"] = []
    if "notes" not in memory:
        memory["notes"] = []
    if "hours" not in memory:
        memory["hours"] = []
    if "dates" not in memory:
        memory["dates"] = []
    if "reminders" not in memory:
        memory["reminders"] = []
    

    return memory


# Sauvegarder la mémoire
def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)

# Afficher les tâches
def show_tasks(memory):
    if memory["tasks"]:
        print("📝 Tes tâches :")
        for i, t in enumerate(memory["tasks"], 1):
            print(f"{i}. {t}")
    else:
        print("📝 Aucune tâche pour l'instant.")

# Afficher les notes
def show_notes(memory):
    if memory["notes"]:
        print("🗒 Tes notes :")
        for i, n in enumerate(memory["notes"], 1):
            print(f"{i}. {n}")
    else:
        print("🗒 Aucune note pour l'instant.")

# Ajouter une tâche
def add_task(memory, task):
    memory["tasks"].append(task)
    print(f"✅ Tâche ajoutée : {task}")

# Ajouter une note
def add_note(memory, note):
    memory["notes"].append(note)
    print(f"✅ Note ajoutée : {note}")
    
#Ajouter une heure 
def add_hour(memory, hour):
    memory["hours"].append(hour)
    print (f"✅ Heure ajoutée : {hour}")

#Afficher les heures
def show_hours(memory): 
    if memory["hours"]:
        print("🕒 Tes heures :")
        for i, h in enumerate(memory["hours"], 1):
            print(f"{i}. {h}")
    else:
        print("🕒 Aucune heure pour l'instant.")
    
#ajouter une date
def add_date(memory, date):
    memory["dates"].append(date)
    print (f"✅ Date ajoutée : {date}")
    
#Afficher les dates
def show_dates(memory):
    if memory["dates"]:
        print("📅 Tes dates :")
        for i, d in enumerate(memory["dates"],1):
            print(f"{i}. {d}")
    else:
        print("📅 Aucune date pour l'instant.")
    
#Ajouter un rappel
def add_reminder(memory, reminder): 
    memory["reminders"].append(reminder)
    print (f"✅ Rappel ajouté : {reminder}")
    
#Afficher les rappels
def show_reminders(memory):         
    if memory["reminders"]:
        print("🔔 Tes rappels :")
        for i, r in enumerate(memory["reminders"], 1):
            print(f"{i}. {r}")
    else:
        print("🔔 Aucun rappel pour l'instant.")

#

# Assistant principal
def assistant():
    print("🤖 Mini-IA Assistant activé ! (tape 'quit' pour sortir)\n")
    memory = load_memory()

    while True:
        user_input = input("👤 Que veux tu que je fasse ? : ").strip().lower()

        if user_input == "quit":
            print("🤖 IA : À bientôt !")
            save_memory(memory)
            break

        elif "ajoute tâche" in user_input or "ajouter tâche" in user_input:
            task = input("📝 Quelle tâche veux-tu ajouter ? ")
            add_task(memory, task)

        elif "liste tâches" in user_input or "mes tâches" in user_input:
            show_tasks(memory)

        elif "ajoute note" in user_input or "ajouter note" in user_input:
            note = input("🗒 Quelle note veux-tu ajouter ? ")
            add_note(memory, note)

        elif "liste notes" in user_input or "mes notes" in user_input:
            show_notes(memory)

        elif "quelle heure" in user_input or "il est quel heure heure" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🕒 Il est {now}")
        
        elif "ajoute heure" in user_input or "ajouter heure" in user_input:
            hour = input("🕒 Quelle heure veux-tu ajouter ? (format HH:MM) ")
            add_hour(memory, hour)
        
        elif "liste heures" in user_input or "mes heures" in user_input:
            show_hours(memory)
            
        elif "ajoute date" in user_input or "ajouter date" in user_input:
            date = input("📅 Quelle date veux-tu ajouter ? (format JJ/MM/AAAA) ")
            add_date(memory, date)  
            
        elif "liste dates" in user_input or "mes dates" in user_input:
            show_dates(memory)
            
        elif "ajoute rappel" in user_input or "ajouter rappel" in user_input:
            reminder = input("🔔 Quel rappel veux-tu ajouter ? ")
            add_reminder(memory, reminder)
        
        elif "liste rappels" in user_input or "mes rappels" in user_input:
            show_reminders(memory)
        
        else:
            print("🤖 IA : Je n'ai pas encore appris à répondre à ça, mais je note tes tâches et notes !")

        save_memory(memory)

if __name__ == "__main__":
    assistant()
