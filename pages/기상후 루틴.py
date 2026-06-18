import streamlit as st
import google.generativeai as genai
from datetime import datetime, time

# 1. 페이지 기본 설정 및 프리미엄 다크 로열 테마 적용
st.set_page_config(
    page_title="SnoozeWise | 미라클 모닝 루틴 플래너",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 고급스러운 야간/우주 테마와 마이크로인터랙션(Hover Scale) 전용 CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght=300;400;500;700&family=Playfair+Display:ital,wght=0,600;1,400&display=swap');
    
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
    @keyframes pulseGlow {
        0%, 100% { border-color: rgba(99, 102, 241, 0.3); box-shadow: 0 0 15px rgba(99, 102, 241, 0.1); }
        50% { border-color: rgba(99, 102, 241, 0.6); box-shadow: 0 0 25px rgba(99, 102, 241, 0.25); }
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
        border: 1px solid rgba(99, 102, 241, 0.2);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .pulse-card {
        animation: pulseGlow 3s infinite ease-in-out;
    }

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
        padding: 0.7rem 2.5rem !important;
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
        <div class="brand-desc">☀️ MIRACLE MORNING ROUTINE PLANNER</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 3. API 키 설정 및 예외 처리
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("⚠️ API 키가 설정되지 않았습니다. Streamlit Cloud의 Secrets에 'GEMINI_API_KEY'를 등록해주세요.")
    st.info("💡 설정 방법: Streamlit Cloud Dashboard -> App Settings -> Secrets 공간에 GEMINI_API_KEY = '내_API_키_값' 등록")
    st.stop()

# 4. 프리미엄 통합 입력 폼
with st.form(key="miracle_morning_form"):
    st.markdown("<h4 style='color: #c7d2fe; font-weight:600; margin-bottom: 1.5rem;'>📝 개인 아침 패턴 & 지향점 분석</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        wake_time = st.time_input("⏰ 1. 보통 몇 시에 눈을 뜨시나요?", value=time(7, 0))
        first_action = st.selectbox(
            "📱 2. 눈뜨자마자 가장 먼저 행하는 행동은?",
            ["스마트폰 확인", "스트레칭", "물 마시기", "바로 씻기", "다시 누워있기", "기타"]
        )
        
    with col2:
        phone_time = st.slider("⏳ 3. 침대 위 무의식적인 스마트폰 사용 시간 (분)", 0, 60, 15, step=5)
        breakfast = st.radio("🍎 4. 아침 식사 혹은 대용식 섭취 패턴", ["먹는다", "마시는 종류만(커피/차/즙)", "먹지 않는다"], horizontal=True)

    st.markdown("---")
    user_goal = st.selectbox(
        "🎯 내가 도달하고 싶은 아침의 이상적인 모습",
        [
            "⚡ 피로를 빠르게 깨우고 활력을 얻는 아침 (에너지 충전)",
            "🧠 집중력을 높여 하루 생산성을 극대화하는 아침 (업무/공부 효율)",
            "🧘 되돌아보며 여유롭고 마음이 차분해지는 아침 (힐링/명상)",
            "🏃 체력을 기르고 몸을 가볍게 만드는 아침 (운동/건강)"
        ]
    )

    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="🧬 AI 초정밀 아침 오거나이징 분석")

# 5. 분석 및 제안 기능 구현
if submit_button:
    if wake_time is None:
        st.warning("⚠️ 기상 시간을 정확하게 입력해주세요!")
    else:
        with st.spinner("✨ AI 라이프 코치가 당신을 위한 웰니스 모닝 타임라인을 구성 중입니다..."):
            wake_time_str = wake_time.strftime("%H시 %M분")
            
            # 고밀도 피드백을 유도하기 위한 페르소나 설계 프롬프트
            prompt = f"""
            너는 세계 최고의 습관 형성 및 생산성 코치야. 유저의 현재 기상 후 패턴을 분석하고, 유저가 원하는 아침의 바램에 맞춰 내일부터 즉시 실행 가능한 최적의 아침 패턴을 제안해줘.

            [유저의 현재 패턴]
            - 기상 시간: {wake_time_str}
            - 눈뜨자마자 하는 행동: {first_action}
            - 침대 위 스마트폰 사용 시간: {phone_time}분
            - 아침 식사 여부: {breakfast}

            [유저가 원하는 아침의 모습(바램)]
            - 목표: {user_goal}

            [답변 규칙 및 출력 양식]
            1. 현재 패턴의 장점과 개선해야 할 점(특히 스마트폰 사용이나 첫 행동 중심)을 부드럽고 격려하는 어조로 2줄 요약해줘.
            2. 유저가 선택한 '원하는 아침의 모습(목표)'에 완벽히 부합하는 '새로운 추천 아침 시간대별 루틴'을 타임라인 형태(예: 기상 직후, 기상 10분 후 등)로 구체적으로 작성해줘.
            3. 마지막에 내일부터 당장 실천할 수 있는 핵심 한 마디(Action Item)로 마무리해줘.
            """

            try:
                # 2.5-flash-preview-09-2025 프리미엄 모델 호출 규격 적용
                model = genai.GenerativeModel("gemini-2.5-flash-preview-09-2025")
                response = model.generate_content(prompt)
                
                # 가독성이 훌륭한 럭셔리 네온 글로우 카드로 결과 렌더링
                st.markdown(
                    f"""
                    <div class="premium-status-box pulse-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                            <h3 style="margin: 0; color: #fff; font-weight: 700;">🌟 SNOOZEWISE AI 모닝 아키텍트 분석</h3>
                            <span style="background: rgba(99, 102, 241, 0.2); color: #c7d2fe; border: 1px solid rgba(99, 102, 241, 0.4); padding: 6px 14px; border-radius: 30px; font-weight: 600; font-size: 0.85rem;">실시간 맞춤 분석 완료</span>
                        </div>
                        <div class="glass-inner-card" style="background: rgba(15, 23, 42, 0.5);">
                            <div style="color: #f1f5f9; font-size: 1.05rem; line-height: 1.8; white-space: pre-wrap;">{response.text}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            except Exception as e:
                st.error(f"API 호출 과정에서 예외가 발생했습니다. 아래 내용을 확인 후 다시 시도해 주세요. (에러: {e})")

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# 6. 명품 감성의 하단 푸터 영역
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.85rem; padding-bottom:2rem;">
        <p>SnoozeWise Premium Miracle Morning — 하루를 결정하는 첫 단추의 힘</p>
        <p style="margin-top:0.3rem; font-family:'Playfair Display', serif; font-style:italic; color:#818cf8;">Own your morning, elevate your life.</p>
    </div>
    """,
    unsafe_allow_html=True
)
