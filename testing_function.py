def create_table():
    list_fields = {'Pressure': 'Float64',
                   'Humidity': 'Float64',
                   'Area_temperature': 'Float64',
                   'Work_temperature': 'Float64',
                   'pH_level': 'Float64',
                   'Weight': 'Float64',
                   'Fluid_flow': 'Float64',
                   'CO2_flow': 'Float64',
                   }
    tmp = list()
    for field in list_fields:
        tmp.append(" ".join(i for i in ["'"+field+"'", list_fields[field]]))

    field_table = ', '.join(i for i in tmp)
    print(field_table)


create_table()
