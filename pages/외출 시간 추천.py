import streamlit as st
from datetime import datetime, timedelta, time
import random

# 1. 페이지 기본 설정 및 프리미엄 다크 로열 테마 적용
st.set_page_config(
    page_title="SnoozeWise | 집돌이·집순이 탈출 타이머",
    page_icon="⏰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 고급스러운 야간/우주 테마와 마이크로인터랙션(Hover Scale) 전용 CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');
    
    /* 기본 폰트 및 모션 백그라운드 디자인 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 스무스 애니메이션 정의 */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseWarning {
        0%, 100% { border-color: rgba(245, 158, 11, 0.3); box-shadow: 0 0 15px rgba(245, 158, 11, 0.1); }
        50% { border-color: rgba(245, 158, 11, 0.7); box-shadow: 0 0 25px rgba(245, 158, 11, 0.3); }
    }
    @keyframes pulseDanger {
        0%, 100% { border-color: rgba(239, 68, 68, 0.3); box-shadow: 0 0 15px rgba(239, 68, 68, 0.1); }
        50% { border-color: rgba(239, 68, 68, 0.7); box-shadow: 0 0 25px rgba(239, 68, 68, 0.3); }
    }

    /* 메인 브랜딩 컨테이너 */
    .header-container {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
        animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .brand-logo {
        font-size: 3.2rem;
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #a5b4fc 0%, #818cf8 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .brand-desc {
        font-size: 1.1rem;
        color: #94a3b8;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* 반응형 프리미엄 리포트 박스 */
    .premium-status-box {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border-radius: 24px;
        padding: 2.2rem;
        margin-top: 1.5rem;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    /* 상황별 맞춤 상태 테두리 애니메이션 */
    .status-safe {
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.05);
    }
    .status-warning {
        border: 1px solid rgba(245, 158, 11, 0.3);
        animation: pulseWarning 2.5s infinite ease-in-out;
    }
    .status-danger {
        border: 1px solid rgba(239, 68, 68, 0.3);
        animation: pulseDanger 2.5s infinite ease-in-out;
    }

    /* 동적 리포트 폰트 스타일 */
    .time-title {
        color: #e2e8f0;
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        margin-bottom: 0.3rem;
    }

    .time-display {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -1px;
        margin-bottom: 0.8rem;
    }

    .status-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }

    .badge-safe { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-warning { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-danger { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }

    /* 글래스 모피즘 카드 */
    .glass-inner-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.04);
        padding: 1.5rem;
        border-radius: 18px;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .glass-inner-card:hover {
        background: rgba(255, 255, 255, 0.04);
        border-color: rgba(255, 255, 255, 0.08);
    }

    /* 스트림릿 기본 인풋 폼 리디자인 */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.07) !important;
        border-radius: 24px !important;
        padding: 2rem !important;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.25) !important;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    /* 커스텀 버튼 고도화 */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        border: none !important;
        color: #fff !important;
        padding: 0.6rem 2rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2) !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.45) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. 프리미엄 메인 헤더
