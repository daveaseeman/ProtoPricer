import os
import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Settings
# May turn into class later
materials = {'pla': .01,
'std': .149,
'eng': .199}

resolution = {'25': 5.0,
'50': 4.0,
'100': 3.0,
'200': 2.0,
'300': 1.0}

finishing = {'none': 1.0,
'basic': 2.0,
'sanded': 3.0,
'primed': 4.0,
'painted': 5.0}

unit_conversion = {'in': 16387.064,
'mm': 1}

rates = {'material': 10,
'labor': 3,
'materials': 10,
'order_min': 15,
'part_min': 10,
'editing': 75}

class Part():
    """
    Part
    """
    def __init__(self, filename, material, resolution, units):
        self.filename = filename
        self.mesh = mesh.Mesh.from_file(filename)
        self.material = materials[file[:3]]
        self.resolution = resolution[file[3:5]]
        self.units = unit_conversion[file[7:9]]
        self.name = file[10:]
        self.volume, self.cog, self.inertia = self.mesh.get_mass_properties()
        self.edit = 0 # can add in editing cost later

    def get_price(self):
        base_cost = rates['part_min']
        editing_cost = rates['editing']*self.edit
        material_cost = rates['materials']*self.material*self.resolution*self.volume*self.unit_conversion
        part_price = material_cost + editing_cost + base_cost

def get_part_files(part_dir):
    part_files = {}
    for file in os.listdir(part_dir):
        if file.endswith(".stl"):
            meta_data = {}
            material = file[:3]
            resolution = file[3:5]
            qty = int(file[5])
            edit = int(file[6])
            unit = file[7:9]
            name = file[10:]
            meta_data["name"] = name
            meta_data["path"] = part_dir + "/" + file
            meta_data["material"] = material
            meta_data["resolution"] = resolution
            meta_data["qty"] = qty
            meta_data["edit"] = edit
            meta_data["unit"] = unit
            part_files[file] = meta_data
    return print(part_files)

def get_part_objects(part_files):
    for file in part_files:
        if file.endswith(".stl"):
            path = part_dir + "/" + file
            part = Part(path)
            attrs = vars(part)
            print(attrs)

get_part_files("Band")
