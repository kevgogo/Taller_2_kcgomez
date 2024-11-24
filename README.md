# API de Animales

Una API básica construida con Flask para consultar información sobre animales y sus sonidos. Incluye una interfaz web para consultas interactivas.

## Funcionalidades
- Obtener el sonido de un animal.
- Listar todos los animales y sus sonidos.
- Interfaz web para explorar la API.

## Endpoints
1. **Obtener el sonido de un animal**  
   - Método: `GET`  
   - URL: `/animales/sonido/[ANIMAL]`  
   - Ejemplo: `/animales/sonido/gato`  

2. **Listar todos los animales y sonidos**  
   - Método: `GET`  
   - URL: `/animales`  

3. **Página principal**  
   - Método: `GET`  
   - URL: `/`  

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/TALLER2-LOGIN.git
   cd TALLER2-LOGIN
   ```
2. Clona el repositorio:
   ```bash
   python -m venv env
   source env/bin/activate  
   # En Windows: env\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicia la aplicación:
   ```bash
   python app.py
   ```

## Uso
- API: Usa Postman o tu navegador para probar los endpoints.
- Interfaz web: Abre http://127.0.0.1:5000 en tu navegador.

## Contacto
- GitHub: https://github.com/kevgogo