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
import os
# Make sure you are in main/catalogs/ directory

STATE_DATE = datetime.now()
CREDENTIALS = {
    'wsdl': 'https://uslugaterytws1test.stat.gov.pl/wsdl/terytws1.wsdl',
    'username': 'TestPubliczny',
    'password': '1234abcd'
}


def establish_connection(credentials):
    token = UsernameToken(
        username=credentials['username'],
        password=credentials['password']
    )

    client = Client(wsdl=credentials['wsdl'], wsse=token)
    is_authenticated = client.service.CzyZalogowany()

    # Checking if auth is working properly
    if not is_authenticated:
        print("Authentication error")
    else:
        print("Login succeed")

    return client, is_authenticated


def download_catalogs(client, is_authenticated=False, all=False, simc=False, ulic=False, terc=False):
    if not is_authenticated:
        return("You are not logged in!")
    elif is_authenticated == True:
        print("Authentication succeded")

    if all == True:
        print("Downloading all catalogs...")
        simc = ulic = terc = True
    
    if simc == True:
        simc_cat = client.service.PobierzKatalogSIMC(STATE_DATE)

        content = simc_cat["plik_zawartosc"]
        decoded = b64decode(content)

        with open("SIMC.zip", 'wb') as file:
            file.write(decoded)
            file.close()
        print(f"Succesfully downloaded: SIMC.zip")

    if ulic == True:
        ulic_cat = client.service.PobierzKatalogULIC(STATE_DATE)

        content = ulic_cat["plik_zawartosc"]
        decoded = b64decode(content)

        with open("ULIC.zip", 'wb') as file:
            file.write(decoded)
            file.close()
        print(f"Succesfully downloaded: ULIC.zip")

    if terc == True:
        terc_cat = client.service.PobierzKatalogTERC(STATE_DATE)

        content = terc_cat["plik_zawartosc"]
        decoded = b64decode(content)

        with open("TERC.zip", 'wb') as file:
            file.write(decoded)
            file.close()
        print(f"Succesfully downloaded: TERC.zip")



def parse_TERC(filename):
    zip_file = ZipFile(filename, 'r')

    with zip_file.open(zip_file.namelist()[1]) as csv_file:
    
        text_file = io.TextIOWrapper(csv_file)
        csv_reader = csv.reader(text_file, delimiter=";")

        count_objects = 0

        for row in csv_reader:
            if row[] == :
            print(row)
            count_objects+=1


def parse_target(filename):
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


def parse_all():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    if len(files) == 0:
        print("Couldn't find any file in current directroy. Make sure you are located in 'main/catalogs/ directory'")
    for f in files:
        if "TERC" in f:
            
        elif "SIMC" in f:

        elif "ULIC" in f:

        else:
            print("Error: this file names are not supported!")




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


# ULIC = client.service.PobierzKatalogULIC(STATE_DATE)

# file_name = ULIC["nazwa_pliku"]
# content = ULIC["plik_zawartosc"]


# decoded = b64decode(content)

# with open(file_name, 'wb') as file:
#     file.write(decoded)
#     file.close()


# zip_file = ZipFile(file_name, 'r')

# print(zip_file.namelist())

# with zip_file.open(zip_file.namelist()[0]) as xml_file:
#     print(xml_file.read(n=1024))

# from xml.dom import minidom

# with zip_file.open(zip_file.namelist()[0]) as xml_file:
#     DOMTree = minidom.parse(xml_file)

#     children = DOMTree.childNodes
#     for row in children[0].getElementsByTagName('row'):
#         print(row.getElementsByTagName('NAZWA')[0].childNodes[0].toxml())


# import csv
# import io

# with zip_file.open(zip_file.namelist()[1]) as csv_file:
#     text_file = io.TextIOWrapper(csv_file)
#     csv_reader = csv.reader(text_file, delimiter=";")
#     for row in csv_reader:
#         print(row)