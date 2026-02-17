#!/bin/bash
while true
do
  echo "--- Iniciando backup automático ---"
  ./salvar.sh
  echo "--- Backup realizado. Próxima conferência em 10 minutos ---"
  sleep 600
done
