# TodoAPI
Todo loyihasi uchun djangoda yozilgan rest api

## Mos keladigan python versiyalari
Python 3.6, 3.7, 3.8, 3.9 va 3.10
3.10 - versiya tavfsiya qilinadi

## Virtual muhitni yaratish

```console
python -m venv env
```

## Virtual muhitni aktivlashtirish
Har safar terminalni qayta ochganda virtual muhitni aktivlashtirish kerak
### Linux
```bash
source env/bin/activate
```

### Windows
cmd.exe
```bat
venv\Scripts\activate.bat
```
PowerShell
```bat
venv\Scripts\activate.ps1
```

## O'rnatish

Kerakli paketlarni o'rnatish uchun [pip](https://pip.pypa.io/en/stable/) paket menejeridan  foydalaning.

```console
pip install -r requirements.txt
```

## Ishga tushirish

```console
python manage.py runserver
```
