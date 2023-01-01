from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime
from main import models
import requests


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


# # Parsing dla miast:
