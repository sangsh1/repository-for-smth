import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(
    page_title="프라이빗 AI 수면 패턴 분석기",
    page_icon="⚜️",
    layout="centered"
)

# 2. AI 수면 컨설팅 로직 (Gemini API)
def get_ai_feedback(efficiency, debt, latency, wakes):
    try:
        # [중요] Streamlit Cloud의 Secrets 관리자로부터 GEMINI_API_KEY를 안전하게 가져옵니다.
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # 모델 설정 (요청사항 반영: gemini-2.5-flash-lite 사용)
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        
        # 고급스러운 톤앤매너를 위한 프롬프트 정교화
        prompt = f"""
        당신은 상류층을 위한 최고급 프라이빗 웰니스 클리닉의 수면 전문 고문 의사입니다. 
        아래의 수면 데이터를 기반으로, VIP 고객에게 드리는 품격 있고 정중하며 깊이 있는 개인 맞춤형 리포트를 작성해 주세요.
        모든 문장은 매우 고급스럽고 부드러운 격식체(~옵니다, ~드립니다, ~하시길 권합니다)로 작성해야 합니다.

        [고객의 수면 데이터]
        - 수면 효율: {efficiency:.1f}%
        - 수면 부족량(목표 대비): {debt:.1f}시간
        - 입면 소요 시간: {latency}분
        - 수면 중 각성 횟수: {wakes}회
        
        [작성 가이드라인]
        1. 헌사 및 현재 수면 상태에 대한 고품격 총평 (한 문장)
        2. 이 패턴이 지속될 경우 생체 리듬과 신체 건강에 미치는 영양학적/의학적 고찰
        3. 오늘 밤 완벽한 휴식을 위해 제안하는 최고급 웰니스 솔루션 2가지 (예: 환경 조율, 심신 이완 루틴 등)
        """
        
        response = model.generate_content(prompt)
        return response.text
    except KeyError:
        return "❌ 오류: Streamlit 시스템 내에 'GEMINI_API_KEY' 가 등록되지 않았습니다. 하단의 Secrets 설정 가이드를 확인해 주세요."
    except Exception as e:
        return f"죄송합니다. AI 컨설턴트와의 연결이 원활하지 않습니다. (사유: {str(e)})"

# 3. UI 디자인 - 프라이빗 클릭 콘셉트
st.title("⚜️ 프라이빗 AI 수면 컨설팅")
st.markdown("""
당신의 온전한 휴식과 내일의 활력을 위한 **고품격 수면 패턴 분석 서비스**입니다.  
수학적 정밀 분석과 **Gemini AI의 전문적인 고문 의견**을 통해 최상의 밤을 설계해 드립니다.
""")

st.divider()

# 4. 사이드바 - 시스템 상태 확인
with st.sidebar:
    st.header("🔑 관제 시스템")
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("현재 API Key 인증이 필요합니다.")
    else:
        st.success("고객 맞춤형 AI 시스템 준비 완료")

# 5. 수면 데이터 입력 세션
st.subheader("📝 오늘의 수면 세부 기록")
st.markdown("<small style='color:gray;'>어제 밤의 수면 환경을 기억하시는 대로 고요히 입력해 주십시오.</small>", unsafe_allow_html=True)

with st.form("luxury_sleep_form"):
    col1, col2 = st.columns(2)
    with col1:
        target = st.number_input("이상적인 목표 수면 시간 (시간)", 4.0, 12.0, 7.5, 0.5)
        bed_time = st.number_input("총 침대 체류 시간 (시간)", 1.0, 24.0, 8.0, 0.5)
    with col2:
        latency = st.number_input("입면까지 소요된 시간 (분)", 0, 120, 20, 5)
        wakes = st.number_input("수면 중 깨어난 횟수 (회)", 0, 10, 1, 1)
    
    submit = st.form_submit_button("⚜️ 프리미엄 분석 리포트 발행")

# 6. 분석 및 고품격 결과 출력
if submit:
    total_bed_min = bed_time * 60
    # 중간 각성 1회당 약 10분의 차감 수치 적용
    actual_sleep_min = total_bed_min - latency - (wakes * 10) 
    
    if actual_sleep_min <= 0:
        st.error("입력하신 수치에 모순이 발견되었습니다. 기입하신 시간을 다시 한 번 고찰해 주시기 바랍니다.")
    else:
        efficiency = (actual_sleep_min / total_bed_min) * 100
        actual_hours = actual_sleep_min / 60
        debt = target - actual_hours
        
        # 1차 정밀 수치 리포트
        st.subheader("📊 정밀 수치 분석서")
        c1, c2, c3 = st.columns(3)
        c1.metric("수면 효율성", f"{efficiency:.1f}%")
        c2.metric("실제 깊은 수면", f"{actual_hours:.1f}시간")
        
        if debt > 0:
            c3.metric("누적된 수면 빚", f"{debt:.1f}시간", delta=f"-{debt:.1f}h", delta_color="inverse")
        else:
            c3.metric("수면 충족도", "매우 충분함", delta=f"+{abs(debt):.1f}h")
        
        st.divider()
        
        # 2차 AI 프리미엄 피드백
        st.subheader("🩺 전문 고문 의사의 맞춤형 처방전")
        with st.spinner("수면 컨설턴트가 데이터를 심도 있게 분석하고 있습니다. 잠시만 기다려 주십시오..."):
            feedback = get_ai_feedback(efficiency, debt, latency, wakes)
            st.markdown(feedback)

st.divider()
st.markdown("<p style='text-align: center; color: #c5a880; font-style: italic;'>“가장 깊은 고요가 당신의 밤에 머물기를 소망합니다.”</p>", unsafe_allow_html=True)
