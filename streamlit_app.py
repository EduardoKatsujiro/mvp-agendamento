import streamlit as st
import datetime
import urllib.parse

# Configuracao da pagina com layout centralizado
st.set_page_config(page_title="Plataforma de Agendamento", layout="centered")

# Cabecalho
st.title("Sistema de Agendamento Online")
st.write("Preencha os campos abaixo para realizar a sua marcaçao de forma direta.")

st.write("---")

# --- SELECIONE DATA E HORARIO ---
st.subheader("1. Dados do Atendimento")

# Calendario selecionavel configurado no padrao brasileiro (DD/MM/AAAA)
data_selecionada = st.date_input(
    label="Selecione a data do atendimento:",
    value=datetime.date.today(),
    min_value=datetime.date.today(),
    format="DD/MM/YYYY" 
)

# Grade de horarios comerciais disponiveis
horarios_disponiveis = [
    "09:00", "10:00", "11:00", "13:00", 
    "14:00", "15:00", "16:00", "17:00"
]
horario_selecionado = st.selectbox("Selecione o horario disponivel:", horarios_disponiveis)

st.write("---")

# --- DADOS DO CLIENTE ---
st.subheader("2. Informacoes de Contato")
nome = st.text_input("Nome completo:")
telefone = st.text_input("Numero do WhatsApp (com DDD):", placeholder="Ex: 47999999999")

st.write("---")

# --- INTEGRACAO COM O WHATSAPP ---
WHATSAPP_PROFISSIONAL = "5547999999999" 

# Botao principal de validacao
if st.button("Confirmar Horario e Agendar", type="primary", use_container_width=True):
    if not nome.strip() or not telefone.strip():
        st.warning("Por favor, preencha todos os campos obrigatorios para prosseguir.")
    else:
        # Texto padronizado e formal para envio
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
        
        st.success("Dados validados com sucesso! Clique no botao abaixo para concluir.")
        
        # Botao nativo de link (Substitui o CSS bugado)
        st.link_button("Abrir no WhatsApp e Enviar Dados", url_whatsapp, use_container_width=True)

# --- RODAPE INSTITUCIONAL ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Projeto de Extensao Universitaria — UNIVALI. Todos os direitos reservados.")
