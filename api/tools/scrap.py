from zeep import Client
from zeep.wsse.username import UsernameToken


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

print(client.service.CzyZalogowany())
