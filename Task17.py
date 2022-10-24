class Human:

    name = "Busola"
    group = "Female"

    def get_name_group(self):
        return self.name + ":" + self.group


Busola = Human()
print(Busola.name, Busola.group, Busola.get_name_group())