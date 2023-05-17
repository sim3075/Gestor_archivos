
class Folder:
    def __init__(self, name:str):
        self.name = name
        self.l_child = None
        self.l_central_child = None
        self.r_central_child = None
        self.r_child = None
        self.father = None
        self.elements = 0
        self.currents = []
    

class File:
    def __init__(self, files:str):
        self.files = files
        self.archives = self.files.split(" ")
        self.archive = self.archives[0].split('.')
        self.size = self.archives[1]
        self.name = self.archive[0]
        self.extension = self.archive[1]
        self.father = None
        self.filename = self.name +"."+self.extension+" "+ self.size
        self.currents = []
        
    
    def change_name(self, name):
        self.filename = name +"."+self.extension+" "+ self.size
        


class Desktop:
    def __init__(self):
        self.root = Folder("root")
    
    def insert_folder(self, root, parent_value:str, new_value:str):
        
        if root is None:
            return

        if parent_value == root.name and isinstance(root, Folder):
            new_folder = Folder(new_value)

            if root.l_child is None:
                root.l_child = new_folder
                root.elements += 1
                root.currents.append(root.l_child)
                root.l_child.father = root
            elif root.l_central_child is None:
                root.l_central_child = new_folder
                root.elements += 1
                root.currents.append(root.l_central_child)
                root.l_central_child.father = root
            elif root.r_central_child is None:
                root.r_central_child = new_folder
                root.elements += 1
                root.currents.append(root.r_central_child)
                root.r_central_child.father = root
            elif root.r_child is None:
                root.r_child = new_folder
                root.elements += 1
                root.currents.append(root.r_child)
                root.r_child.father = root
        else:
            self.insert_folder(root.l_child, parent_value, new_value)
            self.insert_folder(root.l_central_child, parent_value, new_value)
            self.insert_folder(root.r_central_child, parent_value, new_value)
            self.insert_folder(root.r_child, parent_value, new_value)
    
    def insert_file(self, root, parent_value:str, new_value:str):
        if root is None:
            return

        if parent_value == root.name and isinstance(root, Folder):
            new_file = File(new_value)
            if root.l_child is None:
                root.l_child = new_file
                root.elements += 1
                root.currents.append(root.l_child)
                root.l_child.father = root
            elif root.l_central_child is None:
                root.l_central_child = new_file
                root.elements += 1
                root.currents.append(root.l_central_child)
                root.l_child_central.father = root
            elif root.r_central_child is None:
                root.r_central_child = new_file
                root.elements += 1
                root.currents.append(root.r_central_child)
                root.r_central_child.father = root
            elif root.r_child is None:
                root.r_child = new_file
                root.elements += 1
                root.currents.append(root.r_child)
                root.r_child.father = root
        else:
            self.insert_file(root.l_child, parent_value, new_value)
            self.insert_file(root.l_central_child, parent_value, new_value)
            self.insert_file(root.r_central_child, parent_value, new_value)
            self.insert_file(root.r_child, parent_value, new_value)
    
    def available_folder(self, root, parent_value):
        if root:
            if root.name == parent_value:
                if root.elements < 4:
                    return True
            elif root.father is not None and root.name == parent_value:
                for hermano in root.father.currents:
                    if hermano != root and hermano.name == parent_value:
                        return False
            else: 

                self.available_folder(root.l_child, parent_value)
                self.available_folder(root.l_central_child, parent_value)
                self.available_folder(root.r_central_child, parent_value)
                self.available_folder(root.r_child, parent_value)

    def modify_value_folder(self,root, old_value, new_value):
        if root.name == old_value:
            if root.father is not None:
                for hermano in root.father.currents:
                    if hermano != root and hermano.name == new_value:
                        print("Error: El nuevo valor ya está siendo utilizado por otro elemento.")
                        return

            root.name = new_value
            return

        for hijo in root.currents:
            self.modify_value_folder(hijo, old_value, new_value)
    
    def modify_value_file(self,root, old_value, new_value):
        if root:
            if isinstance(root, File):
                if root.filename == old_value:
                    root.filename = new_value
                    return True

            self.modify_value_file(root.l_child, old_value, new_value)
            self.modify_value_file(root.l_central_child, old_value, new_value)
            self.modify_value_file(root.r_central_child, old_value, new_value)
            self.modify_value_file(root.r_child, old_value, new_value)
    
    def all_folder(self, root, greater):
        #print(greater)
        if root is None:
            return
        
        if isinstance(root, Folder):
            if root.r_child is not None:
                if root.r_child.elements >=0:
                    greater.append(root.r_child)
                    self.all_folder(root.r_child, greater)
                
            if root.r_central_child is not None:
               if root.r_central_child.elements >=0:
                    greater.append(root.r_central_child)
                    self.all_folder(root.r_central_child, greater)
            if root.l_central_child is not None:
               if root.l_central_child.elements >=0:
                    greater.append(root.l_central_child)
                    self.all_folder(root.l_central_child, greater)
               
            if root.l_child is not None:
               if root.l_child.elements >=0:
                    greater.append(root.l_child)
                    self.all_folder(root.l_child, greater)
            
        return reversed(greater)

    def max_folder(self, folders):
        mayor = max(folders, key=lambda x : x.elements)
        return mayor

            



    def imprimir_arbol(self):
        self.imprimir_subarbol(self.root, 0)

    def imprimir_subarbol(self, nodo_actual, nivel):
        print(" " * nivel, end="")
        if isinstance(nodo_actual, File):
            print("- " + nodo_actual.filename)
        if isinstance(nodo_actual, Folder):
            print("- " + nodo_actual.name)
            if nodo_actual.l_child is not None:
                self.imprimir_subarbol(nodo_actual.l_child, nivel + 2)
            if nodo_actual.l_central_child is not None:
                self.imprimir_subarbol(nodo_actual.l_central_child, nivel + 2)
            if nodo_actual.r_central_child is not None:
                self.imprimir_subarbol(nodo_actual.r_central_child, nivel + 2)
            if nodo_actual.r_child is not None:
                self.imprimir_subarbol(nodo_actual.r_child, nivel + 2)
    

