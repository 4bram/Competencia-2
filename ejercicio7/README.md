# DESCRIPCIÓN
Se utiliza la gramática básica para reconocer números y operadores.
Incluye un script para leer tokens desde un archivo o desde la entrada directa.
# ¿Cómo usar el ejercicio?

## PASO 1- CLONAR EL REPOSITORIO EJECUTANDO LOS SIGUIENTES COMANDOS
```powershell
git clone "https://github.com/4bram/Competencia-2.git"
```
```powershell
cd Competencia-2
```

## PASO 2- ENTRAR A LA CARPETA DEL EJERCICIO 
```powershell
cd Ejercicio_7
```
## PASO 3- CREAR Y ACTIVAR EL ENTORNO VIRTUAL EJECUTANDO LOS SIGUIENTES COMANDOS
```powershell 
py -m venv .venv
 ```
```powershell
.\.venv\Scripts\Activate.ps1
```
## PASO 4- INSTALAR EL RUNTIME DE ANTLR PARA PHYTON EJECUTANDO EL SIGUIENTE COMANDO
 ```powershell
.\.venv\Scripts\python.exe -m pip install antlr4-python3-runtime==4.13.2
```
## PASO 5- GENERAR EL PARSER Y EL LEXER EJECUTANDO EL SIGUENTE COMANDO
```powershell
java -jar C:\Users\isabe\Downloads\antlr-4.13.2-complete.jar -Dlanguage=Python3-no-listener .\Expr.g4
```
## PASO 6- EJECUTAR EL SCRIPT 

### Opción 1 (ARCHIVO)
```powershell
.\.venv\Scripts\python.exe Text.py prueba.txt
```

### Opción 2 (CONSOLA
```powershell
.\.venv\Scripts\python.exe Text.py "operacion deseada"
```

### Autores
Herrera Morales Jose Angel       21030374

Silva Méndez Abraham             20031313

Silva Macias Guadalupe Isabel    2003108
