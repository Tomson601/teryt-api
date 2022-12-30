from zeep import Client
from zeep.wsse.username import UsernameToken
from datetime import datetime

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

if not is_authenticated:
    print("You are not logged in!")
else:
    print("Login succeed")

wojewodztwa = client.service.PobierzListeWojewodztw(STATE_DATE)
print(wojewodztwa)
