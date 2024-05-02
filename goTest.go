package main

import (
    "fmt"
    "os"
)

// Structure pour représenter une tâche
type Task struct {
    ID   int
    Name string
}

// Structure pour le gestionnaire de tâches
type TaskManager struct {
    tasks []*Task
}

// Fonction pour ajouter une tâche
func (tm *TaskManager) AddTask(name string) {
    task := &Task{
        ID:   len(tm.tasks) + 1,
        Name: name,
    }
    tm.tasks = append(tm.tasks, task)
    fmt.Printf("Tâche ajoutée: %s\n", task.Name)
}

// Fonction pour supprimer une tâche
func (tm *TaskManager) RemoveTask(id int) {
    for i, task := range tm.tasks {
        if task.ID == id {
            tm.tasks = append(tm.tasks[:i], tm.tasks[i+1:]...)
            fmt.Printf("Tâche supprimée: %s\n", task.Name)
            return
        }
    }
    fmt.Println("Tâche non trouvée.")
}

// Fonction pour lister toutes les tâches
func (tm *TaskManager) ListTasks() {
    fmt.Println("Liste des tâches:")
    for _, task := range tm.tasks {
        fmt.Printf("%d. %s\n", task.ID, task.Name)
    }
}

func main() {
    taskManager := TaskManager{}

    for {
        fmt.Println("\nMenu:")
        fmt.Println("1. Ajouter une tâche")
        fmt.Println("2. Supprimer une tâche")
        fmt.Println("3. Lister les tâches")
        fmt.Println("4. Quitter")

        var choice int
        fmt.Print("Choix: ")
        fmt.Scanln(&choice)

        switch choice {
        case 1:
            fmt.Print("Nom de la tâche: ")
            var name string
            fmt.Scanln(&name)
            taskManager.AddTask(name)
        case 2:
            fmt.Print("ID de la tâche à supprimer: ")
            var id int
            fmt.Scanln(&id)
            taskManager.RemoveTask(id)
        case 3:
            taskManager.ListTasks()
        case 4:
            fmt.Println("Au revoir !")
            os.Exit(0)
        default:
            fmt.Println("Choix invalide.")
        }
    }
}

