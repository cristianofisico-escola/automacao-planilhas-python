#!/bin/bash
git add .
git commit -m "Backup Rápido: $(date +'%d/%m/%Y %H:%M')"
git push origin main
echo "✅ Backup concluído e enviado para o GitHub!"