class Menu:
    def __init__(self) -> None:
        self.desktop = Desktop()

    def begin(self):
        while True:
            print("======= MENÚ =======")
            print("1. Agregar Carpeta")
            print("2. Agregar Archivo")
            print("3. Modificar Carpeta")
            print("4. Modificar Archivo")
            print("5. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                parent_value_folder = input("Ingrese el nombre de la carpeta en donde se va guardar el nuevo elemento: ")
                new_value_folder = input("Ingrese el nombre de la nueva carpeta: ")
                if self.desktop.available_folder(self.desktop.root, parent_value_folder):
                    self.desktop.insert_folder(self.desktop.root, parent_value_folder, new_value_folder)
                else:
                    while self.desktop.available_folder(self.desktop.root, parent_value_folder) == False:
                        parent_value_folder = input("Ingresa el nombre de un carpeta con espacio o que el nombre no este repetido: ")
                    self.desktop.insert_folder(self.desktop.root, parent_value_folder, new_value_folder)
                
            elif opcion == "2":
                parent_value_folder = input("Ingrese el nombre de la carpeta en donde se va guardar el nuevo elemento: ")
                new_value_file = input("Ingrese el nombre del nuevo archivo: ")
                if self.desktop.available_folder(self.desktop.root, parent_value_folder):
                    self.desktop.insert_file(self.desktop.root, parent_value_folder, new_value_file)
                else: 
                    while self.desktop.available_folder(self.desktop.root, parent_value_folder) == False:
                        parent_value_folder = input("Ingresa el nombre de un carpeta con espacio: ")
                    self.desktop.insert_file(self.desktop.root, parent_value_folder, new_value_file)

            elif opcion == "3":
                old_folder = input("Ingrese el nombre de la carpeta a cambiar:")
                new_folder = input("Ingrese el nuevo nombre: ")
                self.desktop.modify_value_folder(self.desktop.root, old_folder, new_folder)

            elif opcion == "4":
                old_folder = input("Ingrese el nombre del archivo a cambiar:")
                new_folder = input("Ingrese el nuevo nombre: ")
                self.desktop.modify_value_file(self.desktop.root, old_folder, new_folder)

            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
            
            self.desktop.imprimir_arbol()


menu = Menu()
menu.begin()
# desktop = Desktop()
# # files = File("hola.txt 56")



# desktop.insert_folder(desktop.root, "root", "f1")
# desktop.insert_folder(desktop.root, "root", "f2")
# desktop.insert_folder(desktop.root, "root", "f3")

# desktop.insert_folder(desktop.root, "f1", "hola")


# # desktop.insert_folder(desktop.root, "root", "f4")
# desktop.insert_folder(desktop.root, "f3", "f4")
# desktop.insert_folder(desktop.root, "f3", "f6")
# desktop.insert_folder(desktop.root, "f3", "f3")


# desktop.insert_folder(desktop.root, "f4", "f")
# desktop.insert_folder(desktop.root, "f4", "f")
# desktop.insert_folder(desktop.root, "f4", "f")




# desktop.insert_folder(desktop.root, "f2", "f4")
# desktop.insert_folder(desktop.root, "f2", "f6")
# desktop.insert_folder(desktop.root, "f2", "f3")
# desktop.insert_folder(desktop.root, "f2", "f9")

# desktop.insert_folder(desktop.root, "f9", "fol1")
# desktop.insert_folder(desktop.root, "f9", "fol2")
# desktop.insert_folder(desktop.root, "f9", "fol3")

# desktop.insert_folder(desktop.root, "fol1", "fol1")
# desktop.insert_folder(desktop.root, "fol1", "fol2")
# desktop.insert_folder(desktop.root, "fol1", "fol3")
# desktop.insert_folder(desktop.root, "fol1", "fol3")

# desktop.insert_folder(desktop.root, "fol3", "fol1")
# desktop.insert_folder(desktop.root, "fol3", "fol2")
# desktop.insert_folder(desktop.root, "fol3", "fol3")
# desktop.insert_folder(desktop.root, "fol3", "fol3")

# desktop.imprimir_arbol()
# lista = desktop.all_folder(desktop.root, [])
# # for i in lista:
# #     print(i.name)
# print(desktop.max_folder(lista).name)

# desktop.modificar_valor(desktop.root, "f3", "g1")
# desktop.modificar_valor(desktop.root, "f1", "g1")
# # desktop.insert_folder(desktop.root, "f3", "f10")
# print(desktop.root.l_child.name)
# print(desktop.root.l_central_child.name)
# print(desktop.root.r_central_child.name)
# print(desktop.root.r_child.name)

# desktop.insert_file(desktop.root, "f1", "hola1.txt 56")
# desktop.insert_file(desktop.root, "f1", "hola2.txt 56")
# desktop.insert_file(desktop.root, "f1", "hola3.txt 56")
# desktop.insert_file(desktop.root, "f1", "hola4.txt 56")

#desktop.insert_folder(desktop.root, "root", "f5")
#desktop.insert_file(desktop.root, "hola4.txt 56", "hola5.txt 56")

# print(desktop.root.l_child.father.name)
# print(desktop.root.l_child.father.name)
#print(desktop.root.r_central_child.l_child.father.currents)
# print(desktop.root.l_child.l_central_child.filename)
# print(desktop.root.l_child.r_central_child.filename)
# print(desktop.root.l_child.r_child.filename)
# print(desktop.root.elements)


