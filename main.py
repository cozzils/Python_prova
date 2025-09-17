Lista_obbietivi = []

def aggiungi_obbiettivo(obbiettivo):
    Lista_obbietivi.append(obbiettivo)
    print(f"Obbiettivo '{obbiettivo}' aggiunto.")

def visualizza_target():
    if not Lista_obbietivi:
        print("Nessun obbiettivo presente.")
    else:
        print("Lista degli obbiettivi:")
        for idx, obbiettivo in enumerate(Lista_obbietivi, start=1):
            print(f"{idx}. {obbiettivo}")
        
def rimuovi_obbiettivo(obbiettivo):
    if obbiettivo in Lista_obbietivi:
        Lista_obbietivi.remove(obbiettivo)
        print(f"Obbiettivo '{obbiettivo}' rimosso.")
    else:
        print(f"Obbiettivo '{obbiettivo}' non trovato.")

while True:
    print("\nMenu:")
    print("1. Aggiungi obbiettivo")
    print("2. Visualizza obbiettivi")
    print("3. Rimuovi obbiettivo")
    print("4. Esci")
    
    scelta = input("Scegli un'opzione (1-4): ")
    
    if scelta == '1':
        obbiettivo = input("Inserisci il nuovo obbiettivo: ")
        aggiungi_obbiettivo(obbiettivo)
    elif scelta == '2':
        visualizza_target()
    elif scelta == '3':
        obbiettivo = input("Inserisci l'obbiettivo da rimuovere: ")
        rimuovi_obbiettivo(obbiettivo)
    elif scelta == '4':
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida. Riprova.")

