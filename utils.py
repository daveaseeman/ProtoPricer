from numpy.stl import mesh
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
