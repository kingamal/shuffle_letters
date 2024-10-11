# Projekt Django: Aplikacje do przetwarzania tekstu i walidacji PESEL

## Spis treści
- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Uruchamianie projektu](#uruchamianie-projektu)

## Opis
To jest projekt Django, który zawiera dwie aplikacje:
1. Aplikacja do przetwarzania tekstu - pozwala na wgranie pliku tekstowego, przestawiając litery w każdym wyrazie (z wyjątkiem pierwszej i ostatniej litery).
2. Walidator PESEL - umożliwia użytkownikom wprowadzenie numeru PESEL i sprawdzenie jego poprawności oraz uzyskanie dodatkowych informacji, takich jak data urodzenia i płeć.

## Wymagania
- Python 3.6 lub nowszy
- Django 4.0 lub nowszy
- Pip

## Instalacja
1. Sklonuj repozytorium na swój komputer
   ```
   git clone https://github.com/kingamal/shuffle_letters.git
   ```
2. Przejdź do katalogu projektu
   ```
   cd shuffle_letters
   ```
3. Utwórz i aktywuj wirtualne środowisko
   ```
   python -m venv venv
    .\venv\Scripts\activate   # Windows
    # source venv/bin/activate  # Mac/Linux
   ```
4. Zainstaluj wymagane pakiety
   ```
   pip install -r requirements.txt
   ```

## Uruchamianie projektu
1. Wykonaj migracje bazy danych
   ```
   python manage.py migrate
   ```
2. Uruchom serwer lokalny
   ```
   python manage.py runserver
   ```
3. Otwórz przeglądarkę i przejdź pod adres

http://127.0.0.1:8000/shuffle/   # Aplikacja do przetwarzania tekstu

http://127.0.0.1:8000/pesel/     # Aplikacja walidacji PESEL
