# "CHALLENGE SRE" 

## 1. Exponer el modelo serializado a través API REST.
a. Puedes usar el modelo ya serializado (pickle_model.pkl) o volver a generarlo.

RPTA: Para la creación de la API REST se uso el framework Flask y HTML para la estructura de la web


## 2. Automatizar el proceso de construcción y despliegue de la API, utilizando uno o varios servicios cloud.

RPTA: Para la automatización se uso la siguiente arquitectura.

![image](https://user-images.githubusercontent.com/30010135/217001216-738c55ca-648f-4ef4-b189-4f11ff50b727.png)

Construimos el dockerfile y procedemos a desplegarlo en cloud run.

Para desplegarlo en Cloud RUN, hacemos los siguientes pasos en el terminal:

* gcloud auth login (nos logueamos con nuestra cuenta de GCP)
* gcloud config set project premium-portal-323320 (configuramos el proyecto en la cual vamos a trabajar)
* gcloud builds submit --tag gcr.io/premium-portal-323320/sre --project=premium-portal-323320
* gcloud run deploy --image gcr.io/premium-portal-323320/sre --platform managed --project=premium-portal-323320 --port=80
![image](https://user-images.githubusercontent.com/30010135/217009233-58a4eb28-0215-4d3c-b34a-e3686cd5b2df.png)


## 3. Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas. a. ¿Cómo podrías mejorar el performance de las pruebas anteriores?

RPTA: Obtenemos los siguientes resultados
![image](https://user-images.githubusercontent.com/30010135/217008820-cc3b9bdc-2f83-4e26-93d7-54d86ed5174e.png)

Podría mejorar los resultados con lo siguiente:
* Usando balanceadores de carga.
* Aumento la capacidad computacional (memoria, CPU, instancias).
* Como infraestructura usar multiples pods en kubernetes que permitan hacer el balanceo de la carga nativamente.

## 4. El proceso de creación de infraestructura debe ser realizado con Terraform.

RPTA: Creamos el archimo main.tf en donde configuramos el despliegue en cloud run.
![image](https://user-images.githubusercontent.com/30010135/217009051-a85f35e9-1a03-4a81-b0af-32b91b46ffe4.png)

Para desplegarlo, hacemos los siguientes pasos en el terminal:
* terraform init
* terraform plan
* terraform apply
![image](https://user-images.githubusercontent.com/30010135/217009364-a3f0d0d6-9429-477d-a8f6-14661cde3b86.png)

## 5. ¿Cuáles serían los mecanismos ideales para que sólo sistemas autorizados puedan acceder a esta API? (NO es necesario implementarlo). a. ¿Este mecanismo agrega algún nivel de latencia al consumidor? ¿Por qué?

RPTA: 
* Autenticación obligatoria para usuarios autorizados - Administrar usuarios autorizados con Cloud IAM.

## 6. ¿Cuáles serían los SLIs y SLOs que definirías y por qué?

RPTA: 
* SLI: Alguna metrica para medir la presición del modelo RMSE // SLO: Monitorear el performance del modelo.
* SLI: Medir el tiempo promedio de latencia de la api // SLO: Testear la app. 
