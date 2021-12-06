## Pre-requisitos: 
- Fasttext
- ntlk

## Aplicación:
Esta aplicación le permitirá ingresar un caso de servicio de 'Helpdesk' que requiera de la atención del DSIT de la Universidad de los Andes y le proveerá la categoría más probable para el caso por medio de un modelo de redes neuronales.
Para correr el programa desde una CLI (interfaz por línea de comandos), utilice el comando:
	python main.py
Se le pedirá que ingrese primero el asunto del caso y, posteriormente, la descripción del caso, que debe ser breve pero específica. El programa le indicará la categoría más probable para el caso y 
la probabilidad de que pertenezca a esa categoría, lo cual facilitará la resolución del problema.
