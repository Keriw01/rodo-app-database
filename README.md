# Instrukcja Uruchomienia Projektu

Projekt można uruchomić na dwa sposoby: za pomocą Dockera lub w środowisku lokalnym.

## Opcja 1: Uruchomienie w Dockerze

### Wymagania
- Docker
- Docker Compose

> **Uwaga:** Projekt działa w kontenerach Docker, lokalne środowisko Pythona (venv) nie jest wymagane.

### Instrukcje
1. Przejdź do folderu projektu:
   ```bash
   cd ścieżka/do/projektu
   ```

2. Uruchom projekt:
   ```bash
   docker-compose up --build    # lub "docker-compose up --build -d" dla działania w tle
   ```

3. Sprawdź API:
   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

4. Zatrzymaj:
   ```bash
   docker-compose down          # lub "docker-compose down -v" aby usunąć dane MongoDB
   ```

## Opcja 2: Uruchomienie Lokalne

### Wymagania
- Python 3.13.2
- MongoDB (zainstalowane lokalnie)

> **Uwagi:**
> - Pobierz i zainstaluj Python 3.13.2: https://www.python.org/downloads/
> - Pobierz i zainstaluj MongoDB: https://www.mongodb.com/try/download/community

### Instrukcje
1. Przejdź do folderu projektu:
   ```bash
   cd ścieżka/do/projektu
   ```

2. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   
   # Jeśli poniższa komenda nie działa (błąd zasad wykonywania), wykonaj:
   # Set-ExecutionPolicy Unrestricted -Scope Process
   .\venv\Scripts\Activate.ps1
   ```

3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

4. Uruchom MongoDB lokalnie:
   ```bash
   # Upewnij się, że MongoDB jest zainstalowane i ścieżka do "mongod" jest w zmiennej PATH.
   # W nowym terminalu uruchom:
   mongod
   # Domyślnie MongoDB działa na localhost:27017 bez uwierzytelniania.
   ```

5. Zaktualizuj połączenie do MongoDB:
   ```python
   # Otwórz plik database.py i zmień linię:
   # client = MongoClient("mongodb://mongo:27017/")
   # na:
   # client = MongoClient("mongodb://localhost:27017/")
   # Zapisz zmiany.
   ```

6. Uruchom aplikację:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

7. Sprawdź API:
   - http://127.0.0.1:8000/docs
   - http://127.0.0.1:8000/redoc

8. Zatrzymaj i wyłącz środowisko:
   ```bash
   # Zatrzymaj uvicorn: Ctrl+C
   # Zatrzymaj MongoDB: Ctrl+C w terminalu z mongod
   deactivate
   # Jeśli użyto Set-ExecutionPolicy wcześniej, przywróć domyślne ustawienia:
   # Set-ExecutionPolicy Restricted -Scope Process
   ```
