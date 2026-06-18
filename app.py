import streamlit as st

# 1. 페이지 설정 및 프리미엄 스타일 적용
st.set_page_config(
    page_title="SnoozeWise | 프리미엄 수면 & 루틴 가이드",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 고급스러운 야간/우주 테마와 부드러운 애니메이션 효과를 주는 CSS 정의
st.markdown(
    """
    <style>
    @import url('[https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap](https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap)');
    
    /* 기본 폰트 설정 및 배경색 조정 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 타이틀 영역 애니메이션 */
    @keyframes fadeInDown {
        0% {
            opacity: 0;
            transform: translateY(-20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .header-section {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
        animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #a5b4fc 0%, #6366f1 50%, #4338ca 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .brand-subtitle {
        font-size: 1.2rem;
        color: #94a3b8;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* 카드 그리드 애니메이션 및 호버 효과 */
    .card-container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        min-height: 280px;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        cursor: pointer;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .card-container:hover {
        transform: translateY(-8px);
        background: rgba(99, 102, 241, 0.08);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
    }
    
    .card-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: inline-block;
        transition: transform 0.5s ease;
    }
    
    .card-container:hover .card-icon {
        transform: scale(1.15) rotate(5deg);
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 0.8rem;
    }
    
    .card-desc {
        font-size: 0.95rem;
        color: #94a3b8;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .card-badge {
        font-size: 0.8rem;
        padding: 4px 10px;
        background: rgba(99, 102, 241, 0.2);
        color: #c7d2fe;
        border-radius: 20px;
        align-self: flex-start;
        font-weight: 500;
    }

    /* 탭 스타일 고급화 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
        border: none;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        color: #94a3b8;
        padding: 0px 24px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(99, 102, 241, 0.1);
        color: #fff;
        border-color: rgba(99, 102, 241, 0.2);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #6366f1 !important;
        color: #fff !important;
        border-color: #6366f1 !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    /* 디테일 설명 뷰어 스타일 */
    .detail-box {
        background: linear-gradient(180deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2.5rem;
        margin-top: 1.5rem;
        animation: fadeIn 0.8s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. 메인 브랜드 헤더
st.markdown(
    """
    <div class="header-section">
        <div class="brand-title">SnoozeWise</div>
        <div class="brand-subtitle">THE ART OF SLEEP & MORNING ROUTINE</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 3. 4대 주요 핵심 기능 소개 카드 그리드
st.markdown("<h3 style='text-align: center; font-weight:400; color:#cbd5e1; margin-bottom:2rem;'>핵심 시스템 안내</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="card-container" style="animation-delay: 0.1s;">
            <div>
                <div class="card-icon">🌙</div>
                <div class="card-title">취침시간 추천 계산기</div>
                <div class="card-desc">인체의 90분 수면 사이클 분석을 적용해 가장 개운하게 일어날 수 있는 맞춤 입면 타이밍을 설계합니다.</div>
            </div>
            <div class="card-badge">바이오리듬 최적화</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card-container" style="animation-delay: 0.2s;">
            <div>
                <div class="card-icon">☀️</div>
                <div class="card-title">기상 후 황금 루틴</div>
                <div class="card-desc">눈을 뜨자마자 시작하는 첫 60분. 에너지 레벨을 급상승시키고 생체 시계를 리셋하는 건강 관리 루틴 가이드입니다.</div>
            </div>
            <div class="card-badge">모닝 웰니스</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card-container" style="animation-delay: 0.3s;">
            <div>
                <div class="card-icon">🚗</div>
                <div class="card-title">스마트 외출시간 설정</div>
                <div class="card-desc">이동 시간과 심리적 여유 버퍼를 고려하여 지각 없는 아침과 스트레스 없는 편안한 외출 준비 흐름을 제안합니다.</div>
            </div>
            <div class="card-badge">스트레스 프리</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="card-container" style="animation-delay: 0.4s;">
            <div>
                <div class="card-icon">🧘</div>
                <div class="card-title">규칙적인 수면 솔루션</div>
                <div class="card-desc">수면 호르몬인 멜라토닌 분비를 정상화하고 완벽한 수면 위생을 구축하기 위한 핵심 생활 수칙을 전수합니다.</div>
            </div>
            <div class="card-badge">데일리 오거나이저</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# 4. 탭 클릭 시 스무스하게 상세 정보를 전환하여 보여주는 인터랙티브 섹션
st.markdown("<h3 style='text-align: center; font-weight:400; color:#cbd5e1; margin-bottom:1.5rem;'>자세히 알아보기</h3>", unsafe_allow_html=True)

tabs = st.tabs(["💤 수면 계산 알고리즘", "🌅 활력 루틴 가이드", "⏱️ 안심 외출 로드맵", "🧬 수면 위생 가이드"])

# 탭 1: 취침시간 추천 계산기 원리
with tabs[0]:
    st.markdown(
        """
        <div class="detail-box">
            <h4 style="color:#a5b4fc; margin-bottom:1rem; font-size:1.3rem;">💡 수면의 양보다 중요한 '수면 사이클'의 비밀</h4>
            <p style="color:#94a3b8; line-height:1.7;">
                인간은 밤새 약 <b>90분 주기의 수면 단계(NREM-REM)</b>를 반복합니다. 깊은 수면 단계에서 억지로 깨어나면 하루 종일 극심한 
                피로감(수면 관성)을 느끼게 됩니다. SnoozeWise는 당신이 <b>얕은 수면(REM/Light Sleep)</b> 상태일 때 부드럽게 기상할 수 있도록 역산합니다.
            </p>
            <ul style="color:#cbd5e1; line-height:2; margin-top:1rem; padding-left:1.2rem;">
                <li><b>입면 버퍼 시간:</b> 누워서 실제로 잠들기까지 평균적으로 소요되는 <b>15분</b>을 자동 가산합니다.</li>
                <li><b>최적 사이클 추천:</b> 개인 취향과 피로 수준에 따라 4사이클(6시간), 5사이클(7.5시간), 6사이클(9시간)을 스마트하게 조율합니다.</li>
                <li><b>상쾌함의 극대화:</b> 알람이 울려도 뇌에 타격이 없는 편안한 아침을 보장합니다.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# 탭 2: 일어난 뒤 루틴
with tabs[1]:
    st.markdown(
        """
        <div class="detail-box">
            <h4 style="color:#86efac; margin-bottom:1rem; font-size:1.3rem;">🏃 기상 직후 1시간이 하루 전체를 지배합니다</h4>
            <p style="color:#94a3b8; line-height:1.7;">
                성공적인 아침은 단순히 눈을 빨리 뜨는 것이 아닌, 잠자고 있던 세포를 부드럽게 일깨우는 루틴에서 완성됩니다. 
                SnoozeWise가 권장하는 과학 기반 3단계 웰니스 단계입니다.
            </p>
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:1.5rem; margin-top:1.5rem;">
                <div style="background:rgba(255,255,255,0.02); padding:1.2rem; border-radius:15px; border-left:3px solid #86efac;">
                    <h5 style="color:#fff; margin-bottom:0.5rem;">1. 수분 섭취 (Hydration)</h5>
                    <p style="color:#94a3b8; font-size:0.85rem; margin:0;">밤새 호흡으로 소실된 수분을 충전하고 소화계와 장기를 부드럽게 일깨웁니다.</p>
                </div>
                <div style="background:rgba(255,255,255,0.02); padding:1.2rem; border-radius:15px; border-left:3px solid #86efac;">
                    <h5 style="color:#fff; margin-bottom:0.5rem;">2. 광합성 10분 (Sunlight)</h5>
                    <p style="color:#94a3b8; font-size:0.85rem; margin:0;">자연광을 쬐어 멜라토닌 분비를 멈추고 활력 호르몬인 코르티솔 분비를 촉진합니다.</p>
                </div>
                <div style="background:rgba(255,255,255,0.02); padding:1.2rem; border-radius:15px; border-left:3px solid #86efac;">
                    <h5 style="color:#fff; margin-bottom:0.5rem;">3. 가벼운 스트레칭 (Stretching)</h5>
                    <p style="color:#94a3b8; font-size:0.85rem; margin:0;">굳어 있던 척추와 관절을 이완시켜 전신 혈액 순환을 원활하게 돕습니다.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# 탭 3: 외출시간
with tabs[2]:
    st.markdown(
        """
        <div class="detail-box">
            <h4 style="color:#38bdf8; margin-bottom:1rem; font-size:1.3rem;">🚗 바쁜 아침, 여유를 지켜주는 스마트 안심 플래너</h4>
            <p style="color:#94a3b8; line-height:1.7;">
                매번 외출 전 시간이 부족해서 뛰어다니시나요? 지각에 대한 공포는 아침 뇌의 스트레스 수치를 최고치로 올립니다. 
                SnoozeWise는 역산 공식을 통해 완벽하고 품격 있는 준비 스케줄러를 선사합니다.
            </p>
            <ul style="color:#cbd5e1; line-height:2; margin-top:1rem; padding-left:1.2rem;">
                <li><b>스마트 목적 계산:</b> 미팅, 등교, 데이트 등 외출 성격에 따라 필요한 예비 안전 시간(10~25분)을 자동으로 설계합니다.</li>
                <li><b>준비 정밀 타임라인:</b> 샤워, 메이크업, 옷 입기 등 개인 행동 패턴에 걸리는 리얼 타임을 기상 시간에 완벽히 동기화합니다.</li>
                <li><b>교통 체증 대비 시스템:</b> 이동 중 예측 불가능한 돌발 상황까지 커버하여 목적지까지 마음 편하게 갈 수 있도록 돕습니다.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# 탭 4: 규칙적인 수면 솔루션
with tabs[3]:
    st.markdown(
        """
        <div class="detail-box">
            <h4 style="color:#fca5a5; margin-bottom:1rem; font-size:1.3rem;">🧬 최고의 성과를 위한 올바른 멜라토닌 위생법</h4>
            <p style="color:#94a3b8; line-height:1.7;">
                생체 시계(Circadian Rhythm)가 어긋나면 아무리 많이 자도 피곤함을 느낍니다. 
                매일 밤 더 쉽게 기분 좋은 깊은 잠에 들 수 있도록 돕는 실천 가능한 과학적 수면 습관 가이드라인입니다.
            </p>
            <ul style="color:#cbd5e1; line-height:2; margin-top:1rem; padding-left:1.2rem;">
                <li><b>블루라이트 차단 (암막 효과):</b> 취침 1시간 전 스마트폰 사용을 제한하여 숙면 유도 호르몬인 멜라토닌 분비를 극대화합니다.</li>
                <li><b>일정한 기상/취침 윈도우:</b> 주말에도 평소 기상 시간 기준 최대 1시간 내외의 규칙성을 유지하여 생체 리듬의 축을 고정합니다.</li>
                <li><b>스마트 수면 환경 세팅:</b> 최적 수면 온도인 18~22도 조율과 은은한 백색 소음, 부드러운 전등 배치 기법을 추천합니다.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# 5. 푸터 영역
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.85rem; padding-bottom:2rem;">
        <p>SnoozeWise Premium App — 나만의 완벽한 아침 시뮬레이터</p>
        <p style="margin-top:0.3rem; font-family:'Playfair Display', serif; font-style:italic;">Your personalized sleep path starts here.</p>
    </div>
    """,
    unsafe_allow_html=True
)
