import streamlit as st
import streamlit.components.v1 as components

# 页面配置：宽屏、隐藏侧边栏
st.set_page_config(
    page_title="我的前端应用",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏Streamlit默认菜单、页脚、右上角Deploy按钮
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 读取并渲染前端
with open("index.html", encoding="utf-8") as f:
    html_content = f.read()
components.html(html_content, height=1000, scrolling=True)
