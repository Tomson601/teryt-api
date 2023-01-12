# teryt-api  

Production version of app can be found here: https://teryt-api.herokuapp.com/  

teryt-api is an python based API that uses Django web framework. This app implements TERYT databse which contains latest polish administrative unit objects, e.g. provinces, cities, villages and roads.  
TERYT databse is maintained by "GUS" (polish: Central Statistical Office).  

There are tools that can parse CSV files and import objects to web database.  

[CSV files can be found there](
https://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default)  

# Quickstart  
Clone repository:  
`git clone https://github.com/Tomson601/teryt-api.git`  

Migrate database:  
`python manage.py migrate`  

Download and parse newest catalogs (CSV database files) in django shell

Run server localy:  
`python manage.py runserver`  

# Features  
teryt-api can:
- establish connection with TERYT API via WSDL [establish_connection()](/api/tools/functions.py?plain=1#L19)
- download latest TERC, SIMC and ULIC data files [download_catalogs()](/api/tools/functions.py?plain=1#L37)
- parse and import those files [parse_TERC/SIMC/ULIC()](/api/tools/functions.py?plain=1#L97)
- count quantity of objects in file [check_file_length()](/api/tools/functions.py?plain=1#L97)
- filter objects by any filed that is in databse [filters](/api/main/views.py?plain=1#L14)
- and finally... serve these objects in the form of an API application https://teryt-api.herokuapp.com/

# Gallery  
![API root](/docs/api-root.png)  
![API woj-get](/docs/woj-api-get.png)  
![API filters](/docs/filters.png)  
