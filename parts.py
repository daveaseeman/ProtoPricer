import os


def get_part_files(part_dir):
    part_files = {}
    for file in os.listdir(part_dir):
        if file.endswith(".stl"):
            meta_data = {}
            material = file[:3]
            qty = int(file[3])
            edit = int(file[4])
            unit = file[5:7]
            meta_data["path"] = part_dir + "/" + file
            meta_data["material"] = material
            meta_data["qty"] = qty
            meta_data["edit"] = edit
            meta_data["unit"] = unit
            part_files[file] = meta_data
    return part_files
