class ar:
    color = "BLUE" #class variable
    def __init__(self, model, year, port):
        self.m = model #instance variable
        self.y = year #instance variable
        self.p = port #instance variable

    def walk(self):
        print(f"This {self.m} arduino is walking.")

    def ve(self):
        print(f"This {self.m} arduino is verified.")

a1 = ar("UNO R3", "2023", 1)

#print(f"{a1.m} {a1.y} {a1.p}")
#a1.walk()
#a1.ve()