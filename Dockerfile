# Establecer la imagen base
FROM python:3.11-slim-buster

# Establecer el directorio de trabajo
WORKDIR /my-own-dca

# Copiar los archivos necesarios al contenedor
COPY requirements.txt /my-own-dca
COPY . /my-own-dca


# Instalar las dependencias de Python
RUN apt-get update && apt-get install -y postgresql-client vim \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Establecer las variables de entorno necesarias para Django
ENV DJANGO_SETTINGS_MODULE=my_own_dca.settings
ENV PYTHONUNBUFFERED 1

# Exponer el puerto 8000 para que la aplicación pueda ser accedida desde el exterior
EXPOSE 8000

# Ejecutar las migraciones y arrancar el servidor Django
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
