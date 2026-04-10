import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    if not task.strip():
        raise ValueError("Tarefa não pode ser vazia")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    return load_tasks()

def remove_task(index):
    tasks = load_tasks()
    if index < 0 or index >= len(tasks):
        raise IndexError("Índice inválido")
    tasks.pop(index)
    save_tasks(tasks)

def main():
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        choice = input("Escolha: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            try:
                add_task(task)
                print("Tarefa adicionada!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            tasks = list_tasks()
            for i, t in enumerate(tasks):
                print(f"{i}: {t}")

        elif choice == "3":
            try:
                index = int(input("Índice da tarefa: "))
                remove_task(index)
                print("Tarefa removida!")
            except Exception as e:
                print(e)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()