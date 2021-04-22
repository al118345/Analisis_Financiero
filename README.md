# Analisis_Financiero

Yahoo_fin es un paquete de Python 3 diseñado para extraer datos históricos de precios de acciones, así como para proporcionar información actual sobre límites de mercado, rendimientos de dividendos y qué acciones comprenden las principales bolsas.


En este articulo nos centraremos en la descarga de la informaicón fiscal, exactamente explicaremos cómo obtener el historico de dividindo proporiconado un ticker y almacenar el resultado en un fichero .csv para su posterior consulta.

Más información en la web https://1938.com.es/obtener_dividendos_python  o directamente en la web 1938.com.es. 


### Files

En este repositorio se pueden encontrar los siguientes ficheros:

* **historico_dividendos.py** Este fichero recoge el código necesario parra descargar los dividendos solicitados en el documento tickers.csv.
  
* **tickers.csv** Listado de empresas a obtener la información

* **resultados_dividendos.csv**  Resultado de ejecutar el programa. 

* **requirements.txt** Este archivo menciona los paquetes Python necesarios para ejecutar el código.

### Prerequisites

```
yahoo_fin
pandas
```

### Installing
Para ejecutar este proyecto es necesario ejecutar el siguiente comando:

```
python get-pip.py install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
python get-pip.py  install . -r requirements.txt
```
o en el caso de linux

```
pip install -r requirements.txt
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
```

## Authors
* Rubén Pérez Ibáñez

## License
Released Under CC BY-SA 4.0 License

