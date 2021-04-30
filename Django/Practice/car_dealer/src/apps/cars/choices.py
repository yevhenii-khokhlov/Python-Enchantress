FUEL_GASOLINE = 'g'
FUEL_DIESEL = 'd'
FUEL_ELECTRICAL = 'e'
FUEL_OTHER = 'o'

FUEL_CHOICES = (
    (FUEL_GASOLINE, 'gasoline'),
    (FUEL_DIESEL, 'diesel'),
    (FUEL_ELECTRICAL, 'electrical'),
    (FUEL_OTHER, 'another type of fuel'),
)


ENGINE_ELECTRICAl = 'e'
ENGINE_ICE = 'i'

ENGINE_CHOICES = (
    (ENGINE_ELECTRICAl, 'electrical'),
    (ENGINE_ICE, 'internal combustion engine'),
)


POSITION_FRONT = 'f'
POSITION_BACK = 'b'
POSITION_LEFT = 'l'
POSITION_RIGHT = 'r'
POSITION_INTERIOR = 'i'
POSITION_GENERAL = 'g'

POSITION_CHOICES = (
    (POSITION_FRONT, 'front view'),
    (POSITION_BACK, 'back view'),
    (POSITION_LEFT, 'left view'),
    (POSITION_RIGHT, 'right view'),
    (POSITION_INTERIOR, 'interior view'),
    (POSITION_GENERAL, 'general view'),
)


POPULATION_SEDAN = 's'
POPULATION_UNIVERSAL = 'u'
POPULATION_SUV = 'v'
POPULATION_CABRIOLET = 'a'
POPULATION_COUPE = 'c'
POPULATION_TRUCK = 't'
POPULATION_OTHER = 'o'

POPULATION_CHOICES = (
    (POPULATION_SEDAN, 'sedan'),
    (POPULATION_UNIVERSAL, 'universal'),
    (POPULATION_SUV, 'SUV'),
    (POPULATION_CABRIOLET, 'cabriolet'),
    (POPULATION_COUPE, 'coupe'),
    (POPULATION_TRUCK, 'truck'),
    (POPULATION_OTHER, 'other'),
)


GEAR_CASE_MECHANICAL = 'm'
GEAR_CASE_AUTOMATIC = 'a'
GEAR_CASE_VARIATOR = 'v'

GEAR_CASE_CHOICES = (
    (GEAR_CASE_MECHANICAL, 'mechanical transmission'),
    (GEAR_CASE_AUTOMATIC, 'automatic transmission'),
    (GEAR_CASE_VARIATOR, 'variator transmission'),
)


CAR_STATUS_AVAILABLE = 'a'
CAR_STATUS_NOT_AVAILABLE = 'n'

CAR_STATUS_CHOICES = (
    (CAR_STATUS_AVAILABLE, 'available'),
    (CAR_STATUS_NOT_AVAILABLE, 'not available'),
)
