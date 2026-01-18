@echo off
title Sistema - Backend FastAPI

echo ================================
echo  Iniciando o sistema...
echo ================================

cd /d C:\Users\Caio\Desktop\sistema_online\backend

echo.
echo Abrindo backend FastAPI...
echo (NAO FECHE ESTA JANELA)
echo.

uvicorn main:app --reload

pause
