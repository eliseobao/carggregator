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


class AutoScout24Enum(ExtendedEnum):
    brand = "Marca"
    model = "Modelo"
    version = "Versión"
    price_cash = "Precio"
    fuel = "Tipo de combustible"
    hp = "Potencia"
    odometer = "Kilometraje"
    registration_date = "Año"
    transmission = "Tipo de cambio"
    seller = "Vendedor"


class AutocasionEnum(ExtendedEnum):
    registration_date = 'Fecha de matriculación:'
    odometer = 'Kilómetros:'
    transmission = 'Cambio:'
    fuel = 'Combustible:'
    hp = 'Potencia (cv):'
    # warranty = 'Garantía:'
    # bodywork = 'Carrocería:'
    # color = 'Color:'
    # environmental_badge = 'Distintivo ambiental:'
