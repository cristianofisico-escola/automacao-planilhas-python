import streamlit as st
from datetime import datetime
import database as db

# --- 1. CONFIGURAÇÃO COM TÍTULO 2.0rem E BOTÕES PRÓXIMOS ---
st.set_page_config(page_title="Sistema Escolar Slim", layout="wide")

st.markdown("""
    <style>
    header, [data-testid="stHeader"], .stAppHeader { display: none !important; }
    
    .block-container {
        max-width: 98% !important; 
        padding-top: 0rem !important;    
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0rem !important;
    }

    /* AJUSTE DAS COLUNAS */
    [data-testid="column"] {
        margin-bottom: -15px !important; 
    }

    /* MOLDURA PARA 2.0rem */
    .caixa-titulo {
        height: 38px !important;        
        display: flex !important;
        align-items: center !important;  
        margin-top: 0px !important;
    }

    .caixa-titulo h1 {
        font-size: 2.0rem !important;    
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1 !important;
        white-space: nowrap !important;
    }

    /* BOTÕES VOLTANDO AO TAMANHO IDEAL */
    .stButton > button {
        height: 38px !important;         
        border-radius: 4px !important;
        background-color: #f0f2f6 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
    }
    
    /* LINHA DIVISÓRIA */
    hr { 
        margin-top: 2px !important;      
        margin-bottom: 10px !important; 
        border-top: 1px solid #ddd !important; 
    }

    /* FORMULÁRIO */
    h3 { margin-top: 0px !important; margin-bottom: 2px !important; font-size: 1.1rem !important; }
    .stForm { border: none !important; padding: 0px !important; }
    </style>
    """, unsafe_allow_html=True)

try:
    lista_professores, lista_motivos, lista_alunos = db.buscar_dados()

    # --- SESSÃO 1: REDISTRIBUIÇÃO DE ESPAÇO ---
    # Coluna do título menor (0.3) e botões maiores (0.17 cada)
    col_tit, b1, b2, b3, b4 = st.columns([0.3, 0.17, 0.17, 0.17, 0.17])

    with col_tit:
        st.markdown('<div class="caixa-titulo"><h1>📝 Sistema Escolar</h1></div>', unsafe_allow_html=True)

    with b1: st.button("📄 Novo", use_container_width=True)
    with b2: st.button("🔍 Consultar", use_container_width=True)
    with b3: st.button("✏️ Alterar", use_container_width=True)
    with b4: st.button("❌ Excluir", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- SESSÃO 3: CONTEÚDO ---
    with st.form("form_visual_compacto"):
        col_esq, col_dir = st.columns([0.2, 0.8], gap="small")
        with col_esq:
            st.markdown("### 👤 Professor")
            st.selectbox("P", options=lista_professores, label_visibility="collapsed")
            st.markdown("### 🏷️ Motivo")
            st.radio("M", options=lista_motivos, label_visibility="collapsed")
        with col_dir:
            st.markdown("### 🎓 alunos envolvidos")
            st.multiselect("A", options=lista_alunos, label_visibility="collapsed")
            st.markdown("### 📄 Descrição")
            st.text_area("D", placeholder="Relato...", height=300, label_visibility="collapsed")
        
        st.write("---")
        _, col_btn_save = st.columns([0.85, 0.15])
        with col_btn_save:
            st.form_submit_button("Gravar", use_container_width=True)

except Exception as e:
    st.error(f"Erro: {e}")
    