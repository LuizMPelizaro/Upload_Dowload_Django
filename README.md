# UPLOAD  E DOWNLOAD EM DJANGO 

## Requisitos

Para utilizar baixe os requisitos 

`pip install -m requirements.txt`

Criar pasta media na pasta raiz
```
.vscode
/upload_Dowload
/media
/uploadAndDowloadAPP
.gitgnore
manege.py
requirements.txt
```
## Configuraçao bd 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_bd',
        'HOST': 'host_bd',
        'PORT': 'port_bd',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
```


## Para iniciar o sever 

```
python manage.py makemigrations

python manage.py migrate

python manege.py runserver

```