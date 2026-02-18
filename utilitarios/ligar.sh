#!/bin/bash

# =========================================================================
# 📝 COLA PARA O TERMINAL:
# ./utilitarios/ligar.sh
# =========================================================================

# 1. Entra na pasta do projeto
cd /workspaces/automacao-planilhas-python

echo "-----------------------------------------------------"
echo "🛠️  INSTALANDO BIBLIOTECAS (Pode demorar uns segundos)..."

# 2. Força a instalação das bibliotecas essenciais
# Sem o gspread e oauth2client, o database.py quebra.
pip install flask pandas gspread oauth2client --quiet

echo "✅ Ambiente preparado com sucesso!"

# 3. Garante que o arquivo tem permissão de execução
chmod +x utilitarios/ligar.sh

# 4. Lembretes e Inicialização
echo "🌐 CELULAR: Confira se a Porta 5000 está em 'PUBLIC' na aba Ports!"
echo "🚀 INICIANDO O SISTEMA FLASK..."
echo "-----------------------------------------------------"

# 5. Roda o sistema
python3 app.py
sudo date -s "2026-02-18 00:51:30"