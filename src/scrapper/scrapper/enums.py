from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class AutocasionEnum(ExtendedEnum):
    registration_date = 'Fecha de matriculación:'
    odometer = 'Kilómetros:'
    transmission = 'Cambio:'
    fuel = 'Combustible:'
    hp = 'Potencia (cv):'
    warranty = 'Garantía:'
    bodywork = 'Carrocería:'
    color = 'Color:'
    environmental_badge = 'Distintivo ambiental:'
