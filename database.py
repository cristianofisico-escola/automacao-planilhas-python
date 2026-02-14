import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 1. Função de Conexão (Preservada exatamente como a sua)
def conectar_planilha():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais-ocorrencias-profs.json", scope)
    client = gspread.authorize(creds)
    return client.open("Ocorrencias_profs_01")

# 2. Busca de Listas (Preservada exatamente como a sua)
def buscar_dados():
    planilha_mae = conectar_planilha()
    
    aba_prof = planilha_mae.worksheet("Página1")
    profs = [p for p in aba_prof.col_values(1)[1:] if p.strip() != ""]
    
    aba_tipos = planilha_mae.worksheet("Página2")
    tipos = [t for t in aba_tipos.col_values(1)[1:] if t.strip() != ""]
    
    aba_alunos = planilha_mae.worksheet("Página3")
    dados_alunos = aba_alunos.get_all_records() 
    
    lista_alunos_formatada = [
        f"{a['Turma']} - {a['Chamada']} - {a['Nome']}" 
        for a in dados_alunos 
        if str(a['Nome']).strip() != ""
    ]
    
    return profs, tipos, lista_alunos_formatada

# 3. Funções de CRUD (Ajustadas para evitar erros de resposta)

def salvar_registro(dados_linha):
    """Salva uma nova linha na aba Registros"""
    planilha_mae = conectar_planilha()
    aba_registro = planilha_mae.worksheet("Registros")
    # value_input_option='USER_ENTERED' evita o erro de Response 200 em muitas versões
    aba_registro.append_row(dados_linha, value_input_option='USER_ENTERED')

def listar_registros():
    """Retorna todos os registros salvos para a tela de Consulta"""
    planilha_mae = conectar_planilha()
    aba_registro = planilha_mae.worksheet("Registros")
    return aba_registro.get_all_records()

def excluir_registro(indice_vido_do_app):
    """
    Exclui a linha selecionada. 
    O app envia o índice 0, 1, 2... a planilha precisa de +2 (cabeçalho + 1)
    """
    planilha_mae = conectar_planilha()
    aba_registro = planilha_mae.worksheet("Registros")
    linha_real = indice_vido_do_app + 2
    aba_registro.delete_rows(linha_real)

def atualizar_registro(indice_linha, novos_dados):
    """Sobrescreve uma linha existente com novos dados"""
    planilha_mae = conectar_planilha()
    aba_registro = planilha_mae.worksheet("Registros")
    linha_real = indice_linha + 2
    letra_final = chr(64 + len(novos_dados)) 
    range_linha = f"A{linha_real}:{letra_final}{linha_real}"
    aba_registro.update(range_linha, [novos_dados], value_input_option='USER_ENTERED')
    