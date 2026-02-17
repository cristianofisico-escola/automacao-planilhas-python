#!/bin/bash
while true
do
  HORA=$(date +'%H:%M:%S')
  echo "-----------------------------------------------------"
  echo "[$HORA] 🛡️  Sentinela: Iniciando conferência de backup..."
  
  # Tenta rodar o seu script de salvar
  ./salvar.sh
  
  echo "[$HORA] ✅ Conferência finalizada."
  echo "[$HORA] ⏳ Próxima verificação em 10 minutos (às $(date -d "+10 minutes" +%H:%M:%S))."
  echo "-----------------------------------------------------"
  
  sleep 600
done
