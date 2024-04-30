# Task manager in python for bad coding habits

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tâche '{task.name}' ajoutée avec succès.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Tâche '{task_name}' supprimée avec succès.")
                return
        print(f"Tâche '{task_name}' non trouvée.")

    def list_tasks(self):
        if self.tasks:
            print("Liste des tâches :")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.name} - Priorité: {task.priority} - Complété: {'Oui' if task.completed else 'Non'}")
        else:
            print("Aucune tâche enregistrée.")

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_completed()
                print(f"Tâche '{task_name}' marquée comme complétée.")
                return
        print(f"Tâche '{task_name}' non trouvée.")

def display_menu():
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme complétée")
    print("4. Afficher la liste des tâches")
    print("5. Quitter")

task_manager = TaskManager()

while True:
    display_menu()
    try:
        choice = int(input("Choisissez une option : ")) # Mauvaise pratique : ne traite pas les erreurs de conversion
    except:
        print("Option invalide. Veuillez choisir une option valide.")
        continue
    
    if choice == 1:
        name = input("Nom de la tâche : ")
        description = input("Description de la tâche : ")
        priority = input("Priorité de la tâche (Haute/Moyenne/Basse) : ")
        task = Task(name, description, priority)
        task_manager.add_task(task)

    elif choice == 2:
        task_name = input("Nom de la tâche à supprimer : ")
        task_manager.remove_task(task_name)

    elif choice == 3:
        task_name = input("Nom de la tâche à marquer comme complétée : ")
        task_manager.mark_task_as_completed(task_name)

    elif choice == 4:
        task_manager.list_tasks()

    elif choice == 5:
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
