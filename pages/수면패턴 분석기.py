import datetime
import streamlit as st

# 1. 페이지 기본 설정 및 프리미엄 다크 테마 고정
st.set_page_config(
    page_title="SnoozeWise | 프리미엄 수면 패턴 분석 & 가이드",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 고급스러운 야간 오로라 테마 및 부드러운 모션 애니메이션 커스텀 CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');
    
    /* 기본 폰트 및 백그라운드 디자인 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 스무스한 등장을 위한 키프레임 애니메이션 */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 15px rgba(99, 102, 241, 0.15); }
        50% { box-shadow: 0 0 25px rgba(99, 102, 241, 0.3); }
    }

    /* 헤더 스타일링 */
    .header-container {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem 1rem;
        animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .brand-logo {
        font-size: 3.5rem;
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #a5b4fc 0%, #818cf8 50%, #4f46e5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .brand-desc {
        font-size: 1.15rem;
        color: #94a3b8;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* 카드 컨테이너 디자인 (대시보드 소개용) */
    .card-dashboard {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 1.8rem;
        min-height: 250px;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .card-dashboard:hover {
        transform: translateY(-6px);
        background: rgba(99, 102, 241, 0.06);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.12);
    }

    .card-icon {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
    }
    
    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 0.6rem;
    }
    
    .card-desc-text {
        font-size: 0.9rem;
        color: #94a3b8;
        line-height: 1.5;
    }

    /* 수면 효율 분석 결과 프리미엄 카드 */
    .result-box-premium {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 24px;
        padding: 2.2rem;
        margin-top: 1.5rem;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        animation-fill-mode: both;
        animation-delay: 0.1s;
    }

    .metric-badge-good {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.85rem;
    }

    .metric-badge-warning {
        background: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.85rem;
    }

    .metric-badge-danger {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.85rem;
    }

    /* 탭 스타일 고급화 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        justify-content: center;
        border: none;
        margin-bottom: 2rem;
    }

    .stTabs [data-baseweb="tab"] {
        height: 52px;
        background-color: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 30px;
        color: #94a3b8;
        padding: 0px 28px;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(99, 102, 241, 0.08);
        color: #fff;
        border-color: rgba(99, 102, 241, 0.25);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%) !important;
        color: #fff !important;
        border-color: #6366f1 !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.35);
    }

    /* 입력 박스 슬라이더 및 넘버 입력창 영역 패딩 */
    .input-glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* 스트림릿 기본 요소 리디자인 */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 24px !important;
        padding: 2rem !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
    }
    
    button[kind="primaryFormSubmit"] {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        border: none !important;
        color: #fff !important;
        padding: 0.75rem 2.5rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }
    button[kind="primaryFormSubmit"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. 메인 브랜드 헤더
st.markdown(
    """
    <div class="header-section header-container">
        <div class="brand-logo">SnoozeWise</div>
        <div class="brand-desc">THE PREMIUM SLEEP ARCHITECT</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 4. 기능 선택 탭 레이아웃 (스무스한 화면 이동 제공)
tabs = st.tabs([
    "📊 나의 수면 패턴 분석기",
    "🌙 취침 & 기상 계산기",
    "☀️ 아침 루틴 & 위생 가이드"
])

# ---------------------------------------------------------
# TAB 1: 나의 수면 패턴 분석기 (고객의 새로운 기능 리디자인)
# ---------------------------------------------------------
with tabs[0]:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <h2 style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;">📊 실시간 개인 수면 효율성 자가진단</h2>
            <p style="color: #94a3b8; font-size: 1rem; max-width: 700px; margin: 0 auto;">
                침대 위에 머무는 전체 시간 중 <b>실제 숙면</b>이 차지하는 비율을 정밀 분석합니다. 
                의학적으로 <b>85% 이상</b>의 높은 효율성을 얻는 것이 웰니스의 첫걸음입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 대시보드 카드 정보
    col_i1, col_i2, col_i3 = st.columns(3)
    with col_i1:
        st.markdown(
            """
            <div class="card-dashboard" style="animation-delay: 0.1s; min-height: 180px; padding: 1.5rem;">
                <div class="card-icon">🟢</div>
                <div class="card-title">수면 효율 85% 이상</div>
                <div class="card-desc-text">안정적이고 견고한 수면 구조. 현재의 침실 환경과 야간 생체 바이오리듬이 잘 수렴되어 있습니다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_i2:
        st.markdown(
            """
            <div class="card-dashboard" style="animation-delay: 0.2s; min-height: 180px; padding: 1.5rem;">
                <div class="card-icon">🟡</div>
                <div class="card-title">수면 효율 75% ~ 84%</div>
                <div class="card-desc-text">중간 각성 혹은 입면 지연 현상 발생. 쾌적한 멜라토닌 분비를 방해하는 원인을 교정할 시점입니다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_i3:
        st.markdown(
            """
            <div class="card-dashboard" style="animation-delay: 0.3s; min-height: 180px; padding: 1.5rem;">
                <div class="card-icon">🔴</div>
                <div class="card-title">수면 효율 75% 미만</div>
                <div class="card-desc-text">수면 파편화 및 자극 과다 노출 상태. 자극 조절 요법과 침실 내 디지털 디톡스 도입이 절실합니다.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write(" ")
    st.write(" ")

    # 메인 폼 영역
    with st.form(key="premium_sleep_form"):
        st.markdown("<h4 style='color: #c7d2fe; font-weight:600; margin-bottom: 1.5rem;'>📝 정밀 분석 수면 저널 작성</h4>", unsafe_allow_html=True)
        
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            target_sleep = st.slider(
                "🎯 평소 본인에게 필요한 목표 수면 시간 (시간)",
                min_value=4.0, max_value=12.0, value=7.5, step=0.5,
                help="개인적으로 낮 동안 최고의 컨디션을 내기 위한 기준 수면량입니다."
            )
            bed_time = st.slider(
                "🛌 어제 총 침대에 누워있던 시간 (시간)",
                min_value=1.0, max_value=24.0, value=8.0, step=0.5,
                help="어제 누워서 잠들기 시작한 때부터 눈뜨고 침대 밖으로 완전히 나오기까지의 시간입니다."
            )
        
        with col_f2:
            latency = st.number_input(
                "⏳ 불을 끄고 잠들 때까지 걸린 시간 (분)",
                min_value=0, max_value=120, value=20, step=5,
                help="잠자리에 들어가 의식을 잃고 수면에 빠져들기 전까지의 평균 입면 대기 시간입니다."
            )
            wake_count = st.number_input(
                "🔔 자다가 중간에 깨어난 횟수 (회)",
                min_value=0, max_value=10, value=1, step=1,
                help="자다가 일시적으로 깬 횟수를 뜻합니다. (회당 수면 구조 이완 복귀를 위해 최소 10분이 감산 처리됩니다.)"
            )
            
        # 1회당 수면 조각화 및 재수면 준비 평균 10분 가산 적용
        wake_minutes = wake_count * 10
        
        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
        submit_button = st.form_submit_button(label="🧬 나만의 프리미엄 수면 패턴 분석 시작")

    # 결과 표출 (조건부 스무스 렌더링)
    if submit_button:
        total_bed_minutes = bed_time * 60
        actual_sleep_minutes = total_bed_minutes - latency - wake_minutes
        
        if actual_sleep_minutes <= 0:
            st.error("⚠️ 경고: 수면 장애/뒤척임 환산 시간의 합이 총 침대에 누워있던 시간보다 깁니다. 정밀 분석을 위해 입력값을 신중히 보정해 주세요.")
        else:
            sleep_efficiency = (actual_sleep_minutes / total_bed_minutes) * 100
            actual_sleep_hours = round(actual_sleep_minutes / 60, 1)
            sleep_debt = target_sleep - actual_sleep_hours
            
            # 효율 등급 분류 및 스타일 결정
            if sleep_efficiency >= 85:
                status_class = "metric-badge-good"
                status_text = "🟢 최고 등급: 완벽한 수면 효율"
                status_desc = "체계적인 신체 순환 주기와 양질의 깊은 수면을 취하고 있습니다. 당신의 침실 온도, 매트리스, 스트레스 해소 능력이 최상의 밸런스를 이룹니다. 현재의 생체 라이프스타일을 지속적으로 보존하세요."
            elif sleep_efficiency >= 75:
                status_class = "metric-badge-warning"
                status_text = "🟡 중간 등급: 개선 필요 단계"
                status_desc = "정상 범주에 속하나 입면 시간 지연이나 수면 유지 도중 경미한 뇌파 각성이 발생하고 있습니다. 취침 전 스마트폰 블루라이트를 통제하고, 카페인 섭취 골든타임을 점검해 보세요."
            else:
                status_class = "metric-badge-danger"
                status_text = "🔴 경고 등급: 수면 단편화 현상"
                status_desc = "침대에서 낭비되는 비효율적 뇌파가 많습니다. 이러한 패턴이 만성화되면 피로감과 아침 수면 관성이 누적됩니다. 20분 이상 기상 시 즉시 침대를 벗어나는 '자극통제요법'을 시작할 것을 적극 제안합니다."

            # 고급 카드 렌더링
            st.markdown(
                f"""
                <div class="result-box-premium">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                        <h3 style="margin: 0; color: #fff; font-weight: 700;">📊 SNOOZEWISE 정밀 수면 진단 보고서</h3>
                        <span class="{status_class}">{status_text}</span>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.7;">{status_desc}</p>
                    </div>
                    <hr style="border-color: rgba(255, 255, 255, 0.08); margin: 1.5rem 0;">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.5rem; text-align: center;">
                        <div style="background: rgba(255, 255, 255, 0.02); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.04);">
                            <span style="color: #94a3b8; font-size: 0.85rem;">실제 알짜배기 수면 시간</span>
                            <h2 style="color: #f1f5f9; margin: 0.5rem 0; font-weight: 700;">{actual_sleep_hours} hr</h2>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.02); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.04);">
                            <span style="color: #94a3b8; font-size: 0.85rem;">개인 맞춤형 수면 효율성</span>
                            <h2 style="color: #818cf8; margin: 0.5rem 0; font-weight: 700;">{sleep_efficiency:.1f} %</h2>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.02); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.04);">
                            <span style="color: #94a3b8; font-size: 0.85rem;">부족한 수면량 (수면 빚)</span>
                            <h2 style="color: {'#fbbf24' if sleep_debt > 0 else '#34d399'}; margin: 0.5rem 0; font-weight: 700;">
                                {f'{sleep_debt:.1f} hr' if sleep_debt > 0 else '충분함'}
                            </h2>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # 수면 빚 경고 및 정교한 생리학적 제언
            if sleep_debt > 1.5:
                st.info(f"💡 **수면 빚(Sleep Debt) 밀착 솔루션:** 목표 수면량 대비 현재 **{sleep_debt:.1f}시간**의 누적 채무가 발생했습니다. 평일에 무너진 리듬을 보충하기 위해 주말에 몰아 자는 대신, 기상 시각은 일정하게 가져가며 저녁 취침 시각을 1~2시간 앞당기는 점진적 압축 기법을 실천해 보세요.")

# ---------------------------------------------------------
# TAB 2: 취침 & 기상 시간 계산기 (수면 역산 공식 적용)
# ---------------------------------------------------------
with tabs[1]:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <h2 style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;">🌙 최적 기상 & 입면 역산 시뮬레이터</h2>
            <p style="color: #94a3b8; font-size: 1rem; max-width: 700px; margin: 0 auto;">
                지각에 대한 스트레스 없이 가뿐한 하루를 여는 맞춤형 스케줄러입니다. 
                중요 면접이나 출근, 데이트 등의 목적에 맞는 아침 안전 버퍼 시간을 정밀하게 설계합니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_sch1, col_sch2 = st.columns([1, 2])

    with col_sch1:
        st.markdown("<h4 style='color: #c7d2fe; font-weight:600;'>⚙️ 스케줄 제어 파라미터</h4>", unsafe_allow_html=True)
        activity_type = st.selectbox(
            "오늘 외출의 핵심 목적이 무엇인가요?",
            ["일반 직장 출근 및 등교", "대외적 중요한 미팅/면접", "주말 데이트 및 소셜 모임", "기타 여유로운 루틴"],
            key="act_type"
        )
        
        # 목적별 버퍼 시간 조정
        if activity_type == "대외적 중요한 미팅/면접":
            buffer_min = 25
            sub_info = "미팅 전 마인드 컨트롤 및 대기 시간 25분이 포함됩니다."
        elif activity_type == "주말 데이트 및 소셜 모임":
            buffer_min = 15
            sub_info = "미용 정비 및 미팅 장소 사전 탐색을 고려해 15분이 포함됩니다."
        else:
            buffer_min = 10
            sub_info = "돌발 도로 상황 지연을 커버하는 안심 버퍼 10분이 포함됩니다."

        st.caption(f"🛡️ **안전 버퍼 자동화:** {sub_info}")
        st.write("---")

        target_arrival = st.time_input(
            "⏱️ 목적지 정시 도착 희망 시간", datetime.time(9, 0),
            key="tar_arr"
        )
        
        commute_time = st.number_input(
            "🚗 예상 이동 수단 소요 시간 (분)", min_value=0, max_value=240, value=40, step=5,
            key="comm_time"
        )
        
        prep_time = st.number_input(
            "💄 세안 및 모닝 스타일링 준비 시간 (분)", min_value=0, max_value=180, value=50, step=5,
            key="pr_time"
        )
        
        sleep_cycle = st.selectbox(
            "💤 선호하는 바이오 사이클",
            options=[6.0, 7.5, 9.0],
            format_func=lambda x: f"{x}시간 (추천: {int(x//1.5)} 수면 사이클)",
            index=1,
            key="sl_cycle"
        )

    with col_sch2:
        st.markdown("<h4 style='color: #c7d2fe; font-weight:600;'>⌛ 스마트 아침 스케줄 분석 시나리오</h4>", unsafe_allow_html=True)
        
        # 스케줄 계산 로직
        try:
            today = datetime.date.today()
            arrival_datetime = datetime.datetime.combine(today, target_arrival)
            
            # 외출 시간 역산 = 이동시간 + 준비시간 + 버퍼시간
            total_required_minutes = commute_time + prep_time + buffer_min
            wakeup_datetime = arrival_datetime - datetime.timedelta(minutes=total_required_minutes)
            
            # 입면 역산 = 기상 시간 - 수면 사이클 - 평균 낙하수면 시간(15분)
            fall_asleep_buffer = 15
            total_sleep_minutes = int(sleep_cycle * 60) + fall_asleep_buffer
            bedtime_datetime = wakeup_datetime - datetime.timedelta(minutes=total_sleep_minutes)
            
            wakeup_str = wakeup_datetime.strftime("%H:%M")
            bedtime_str = bedtime_datetime.strftime("%H:%M")
            ready_str = (wakeup_datetime + datetime.timedelta(minutes=prep_time)).strftime("%H:%M")
            
            st.markdown(
                f"""
                <div class="result-box-premium" style="margin-top: 0;">
                    <span style="font-size: 1.1rem; font-weight: bold; color: #a5b4fc; display: block; margin-bottom: 0.5rem;">🌙 최적 입면 시각</span>
                    <h1 style="margin: 0; color: #fff; font-size: 3rem; font-weight: 700;">{bedtime_str}</h1>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 0.3rem;">평균 입면 소요 15분이 고려되어 있습니다. 침실 라이트를 끄고 매트리스에 완전히 이완되는 타깃 시간입니다.</p>
                </div>
                
                <div class="result-box-premium" style="border-color: rgba(56, 189, 248, 0.2);">
                    <span style="font-size: 1.1rem; font-weight: bold; color: #38bdf8; display: block; margin-bottom: 0.5rem;">⏰ 한계 마지노선 기상 시각</span>
                    <h1 style="margin: 0; color: #fff; font-size: 3rem; font-weight: 700;">{wakeup_str}</h1>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 0.3rem;">90분 램수면 주기 복귀점에 맞춘 세팅입니다. 해당 시간에 알람이 울려야 가뿐한 각성이 일어납니다.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            with st.expander("📍 타임 테이블 상세 흐름도"):
                st.markdown(
                    f"""
                    - **{bedtime_str}** : 전자기기를 완전히 소등하고 침실 입면 유도
                    - **{wakeup_str}** : 멜라토닌 분비 정상 정점 뇌파 각성 (기상 알람 작동)
                    - **{ready_str}** : 스타일링, 의복 정비 및 외출 준비 완료 후 도어 아웃
                    - **{arrival_datetime.strftime('%H:%M')}** : 목적지 도착 (돌발 여유 {buffer_min}분 사전 내포)
                    """
                )
        except Exception as e:
            st.error(f"계산 수행 오류: 타임 데이터를 올바르게 지정했는지 확인해 주세요. ({e})")

# ---------------------------------------------------------
# TAB 3: 아침 루틴 & 위생 가이드 (가독성 높은 위젯)
# ---------------------------------------------------------
with tabs[2]:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <h2 style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem;">🧠 아침 활력과 고밀도 숙면을 여는 생리적 원칙</h2>
            <p style="color: #94a3b8; font-size: 1rem; max-width: 700px; margin: 0 auto;">
                성공한 리더와 건강한 신체를 가진 이들이 고수하는 루틴과 위생법입니다. 
                매일 사소하게 바꾸어 가는 기적을 직접 경험하세요.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown(
            """
            <div class="result-box-premium" style="margin-top:0;">
                <h4 style="color: #818cf8; font-weight: 700; margin-bottom: 1rem;">🌅 기상 후 황금 60분 모닝 웰니스 가이드</h4>
                <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6;">
                    눈을 뜬 직후의 선택이 그날 오후의 피로도와 업무 효율을 결정합니다.
                </p>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">1. 미온수 한 잔 수분 긴급 주입</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">수면 도중 소실된 호흡기 및 피부의 땀, 수분을 긴급 벌크업하고 오장육부 소화 기계를 부드럽게 재부팅합니다.</p>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">2. 수직 천연 햇빛 샤워 (10분)</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">기상 직후 자연광을 눈 안쪽의 망막에 인식시키면 멜라토닌 분비가 끊어지고 스트레스를 억제하는 세로토닌의 폭발적 분비가 유도됩니다.</p>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">3. 모닝 림프 스트레칭</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">수면 시간 동안 경직되고 고여 있었던 관절막과 어깨 척추 라인을 이완하는 것만으로 심박수가 안심 궤도로 전환됩니다.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_g2:
        st.markdown(
            """
            <div class="result-box-premium" style="margin-top:0; border-color: rgba(248, 113, 113, 0.2);">
                <h4 style="color: #f87171; font-weight: 700; margin-bottom: 1rem;">🧬 완벽한 깊은 잠을 위한 핵심 수면 위생 수칙</h4>
                <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6;">
                    뇌가 수면에 최적화된 호르몬을 준비하도록 하는 야간 루틴입니다.
                </p>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">🚫 블루라이트 & 정보성 뇌 자극 금지</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">취침 최소 1시간 전 스마트폰 뇌파 자극을 차단해야 멜라토닌이 방해 없이 정상적으로 기저 분비되어 급속 입면이 가능해집니다.</p>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">🌡️ 최적의 침실 온온도 및 암막 유지</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">수면 중 심부 온도는 서서히 낮아집니다. 침실 온도를 약간 서늘한 18도에서 22도로 세팅하고, 완벽한 빛 차단 환경을 조성하세요.</p>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 1.2rem; border-radius: 12px;">
                    <h5 style="color: #f1f5f9; margin-top: 0;">⏱️ 주말 기상 골든 윈도우 사수</h5>
                    <p style="color: #94a3b8; font-size: 0.85rem; margin: 0;">평일 기상 시각과 주말 기상 시각 차이가 1.5시간 이상 과도하게 벌어지면 '사회적 시차증'에 빠집니다. 주말 늦잠은 일찍 잠드는 쪽으로 대체하세요.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# 5. 명품 감성의 하단 푸터 영역
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.85rem; padding-bottom:2rem;">
        <p>SnoozeWise Premium Analyzer — 설계된 내일을 살아가는 힘</p>
        <p style="margin-top:0.3rem; font-family:'Playfair Display', serif; font-style:italic; color:#818cf8;">Elevate your life with structured recovery.</p>
    </div>
    """,
    unsafe_allow_html=True
)
