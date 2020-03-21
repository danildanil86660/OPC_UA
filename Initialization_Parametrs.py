class Init_parametrs:

    def __init__(self, name, lower_bound, upper_bound):
        self.name = name
        self.restriction = [lower_bound, upper_bound]
        self.value = None

    def to_JSON(self):
        return {self.name: self.restriction, "value": self.value}

    def set_value(self, value):
        self.value = value


Parametrs = [Init_parametrs('Pressure', 0, 10e6), Init_parametrs('Humidity', 0, 100),
             Init_parametrs('Area_temperature', 15, 30), Init_parametrs('Work_temperature', 30, 90),
             Init_parametrs('pH_level', 0, 14), Init_parametrs('Weight', 1, 100),
             Init_parametrs('Fluid_flow', 1, 100), Init_parametrs('CO2_flow', 1, 100)]