st.markdown(
    """
    <div class="header-container">
        <div class="brand-logo">SnoozeWise</div>
        <div class="brand-desc">⏰ OUTING ARCHITECT & TIMER</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 세션 상태 초기화 (재미있는 잔소리 수동 갱신용)
if "nag_message" not in st.session_state:
    st.session_state.nag_message = ""

# 3. 프리미엄 입력 구간
with st.form(key="outing_form"):
    st.markdown("<h4 style='color: #c7d2fe; font-weight:600; margin-bottom: 1.5rem;'>📝 오늘의 탈출 스케줄 설계</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        appointment_time = st.time_input("🎯 약속 시간은 언제인가요?", time(18, 0))
        travel_time = st.number_input("🚗 예상 이동 시간 (분 단위)", min_value=5, max_value=300, value=30, step=5)
        
    with col2:
        purpose = st.selectbox(
            "📍 오늘의 외출 목적은?",
            ["중요한 비즈니스", "이성과의 데이트", "친구들과의 소소한 모임", "귀찮지만 가야 하는 출근/등교", "숨쉬듯 자연스러운 덕질"]
        )
        persona = st.radio(
            "🔊 맞춤 알림 스타일 선택",
            ["팩트폭행형", "둥둥이 응원형", "스파르타 교관형"],
            horizontal=True
        )

    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="🧬 개인화 출발 타이밍 산출 시작")

# 4. 연산 및 동적 시각화 영역
now = datetime.now()
appointment_datetime = datetime.combine(now.date(), appointment_time)

# 약속 시간이 이미 지났다면 다음날(내일)로 보정 처리
if appointment_datetime < now:
    appointment_datetime += timedelta(days=1)

# 출발 필요 시각 및 남은 시간(분) 정밀 연산
departure_datetime = appointment_datetime - timedelta(minutes=travel_time)
time_left = departure_datetime - now
minutes_left = int(time_left.total_seconds() / 60)

# 출력 문자열 가공
departure_str = departure_datetime.strftime("%H시 %M분")

# 시간 흐름 단계에 따른 다이내믹 그라데이션 스타일 결정
if minutes_left > 60:
    status_class = "status-safe"
    badge_class = "badge-safe"
    status_badge_text = "🟢 평온 단계: 침대와 한몸 유지 가능"
    feedback_msg = f"여유 부릴 시간이 무려 {minutes_left // 60}시간 {minutes_left % 60}분이나 남았습니다. 아직은 미동조차 하지 않아도 무죄입니다."
elif 0 <= minutes_left <= 60:
    status_class = "status-warning"
    badge_class = "badge-warning"
    status_badge_text = "🟡 경보 단계: 초고속 기상 모드 가동"
    feedback_msg = f"🚨 긴급! 출발까지 단 **{minutes_left}분** 남았습니다. 스마트폰을 내려놓고 양치하면서 입을 옷을 빠르게 매칭해 보세요."
else:
    status_class = "status-danger"
    badge_class = "badge-danger"
    status_badge_text = "🔴 멸망 단계: 시공간 붕괴 현상 발생"
    feedback_msg = f"☠️ 이미 {abs(minutes_left)}분 전에 집 밖으로 탈출했어야 했습니다. 즉시 카카오T를 호출하거나 진심 어린 대가리 사과 메시지 작성을 권장합니다."

# 5. 리포트 메인 카드 렌더링
st.markdown(
    f"""
    <div class="premium-status-box {status_class}">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
            <h3 style="margin: 0; color: #fff; font-weight: 700;">🚀 SNOOZEWISE 맞춤형 탈출 오더</h3>
            <span class="status-badge {badge_class}">{status_badge_text}</span>
        </div>
        <div class="time-title">현관문을 열고 반드시 박차고 나가야 할 시각</div>
        <div class="time-display">{departure_str}</div>
        <div class="glass-inner-card">
            <span style="color: #94a3b8; font-size: 0.85rem; display: block; margin-bottom: 0.3rem;">🚨 현 상황 디렉팅</span>
            <p style="color: #f1f5f9; margin: 0; font-size: 1rem; line-height: 1.6;">{feedback_msg}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 6. 재미있는 맞춤형 잔소리 생성기 (고급 패널로 감싸기)
nags = {
    "팩트폭행형": [
        f"누가 보면 {purpose}에 목숨 안 건 줄 알겠어요. 지금 안 나가면 물리적으로 무조건 지각입니다.",
        "당신의 '지금 출발함'이라는 텍스트가 거짓말인 것쯤은 온 세상 친구들이 이미 간파하고 있습니다. 신발 끈 묶으세요.",
        f"이동 시간 {travel_time}분은 축지법 기준이 아닙니다. 엄격한 우주 물리 법칙을 존중하십시오."
    ],
    "둥둥이 응원형": [
        f"오늘 {purpose} 현장에서 당신이 가장 눈부실 예정! 지각해서 숨 가쁘게 들어가면 속상하잖아요. 우아하게 세레머니 하듯 가봅시다! ✨",
        "할 수 있습니다! 머리 감기부터 패션 장착까지 초단기 10분 컴플리트 트라이얼 도전!",
        "도착해서 미안해하는 눈물 젖은 사죄보다, 여유롭게 아이스 아메리카노 한 잔 든 멋진 등장이 훨씬 당신답습니다 😊"
    ],
    "스파르타 교관형": [
        f"정신 똑바로 안 차립니까? {purpose}(이)가 애들 장난입니까? 지금 당장 침대 스프링에서 로켓처럼 발사되십시오.",
        "당신의 나태한 미지근함이 소중한 인간관계를 조용히 파괴하고 있습니다. 180초 내로 양말을 신지 않으면 즉시 탈락입니다.",
        "움직이십시오! 패배자는 이불 속에 누워 변명을 생산하고, 진정한 위너는 약속 장소에 10분 먼저 골인해 미소를 짓습니다!"
    ]
}

# 정신 자극 메시지 카드
col_btn, col_empty = st.columns([1, 1])

with col_btn:
    if st.button("🔥 내 정신을 깨우는 프리미엄 한마디 보기"):
        st.session_state.nag_message = random.choice(nags[persona])

if st.session_state.nag_message:
    st.markdown(
        f"""
        <div class="premium-status-box" style="margin-top: 1rem; background: rgba(99, 102, 241, 0.08); border: 1px dashed rgba(99, 102, 241, 0.3); animation: fadeInUp 0.5s ease-out both;">
            <span style="font-weight: 700; color: #a5b4fc; display: block; margin-bottom: 0.5rem;">💬 [{persona}] 멘탈 스트레칭 자극</span>
            <p style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.6; font-style: italic; margin: 0;">"{st.session_state.nag_message}"</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# 7. 명품 감성의 하단 푸터 영역
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.85rem; padding-bottom:2rem;">
        <p>SnoozeWise Premium Outing Architect — 시간 약속을 지키는 힘</p>
        <p style="margin-top:0.3rem; font-family:'Playfair Display', serif; font-style:italic; color:#818cf8;">Master your schedule, control your day.</p>
    </div>
    """,
    unsafe_allow_html=True
)
