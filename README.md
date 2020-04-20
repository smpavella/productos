# productos

Extrae los precios de tres grupos de productos (Tuberculos, Lacteos, Hortalizas) de la página web de [Corabastos](https://www.corabastos.com.co/aNuevo/index.php/features/servicios-web/historico-de-precios/) (Corporación de Abastos de Bogotá S.A.) 

Para ejecutar el script es necesario instalar la siguientes bibliotecas:
```
pip install requests
pip install lxml
pip install beautifulsoup4
```

El script se debe ejecutar con los siguientes argumentos:

```
python corabastos.py --fechaInicio 2019-10-28 --fechaFin 2019-11-02 --Grupo 3
```

Donde **fechaInicio** es la fecha inicial del intervalo a consultar en formato Y-m-d, **fechaFin** es la fecha final del intervalo a consultar en formato Y-m-d y **Grupo** corresponde al grupo de productos a consultar (1=Tuberculos, 2=Lacteos, 3=Hortalizas).

Los registros se almacenan en un archivo de tipo CSV denominado **productos_dataset.csv**. 

Se extraen las siguientes caracteristicas:

- Fecha
- Nombre
- Presentación
- Cantidad
- Unidad
- Pesos Calidad Extra
- Precio Calidad Primera
- Precio Calidad Corriente
- Grandes Superficies
