import streamlit as st
import base64

# 페이지 기본 설정
st.set_page_config(page_title="자기소개 도우미 ver 1.0", layout="centered", initial_sidebar_state="collapsed")

# base64 이미지 인코딩 함수
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img64 = get_image_base64("ai.png")

# 스타일 정의
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #f5faff, #ffffff);
    }
    .intro-title {
        font-size: 88px;
        text-align: center;
        font-weight: bold;
        margin-top: 40px;
        white-space: nowrap;
    }
    .intro-subtitle {
        font-size: 24px;
        text-align: center;
        color: #666;
        margin-top: 10px;
    }
    .intro-highlight {
        font-size: 20px;
        text-align: center;
        color: #888;
        margin-top: 20px;
    }
    .launch-button {
        display: flex;
        justify-content: center;
        margin-top: 60px;
    }
    .launch-button button {
        font-size: 28px;
        padding: 20px 40px;
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .launch-button button:hover {
        background-color: #125d99;
        transform: scale(1.05);
    }
    .footer {
        position: fixed;
        bottom: 30px;
        right: 20px;
        text-align: right;
        font-size: 28px;
        color: gray;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 이미지 출력 (base64 방식)
st.markdown(f"<img src='data:image/png;base64,{img64}' width='140' style='display:block; margin:auto;'>", unsafe_allow_html=True)

# 타이틀 출력
st.markdown("<div class='intro-title'>자기소개 도우미 ver 1.0</div>", unsafe_allow_html=True)

# 서브타이틀 설명
st.markdown("<div class='intro-subtitle'>전략기획본부 직원들의 자기소개를 듣고,<br>적절한 질문을 던져주는 AI 도우미입니다.</div>", unsafe_allow_html=True)

# 추가 설명 문구
st.markdown("<div class='intro-highlight'>오늘도 멋진 이야기, 함께 들어볼까요?</div>", unsafe_allow_html=True)

# 버튼 출력
with st.container():
    st.markdown("<div class='launch-button'><a href='./main_page' target='_self'><button>🤖 도우미 실행하기</button></a></div>", unsafe_allow_html=True)

# 푸터 표시
st.markdown(
    """
    <div class="footer">
        기획 · 개발 : 정욱<br>AI 파트너 : ChatGPT
    </div>
    """,
    unsafe_allow_html=True
)
