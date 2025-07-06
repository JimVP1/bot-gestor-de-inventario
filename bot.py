#Base de datos
dataBase = {
    "saludos": ["hola", "buenos dias", "buenas tardes", "buenas noches", "hello", "hola amiguito"],
    "despedida": ["adios", "chao", "hasta luego", "nos vemos", "bye", "te me cuidas"],
    "ayuda": ["ayuda", "necesito ayuda", "podrias ayudarme"],
    "dime_algo":["dime algo"],
    "añadir_producto": ["añadir", "agregar","adicionar"],
    "ver_lista":["ver lista", "ver inventario", "ver productos disponibles"],
    "modificar_producto": ["modificar", "cambiar", "editar"],
    "buscar_producto": ["buscar", "encontrar", "hallar"],
    "elminar_producto": ["eliminar", "borrar"],
    "afirmaciones": ["si", "estoy seguro", "no tengo dudas"],
    "negaciones": ["no", "denegado", "no estoy seguro", "cancelar"]
}


botAnswers = {
    "saludos": "Hola! =), espero que te encuentre bien, ¿como puedo ayudarte?",
    "despedida":"Adios, que tengas un excelente dia =D",
    "ayuda": "Claro ¿que necesitas? ;)",
    "dime_algo":"algo :D"
}


storageData = {
    "smartphone":{
        "Precio":799.99,
        "Cantidad":25
    },
    "laptop":{
        "Precio":1299.99,
        "Cantidad":15
    },
    "tablet":{
        "Precio":499.99,
        "Cantidad":30
    },
    "earbuds":{
        "Precio":149.99,
        "Cantidad":60
    },
    "smartwatch":{
        "Precio":299.99,
        "Cantidad":40
    }
}


print("Hola soy tu asistente virtual")
print("Puedes llamarme como quieras =D")
print("Estoy aqui para ayudarte en lo que necesites ;)")
print('Escribe "cerrar chatbot" si quieres concluir la sesion')


while True:
    user = input("Tu: ").lower().strip()
    if user == "cerrar chatbot":
        print("Chatbot: Cerrando chatbot, hasta luego que tengas un buen dia :)")
        break
    
    answer = True

    if answer:
        for categoria, userAnswers in dataBase.items():
            if any(palabra in user for palabra in userAnswers):
                if categoria in botAnswers:
                    print(f"ChatBot: {botAnswers[categoria]}")
                    break

    if answer:
        if any(palabra in user for palabra in dataBase["añadir_producto"]):
            addProduct = input("Chatbot: ¿Que producto desea añadir? ").lower().strip()
            if addProduct in storageData:
                print("Ese producto ya se encuentra en la base de datos, por favor puedes ingresar un producto diferente :D")
            else:
                cantidad = int(input("Chatbot: ¿Que cantidad de ese producto desea añadir? "))
                precio = float(input("Chatbot: ¿Cual sera el precio de este nuevo producto? "))
                storageData[addProduct] = {
                    "Precio": precio,
                    "Cantidad": cantidad
                }
                print("Chatbot: El producto a sido correctamente añadido al inventario ;)")
            answer = False

    if answer:
        if any(palabra in user for palabra in dataBase["ver_lista"]):
            print("Chatbot: El inventario disponible es:")
            for productName, detalles in storageData.items():
                print(f"Producto: {productName}")
                print(f"Precio: {detalles["Precio"]}")
                print(f"Cantidad: {detalles["Cantidad"]}")
            answer= False

    if answer:
        if any(palabra in user for palabra in dataBase["modificar_producto"]):
            modificar = input("Chatbot: Por favor digame cual producto desea cambiar :) (Por favor escriba unicamente el nombre del producto) ")
            if any(p in modificar for p in storageData):
                cantidad = int(input("Chatbot: ¿Cual sera la nueva cantidad de ese producto? "))
                precio = float(input("Chatbot: ¿Cual sera el nuevo precio de ese producto? "))
                storageData[modificar] = {
                    "Precio": precio,
                    "Cantidad": cantidad
                }
                print("Chatbot: El producto seleccionado recibio los cambios de manera exitosa")
            else:
                print(f"Chatbot: Lo siento, el producto {modificar} no se emcuentra en la base de datos ")
                print('Chatbot: Si es un producto nuevo, por favor añadalo al sistema usando el comando "añadir"')
            answer = False

    if answer:
        if any(palabra in user for palabra in dataBase["buscar_producto"]):
            buscar = str(input("Chatbot: ¿Que producto desea buscar? (Por favor escriba unicamente el nombre del producto) ")).lower().strip()
            if buscar in storageData and storageData[buscar]["Cantidad"] > 0:
                print("Chatbot: El producto fue encontrado :D")
                print(f"Producto: {buscar}")
                print(f"Precio: {storageData[buscar]["Precio"]}")
                print(f"Cantidad: {storageData[buscar]["Cantidad"]}")
            elif buscar in storageData and storageData[buscar]["Cantidad"] == 0:
                print("Chatbot: El producto ya no se encuentra disponible")
            else:
                print("Chatbot: Lo siento, no pude encontrar el producto :( ")
            answer = False

    if answer:
        if any (palabra in user for palabra in dataBase["elminar_producto"]):
            eliminar = input("Chatbot: ¿Cual producto desea eliminar? (Por favor escriba unicamente el nombre del producto) ").lower().strip()
            if eliminar in storageData:
                confirmacion = input(f"Chatbot: ¿Esta seguro que desea elminar {eliminar} del sistema? ").lower().strip()
                if confirmacion in dataBase["afirmaciones"]:
                    del storageData[eliminar]
                    print(f"Chatbot: El producto {eliminar} fue eliminado del sistema de manera exitosa ;)")
                elif confirmacion in dataBase["negaciones"]:
                    print(f"Chatbot: La operacion fue cancelada, el producto {eliminar} sigue en el sistema =D")
            else:
                print(f"Chatbot: El producto {eliminar} no se encuentra en el sistema")
            answer = False

    if answer: 
        print("Chatbot: No entedi, podrias repetirlo por favor")
        print('Chatbot: Puedes usar los comandos "eliminar", "añadir", "modificar", "buscar", "ver lista"')