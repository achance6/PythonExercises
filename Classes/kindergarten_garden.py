STUDENTS = 'Alice, Bob, Charlie, David, Eve, Fred, Ginny, Harriet, Ileana, Joseph, Kincaid, Larry'.split(', ')
SYMBOL_TO_PLANT = str.maketrans({'V': 'Violets', 'R': 'Radishes', 'G': 'Grass', 'C': 'Clover'})

class Garden:
    def __init__(self, diagram: str, students: list[str] = STUDENTS):
        self.plants_list = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, name: str) -> list[str]:
        index = self.students.index(name) * 2
        plant_str = (self.plants_list[0][index: index + 2] + 
                     self.plants_list[1][index: index + 2])
        return [plant.translate(SYMBOL_TO_PLANT) for plant in plant_str]

# garden = Garden('VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV')
# print(garden.plants('Larry'))