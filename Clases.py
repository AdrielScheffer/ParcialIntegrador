import json
import uuid


class Transaccion(json.JSONEncoder):
    def __init__(self, transaccion_id, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self.transaccion_id = transaccion_id
        self.dni_cliente = dni_cliente
        self.tipo_movimiento = tipo_movimiento
        self.monto_movimiento = monto_movimiento
        self.estado = estado
        self.nombre_comercio = nombre_comercio



    @classmethod
    def creador_transaccion(self):
        transaccion_id = uuid.uuid4()
        dni_cliente = int(input("ingrese el dni del cliente: "))
        tipo_movimiento = input("ingrese el tipo de movimiento: ")
        monto_movimiento = int(input("ingrese el monto del movimiento: "))
        estado = input("ingrese el estado: ")
        nombre_comercio = input("ingrese el nombre del comercio: ")
        transaccion = Transaccion (transaccion_id, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio)
        return transaccion

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



    def crear_archivo(self):
        datos = Transaccion.creador_transaccion()
        archivo = open(f'./data/{self.transaccion_id.json}', "w")
        archivo.write(str(datos.toJSON()))
        archivo.close()


    def menor_100000(self):
        monto = self.monto_movimiento

        if monto>=100000:
            print("El valor no requiere justificacion")
        elif monto<100000:
            print("el valor requiere justificacion")





