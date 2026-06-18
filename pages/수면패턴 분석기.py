import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 맞춤형 수면 패턴 분석기",
    page_icon="📊",
    layout="centered"
)

# 2. 타이틀 및 앱 소개
st.title("📊 나의 수면 패턴 분석기")
st.markdown("""
최근 수면 습관을 입력하고 나의 **수면 효율성 점수**와 **수면 상태 진단**을 받아보세요.
의학적으로 수면 효율이 **85% 이상**일 때 건강한 수면 패턴이라고 합니다.
""")

st.divider()

# 3. 사이드바 - 분석 기준 안내
with st.sidebar:
    st.header("🔍 수면 분석 기준")
    st.markdown("""
    * **수면 효율이란?**
      침대에 누워있는 시간 중 실제로 잠든 시간의 비율입니다.
    
    * **점수별 상태 정의**
      * 🟢 **85% 이상**: 양호 (건강한 패턴)
      * 🟡 **75% ~ 84%**: 주의 (수면 환경 개선 필요)
      * 🔴 **75% 미만**: 불량 (불면증 및 습관 교정 필요)
    """)
    st.info("💡 누워있는 시간 대비 잠든 시간이 많아야 양질의 수면입니다.")

# 4. 사용자 데이터 입력 구간
st.subheader("📝 최근 수면 기록 입력")

with st.form(key="sleep_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        target_sleep = st.number_input("평소 나에게 필요한 목표 수면 시간 (시간)", min_value=4.0, max_value=12.0, value=7.5, step=0.5)
        bed_time = st.number_input("어제 총 침대에 누워있던 시간 (시간)", min_value=1.0, max_value=24.0, value=8.0, step=0.5)
    
    with col2:
        latency = st.number_input("불을 끄고 잠들 때까지 걸린 시간 (분)", min_value=0, max_value=120, value=20, step=5)
        wake_count = st.number_input("자다가 중간에 깨어난 횟수 (회)", min_value=0, max_value=10, value=1, step=1)
    
    # 예외 방지: 중간에 깨서 뒤척인 시간 자동 산정 (1회당 평균 10분으로 가정)
    wake_minutes = wake_count * 10
    
    submit_button = st.form_submit_button(label="📊 나의 수ence 패턴 분석하기")

# 5. 분석 및 결과 출력
if submit_button:
    # 계산 로직 (시간 단위를 분 단위로 통일하여 계산)
    total_bed_minutes = bed_time * 60
    actual_sleep_minutes = total_bed_minutes - latency - wake_minutes
    
    # 예외 처리: 입력값이 비현실적이어서 실제 수면 시간이 0 이하가 되는 경우 방지
    if actual_sleep_minutes <= 0:
        st.error("⚠️ 입력된 뒤척인 시간과 잠들기까지의 시간이 총 누워있던 시간보다 길거나 같습니다. 입력 값을 확인해주세요.")
    else:
        # 수면 효율 계산 (%)
        sleep_efficiency = (actual_sleep_minutes / total_bed_minutes) * 100
        actual_sleep_hours = round(actual_sleep_minutes / 60, 1)
        
        # 수면 빚(Sleep Debt) 계산
        sleep_debt = target_sleep - actual_sleep_hours
        
        st.subheader("📋 수면 패턴 분석 결과 보고서")
        
        # 결과 대시보드 시각화
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="실제 수면 시간", value=f"{actual_sleep_hours} 시간")
        with c2:
            st.metric(label="수면 효율성", value=f"{sleep_efficiency:.1f} %")
        with c3:
            if sleep_debt > 0:
                st.metric(label="족한 수면(수면 빚)", value=f"{sleep_debt:.1f} 시간", delta=f"-{sleep_debt:.1f}", delta_color="inverse")
            else:
                st.metric(label="수면 충족도", value="충분함", delta=f"+{abs(sleep_debt):.1f}")

        st.markdown("---")
        
        # 종합 진단 및 솔루션 제안
        st.markdown("### 🩺 종합 진단 결과")
        
        # 1단계: 수면 효율에 따른 진단
        if sleep_efficiency >= 85:
            st.success("🟢 **양호: 효율적인 수면을 취하고 계십니다!**")
            st.markdown("침대에 누워 불필요하게 뒤척이는 시간이 적고 알차게 주무셨습니다. 현재의 수면 환경과 취침 전 루틴을 잘 유지하세요.")
        elif sleep_efficiency >= 75:
            st.warning("🟡 **주의: 수면 효율을 개선할 여지가 있습니다.**")
            st.markdown("잠들기까지 다소 시간이 걸리거나 중간에 깨는 현상이 있습니다. 취침 1시간 전 스마트폰 사용을 줄이고 방을 더 어둡고 선선하게 유지해 보세요.")
        else:
            st.error("🔴 **불량: 수면 조각화 및 비효율적 패턴이 관찰됩니다.**")
            st.markdown("누워있는 시간에 비해 실제 깊은 잠에 든 시간이 많이 부족합니다. 잠이 오지 않을 때는 침대에서 일어나 가벼운 독서를 하다가 다시 졸릴 때 눕는 '자극 조절 요법'을 추천합니다.")
            
        # 2단계: 수면 시간에 따른 추가 조언
        if sleep_debt > 1.5:
            st.info(f"⚠️ **추가 조언**: 현재 목표하신 시간에 비해 **{sleep_debt:.1f}시간** 수면이 부족합니다. 주중에 밀린 잠은 주말에 1~2시간 일찍 잠드는 방식으로 보충하여 수면 빚을 탕감해 주세요.")

st.divider()
st.markdown("<p style='text-align: center; color: gray;'>정확한 분석을 위해 매일 아침 꾸준히 기록해 보세요! 🛌</p>", unsafe_allow_html=True)
