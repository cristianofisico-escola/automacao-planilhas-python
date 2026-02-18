# COLA
#!/bin/bash

# =================================================================
# SCRIPT DE BACKUP - SISTEMA DE OCORRÊNCIAS
# =================================================================

# 1. Identifica a pasta onde o script está e entra nela
DIR_ATUAL="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR_ATUAL"

# 2. Define o nome do arquivo com timestamp
# O backup será salvo aqui mesmo na pasta 'utilitarios'
NOME_BACKUP="backup_ocorrencias_$(date +%Y%m%d_%H%M%S).zip"

echo "📂 Local de destino: $DIR_ATUAL"
echo "📦 Criando backup em $NOME_BACKUP..."

# 3. Sobe um nível para a raiz do projeto para zipar tudo de lá
cd ..

# 4. Comando ZIP:
# O arquivo é gerado dentro de 'utilitarios/' referenciando a raiz '.'
zip -r "utilitarios/$NOME_BACKUP" . \
    -x "node_modules/*" \
    ".git/*" \
    ".python-*-*" \
    "*.zip" \
    "venv/*" \
    "__pycache__/*" \
    ".cache/*" \
    ".devcontainer/*"

echo "---------------------------------------------------"
echo "✅ Backup finalizado com sucesso!"
echo "💾 Arquivo gerado em: utilitarios/$NOME_BACKUP"
echo "👉 DICA: Abra a pasta 'utilitarios', clique com o botão direito no .zip e baixe-o."
echo "---------------------------------------------------"
