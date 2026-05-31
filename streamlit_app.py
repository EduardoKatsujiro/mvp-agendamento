import streamlit as st
import datetime
import urllib.parse

# Configuracao da pagina com layout centralizado
st.set_page_config(
    page_title="Plataforma de Agendamento", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilizacao CSS para melhorar a interface, fontes e botoes (Design Moderno)
st.markdown("""
    <style>
    /* Alterar a fonte principal e fundo secundario */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Estilizar o bloco do titulo */
    .main-title {
        font-size: 28px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 8px;
    }
    .subtitle {
        font-size: 15px;
        color: #64748b;
        margin-bottom: 24px;
    }
    /* Deixar os blocos de secao com fundo branco (estilo Cards) */
    .css-1r6g72h, .stForm, div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecalho Customizado
st.markdown('<p class="main-title">Sistema de Agendamento Online</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Preencha os campos abaixo para realizar a sua marcacao de forma direta.</p>', unsafe_allow_html=True)

st.divider()

# --- SELECAO DE DATA E HORARIO ---
st.markdown("#### 1. Dados do Atendimento")

# Calendario selecionavel configurado no padrao brasileiro (DD/MM/AAAA)
data_selecionada = st.date_input(
    label="Selecione a data do atendimento:",
    value=datetime.date.today(),
    min_value=datetime.date.today(),
    format="DD/MM/YYYY"  # Forca a exibicao no formato do Brasil
)

# Grade de horarios comerciais disponiveis
horarios_disponiveis = [
    "09:00", "10:00", "11:00", "13:00", 
    "14:00", "15:00", "16:00", "17:00"
]
horario_selecionado = st.selectbox("Selecione o horario disponivel:", horarios_disponiveis)

st.divider()

# --- DADOS DO CLIENTE ---
st.markdown("#### 2. Informacoes de Contato")
nome = st.text_input("Nome completo:")
telefone = st.text_input("Numero do WhatsApp (com DDD):", placeholder="Ex: 47999999999")

st.divider()

# --- INTEGRACAO COM O WHATSAPP ---
WHATSAPP_PROFISSIONAL = "5547999999999" 

# Espacamento visual antes do botao
st.write("")

if st.button("Confirmar Horario e Agendar", use_container_width=True):
    if not nome.strip() or not telefone.strip():
        st.error("Por favor, preencha todos os campos obrigatorios para prosseguir.")
    else:
        # Texto padronizado e formal para envio comercial
        mensagem = (
            f"Solicitacao de Agendamento\n\n"
            f"Cliente: {nome}\n"
            f"Data: {data_selecionada.strftime('%d/%m/%Y')}\n"
            f"Horario: {horario_selecionado}\n"
            f"Contato: {telefone}\n\n"
            f"Enviado via Plataforma de Agendamento."
        )
        
        # Codificacao para URL do WhatsApp
        texto_codificado = urllib.parse.quote(mensagem)
        url_whatsapp = f"https://api.whatsapp.com/send?phone={WHATSAPP_PROFISSIONAL}&text={texto_codificado}"
        
        st.success("Horario selecionado. Prossiga para a confirmacao externa.")
        
        # Link estilizado em formato de aviso de acao
        st.markdown(
            f'<div style="text-align: center; margin-top: 15px;">'
            f'<a href="{url_whatsapp}" target="_blank" style="text-decoration: none; background-color: #25d366; color: white; padding: 12px 24px; border-radius: 6px; font-weight: bold; display: inline-block;">'
            f'Abrir no WhatsApp e Enviar Dados'
            f'</a>'
            f'</div>', 
            unsafe_allow_html=True
        )

# --- RODAPE INSTITUCIONAL ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.caption("Projeto de Extensao Universitaria — UNIVALI. Todos os direitos reservados.")
