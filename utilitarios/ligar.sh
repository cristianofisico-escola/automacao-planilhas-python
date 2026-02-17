# =========================================================================
# 📝 COLA PARA O TERMINAL:
# ./utilitarios/ligar.sh
# =========================================================================
# DICA: Use a "Seta para Cima" no teclado para repetir este comando!

#!/bin/bash

# 1. Garante que estamos na pasta correta do projeto
cd /workspaces/automacao-planilhas-python

echo "-----------------------------------------------------"
echo "🛠️  PREPARANDO AMBIENTE..."

# 2. Instala as bibliotecas caso o Codespaces as tenha removido
pip install flask pandas --quiet
echo "✅ Bibliotecas verificadas."

# 3. Lembretes importantes
echo "🌐 CELULAR: Confira se a Porta 5000 está em 'PUBLIC' na aba Ports!"
echo "🚀 INICIANDO O SISTEMA FLASK..."
echo "-----------------------------------------------------"

# 4. Inicia o servidor Python
python3 app.py
