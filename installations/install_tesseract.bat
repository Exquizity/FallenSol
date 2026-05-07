@echo off
if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set ARCH=w64
) else if "%PROCESSOR_ARCHITEW6432%"=="AMD64" (
    set ARCH=w64
) else (
    set ARCH=w32
)

echo Downloading installer
curl -L "https://github.com/UB-Mannheim/tesseract/releases/download/v5.5.0.20241111/tesseract-ocr-%ARCH%-setup-5.5.0.20241111.exe" -o "%TEMP%\tesseract_installer.exe"

if %errorlevel% neq 0 (
    echo Failed to download the installer possibly due to your internet.
    pause
    exit /b 1
)

echo Downloaded, launching installer
echo After installing, restart your macro.
start "" "%TEMP%\tesseract_installer.exe"
pause