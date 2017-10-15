from config import materials, conversion, rates
import os
# from numpy.stl import mesh
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


def get_stl_image(file):
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(file)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.axis('off')
    image = pyplot.show()
    return image


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


def get_rate_prices(part_dir):
    total = 0
    part_total = {}
    part_prices = {}
    parts = get_part_files(part_dir)
    for part in parts:
        # STL data
        meta = parts[part]
        part_mesh = mesh.Mesh.from_file(meta['path'])
        volume, cog, inertia = part_mesh.get_mass_properties()
        volume = volume * .001 * conversion[meta['unit']]
        meta['volume'] = volume
        # Price Calculation
        material_cost = materials[meta['material']] * volume * rates['labor_rate'] * rates['material_rate']
        editing_cost = meta['edit'] * rates['editing']
        part_price = material_cost + editing_cost
        # Save Price & Total
        total += part_price
        meta['price'] = part_price
        part_pricing[part] = meta  # .items()
    part_total['price'] = total
    part_pricing['total'] = part_total
    part_pricing = part_pricing  # .items()
    return part_prices


def get_base_pricing(part_dir):
    total = 0
    part_total = {}
    part_pricing = {}
    parts = get_part_files(part_dir)
    for part in parts:
        # STL data
        meta = parts[part]
        part_mesh = mesh.Mesh.from_file(meta['path'])
        volume, cog, inertia = part_mesh.get_mass_properties()
        volume = volume * .001 * conversion[meta['unit']]
        meta['volume'] = volume
        # Price Calculation
        material_cost = materials[meta['material']] * volume * rates['material_base']
        editing_cost = meta['edit'] * rates['editing']
        part_price = material_cost + editing_cost + rates['part_base']
        # Save Price & Total
        total += part_price
        meta['price'] = part_price
        part_pricing[part] = meta  # .items()
    part_total['price'] = total
    part_pricing['total'] = part_total
    part_pricing = part_pricing  # .items()
    return part_pricing


def print_part_data(meta):
    volume = meta['volume']
    unit = meta['unit']
    print("{0:.2f}{1:s}^3".format(volume, unit))
    return None


def print_pricing(part_pricing, print_data, print_image):
    print('Part Pricing:')
    for part in part_pricing:
        meta = part_pricing[part]
        if part != 'total':
            if print_image == 1:
                part_path = meta['path']
                get_stl_image(part_path)
            if print_data == 1:
                print_part_data(meta)
        print("{0:s} - ${1:.2f}".format(part, meta['price']))
    return None