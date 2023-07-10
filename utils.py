def filter_laptops_by_description(laptops, description):
    filtered_laptops = []
    for laptop in laptops:
        if description.lower() in laptop['description'].lower():
            filtered_laptops.append(laptop)
    return filtered_laptops