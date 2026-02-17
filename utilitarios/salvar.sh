#!/bin/bash

# 1. Entra na pasta principal do projeto (onde está o .git)
cd /workspaces/automacao-planilhas-python

# 2. Adiciona TUDO (incluindo as pastas novas e subpastas)
git add -A

# 3. Faz o commit com a data e hora atual
git commit -m "Backup Automático - $(date +'%d/%m/%Y %H:%M:%S')"

# 4. Envia para o GitHub
git push origin main

echo "🚀 [$(date +'%H:%M:%S')] GitHub Atualizado!"
