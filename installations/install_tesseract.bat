@echo off
echo Downloading the Tesseract OCR installer...
curl -L "https://github.com/UB-Mannheim/tesseract/releases/download/v5.5.0.20241111/tesseract-ocr-w64-setup-5.5.0.20241111.exe" -o "%TEMP%\tesseract_installer.exe"
if %errorlevel% neq 0 (
    echo Failed to download the installer possibly due to your internet.
    pause
    exit /b 1
)
echo Downloaded, launching installer
echo After installing, restart your macro.
start "" "%TEMP%\tesseract_installer.exe"
pause