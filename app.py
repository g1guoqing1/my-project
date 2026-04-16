import streamlit as st
import streamlit.components.v1 as components

# 读取和app.py同目录下的index.html
with open("index.html", encoding="utf-8") as f:
    html_content = f.read()

# 渲染前端页面
components.html(
    html_content,
    height=800,    # 页面高度，可自行调整
    scrolling=True # 允许滚动
)