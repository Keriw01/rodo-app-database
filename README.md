# Windows, w folderze projektu: <br />
Set-ExecutionPolicy Unrestricted -Scope Process <br />
venv\Scripts\Activate.ps1 <br />
Set-ExecutionPolicy Restricted -Scope Process <br />

pip install -r requirements.txt #Instalacja określonych bibliotek <br />
docker-compose up -d #Uruchomi kontenery w tle <br />
uvicorn main:app --host 0.0.0.0 --port 8000 --reload #Uruchomienie FastApi http://127.0.0.1:8000/docs <br />
