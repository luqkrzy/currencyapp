# Currency Converter APP

Simple Api to convert currencies in polish market. It connects with Polish national bank NBP api,
gets exchange rate and converts to requested currency.

Service reply is returned in the JSON format

### Query string parameters
* code - currency code i.e USD, PLN
* amount - number float or integer

    > http://localhost:8080/api/convert?from={code}&to={code}&amount={amount}

## Run
todo
