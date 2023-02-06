# "CHALLENGE SRE" 

## 1. Exponer el modelo serializado a través API REST.
a. Puedes usar el modelo ya serializado (pickle_model.pkl) o volver a generarlo.

RPTA: Para la creación de la API REST se uso el framework Flask y HTML para la estructura de la web


2. Automatizar el proceso de construcción y despliegue de la API, utilizando uno o varios servicios cloud.

RPTA: Para la automatización se uso la siguiente arquitectura.

![image](https://user-images.githubusercontent.com/30010135/217001216-738c55ca-648f-4ef4-b189-4f11ff50b727.png)

Para desplegarlo en Cloud RUN, hacemos los siguientes pasos en el terminal:

* gcloud auth login (cnos logueamos con nuestra cuenta de GCP)
* gcloud config set project premium-portal-323320 (configuramos el proyecto en la cual vamos a trabajar)
* 
