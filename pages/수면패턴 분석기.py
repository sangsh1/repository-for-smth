import streamlit as st
import google.generativeai as genai
import time as time_module

# 1. 페이지 설정 및 다크 골드 프리미엄 테마 적용
st.set_page_config(
    page_title="SnoozeWise | 프라이빗 AI 수면 분석",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 최고급 프라이빗 클리닉 감성의 Royal Gold & Deep Indigo 톤앤매너 CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');
    
    /* 기본 폰트 및 모션 백그라운드 디자인 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 애니메이션 설계 */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes goldGlow {
        0%, 100% { border-color: rgba(197, 168, 128, 0.2); box-shadow: 0 0 15px rgba(197, 168, 128, 0.05); }
        50% { border-color: rgba(197, 168, 128, 0.5); box-shadow: 0 0 25px rgba(197, 168, 128, 0.2); }
    }

    /* 로열 헤더 컨테이너 */
    .royal-header {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
        animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .royal-crest {
        font-family: 'Cinzel', serif;
        font-size: 1.5rem;
        letter-spacing: 6px;
        color: #c5a880;
        margin-bottom: 0.8rem;
    }
    
    .royal-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #f5efe6 0%, #c5a880 50%, #8a704c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .royal-desc {
        font-size: 1.1rem;
        color: #94a3b8;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* 럭셔리 글래스모피즘 메인 카드 */
    .luxury-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(197, 168, 128, 0.15);
        border-radius: 28px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .luxury-card:hover {
        transform: translateY(-5px);
        border-color: rgba(197, 168, 128, 0.35);
        box-shadow: 0 20px 45px rgba(197, 168, 128, 0.1);
    }
    
    .luxury-glow {
        animation: goldGlow 4s infinite ease-in-out;
    }

    /* 내포된 글래스 영역 */
    .glass-inner-prescription {
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid rgba(197, 168, 128, 0.1);
        padding: 2rem;
        border-radius: 20px;
        margin-top: 1.5rem;
    }

    /* 섹션 레이블 스타일 */
    .luxury-section-title {
        font-family: 'Cinzel', serif;
        color: #c5a880;
        font-weight: 600;
        font-size: 1.4rem;
        letter-spacing: 2px;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid rgba(197, 168, 128, 0.15);
        padding-bottom: 0.5rem;
    }

    /* 스트림릿 디폴트 Form 리스타일 */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.01) !important;
        border: 1px solid rgba(197, 168, 128, 0.12) !important;
        border-radius: 28px !important;
        padding: 2.2rem !important;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3) !important;
        animation: fadeInUp 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    /* 로열 버튼 디자인 */
    div.stButton > button {
        background: linear-gradient(135deg, #c5a880 0%, #8a704c 100%) !important;
        border: none !important;
        color: #0f172a !important;
        padding: 0.8rem 2.5rem !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 18px rgba(197, 168, 128, 0.25) !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(197, 168, 128, 0.45) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. 로열 메인 헤더
st.markdown(
    """
    <div class="royal-header">
        <div class="royal-crest">PRIVATE CLINIC</div>
        <div class="royal-title">SnoozeWise AI</div>
        <div class="royal-desc">⚜️ 프라이빗 AI 수면 컨설팅</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 3. AI 수면 컨설팅 로직 (안정성이 뛰어난 gemini-1.5-flash 탑재 및 지수 백오프 적용)
def get_ai_feedback(efficiency, debt, latency, wakes):
    # 지수 백오프 알고리즘 설계 (최대 5회 트라이)
    retries = 5
    delay = 1.0
    
    # 고급스러운 웰니스 처방 프롬프트 고도화
    prompt = f"""
    당신은 상류층을 위한 최고급 프라이빗 웰니스 클리닉의 최고 존엄 수면 고문 의사입니다. 
    아래의 정확한 신체 수면 데이터를 엄밀히 분석하여, VIP 고객만을 위한 단 하나의 고품격 맞춤 종합 리포트를 발행해 주십시오.
    모든 문장은 지극히 기품 있고 정중하며 신뢰감을 부여하는 궁극의 상류층 격식체(~옵니다, ~드립니다, ~하시길 권장하옵니다)로 아름답게 일관성을 유지해야 합니다.

    [고객의 수면 지표]
    - 수면 효율: {efficiency:.1f}%
    - 수면 부족량(목표 시각 대비): {debt:.1f}시간
    - 입면 대기 시간: {latency}분
    - 중간 각성 빈도: {wakes}회
    
    [처방지 양식 구조 가이드]
    1. 【 헌사 및 오늘 밤 수면 상태에 대한 고고한 진단 】 (우아한 서두 도입)
    2. 【 현 패턴 방치 시 발생 가능한 뇌 인지기능 및 자율신경계 의학적 고찰 】 (엄밀하고 과학적인 생리적 피드백)
    3. 【 오직 귀하만을 위해 설계하는 야간 명품 슬립 마스터 의식(Ritual) 2가지 】 (구체적이며 품격 있는 행동 가이드)
    """

    for i in range(retries):
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            
            # 100% 구동이 보장되는 고속 표준 모델로 에러 해결
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if i == retries - 1:
                return f"귀빈의 수면 일지를 정밀 검토하는 과정에서 통신 허브 지연이 관찰되었습니다. 불편을 드려 송구하오며, 잠시 후 다시 확인을 부탁드리옵니다. (상세 사유: {str(e)})"
            time_module.sleep(delay)
            delay *= 2

# 4. 사이드바 - 관제 시스템 세션
with st.sidebar:
    st.markdown("<h3 style='font-family: \"Cinzel\", serif; color:#c5a880; font-size:1.1rem;'>🔑 CONCIERGE SYSTEM</h3>", unsafe_allow_html=True)
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("현재 컨시어지 인증이 만료되었습니다.")
    else:
        st.success("VIP 컨설턴트 시스템 로딩 완료")

# 5. 수면 데이터 입력 세션
st.markdown(
    """
    <div class="luxury-card">
        <div class="luxury-section-title">📝 DAILY SLEEP JOURNAL</div>
        <p style="color: #94a3b8; font-size: 0.9rem; margin-top: -0.8rem; margin-bottom: 1.5rem;">
            어젯밤 귀하께서 마주하신 침실 내부의 미시적 정황을 평온한 마음으로 작성해 주시기 바랍니다.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("luxury_sleep_form"):
    col1, col2 = st.columns(2)
    with col1:
        target = st.number_input("🎯 귀하에게 최적인 목표 수면 시간 (시간)", 4.0, 12.0, 7.5, 0.5)
        bed_time = st.number_input("🛌 침실에 누워 휴식을 취한 총 시간 (시간)", 1.0, 24.0, 8.0, 0.5)
    with col2:
        latency = st.number_input("⏳ 등불을 끄고 완벽한 입면에 도달하기까지의 시간 (분)", 0, 120, 20, 5)
        wakes = st.number_input("🔔 야간 수면 중 의식이 깨어난 횟수 (회)", 0, 10, 1, 1)
    
    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
    submit = st.form_submit_button("⚜️ 프리미엄 수면 분석서 발행")

# 6. 분석 및 고품격 결과 출력
if submit:
    total_bed_min = bed_time * 60
    # 중간 각성 1회당 수면 밀도 복귀 가중치 10분 자동 감산 알고리즘 적용
    actual_sleep_min = total_bed_min - latency - (wakes * 10) 
    
    if actual_sleep_min <= 0:
        st.error("⚠️ 입력해 주신 시간 지표에 의학적 불일치가 발견되었습니다. 작성하신 데이터를 면밀히 검토 후 재제출을 권장하옵니다.")
    else:
        efficiency = (actual_sleep_min / total_bed_min) * 100
        actual_hours = actual_sleep_min / 60
        debt = target - actual_hours
        
        # 1차 정밀 등급 및 컬러 글로우 동적 세팅
        if efficiency >= 85:
            accent_color = "#34d399"
            desc_badge = "🟢 HIGH-GRADE (안정형 수면)"
        elif efficiency >= 75:
            accent_color = "#fbbf24"
            desc_badge = "🟡 GUARD-GRADE (관심형 수면)"
        else:
            accent_color = "#f87171"
            desc_badge = "🔴 WARNING-GRADE (주의형 수면)"

        st.markdown(
            f"""
            <div class="luxury-card">
                <div class="luxury-section-title">📊 PHYSIOLOGICAL REPORT (정밀 생리 분석 보고서)</div>
                <p style="color: #94a3b8; font-size: 0.9rem; margin-top: -0.8rem; margin-bottom: 2rem;">
                    생체 바이오리듬과 수면 다원 검사 원리를 대입하여 수학적으로 도출한 정량 데이터입니다.
                </p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; text-align: center;">
                    <div style="background: rgba(255, 255, 255, 0.02); padding: 1.5rem; border-radius: 20px; border: 1px solid rgba(197,168,128,0.15);">
                        <span style="color: #94a3b8; font-size: 0.85rem; letter-spacing:1px; display:block; margin-bottom:0.5rem;">신체 수면 효율성</span>
                        <h2 style="color: {accent_color}; margin: 0; font-weight: 700; font-size: 2.2rem;">{efficiency:.1f}%</h2>
                        <span style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.5rem; display:block;">{desc_badge}</span>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.02); padding: 1.5rem; border-radius: 20px; border: 1px solid rgba(197,168,128,0.15);">
                        <span style="color: #94a3b8; font-size: 0.85rem; letter-spacing:1px; display:block; margin-bottom:0.5rem;">알짜베기 실 수면 시간</span>
                        <h2 style="color: #f1f5f9; margin: 0; font-weight: 700; font-size: 2.2rem;">{actual_hours:.1f} hr</h2>
                        <span style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.5rem; display:block;">총 {int(actual_sleep_min)}분 완전 회복</span>
                    </div>
                    <div style="background: rgba(255, 255, 255, 0.02); padding: 1.5rem; border-radius: 20px; border: 1px solid rgba(197,168,128,0.15);">
                        <span style="color: #94a3b8; font-size: 0.85rem; letter-spacing:1px; display:block; margin-bottom:0.5rem;">미상환 수면 부채</span>
                        <h2 style="color: {'#fbbf24' if debt > 0 else '#34d399'}; margin: 0; font-weight: 700; font-size: 2.2rem;">
                            {f'{debt:.1f} hr' if debt > 0 else '정상 충족'}
                        </h2>
                        <span style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.5rem; display:block;">
                            {f'-{debt:.1f}시간 채무' if debt > 0 else '리듬 밸런스 균형 상태'}
                        </span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # 2차 AI 프리미엄 피드백 가이드
        st.write(" ")
        with st.spinner("최고 자문 고문이 귀하의 야간 수면 뇌파를 면밀히 프로파일링 중이오니, 잠시만 대기해 주시옵소서..."):
            feedback = get_ai_feedback(efficiency, debt, latency, wakes)
            
            st.markdown(
                f"""
                <div class="luxury-card luxury-glow">
                    <div class="luxury-section-title">🩺 MEDICAL CONSULTATION DIARY (고문 전문 처방전)</div>
                    <div class="glass-inner-prescription">
                        <div style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.9; white-space: pre-wrap; font-family: 'Noto Sans KR', sans-serif;">{feedback}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.write(" ")
st.markdown("<p style='text-align: center; color: #c5a880; font-style: italic; font-family: \"Playfair Display\", serif; font-size:1.1rem; letter-spacing:1px;'>“Let the profound silence embrace your tranquility tonight.”</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem; margin-top:0.3rem;'>© SnoozeWise Private Clinic. All rights reserved.</p>", unsafe_allow_html=True)
