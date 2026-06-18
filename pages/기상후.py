import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 디자인
st.set_page_config(
    page_title="미라클 모닝 루틴 플래너",
    page_icon="☀️",
    layout="centered"
)

st.title("☀️ 미라클 모닝 루틴 플래너")
st.markdown("""
진정한 아침의 변화는 나의 현재를 아는 것부터 시작됩니다. 
현재 기상 후 패턴을 입력하고, 원하는 아침의 모습을 선택하시면 **AI가 맞춤형 최적 루틴**을 제안해 드립니다!
""")
st.divider()

# 2. API 키 설정 및 예외 처리
# Streamlit Community Cloud의 Secrets 기능을 사용합니다.
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("⚠️ API 키가 설정되지 않았습니다. Streamlit Cloud의 Secrets에 'GEMINI_API_KEY'를 등록해주세요.")
    st.stop()

# 3. 유저 입력 폼 (한 페이지 구성)
st.subheader("📋 Step 1. 나의 현재 아침 패턴")

col1, col2 = st.columns(2)
with col1:
    wake_time = st.time_input("1. 보통 몇 시에 일어나시나요?", value=None)
    first_action = st.selectbox(
        "2. 눈뜨자마자 가장 먼저 하는 행동은?",
        ["스마트폰 확인", "스트레칭", "물 마시기", "바로 씻기", "다시 누워있기", "기타"]
    )
with col2:
    phone_time = st.slider("3. 침대 위 스마트폰 사용 시간 (분)", 0, 60, 15, step=5)
    breakfast = st.radio("4. 아침 식사 혹은 대용식 섭취 여부", ["먹는다", "마시는 종류만(커피/차/즙)", "먹지 않는다"])

st.divider()

st.subheader("🎯 Step 2. 내가 원하는 아침의 모습 (바램)")
user_goal = st.selectbox(
    "어떤 아침을 맞이하고 싶으신가요? (선택에 따라 AI의 답변 방향이 달라집니다)",
    [
        "⚡ 피로를 빠르게 깨우고 활력을 얻는 아침 (에너지 충전)",
        "🧠 집중력을 높여 하루 생산성을 극대화하는 아침 (업무/공부 효율)",
        "🧘 되돌아보며 여유롭고 마음이 차분해지는 아침 (힐링/명상)",
        "🏃 체력을 기르고 몸을 가볍게 만드는 아침 (운동/건강)"
    ]
)

st.divider()

# 4. 분석 및 제안 기능 구현
st.subheader("🚀 Step 3. AI 맞춤형 루틴 확인하기")

if st.button("내 아침 패턴 분석하고 맞춤 루틴 받기", type="primary"):
    if wake_time is None:
        st.warning("기상 시간을 입력해주세요!")
    else:
        with st.spinner("AI가 당신의 아침을 분석하여 최적의 루틴을 설계 중입니다..."):
            # 프로그래밍적 데이터 정리
            wake_time_str = wake_time.strftime("%H시 %M분")
            
            # Gemini 프롬프트 구성
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
                # gemini-2.5-flash-lite 모델 호출
                model = genai.GenerativeModel("gemini-2.5-flash-lite")
                response = model.generate_content(prompt)
                
                # 결과 출력
                st.success("✨ AI 분석 완료!")
                st.markdown("### 📊 AI 코칭 리포트")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"API 호출 중 오류가 발생했습니다. 다시 시도해주세요. (오류 내용: {e})")
