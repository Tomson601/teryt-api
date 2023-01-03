from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime
from main import models
# import requests
# import time
from base64 import b64decode
from zipfile import ZipFile
import csv
import io
import json
import os


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

# Make sure you are in main/catalogs/ directory
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

# Wojewodztwa, powiaty, gminy
def parse_TERC(filename, verbose=True):
    zip_file = ZipFile(filename, 'r')

    with zip_file.open(zip_file.namelist()[1]) as csv_file:
    
        text_file = io.TextIOWrapper(csv_file)
        csv_reader = csv.reader(text_file, delimiter=";")
        count_objects = 0

        # Gathering keywords
        first_row = csv_reader.__next__()

        index_status_on_day = first_row.index("STAN_NA")
        index_extra_name = first_row.index("NAZWA_DOD")
        index_name = first_row.index("NAZWA")
        index_woj = first_row.index("\ufeffWOJ")
        index_pow = first_row.index("POW")
        index_gmi = first_row.index("GMI")

        for row in csv_reader:
            if row != []:
                if row[index_woj] != '' and row[index_pow] == '' and row[index_gmi] == '':
                    wojewodztwo = models.Wojewodztwo.objects.create(
                        name = row[index_name],
                        extra_name = row[index_extra_name],
                        woj_id = row[index_woj],
                        status_on_day = row[index_status_on_day],
                    )
                    if verbose:
                        print(f"Created wojwodztwo: {wojewodztwo}")

                elif row[index_woj] != '' and row[index_pow] != '' and row[index_gmi] == '':
                    powiat = models.Powiat.objects.create(
                        name = row[index_name],
                        extra_name = row[index_extra_name],
                        pow_id = row[index_pow],
                        status_on_day = row[index_status_on_day],
                        wojewodztwo = wojewodztwo,
                    )
                    if verbose:
                        print(f"Created powiat: {powiat}, in wojewodztwo: {wojewodztwo}")

                else:
                    gmina = models.Gmina.objects.create(
                        name = row[index_name],
                        extra_name = row[index_extra_name],
                        gmi_id = row[index_gmi],
                        status_on_day = row[index_status_on_day],
                        wojewodztwo = wojewodztwo,
                        powiat = powiat,
                    )
                    if verbose:
                        print(f"Created gmina: {gmina}, in powiat: {powiat}")
                count_objects+=1

            else:
                if verbose:
                    print(f"Found blank line: {row}, passing...")

    return print(f"Successfully created {count_objects} objects.")

# Miejscowosci EST: 10:00 mins, 102311 objects
def parse_SIMC(filename):
    zip_file = ZipFile(filename, 'r')

    with zip_file.open(zip_file.namelist()[1]) as csv_file:
    
        text_file = io.TextIOWrapper(csv_file)
        csv_reader = csv.reader(text_file, delimiter=";")

        # Gathering keywords
        first_row = csv_reader.__next__()

        index_status_on_day = first_row.index("STAN_NA")
        index_name = first_row.index("NAZWA")
        index_woj = first_row.index("\ufeffWOJ")
        index_pow = first_row.index("POW")
        index_gmi = first_row.index("GMI")

        for row in csv_reader:
            if row != []:
                wojewodztwo = models.Wojewodztwo.objects.get(woj_id=row[index_woj])

                powiaty = models.Powiat.objects.filter(wojewodztwo=wojewodztwo)
                for i in powiaty:
                    if i.pow_id == row[index_pow]:
                        powiat = i

                gminy = models.Gmina.objects.filter(wojewodztwo=wojewodztwo, powiat=powiat)
                for i in gminy:
                    if i.gmi_id == row[index_gmi]:
                        gmina = i

                miejscowosc = models.Miejscowosc.objects.create(
                    name = row[index_name],
                    miejsc_id = row[index_woj],
                    wojewodztwo = wojewodztwo,
                    powiat = powiat,
                    gmina = gmina,
                    status_on_day = row[index_status_on_day],
                )

                print(f"Created miejscowosc: {miejscowosc}")


def parse_ULIC(filename):
    zip_file = ZipFile(filename, 'r')

    with zip_file.open(zip_file.namelist()[1]) as csv_file:
    
        text_file = io.TextIOWrapper(csv_file)
        csv_reader = csv.reader(text_file, delimiter=";")

        # Gathering keywords
        # first_row = csv_reader.__next__()

        # index_status_on_day = first_row.index("STAN_NA")
        # index_name = first_row.index("NAZWA")
        # index_woj = first_row.index("\ufeffWOJ")
        # index_pow = first_row.index("POW")
        # index_gmi = first_row.index("GMI")

        for row in csv_reader:
            if row != []:
                print(row)
                input("SIEMA!")
                # wojewodztwo = models.Wojewodztwo.objects.get(woj_id=row[index_woj])

                # powiaty = models.Powiat.objects.filter(wojewodztwo=wojewodztwo)
                # for i in powiaty:
                #     if i.pow_id == row[index_pow]:
                #         powiat = i

                # gminy = models.Gmina.objects.filter(wojewodztwo=wojewodztwo, powiat=powiat)
                # for i in gminy:
                #     if i.gmi_id == row[index_gmi]:
                #         gmina = i

                # miejscowosc = models.Miejscowosc.objects.create(
                #     name = row[index_name],
                #     miejsc_id = row[index_woj],
                #     wojewodztwo = wojewodztwo,
                #     powiat = powiat,
                #     gmina = gmina,
                #     status_on_day = row[index_status_on_day],
                # )

                # print(f"Created miejscowosc: {miejscowosc}")
