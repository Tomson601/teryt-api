from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime
from main import models


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

wojewodztwa = client.service.PobierzListeWojewodztw(STATE_DATE)

# Creating objects in database
for obj in wojewodztwa:
    woj = models.Wojewodztwo.objects.create(
        name = obj['NAZWA'],
        extra_name = obj['NAZWA_DOD'],
        woj_id = obj['WOJ'],
        status_on_day = obj['STAN_NA']
    )
    print(f"Created: {woj.id}, {woj.name}")
