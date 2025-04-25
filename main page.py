import streamlit as st
import random
import time
import base64
from questions import questions

# 로컬 이미지 base64 변환 함수
def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(page_title="전략기획본부 랜덤 질문기", layout="centered", initial_sidebar_state="collapsed")

if "global_history" not in st.session_state:
    st.session_state.global_history = set()
if "current_speaker_history" not in st.session_state:
    st.session_state.current_speaker_history = set()
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "is_loading" not in st.session_state:
    st.session_state.is_loading = False
if "suppress_thinking" not in st.session_state:
    st.session_state.suppress_thinking = False
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True
if "first_question" not in st.session_state:
    st.session_state.first_question = True

# 스타일 정의
st.markdown("""
<style>
.big-question {
    font-size: 100px;
    text-align: center;
    padding: 80px 60px;
    font-weight: bold;
    animation: fadeIn 1s ease-in-out;
    max-width: 80%;
    margin: 80px auto;
    word-break: keep-all;
    line-height: 1.2;
    border-radius: 50px;
    background: #ffffff;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    border: 4px solid #dddddd;
    position: relative;
}
.vs-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 100px;
    gap: 40px;
}
.vs-bubble {
    font-size: 72px;
    font-weight: bold;
    padding: 60px 50px;
    background: #fff;
    border-radius: 50px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    border: 4px solid #dddddd;
    word-break: keep-all;
    max-width: 35%;
    text-align: center;
}
.vs-center {
    font-size: 100px;
    font-weight: bold;
    color: #ff5252;
}
.ai-center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 120px;
}
.ai-center-container img {
    width: 160px;
    height: 160px;
}
.ai-thought {
    background: #f0f4ff;
    color: #333;
    font-size: 36px;
    padding: 25px 40px;
    border-radius: 50px;
    box-shadow: 4px 4px 18px rgba(0,0,0,0.2);
    margin-top: 30px;
    text-align: center;
    max-width: 1000px;
    animation: fadeIn 1s ease-in-out;
}
.block-container {
    max-width: 90% !important;
    padding-left: 3rem;
    padding-right: 3rem;
}
@keyframes fadeIn {
    0% { opacity: 0; transform: scale(0.95); }
    100% { opacity: 1; transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🗣️ 전략기획본부 랜덤 인터뷰 : 진실 혹은 TMI</h1>", unsafe_allow_html=True)

img64 = get_image_base64("ai.png")
image_tag = f"<img src='data:image/png;base64,{img64}' width='160' height='160'>"

# 버튼 라벨 설정
label_text = "🙋‍♂️ 이제 자기소개 분석 시작해줘" if st.session_state.first_visit else "🙋‍♂️ 다음 자기소개 분석 시작해줘"
button_text = "🎯 이제 질문 추천해줘" if st.session_state.first_question else "🎯 다음 질문 추천해줘"

# 버튼 UI 중앙 배치
col1, col2, col3, col4 = st.columns([1, 3, 3, 1])
with col2:
    if st.button(label_text, key="speaker"):
        for q_text, repeatable in questions:
            if not repeatable and q_text in st.session_state.current_speaker_history:
                st.session_state.global_history.add(q_text)
        st.session_state.current_speaker_history = set()
        st.session_state.current_question = ""
        st.session_state.is_loading = False
        st.session_state.first_visit = False
        st.session_state.first_question = True
        st.session_state.suppress_thinking = False
        st.rerun()

with col3:
    if st.button(button_text, key="question"):
        st.session_state.current_question = ""
        st.session_state.is_loading = True
        st.session_state.suppress_thinking = True
        st.session_state.first_question = False
        st.rerun()

# 질문 상태 표현
if st.session_state.is_loading:
    loading_text = random.choice([
        "🤔 어떤 질문이 좋을까나?", "🌀 질문 회전 중...", "💭 질문을 고민 중이에요", "🔍 알맞은 질문을 찾는 중입니다",
        "🧠 질문 알고리즘 가동 중...", "🎲 오늘의 운명 질문은?", "👀 재미있는 질문을 골라볼게요!",
        "🧩 조각을 맞추는 중...", "✨ 질문을 마법처럼 뽑는 중입니다!", "⏳ 잠깐만요, 질문 생성 중!",
        "📚 질문 리스트 정렬 중...", "😎 괜찮은 질문 찾는 중이니까 조금만 기다려주세요!",
        "🎯 정답 같은 질문을 찾아가는 중...", "🌐 질문 로딩 중... 연결은 원활합니다!", "🧙‍♂️ 질문 마법사가 작동 중이에요",
        "다른 질문도 추천해볼게요!", "질문 바꿔달라고 하신 거 맞죠? 😊", "그럼 조금 다른 각도에서 하나 더 드릴게요!",
        "이건 어떤가요?"
    ])
    st.markdown(f"""
        <div class='ai-center-container'>
            {image_tag}
            <div class='ai-thought'>{loading_text}</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
    available_questions = [
        (q, r) for q, r in questions
        if (r or q not in st.session_state.global_history) and q not in st.session_state.current_speaker_history
    ]
    selected = random.choice(available_questions)
    st.session_state.current_question = selected[0]
    st.session_state.current_speaker_history.add(selected[0])
    st.session_state.is_loading = False
    st.session_state.suppress_thinking = False
    st.rerun()

elif st.session_state.current_question:
    is_vs = " vs " in st.session_state.current_question and not st.session_state.current_question.endswith("방식은?")
    if is_vs:
        parts = st.session_state.current_question.split(" vs ")
        left = parts[0].strip()
        right = parts[1].strip()
        st.markdown(f"""
            <div class='vs-container'>
                <div class='vs-bubble'>{left}</div>
                <div class='vs-center'>VS</div>
                <div class='vs-bubble'>{right}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='big-question'>{st.session_state.current_question}</div>", unsafe_allow_html=True)

elif not st.session_state.suppress_thinking:
    thinking_text = "안녕하세요! 자기소개를 시작할 준비가 되면 말씀해주세요!" if st.session_state.first_visit else "자기소개 들으며 좋은 질문 생각 중..."
    st.markdown(f"""
        <div class='ai-center-container'>
            {image_tag}
            <div class='ai-thought'>{thinking_text}</div>
        </div>
    """, unsafe_allow_html=True)
