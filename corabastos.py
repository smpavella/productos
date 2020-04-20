# librerias a utilizar
import os
import argparse
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
# Argumentos de la linea de comando
mods = argparse.ArgumentParser()
mods.add_argument("--fechaInicio", help="Ingrese la fecha de inicio del rango")
mods.add_argument("--fechaFin", help="Ingrese la fecha final del rango")
mods.add_argument("--Grupo", help="Ingrese el grupo 1=Tuberculos 2=Lacteos 3=Hortalizas")
argumentos = mods.parse_args()
#Function principal
def buscarPrecios( URL,grupo,valoresCabecera,fecha,listado ):
  URL = URL + "?c=" + grupo + "&d=ok&f=" + fecha + "&d=ok&l="
  response= requests.post(URL, headers=valoresCabecera, verify=False)
  soup = BeautifulSoup(response.text,"html.parser")
  #print(soup.prettify())
  tabla=soup.find('table');
  Indice=0
  for row in tabla.findAll("tr"):
    cells = row.findAll('td')
    if (Indice > 0):
    	Nombre=cells[0].find(text=True)
    	Presentacion=cells[1].find(text=True)
    	Cantidad=cells[2].find(text=True)
    	Unidad=cells[3].find(text=True)
    	PesosCalidadExtra=cells[4].find(text=True)
    	PrecioCalidadPrimera=cells[5].find(text=True)
    	PrecioCalidadCorriente=cells[6].find(text=True)
    	GrandesSuperficies=cells[7].find(text=True)
    	elemento=[fecha,Nombre,Presentacion,Cantidad,Unidad,PesosCalidadExtra,PrecioCalidadPrimera,PrecioCalidadCorriente,GrandesSuperficies]
    	listado.append(elemento)
    Indice=Indice+1
  return
#Directorio donde se localiza el script
directorioAct = os.path.dirname(__file__)
nombreArchivo = "productos_dataset.csv"
rutaArchivo = os.path.join(directorioAct, nombreArchivo)
CorabastosUrl="https://www.corabastos.com.co/sitio/historicoApp2/reportes/historicos.php"
fechaPros=''
valoresHeader={}
datosForm={}
#Valores de HTTP Request
valoresHeader['Accept']='*/*' 
valoresHeader['Connection']='keep-alive'
valoresHeader['Host']='www.corabastos.com.co'
valoresHeader['Origin']='https://www.corabastos.com.co'
valoresHeader['Referer']='https://www.corabastos.com.co/sitio/historicoApp2/reportes/index.php'
valoresHeader['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
#valores del POST de HTTP Request
# Tuberculos
valGrupo1='305200|305301|305302|305303|305304|305305|305306|305307|305308|305309|305310|305311|305312|305401|305402|308700|308701'
#lacteos
valGrupo2='607401|607402|607403|607404|607405|607406'
#Hortalizas
valGrupo3='100100|100200|100301|100400|100500|100601|100700|100800|100900|101000|101101|101102|101103|101104|101105|101200|101300|101400|101501|101502|101503|101601|101700|101800|101900|102001|102002|102100|102201|102300|102400|102401|102501|102502|102503|102504|102600|108800|108900|109200|109300|109500|109700|110300|110400|110500|111300|111700|113100|113900|114100'

fechaInicio = datetime.strptime(argumentos.fechaInicio,'%Y-%m-%d')
fechaFin = datetime.strptime(argumentos.fechaFin,'%Y-%m-%d')
tipoGrupo = argumentos.Grupo
if (tipoGrupo == '1'):
	valGrupo=valGrupo1
if (tipoGrupo == '2'):
	valGrupo=valGrupo2
if (tipoGrupo == '3'):
	valGrupo=valGrupo3		
listaPrecios=[]
listaCabecera=["Fecha","Nombre", "Presentación", "Cantidad", "Unidad", "Pesos Calidad Extra", "Precio Calidad Primera", "Precio Calidad Corriente", "Grandes Superficies"]
listaPrecios.append(listaCabecera)
while fechaInicio <= fechaFin:
  fechaPros = fechaInicio.strftime('%Y-%m-%d')
  print ("Generando dataset de %s" %  fechaPros)
  buscarPrecios(CorabastosUrl,valGrupo,valoresHeader,fechaPros,listaPrecios)
  fechaInicio = fechaInicio + timedelta(days=1) 
#Escribir a archivo
with open(rutaArchivo, 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for priceElement in listaPrecios:
    writer.writerow(priceElement)