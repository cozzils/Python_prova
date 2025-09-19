menu = ["Margherita", "Pepperoni", "Quattro Stagioni"]
class pizzeria:
    def __init__(self, nome, Ncoperti, menu, email, telefono, indirizzo):
        self.nome = nome
        self.Ncoperti = Ncoperti 
        self.menu = menu 
        self.email = email
        self.telefono = telefono
        self.indirizzo = indirizzo

    def add_menu_item(self, pizza):
        self.menu.append(pizza)
        print(f"Pizza '{pizza}' aggiunta al menu.")




Da_mario = pizzeria("Pizzeria da Mario", 50, menu,"damario@bella", 1234567890, "Via Roma 1")
pizza = input("Inserisci il nome della pizza da aggiungere al menu: ")
Da_mario.add_menu_item(pizza)

print(f"Nome pizzeria: {Da_mario.nome} - Coperti: {Da_mario.Ncoperti} - Menu: {Da_mario.menu} - Email: {Da_mario.email} - Telefono: {Da_mario.telefono} - Indirizzo: {Da_mario.indirizzo}")

