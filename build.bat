@echo off
setlocal
title RSUD Tigaraksa - Pelaporan Alat Kesehatan (Flask)

REM ==============================
REM 1. Pastikan Python terpasang
REM ==============================
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
  echo [ERROR] Python belum terpasang. Silakan install dari:
  echo https://www.python.org/downloads/
  pause
  exit /b 1
)

REM ==============================
REM 2. Aktifkan pip (kalau belum ada)
REM ==============================
python -m ensurepip --default-pip >nul 2>nul
python -m pip install --upgrade pip >nul 2>nul

REM ==============================
REM 3. Buat Virtual Environment
REM ==============================
if not exist .venv (
  python -m venv .venv
)
call .venv\Scripts\activate.bat

REM ==============================
REM 4. Install Dependencies
REM ==============================
pip install -r requirements.txt

REM ==============================
REM 5. Inisialisasi Database (optional)
REM ==============================
if exist app.db (
  echo Database sudah ada.
) else (
  echo Membuat database baru...
  python app.py --init-db
)

REM ==============================
REM 6. Cari IP Otomatis
REM ==============================
for /f "tokens=2 delims=:" %%A in ('ipconfig ^| findstr /R /C:"IPv4 Address" /C:"Alamat IPv4"') do (
  if not defined ip set ip=%%A
)
set ip=%ip: =%

REM ==============================
REM 7. Jalankan Flask Server
REM ==============================
start cmd /k "python app.py"

timeout /t 2 >nul

REM ==============================
REM 8. Buka Browser Otomatis
REM ==============================
start http://%ip%:5000

echo.
echo ========================================
echo Server Flask siap dijalankan
echo ----------------------------------------
echo Akses di komputer ini: http://localhost:5000
echo Akses dari LAN:        http://%ip%:5000
echo ========================================
echo Tekan tombol apapun untuk menutup...
pause >nul