@echo off
cd /d "%~dp0"
echo.
echo ==========================================
echo     MONITOR DE GERACAO - SERVICE ROLE
echo ==========================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Criando ambiente virtual...
    py -m venv .venv
    if errorlevel 1 (
        echo ERRO: Python nao encontrado.
        pause
        exit /b 1
    )
)

echo Instalando/verificando dependencias...
".venv\Scripts\python.exe" -m pip install -r requirements.txt

if not exist ".env" (
    echo.
    echo ERRO: arquivo .env nao encontrado.
    echo Copie .env.example para .env e informe a service_role.
    pause
    exit /b 1
)

echo.
echo Iniciando Monitor de Geracao...
echo Abra http://127.0.0.1:8080
echo.
".venv\Scripts\python.exe" app.py
pause
