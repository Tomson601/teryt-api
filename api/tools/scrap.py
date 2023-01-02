from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime
# from main import models
# import requests
# import time
from base64 import b64decode
from zipfile import ZipFile
import csv
import io
import json


STATE_DATE = datetime.now()
CREDENTIALS = {
    'wsdl': 'https://uslugaterytws1test.stat.gov.pl/wsdl/terytws1.wsdl',
    'username': 'TestPubliczny',
    'password': '1234abcd'
}

token = UsernameToken(
    username=CREDENTIALS['username'],
    password=CREDENTIALS['password']
)

client = Client(wsdl=CREDENTIALS['wsdl'], wsse=token)

is_authenticated = client.service.CzyZalogowany()

# Checking if auth is working properly
if not is_authenticated:
    print("You are not logged in!")
else:
    print("Login succeed")


def parse_simc_csv():
    catalog = client.service.PobierzKatalogSIMC(STATE_DATE)

    filename = catalog['nazwa_pliku']
    content = catalog['plik_zawartosc']

    decoded = b64decode(content)

    zip_file = ZipFile(filename+".zip", 'r')

    with open(filename+".json", "w") as json_file:

        with zip_file.open(zip_file.namelist()[1]) as csv_file:

            text_file = io.TextIOWrapper(csv_file)
            csv_reader = csv.reader(text_file, delimiter=";")
            
            json_file.write("[")

            for row in csv_reader:
                if len(row) == 0:
                    break
                dictionary = {
                    "WOJ": row[0],
                    "POW": row[1],
                    "GMI": row[2],
                    "RODZ_GMI": row[3],
                    "RM": row[4],
                    "MZ": row[5],
                    "NAZWA": row[6],
                    "SYM": row[7],
                    "SYMPOD": row[8],
                    "STAN_NA": row[9],
                }
                converted_json = json.dumps(dictionary, indent=4)
                json_file.write(converted_json)
                json_file.write(",")

            json_file.write("]")
























STATE_DATE = datetime.now()

CREDENTIALS = {
    'wsdl': 'https://uslugaterytws1test.stat.gov.pl/wsdl/terytws1.wsdl',
    'username': 'TestPubliczny',
    'password': '1234abcd'
}

token = UsernameToken(
    username=CREDENTIALS['username'],
    password=CREDENTIALS['password']
)
client = Client(wsdl=CREDENTIALS['wsdl'], wsse=token)

is_authenticated = client.service.CzyZalogowany()

# Checking if auth is working properly
if not is_authenticated:
    print("You are not logged in!")
else:
    print("Login succeed")

# wojewodztwa = client.service.PobierzListeWojewodztw(STATE_DATE)

## Creating objects in database
# for obj in wojewodztwa:
#     woj = models.Wojewodztwo.objects.create(
#         name = obj['NAZWA'],
#         extra_name = obj['NAZWA_DOD'],
#         woj_id = obj['WOJ'],
#         status_on_day = obj['STAN_NA']
#     )
#     print(f"Created: {woj.woj_id}, {woj.name}")


# powiaty = client.service.PobierzListePowiatow("02", STATE_DATE)

# ## Creating objects in database
# for obj in wojewodztwa:
#     woj_id = obj['WOJ']
#     current_woj = models.Wojewodztwo.objects.get(woj_id=woj_id)

#     powiaty = client.service.PobierzListePowiatow(woj_id, STATE_DATE)

#     for i in powiaty:
#         pow = models.Powiat.objects.create(
#             name = i['NAZWA'],
#             extra_name = i['NAZWA_DOD'],
#             pow_id = i['POW'],
#             status_on_day = i['STAN_NA'],
#             wojewodztwo = current_woj
#         )
#         print(f"Created: {pow.pow_id}, {pow.name}")

# # # Geting data from API:

# # request = requests.get("https://tomson601.pythonanywhere.com/wojewodztwa/")

# # print(request.json())


# # Parsing gminy:
# wojewodztwa = models.Wojewodztwo.objects.all()

# for woj in wojewodztwa:
#     print(woj.name)
#     powiaty = models.Powiat.objects.filter(wojewodztwo=woj.id)
#     for pow in powiaty:
#         print(pow.name)
#         gminy = client.service.PobierzListeGmin(woj.woj_id, pow.pow_id, STATE_DATE)
#         for gmi in gminy:
#             gmina = models.Gmina.objects.create(
#                 name = gmi['NAZWA'],
#                 extra_name = gmi['NAZWA_DOD'],
#                 gmi_id = gmi['GMI'],
#                 status_on_day = gmi['STAN_NA'],
#                 wojewodztwo = woj,
#                 powiat = pow,
#             )
#             print(gmina)


# Parsing dla miast:

# wojewodztwa = models.Wojewodztwo.objects.all()

# for woj in wojewodztwa:
#     print(woj.name)
#     powiaty = models.Powiat.objects.filter(wojewodztwo=woj.id)

#     for pow in powiaty:
#         print(pow.name)
#         gminy = models.Gmina.objects.filter(powiat=pow.id)

#         for gmi in gminy:
#             print(gmi.name)

#             time.sleep(2.5)

#             miejscowosci = client.service.PobierzListeMiejscowosciWGminie(woj.name, pow.name, gmi.name, STATE_DATE)

#             if miejscowosci is not None:

#                 for miej in miejscowosci:
#                     miejscowosc = models.Miejscowosc.objects.create(
#                         name = miej['Nazwa'],
#                         miejsc_id = miej['Symbol'],
#                         wojewodztwo = woj,
#                         powiat = pow,
#                         gmina = gmi,
#                     )
#                     print(f"Created object: {miejscowosc}, in wojewodztwo: {woj}")
#             else:
#                 print(f"Not found any miejscowosci for {gmi}. Skiping...")


ULIC = client.service.PobierzKatalogULIC(STATE_DATE)

file_name = ULIC["nazwa_pliku"]
content = ULIC["plik_zawartosc"]


decoded = b64decode(content)

with open(file_name, 'wb') as file:
    file.write(decoded)
    file.close()


zip_file = ZipFile(file_name, 'r')

print(zip_file.namelist())

with zip_file.open(zip_file.namelist()[0]) as xml_file:
    print(xml_file.read(n=1024))

from xml.dom import minidom

with zip_file.open(zip_file.namelist()[0]) as xml_file:
    DOMTree = minidom.parse(xml_file)

    children = DOMTree.childNodes
    for row in children[0].getElementsByTagName('row'):
        print(row.getElementsByTagName('NAZWA')[0].childNodes[0].toxml())


import csv
import io

with zip_file.open(zip_file.namelist()[1]) as csv_file:
    text_file = io.TextIOWrapper(csv_file)
    csv_reader = csv.reader(text_file, delimiter=";")
    for row in csv_reader:
        print(row)