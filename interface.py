import streamlit as st

def configurar_estetica():
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
    
    