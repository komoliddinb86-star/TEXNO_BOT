CATEGORIES = {
    'Iphone': 'katalog/smartfony-apple/',
    'TV': 'katalog/televizory-lg/',
    'Ofis tex': 'katalog/printer-i-mfu-3/',
    'Avto Jixoz': 'katalog/radar-detektor-neoline/',
    'Laptop HP': 'katalog/noutbuki-hp/',
    'Samsung': 'katalog/smartfon-samsung/'
}

def get_values(category):
    for k,v in CATEGORIES.items():
        if k==category:
            return v