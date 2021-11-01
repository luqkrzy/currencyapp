# Currency Converter APP

Simple Api to convert currencies in polish market. It connects with Polish national bank NBP api,
gets exchange rate and converts to requested currency.

Service reply is returned in the JSON format

```json
{
    "amount": 100.0,
    "base_currency": "pln",
    "exchange_rate": 3.9938,
    "result": 25.038810155741402,
    "to_currency": "usd"
}
```

### Query string parameters
* currency1 - currency code i.e USD (exactly 3 letters)
* currency2 - currency code i.e PLN (exactly 3 letters)
* amount - number float or integer
```bash
http://localhost:8080/api/convert?from={currency1}&to={currency2}&amount={amount}
```

#### example:
```bash
http://localhost:8080/api/convert?from=huf&to=usd&amount=100
```

#### Env variables:
```json
PSQL_USER_NAME=username
PSQL_PASS=password
PSQL_DB_NAME=currency_app
```

##Run
1. Create postgres database ```psql -c "create database currency_app"```
2. cd to main project path
3. run ````psql -U <your_username> demo < db.sql````
4. setup environmental variables
5. run ```pip install requirements.txt```
6. set ``` export FLASK_APP=converter_app/run.py```
7. run ```python3 -m flask run```
