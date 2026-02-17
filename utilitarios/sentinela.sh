# =========================================================================
# 📝 COLA PARA O TERMINAL (BACKUP AUTOMÁTICO):
# ./utilitarios/sentinela.sh
# =========================================================================
# DICA: Deixe este comando rodando em um terminal separado (Terminal 1).

#!/bin/bash

# 1. Garante que o script execute a partir da pasta onde ele está (utilitarios)
cd /workspaces/automacao-planilhas-python/utilitarios

while true
do
  # 2. Configura o fuso horário e calcula as horas
  export TZ="America/Sao_Paulo"
  HORA=$(date +'%H:%M:%S')
  PROXIMA=$(date -d "+10 minutes" +'%H:%M:%S')
  
  echo "-----------------------------------------------------"
  echo "[$HORA] 🇧🇷 Sentinela: Iniciando ciclo de backup..."
  
  # 3. Executa o script de salvar que está na mesma pasta
  # Usamos ./salvar.sh porque agora o 'cd' acima já nos colocou na pasta correta
  chmod +x salvar.sh
  ./salvar.sh
  
  echo "[$HORA] ✅ Backup processado."
  echo "[$HORA] ⏳ Próxima verificação agendada para: $PROXIMA"
  echo "-----------------------------------------------------"
  
  # 4. Aguarda 10 minutos (600 segundos)
  sleep 600
done
