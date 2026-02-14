import streamlit as st
from datetime import datetime
import pandas as pd
import database as db
import interface as ui

# 1. Estética
ui.configurar_estetica()

# 2. CACHE DE DADOS (O segredo da velocidade)
# O app só vai ao Google Sheets se o cache for limpo após gravar/excluir
@st.cache_data(show_spinner="Carregando dados...")
def carregar_registros_cache():
    return db.listar_registros()

@st.cache_data(ttl=600)
def carregar_configuracoes():
    return db.buscar_dados()

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'novo'

# --- FUNÇÕES DE AÇÃO ---

def acao_gravar():
    prof = st.session_state.get("sel_prof")
    mot = st.session_state.get("rad_mot")
    alu = st.session_state.get("mul_alu")
    desc = st.session_state.get("txt_desc", "")
    
    if alu:
        try:
            db.salvar_registro([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), prof, mot, ", ".join(alu), desc])
            st.session_state["mul_alu"] = []
            st.session_state["txt_desc"] = ""
            st.cache_data.clear() # Limpa o cache para forçar nova leitura após gravar
            st.toast("✅ Gravado!", icon="🎉")
        except Exception as e:
            st.error(f"Erro: {e}")

def acao_excluir():
    selecao = st.session_state.get("tabela_principal", {}).get("selection", {}).get("rows", [])
    if selecao:
        try:
            indice = selecao[0]
            db.excluir_registro(indice)
            st.cache_data.clear() # Limpa o cache para a linha sumir da tela na hora
            st.toast("🗑️ Excluído!", icon="✅")
        except Exception as e:
            st.error(f"Erro: {e}")

# --- INTERFACE ---

try:
    # Busca configurações (Professores/Alunos) - Rápido via Cache
    lista_prof, lista_mot, lista_alu = carregar_configuracoes()

    # Layout Cabeçalho
    col_tit, b1, b2, b3, b4, b_save = st.columns([0.28, 0.14, 0.14, 0.14, 0.14, 0.16])

    with col_tit:
        st.markdown('<div class="caixa-titulo"><h1>📝 Sistema Escolar</h1></div>', unsafe_allow_html=True)

    with b1:
        if st.button("📄 Novo", use_container_width=True):
            st.session_state.pagina = 'novo'; st.rerun()
    with b2:
        if st.button("🔍 Consultar", use_container_width=True):
            st.session_state.pagina = 'consultar'; st.rerun()
    with b4:
        # Pega a seleção da tabela sem recarregar o banco de dados
        selecao_viva = st.session_state.get("tabela_principal", {}).get("selection", {}).get("rows", [])
        pode_excluir = (st.session_state.pagina == 'consultar' and len(selecao_viva) > 0)
        
        st.button("❌ Excluir", 
                  use_container_width=True, 
                  disabled=not pode_excluir, 
                  type="primary" if pode_excluir else "secondary",
                  on_click=acao_excluir)

    with b_save:
        if st.session_state.pagina == 'novo':
            st.button("💾 Gravar", type="primary", use_container_width=True, on_click=acao_gravar)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- CONTEÚDO ---

    if st.session_state.pagina == 'novo':
        c_esq, c_dir = st.columns([0.2, 0.8], gap="small")
        with c_esq:
            st.markdown("### 👤 Professor")
            st.selectbox("P", options=lista_prof, key="sel_prof", label_visibility="collapsed")
            st.markdown("### 🏷️ Motivo")
            st.radio("M", options=lista_mot, key="rad_mot", label_visibility="collapsed")
        with c_dir:
            st.markdown("### 🎓 Alunos envolvidos")
            st.multiselect("A", options=lista_alu, key="mul_alu", label_visibility="collapsed")
            st.markdown("### 📄 Descrição")
            st.text_area("D", placeholder="Relato...", height=300, key="txt_desc", label_visibility="collapsed")

    elif st.session_state.pagina == 'consultar':
        st.markdown("### 🔍 Histórico de Registros")
        
        # USA O CACHE AQUI - Isso remove a lentidão da piscada
        dados_tabela = carregar_registros_cache()
        df = pd.DataFrame(dados_tabela)

        if not df.empty:
            st.dataframe(
                df, 
                use_container_width=True, 
                hide_index=True, 
                selection_mode="single-row", 
                on_select="rerun",
                key="tabela_principal" 
            )
        else:
            st.info("Nenhum registro encontrado.")

except Exception as e:
    st.error(f"Erro: {e}")
    