import datetime
import streamlit as st

# 1. 페이지 기본 설정 및 고급스러운 테마 커스텀
st.set_page_config(
    page_title="SnoozeWise | 맞춤형 수면&준비 타이머",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 고급스러운 분위기를 위한 커스텀 CSS (폰트, 부드러운 그라데이션, 카드 스타일)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #764ba2;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    .result-card:hover {
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 2. 메인 타이틀 세션
st.markdown("<h1 class='main-title'>🌙 SnoozeWise</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-title'>당신의 완벽한 아침을 위한 맞춤형 수면 및 외출 준비 시뮬레이터</p>",
    unsafe_allow_html=True,
)

# 3. 사이드바 - 개인별 기능 설정 영역 (설정 메뉴 차별화)
st.sidebar.header("⚙️ 개인 맞춤 설정")

# 외출 목적 선택에 따른 기본 심리적 여유 시간 계산 (차별화 요소)
activity_type = st.sidebar.selectbox(
    "외출 목적이 무엇인가요?", ["일반 출근/등교", "중요한 미팅/면접", "여유로운 주말 데이트", "기타"]
)

buffer_minutes = 10
if activity_type == "중요한 미팅/면접":
    buffer_minutes = 25
elif activity_type == "여유로운 주말 데이트":
    buffer_minutes = 15
else:
    buffer_minutes = 10

st.sidebar.markdown("---")
st.sidebar.caption(
    f"💡 **💡 Tip:** {activity_type} 목적을 고려해 아침 여유 버퍼 시간을 **{buffer_minutes}분**으로 자동 세팅했습니다."
)


# 4. 메인 화면 - 입력 인터페이스 (Smooth 인터랙션)
st.subheader("📊 나의 하루 루틴 입력하기")

col1, col2 = st.columns(2)

with col1:
    target_arrival = st.time_input(
        "⏱️ 목적지 도착 필요 시간", datetime.time(9, 0)
    )
    commute_time = st.number_input(
        "🚗 이동 시간 (분 단위)", min_value=0, max_value=240, value=40, step=5
    )

with col2:
    prep_time = st.number_input(
        "💄 외출 준비 시간 (분 단위)", min_value=0, max_value=180, value=50, step=5
    )
    sleep_cycle = st.selectbox(
        "💤 선호하는 수면 패턴",
        options=[6.0, 7.5, 9.0],
        format_func=lambda x: f"{x}시간 (추천: {int(x//1.5)} 사이클)",
        index=1,
    )


# 5. 핵심 연산 및 예외 처리 (오류 없는 안정적 구현)
st.markdown("---")

try:
    # 1) 기상 시간 계산
    # 수월한 시간 연산을 위해 datetime 객체로 변환
    today = datetime.date.today()
    arrival_datetime = datetime.datetime.combine(today, target_arrival)

    # 총 필요 차감 시간 = 이동 시간 + 준비 시간 + 목적에 따른 버퍼 시간
    total_prep_minutes = commute_time + prep_time + buffer_minutes
    wakeup_datetime = arrival_datetime - datetime.timedelta(
        minutes=total_prep_minutes
    )

    # 2) 취침 시간 계산 (수면 사이클 차감 + 잠드는 시간 평균 15분 추가)
    fall_asleep_buffer = 15
    total_sleep_minutes = int(sleep_cycle * 60) + fall_asleep_buffer
    bedtime_datetime = wakeup_datetime - datetime.timedelta(
        minutes=total_sleep_minutes
    )

    # 화면 출력용 포맷팅
    wakeup_str = wakeup_datetime.strftime("%H:%M")
    bedtime_str = bedtime_datetime.strftime("%H:%M")

    # 6. 결과 시각화 (고급스러운 카드 형태 레이아웃)
    st.subheader("✨ 당신만을 위한 맞춤 타임라인 리포트")

    col_res1, col_res2 = st.columns(2)

    with col_res1:
        st.markdown(
            f"""
            <div class="result-card">
                <span style="font-size: 1.2rem; font-weight: bold; color: #764ba2;">💤 추천 취침 시간</span>
                <h2 style="margin: 0.5rem 0; color: #2d3748;">{bedtime_str}</h2>
                <p style="font-size: 0.85rem; color: #a0aec0; margin: 0;">잠드는 평균 시간 15분이 포함됨</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_res2:
        st.markdown(
            f"""
            <div class="result-card" style="border-left-color: #3182ce;">
                <span style="font-size: 1.2rem; font-weight: bold; color: #3182ce;">⏰ 반드시 일어나야 하는 시간</span>
                <h2 style="margin: 0.5rem 0; color: #2d3748;">{wakeup_str}</h2>
                <p style="font-size: 0.85rem; color: #a0aec0; margin: 0;">돌발 상황 대비 버퍼 {buffer_minutes}분 포함</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # 7. 추가 디테일 안내 (스무스한 UI 요소)
    with st.expander("🔍 상세 타임라인 스케줄 보기"):
        st.write(
            f"1. **{bedtime_str}** : 침대에 누워 불을 끕니다. (15분간 서서히 잠들기)"
        )
        st.write(
            f"2. **{wakeup_str}** : 기상 후 **{prep_time}분** 동안 외출 준비를 합니다."
        )
        # 기상 후 준비 완료 시간 계산
        ready_datetime = wakeup_datetime + datetime.timedelta(minutes=prep_time)
        st.write(
            f"3. **{ready_datetime.strftime('%H:%M')}** : 준리를 마치고 집에서 출발합니다. (**{commute_time}분** 이동)"
        )
        st.write(
            f"4. **{arrival_datetime.strftime('%H:%M')}** : 목적지 여유롭게 도착! (돌발 버퍼 여유 {buffer_minutes}분 확보 완료)"
        )

except Exception as e:
    st.error(
        f"시간을 계산하는 도중 예상치 못한 오류가 발생했습니다. 입력을 확인해 주세요. (에러: {e})"
    )

# 하단 푸터
st.markdown("---")
st.caption("© 2026 SnoozeWise. 기분 좋은 아침을 응원합니다.")
