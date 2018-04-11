# -*- coding: utf-8 -*-

import csv
import erppeek

"""
Dans le modèle 'Device', j'ai passé le champs 'serial_number' en unique 
pour pouvoir tester si un appareil est déjà existant.
"""

server = 'http://localhost:8071'
database = 'lpdip'
user = 'admin'
password = 'admin'

client = erppeek.Client(server, db=database, user=user, password=password)

with open('import.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Search in models if the differents elements already exists
        partner = client.search('res.partner', [('name', '=', row['partner'])])
        model_type = client.search('iut.it.model.type', [('name', '=', row['type'])])
        brand = client.search('iut.it.brand', [('name', '=', row['brand'])])
        model = client.search('iut.it.model', [('name', '=', row['model'])])

        if not partner and row['partner']:
            id_partner = client.create('res.partner', {
                'name': row['partner']
            })

        elif partner:
            id_partner = partner[0]

        else:
            id_partner = False

        if not model_type and row['type']:
            id_model_type = client.create('iut.it.model.type', {
                'name': row['type']
            })

        elif partner:
            id_model_type = model_type[0]

        else:
            id_model_type = False

        if not brand and row['brand']:
            id_brand = client.create('iut.it.brand', {
                'name': row['brand'],
                'warrantly_delay_month': 12
            })

        elif brand:
            id_brand = brand[0]

        else:
            id_brand = False

        if not model and row['model']:
            id_model = client.create('iut.it.model', {
                'name': row['model'],
                'ref': row['model'],
                'type_ids': [(4, id_model_type)],
                'brand_id': id_brand
            })

        elif model:
            id_model = model[0]
            client.write('iut.it.model', [id_model], {'type_ids': [(4, id_model_type)]})

        else:
            id_model = False

        name = row['brand'] + row['model'] + row['serial_number']

        try:
            client.create('iut.it.device', {
                'name': name,
                'date_allocation': row['date_allocation'],
                'serial_number': row['serial_number'],
                'date_purchase': row['date_purchase'],
                'res_partner_id': id_partner,
                'model_id': id_model,
            })

        except Exception as e:
            print(e)
