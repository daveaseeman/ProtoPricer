from numpy.stl import mesh


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
        material_cost = materials[meta['material']] * volume * labor_rate * material_rate
        editing_cost = meta['edit'] * editing
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
        material_cost = materials[meta['material']] * volume * material_base
        editing_cost = meta['edit'] * editing
        part_price = material_cost + editing_cost + part_base
        # Save Price & Total
        total += part_price
        meta['price'] = part_price
        part_pricing[part] = meta  # .items()
    part_total['price'] = total
    part_pricing['total'] = part_total
    part_pricing = part_pricing  # .items()
    return part_pricing
