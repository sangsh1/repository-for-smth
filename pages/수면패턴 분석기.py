import streamlit as st
from datetime import datetime, timedelta

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="개운한 아침을 위한 수면 계산기",
    page_icon="🌙",
    layout="centered"
)

# 2. 앱 타이틀 및 소개
st.title("🌙 수면 타임 추천 계산기")
st.markdown("""
사람의 수면은 보통 **90분 주기**로 반복됩니다. 
수면 주기가 끝나는 시점에 깨어나야 알람을 들었을 때 개운하게 일어날 수 있습니다.
잠드는 데 걸리는 평균 시간(**15분**)을 고려한 최적의 시간을 찾아보세요!
""")

st.divider()

# 3. 사이드바 - 수면 팁 정보
with st.sidebar:
    st.header("💡 건강한 수면 팁")
    st.markdown("""
    * **90분 주기 법칙**: 보통 5~6번의 수면 주기(7.5시간~9시간)를 채우는 것이 성인에게 가장 이상적입니다.
    * **스마트폰 멀리하기**: 잠들기 30분 전 전자기기 사용은 멜라토닌 분비를 방해해요.
    * **일정한 시간**: 주말에도 평소와 비슷한 시간에 일어나면 생체 리듬이 유지됩니다.
    """)
    st.info("이 앱은 과학적인 90분 수면 주기 이론을 바탕으로 계산되었습니다.")

# 4. 메인 기능 (탭 분리)
tab1, tab2 = st.tabs(["⏰ 언제 자야 할까요?", "💤 지금 자면 언제 깰까요?"])

# --- 탭 1: 기상 시간을 입력하여 취침 시간 추천받기 ---
with tab1:
    st.subheader("목표 기상 시간 입력")
    
    # 시간 선택 UI (기본값 설정시 예외 처리 포함)
    try:
        target_time = st.time_input("몇 시에 일어나고 싶으신가요?", value=datetime.strptime("07:00", "%H:%M").time())
    except Exception as e:
        st.error("시간 선택 중 오류가 발생했습니다. 올바른 시간 형식인지 확인해주세요.")
        target_time = datetime.now().time()

    if st.button("추천 취침 시간 보기", key="btn_sleep"):
        # 오늘 날짜와 입력된 시간을 조합하여 datetime 객체 생성
        today = datetime.today()
        target_datetime = datetime.combine(today, target_time)
        
        st.success(f"🎯 **{target_time.strftime('%H:%M')}**에 깨어나기 위한 추천 취침 시간입니다:")
        st.caption("(잠드는 시간 15분을 미리 반영한 결과입니다.)")
        
        # 수면 주기 계산 (4주기: 6시간, 5주기: 7.5시간, 6주기: 9시간) + 잠드는 시간 15분 역산
        cycles = [6, 5, 4]  # 추천 순서 (9시간, 7.5시간, 6시간 수면)
        
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        
        for i, cycle in enumerate(cycles):
            # (수면 시간 + 잠드는 시간 15분)을 빼줌
            total_minutes_to_subtract = (cycle * 90) + 15
            suggested_sleep_time = target_datetime - timedelta(minutes=total_minutes_to_subtract)
            
            with cols[i]:
                st.metric(
                    label=f"{cycle}주기 ({cycle*1.5}시간 수면)", 
                    value=suggested_sleep_time.strftime("%H:%M")
                )
                if cycle == 5:
                    st.caption("⭐ 가장 추천 (7.5h)")
                elif cycle == 6:
                    st.caption("💤 듬뿍 숙면 (9.0h)")
                else:
                    st.caption("🏃 최소 수면 (6.0h)")

# --- 탭 2: 지금 잘 때 기상 시간 추천받기 ---
with tab2:
    st.subheader("지금 바로 침대로 가시나요?")
    
    if st.button("지금 잘 때 기상 시간 확인", key="btn_wake"):
        now = datetime.now()
        # 잠드는 시간 15분 더하기
        sleep_start = now + timedelta(minutes=15)
        
        st.info(f"현재 시간: {now.strftime('%H:%M')} (약 {sleep_start.strftime('%H:%M')} 쯤 잠들 대 전제)")
        
        cycles = [4, 5, 6]  # 6시간, 7.5시간, 9시간 뒤 기상
        
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
        
        for i, cycle in enumerate(cycles):
            total_minutes_to_add = (cycle * 90)
            suggested_wake_time = sleep_start + timedelta(minutes=total_minutes_to_add)
            
            with cols[i]:
                st.metric(
                    label=f"{cycle}주기 ({cycle*1.5}시간 뒤)", 
                    value=suggested_wake_time.strftime("%H:%M")
                )
                if cycle == 5:
                    st.caption("⭐ 가장 추천")

st.divider()
st.center = st.markdown("<p style='text-align: center; color: gray;'>오늘 밤도 좋은 꿈 꾸세요! 🌙</p>", unsafe_allow_html=True)
