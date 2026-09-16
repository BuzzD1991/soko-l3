import streamlit as st

from common import RESOURCE_COLUMNS, inject_css, load_data

inject_css()

df_res, df_raw = load_data()

st.title("Ressourcen")

st.markdown("Weiterführende Materialien und externe Ressourcen.")

resource_columns = [col for col in RESOURCE_COLUMNS if col in df_res.columns]

st.dataframe(
    df_res[resource_columns],
    width="stretch",
    hide_index=True,
)
