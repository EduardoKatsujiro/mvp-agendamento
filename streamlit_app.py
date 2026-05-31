import streamlit as st
import datetime
import urllib.parse

# Configuracao da pagina para modo responsivo (Mobile First)
st.set_page_config(page_title="Sistema de Agendamento", layout="centered")

# Cabecalho institucional e limpo
st.title("Sistema de Agendamento Online")
st.write("Selecione a data, o horario desejado e preencha seus dados para realizar a marcacao.")

st.divider()

# --- SELECAO DE DATA E HORARIO ---
st.markdown("### 1. Dados do Atendimento")

# Selecao de data (bloqueando dias passados)
data_selecionada = st.date_input("Data do atendimento:", min_value=datetime.date.today())

# Lista de horarios disponiveis para a grade do profissional
horarios_disponiveis = [
    "09:00", "10:00", "11:00", "13:00", 
    "14:00", "15:00", "16:00", "17:00"
]
horario_selecionado = st.selectbox("Horarios disponiveis:", horarios_disponiveis)

st.divider()

# --- DADOS DO CLIENTE ---
st.markdown("### 2. Informacoes de Contato")
nome = st.text_input("Nome completo:")
telefone = st.text_input("Numero do WhatsApp (com DDD):", placeholder="Ex: 47999999999")

st.divider()

# --- INTEGRACAO COM O WHATSAPP ---
# Numero do profissional que recebera as notificacoes
WHATSAPP_PROFISSIONAL = "5547999999999" 

if st.button("Confirmar Horario", use_container_width=True):
    if not nome.strip() or not telefone.strip():
        st.error("Por favor, preencha todos os campos obrigatorios antes de prosseguir.")
    else:
        # Texto formal e diretoizado para o envio
        mensagem = (
            f"Solicitacao de Agendamento\n\n"
            f"Cliente: {nome}\n"
            f"Data: {data_selecionada.strftime('%d/%m/%Y')}\n"
            f"Horario: {horario_selecionado}\n"
            f"Contato: {telefone}\n\n"
            f"Enviado via Plataforma de Agendamento Comunitario."
        )
        
        # Codificacao padrao de URL
        texto_codificado = urllib.parse.quote(mensagem)
        url_whatsapp = f"https://api.whatsapp.com/send?phone={WHATSAPP_PROFISSIONAL}&text={texto_codificado}"
        
        # Mensagem informativa de conclusao de etapa
        st.success("Horario selecionado com sucesso.")
        st.markdown(f"[Clique aqui para enviar a confirmacao via WhatsApp]({url_whatsapp})")

# --- RODAPE ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.caption("Projeto de Extensao Universitaria — UNIVALI. Todos os direitos reservados.")
