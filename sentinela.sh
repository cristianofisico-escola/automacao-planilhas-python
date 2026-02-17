# =========================================================================
# PARA LIGAR O BACKUP AUTOMÁTICO, COPIE E COLE O COMANDO ABAIXO NO TERMINAL:
# ./sentinela.sh
# =========================================================================

#!/bin/bash
while true
do
  export TZ="America/Sao_Paulo"
  HORA=$(date +'%H:%M:%S')
  PROXIMA=$(date -d "+10 minutes" +'%H:%M:%S')
  
  echo "-----------------------------------------------------"
  echo "[$HORA] 🇧🇷 Sentinela: Iniciando backup..."
  
  ./salvar.sh
  
  echo "[$HORA] ✅ Conferência finalizada."
  echo "[$HORA] ⏳ Próxima verificação às $PROXIMA."
  echo "-----------------------------------------------------"
  
  sleep 600
done
