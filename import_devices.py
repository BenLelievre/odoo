import csv
import erppeek

client = erppeek.Client.from_config('test')

iutdevice = client.model('iutdevice')
iutbrand = client.model('iutbrand')
iuttype = client.model('iuttype')
iutmodel = client.model('iutmodel')
respartner = client.model('res.partner')


rech_brand = iutbrand.search([('name', '=', '')])
rech_type = iuttype.search([('name', '=', '')])
rech_model = iutmodel.search([('name', '=', '')])
rech_respartner = respartner.search([('name', '=', '')])

with open('deviceexo2.csv') as csvfile:
    lirecsv = csv.reader(csvfile)
    for row in lirecsv:
        iutdevice.write({'name':row[1]})
        rech_brand=iutbrand.search([('name', '=', row[4])])
        print(row[4])
        print(rech_brand)
