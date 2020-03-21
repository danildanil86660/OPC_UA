class InitParameters:

    def __init__(self, name, lower_bound, upper_bound):
        self.name = name
        self.name = name
        self.restriction = [lower_bound, upper_bound]
        self.value = None

    def to_JSON(self):
        return {self.name: self.restriction, "value": self.value}

    def set_value(self, value):
        self.value = value


Parametrs = [InitParameters('Pressure', 0, 10e6), InitParameters('Humidity', 0, 100),
             InitParameters('Area_temperature', 15, 30), InitParameters('Work_temperature', 30, 90),
             InitParameters('pH_level', 0, 14), InitParameters('Weight', 1, 100),
             InitParameters('Fluid_flow', 1, 100), InitParameters('CO2_flow', 1, 100)]

