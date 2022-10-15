from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class MotorEsEnum(ExtendedEnum):
    brand = "Marca"
    model = "Modelo"
    version = "Versión"
    price_cash = "Precio al contado"
    price_financed = "Precio financiado"
    fuel = "Combustible"
    hp = "Potencia"
    odometer = "Kilómetros"
    registration_date = "Matriculación"
    transmission = "Cambio"
    seats = "Plazas"
    doors = "Puertas"
    color = "Color exterior"


class FlexicarEnum(ExtendedEnum):
    year = 'Año'
    odometer = 'Kilómetros'
    fuel = 'Combustible'
    doors_seats = 'Puertas / Plazas'
    engine = 'Motor'
    color = 'Color'
    transmission = 'Cambio'
    consumption = 'Consumo'
    deductible = 'I.V.A Deducible'
