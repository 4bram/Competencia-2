# DESCRIPCIÓN
Se utiliza la gramática básica para reconocer números y el operador mas "+". Incluye un script para leer tokens desde un archivo o desde la entrada directa.

## ¿Cómo usar lo archivos del ejercico?
### PASO 1-
CLONAR EL REPOSITORIO EJECUTANDO LOS SIGUIENTES COMANDOS

```powershell
git clone https://github.com/tu-usuario/Competencia-2.git
```
```powershell
cd Competencia-2
```

### PASO 2-
ENTRAR A LA CARPETA DEL EJERCICIO

```powershell
cd Ejercicio_1
```

### PASO 3-
CREAR Y ACTIVAR EL ENTORNO VIRTUAL EJECUTANDO LOS SIGUIENTES COMANDOS

```powershell
py -m venv .venv
```
```powershell
.\venv\Scripts\Activate.ps1
```

### PASO 4-
INSTALAR EL RUNTIME DE ANTLR PARA PHYTON EJECUTANDO EL SIGUIENTE COMANDO

```powershell
pip install -r requirements.txt
```

### PASO 5-
GENERAR EL PARSER Y EL LEXER EJECUTANDO EL SIGUENTE COMANDO 

```powershell
java -jar $env:CLASSPATH -Dlanguage=Python3 -no-listener.\Expr.g4
```
NOTA: Es importantes agregar al PATH el archivo:  **antlr-4.13.2-complete.jar** este archivo en el codigo se manda allamar por la variable de entorno CLASSPATH


### PASO 6- EJECUTAR EL SCRIPT
Opción 1 (ARCHIVO) 
```powershell
py .\Text.py archivo.txt`
```
Opción 2 (CONSOLA) 
```powershell
py .\Text.py`
```
