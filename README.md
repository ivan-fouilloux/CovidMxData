# CovidMxData

Descarga archivos de datos de Covid 19 de la Dirección General de Epidemiología (DGE) de la Secretaría de Salud del Gobierno de México.

Scraping:

- Último archivo de datos.
- Diccionario de datos
- Histórico de datos.

## Inicializa
```
covid = CovidMxData()
```

### Descarga útlimo archivo proporcionado por la DGE.
```
covid.reciente()

# Descargar archivo en formato .zip
reciente(unzip=False)
```

### Descarga diccionario de datos proporcionado por la DGE.
```
covid.diccionario_covid()

# Descargar carpeta en formato .zip
covid.diccionario_covid(unzip=False)
```

### Descarga los archivos históricos proporcionado por la DGE.
```
covid.historico_covid()

# Descargar archivos en formato .zip
covid.historico_covid(unzip=False)
```

Los archivos descargados serán guardados en una carpeta que se creará de manera automática con el nombre 'descargas_covid' en la raíz del proyecto.