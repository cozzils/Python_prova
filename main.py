# Lista per memorizzare i task
task_list = []

# Funzione per aggiungere un task
def aggiungi_task(descrizione):
    task_list.append(descrizione)
    print(f"Task '{descrizione}' aggiunto!")

# Funzione per visualizzare i task
def visualizza_task():
    if not task_list:
        print("Nessun task presente.")
    else:
        print("Lista dei task:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

# Funzione per rimuovere un task
def rimuovi_task(indice):
    if 1 <= indice <= len(task_list):
        task_rimosso = task_list.pop(indice - 1)
        print(f"Task '{task_rimosso}' rimosso!")
    else:
        print("Indice non valido.")

# Menu principale
while True:
    print("\n--- Gestione Task ---")
    print("1. Aggiungi task")
    print("2. Visualizza task")
    print("3. Rimuovi task")
    print("4. Esci")

    scelta = input("Scegli un'opzione (1-4): ")

    if scelta == "1":
        descrizione = input("Inserisci la descrizione del task: ")
        aggiungi_task(descrizione)
    elif scelta == "2":
        visualizza_task()
    elif scelta == "3":
        visualizza_task()
        indice = int(input("Inserisci il numero del task da rimuovere: "))
        rimuovi_task(indice)
    elif scelta == "4":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida. Riprova.")
