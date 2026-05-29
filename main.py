import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# --- CONFIGURAÇÃO VISUAL DE ELITE ---
st.set_page_config(page_title="AXON | Inteligência Comercial", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #0B0E14; }
    [data-testid="stSidebar"] { background-color: #121620; border-right: 1px solid #2D333D; }
    .main-card { background-color: #1A1F2B; padding: 20px; border-radius: 12px; border: 1px solid #2D333D; margin-bottom: 15px; }
    .axon-gradient {
        background: linear-gradient(90deg, #00D4FF 0%, #0047AB 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; font-size: 24px;
    }
    .metric-value { font-size: 28px; font-weight: bold; color: #00D4FF; }
    </style>
    """, unsafe_allow_html=True)

# --- SIMULAÇÃO DE BANCO DE DADOS ---
if 'db_produtos' not in st.session_state:
    st.session_state.db_produtos = pd.DataFrame([
        {"id": 1, "nome": "Camiseta Premium", "estoque": 45, "custo": 35.0, "venda": 89.90, "giro": "Alto"},
        {"id": 2, "nome": "Calça Slim Fit", "estoque": 12, "custo": 80.0, "venda": 189.90, "giro": "Médio"},
        {"id": 3, "nome": "Tênis Urban", "estoque": 4, "custo": 120.0, "venda": 299.90, "giro": "Crítico"}
    ])

if 'db_vendas' not in st.session_state:
    st.session_state.db_vendas = pd.DataFrame(columns=["Data", "Produto", "Qtd", "Total", "Lucro"])

# --- BARRA LATERAL (Navegação) ---
with st.sidebar:
    st.markdown('<p class="axon-gradient">🧬 AXON SYSTEM</p>', unsafe_allow_html=True)
    st.caption("v1.0.4 | Umuarama-PR")
    st.markdown("---")
    aba = st.radio("MENU PRINCIPAL", ["🏠 Visão Geral", "🛒 Frente de Caixa", "📦 Estoque Inteligente", "🧠 AXON Mind (IA)"])
    st.markdown("---")
    st.markdown("### 👤 Usuário\n**Admin - Master**")

# --- TELA: VISÃO GERAL ---
if aba == "🏠 Visão Geral":
    st.title("Painel de Controle")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="main-card"><p>Faturamento (Mês)</p><p class="metric-value">R$ 14.250,80</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="main-card"><p>Lucro Líquido</p><p class="metric-value">R$ 5.120,30</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="main-card"><p>Itens em Falta</p><p class="metric-value" style="color:#FF4B4B;">12</p></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="main-card"><p>Ticket Médio</p><p class="metric-value">R$ 185,40</p></div>', unsafe_allow_html=True)

    st.subheader("Performance de Vendas")
    df_grafico = pd.DataFrame({"Dia": list(range(1,31)), "Vendas": [100, 120, 90, 150, 200, 180, 250, 300, 280, 320]*3})
    fig = px.area(df_grafico, x="Dia", y="Vendas", color_discrete_sequence=['#00D4FF'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# --- TELA: FRENTE DE CAIXA ---
elif aba == "🛒 Frente de Caixa":
    st.title("Frente de Caixa (PDV)")
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        col_p, col_q = st.columns([3, 1])
        prod_selecionado = col_p.selectbox("Buscar Produto", st.session_state.db_produtos['nome'])
        qtd = col_q.number_input("Qtd", min_value=1, value=1)
        if st.button("FINALIZAR VENDA"):
            st.success(f"Venda de {prod_selecionado} registrada!")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA: ESTOQUE ---
elif aba == "📦 Estoque Inteligente":
    st.title("Gestão de Inventário")
    st.dataframe(st.session_state.db_produtos, use_container_width=True)

# --- TELA: AXON MIND ---
elif aba == "🧠 AXON Mind (IA)":
    st.title("🧠 AXON Mind")
    st.markdown('<div class="main-card"><h4>Relatório de Inteligência - Umuarama</h4><p>Análise preditiva ativa para o seu comércio.</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.error("📉 **Risco de Ruptura**\nO item 'Tênis Urban' tem apenas 4 unidades no estoque.")
    with c2: st.success("💰 **Oportunidade**\n'Camiseta Premium' em alta procura. Sugerimos ajuste sutil no preço.")
