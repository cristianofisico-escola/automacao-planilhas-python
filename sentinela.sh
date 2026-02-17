#!/bin/bash
while true
do
  # Define o fuso horário para Brasília/São Paulo
  export TZ="America/Sao_Paulo"
  
  HORA=$(date +'%H:%M:%S')
  PROXIMA=$(date -d "+10 minutes" +'%H:%M:%S')
  
  echo "-----------------------------------------------------"
  echo "[$HORA] 🇧🇷  Sentinela (BR): Iniciando backup..."
  
  ./salvar.sh
  
  echo "[$HORA] ✅ Conferência finalizada."
  echo "[$HORA] ⏳ Próxima verificação às $PROXIMA."
  echo "-----------------------------------------------------"
  
  sleep 600
done
