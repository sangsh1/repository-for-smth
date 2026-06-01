import streamlit as st

st.set_page_config(
    page_title="이한빈의 스키비디 토일렛 완전 정복 위키",
    page_icon="🚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&family=Black+Han+Sans&display=swap');

html, body, .stApp {
    background-color: #080814 !important;
    color: #dde4ff !important;
    font-family: 'Nanum Gothic', sans-serif !important;
}
section[data-testid="stSidebar"] {
    background: #0c0c20 !important;
    border-right: 1px solid #1e1e4a;
}
section[data-testid="stSidebar"] * { color: #c0caff !important; }
h1,h2,h3 { font-family: 'Black Han Sans', cursive !important; }
h1 { font-size:2.4rem !important; color:#7eb3ff !important; letter-spacing:3px; }
h2 { font-size:1.5rem !important; color:#aac8ff !important; }
h3 { font-size:1.1rem !important; color:#c8dcff !important; }

.stTabs [data-baseweb="tab-list"] {
    background:#10102a; border-radius:10px; padding:4px; gap:4px;
}
.stTabs [data-baseweb="tab"] {
    background:transparent; color:#7788bb;
    border-radius:8px; font-family:'Nanum Gothic',sans-serif; font-weight:700;
}
.stTabs [aria-selected="true"] { background:#22226a !important; color:#aaccff !important; }

div[data-baseweb="input"] input {
    background:#12122e !important; color:#d0d8ff !important;
    border:1px solid #2a2a6a !important; border-radius:8px !important;
}
div[data-baseweb="select"] > div {
    background:#12122e !important; color:#d0d8ff !important;
    border:1px solid #2a2a6a !important;
}
.stRadio label { color:#b0b8e8 !important; }
hr { border-color:#1a1a3a !important; }

/* ── 카드 ── */
.wiki-card {
    background:#0e0e24;
    border:1px solid #1e1e4a;
    border-radius:14px;
    padding:20px 22px 16px;
    margin-bottom:18px;
    position:relative; overflow:hidden;
}
.wiki-card::before {
    content:''; position:absolute; top:0; left:0;
    width:4px; height:100%;
}
.wiki-card.toilet::before  { background:#ff3333; }
.wiki-card.alliance::before{ background:#3388ff; }
.wiki-card.astro::before   { background:#aa44ff; }
.wiki-card.neutral::before { background:#ffaa33; }
.wiki-card.episode::before { background:#33ccaa; }

/* ── 배지 ── */
.badge {
    display:inline-block; padding:3px 10px; border-radius:20px;
    font-size:0.72rem; font-weight:800; margin:2px; letter-spacing:0.5px;
}
.b-toilet   { background:#2a0000; border:1px solid #ff3333; color:#ff9999; }
.b-alliance { background:#001a33; border:1px solid #3388ff; color:#88ccff; }
.b-astro    { background:#1a0033; border:1px solid #aa44ff; color:#cc99ff; }
.b-neutral  { background:#1a1400; border:1px solid #ffaa33; color:#ffdd99; }
.b-alive    { background:#001a00; border:1px solid #33cc33; color:#88ff88; }
.b-dead     { background:#1a0000; border:1px solid #cc3333; color:#ff8888; }
.b-infected { background:#1a0d00; border:1px solid #ff8833; color:#ffcc88; }
.b-unknown  { background:#111111; border:1px solid #666666; color:#aaaaaa; }
.b-type     { background:#0e0e2a; border:1px solid #334488; color:#8899cc; }
.b-ep       { background:#001a14; border:1px solid #336655; color:#77ccaa; }

/* ── 이한빈 말풍선 ── */
.hb-talk {
    background:#0c0c22;
    border:1px solid #2244aa;
    border-radius:14px 14px 14px 2px;
    padding:12px 16px;
    margin-bottom:14px;
    font-size:0.88rem; line-height:1.8; color:#b8caff;
    position:relative;
}
.hb-talk::before {
    content:'🎮 이한빈';
    display:block; font-weight:800; font-size:0.75rem;
    color:#5588ff; margin-bottom:5px;
}
.hb-intro {
    background:#0c0c22;
    border:1.5px solid #3355bb;
    border-radius:12px;
    padding:14px 18px;
    margin:16px 0 22px;
    font-size:0.92rem; line-height:1.85; color:#c0d0ff;
}
.hb-intro::before {
    content:'🎮 이한빈 인트로';
    display:block; font-weight:800; font-size:0.8rem;
    color:#5588ff; margin-bottom:7px;
}

/* ── 섹션 타이틀 ── */
.sec-title {
    font-family:'Black Han Sans',cursive;
    font-size:1rem; color:#5588ff;
    border-bottom:1px solid #1a1a3a;
    padding-bottom:5px; margin:12px 0 10px;
}

/* ── 설명박스 ── */
.desc-box {
    background:#0a0a1e; border-radius:10px; padding:12px 14px;
    font-size:0.88rem; line-height:1.8; color:#b0bce0; margin-bottom:12px;
}

/* ── 능력 태그 ── */
.ab-tag {
    display:inline-block; background:#111830;
    border:1px solid #223366;
    border-radius:6px; padding:3px 10px; margin:2px;
    font-size:0.77rem; color:#99aace;
}

/* ── 약점 ── */
.weak-box {
    background:#140808; border:1px solid #441111;
    border-radius:8px; padding:7px 12px;
    font-size:0.82rem; color:#ff8888; margin-bottom:10px;
}

/* ── 스탯 ── */
.stat-row { margin:3px 0; display:flex; align-items:center; gap:6px; }
.stat-lbl { font-size:0.77rem; color:#6677aa; width:44px; flex-shrink:0; }
.stat-val { font-size:0.77rem; font-weight:800; width:26px; text-align:right; flex-shrink:0; }
.stat-bar-bg { flex:1; background:#0a0a1e; border-radius:4px; height:7px; overflow:hidden; }
.stat-bar-fill { height:7px; border-radius:4px; }

/* ── 에피소드 카드 ── */
.ep-card {
    background:#0a0a1e; border:1px solid #1a1a3a;
    border-radius:12px; padding:14px 16px; margin-bottom:12px;
    position:relative; overflow:hidden;
}
.ep-card::before {
    content:''; position:absolute; top:0; left:0;
    width:3px; height:100%; background:#33ccaa;
}
.ep-num { font-family:'Black Han Sans',cursive; font-size:1rem; color:#33ccaa; margin-bottom:4px; }
.ep-title { font-size:0.9rem; font-weight:800; color:#c0d0ff; margin-bottom:6px; }
.ep-desc { font-size:0.82rem; line-height:1.75; color:#8899bb; }
.ep-hb { font-size:0.8rem; color:#5566aa; font-style:italic; margin-top:6px;
    border-top:1px solid #111128; padding-top:6px; }

/* ── 통계 카드 ── */
.stat-summary-card {
    background:#0e0e24; border:1px solid #1e1e4a;
    border-radius:12px; padding:16px; text-align:center;
}
.ssn { font-family:'Black Han Sans',cursive; font-size:1.9rem; }
.ssl { font-size:0.78rem; color:#445577; margin-top:2px; }

/* ── 아스트로 특별 ── */
.astro-glow {
    box-shadow: 0 0 18px #aa44ff22;
    border-color: #4422aa !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
#  데이터
# ══════════════════════════════════════════════════════════════════

CHARS = [
    # ── 토일렛 진영 ──────────────────────────────────────────────
    dict(name="노멀 스키비디 토일렛", emoji="🚽", faction="toilet",
         status="alive", type_="기본 유닛", ep="에피소드 1",
         desc="변기 위에 사람 머리가 달라붙은 기본 유닛이야. 혼자론 약하지만 수십~수백 마리가 한꺼번에 몰려오면 진짜 답이 없음. 물 뿜기랑 물어뜯기로 공격하는데 초반에 카메라맨들 완전히 압도하면서 등장해서 시청자들한테 충격을 줬지.",
         quote="야 이거 처음 봤을 때 '이게 뭐야?' 하고 웃었는데 진짜 무서워지는 게 이 시리즈의 포인트임 ㅋㅋ",
         abilities=["물 분사", "물어뜯기", "떼 습격", "기습 돌진"],
         weakness="카메라맨 플래시·스피커맨 음파",
         stats=dict(공격=30, 방어=20, 속도=50, 지능=10)),
    dict(name="라지 스키비디 토일렛", emoji="🚽", faction="toilet",
         status="alive", type_="대형 유닛", ep="에피소드 4",
         desc="노멀보다 훨씬 크고 육중한 대형 변기야. 강력한 물 분사랑 돌진으로 카메라맨 여러 명을 한 번에 날려버려. 혼자로도 상당히 위협적이라 중반까지 동맹군이 꽤 고생하는 상대임.",
         quote="이 녀석은 덩치로 밀어붙이는 타입인데 카메라맨 혼자 붙으면 진짜 위험함.",
         abilities=["강력한 물 분사", "돌진", "광역 충격파"],
         weakness="집중 포화·협동 공격",
         stats=dict(공격=60, 방어=55, 속도=30, 지능=20)),
    dict(name="자이언트 스키비디 토일렛", emoji="🏗️", faction="toilet",
         status="alive", type_="초대형 유닛", ep="에피소드 10",
         desc="건물이랑 맞먹는 크기의 초대형 변기야. 등장 자체가 이벤트 수준이고 밟기만 해도 건물이 무너짐. 분사 공격 한 방에 지역 전체가 날아가는 수준이라 G맨이나 타이탄 없이는 진짜 답 없음.",
         quote="처음 등장했을 때 채팅창이 '와' 로 도배됐잖아 ㅋㅋ 진짜 스케일이 달랐음.",
         abilities=["초대형 물 분사", "건물 파괴", "지진 발생", "광역 범위 공격"],
         weakness="타이탄급 동맹군·G맨 집중 공격",
         stats=dict(공격=95, 방어=85, 속도=15, 지능=35)),
    dict(name="스트롱 스키비디 토일렛", emoji="💪", faction="toilet",
         status="alive", type_="근력 특화형", ep="에피소드 7",
         desc="근육이 비정상적으로 발달한 강화형 변기야. 근접 전투에서 카메라맨을 한 방에 날려버리는 괴력을 가지고 있어. 보기엔 웃기지만 막상 싸우면 진짜 무서운 유닛임.",
         quote="팔뚝 보고 웃다가 카메라맨 날아가는 거 보고 ㄹㅇ 충격받았음 ㅋㅋ",
         abilities=["근접 강타", "던지기 공격", "돌진 박치기"],
         weakness="원거리 공격·스피커맨 음파",
         stats=dict(공격=75, 방어=70, 속도=35, 지능=25)),
    dict(name="카무플라주 스키비디 토일렛", emoji="🫥", faction="toilet",
         status="alive", type_="스텔스형", ep="에피소드 12",
         desc="투명 위장 기능을 가진 은신 특화 유닛이야. 탐지 장비 없이는 발견 자체가 불가능해. 기습 공격 전문이고 단독 침투 임무에 자주 활용됨.",
         quote="처음엔 진짜 몰랐음. 카메라맨이 갑자기 날아가는데 원인을 모르는 거야 ㄷㄷ",
         abilities=["투명화", "소음 제거", "기습 공격"],
         weakness="열화상 카메라·음파 탐지기",
         stats=dict(공격=55, 방어=30, 속도=70, 지능=60)),
    dict(name="파라슈트 스키비디 토일렛", emoji="🪂", faction="toilet",
         status="alive", type_="공중 강하형", ep="에피소드 8",
         desc="낙하산을 달고 하늘에서 강하하는 변기야. 동맹군 기지 위에서 쏟아지듯 떨어지는 방식으로 기습하고 낙하 충격으로 폭발 효과도 만들어냄.",
         quote="하늘에서 변기가 쏟아진다는 발상이 이미 천재임 ㅋㅋㅋ",
         abilities=["공중 강하", "낙하 충격 폭발", "정찰"],
         weakness="대공 무기·TV맨 레이저",
         stats=dict(공격=45, 방어=35, 속도=65, 지능=40)),
    dict(name="제트팩 스키비디 토일렛", emoji="🚀", faction="toilet",
         status="alive", type_="비행 전투형", ep="에피소드 13",
         desc="제트팩으로 자유롭게 비행하는 고기동 유닛이야. 엄청 빠른 속도로 진형을 교란하고 공중에서 폭격하는 방식으로 싸워. 따라잡기도 진짜 힘든 녀석임.",
         quote="이 녀석은 진짜 빠름. 도망가는 건지 공격하는 건지 구분도 안 됨 ㅋㅋ",
         abilities=["고속 비행", "공중 폭격", "기동 회피"],
         weakness="대공 미사일·G맨 공중전",
         stats=dict(공격=60, 방어=40, 속도=85, 지능=45)),
    dict(name="탱크 스키비디 토일렛", emoji="🛡️", faction="toilet",
         status="alive", type_="중장갑형", ep="에피소드 16",
         desc="두꺼운 장갑판을 두른 요새 같은 변기야. 포탑까지 달려있어서 원거리 포격도 가능하고 정면 돌파 전술에 완전 특화됨. 왠만한 공격은 그냥 씹어버리는 내구성임.",
         quote="포탄 맞아도 멀쩡히 걸어오는 거 보고 '아 이건 답없다' 했잖아.",
         abilities=["장갑 방어", "포탑 사격", "돌격 돌파"],
         weakness="EMP 공격·강력한 폭발물",
         stats=dict(공격=80, 방어=90, 속도=20, 지능=30)),
    dict(name="보스 스키비디 토일렛", emoji="👑", faction="toilet",
         status="alive", type_="총사령관", ep="에피소드 20",
         desc="스키비디 토일렛 군단 전체를 지휘하는 두뇌이자 최강 유닛이야. 에너지 폭발, 재생 능력, 텔레포트를 모두 보유하고 다른 유닛들도 원격 강화할 수 있어. G맨이나 TV맨이 아니면 상대 자체가 안 되는 레벨임.",
         quote="이 녀석이 나오는 에피소드는 긴장감 자체가 다름. 진짜 최종 보스 느낌.",
         abilities=["에너지 폭발", "재생 능력", "유닛 강화", "텔레포트", "심리 지배"],
         weakness="G맨+TV맨 연합 공격",
         stats=dict(공격=92, 방어=88, 속도=50, 지능=95)),
    dict(name="스파이더 스키비디 토일렛", emoji="🕷️", faction="toilet",
         status="alive", type_="거미형 특수체", ep="에피소드 18",
         desc="거미 다리를 달고 벽이랑 천장을 자유롭게 이동하는 특수 유닛이야. 좁은 건물 내부에서 특히 무서운데 거미줄로 적을 속박하고 독 공격도 가능해서 장기전에서 진짜 골치임.",
         quote="천장에서 뚝 떨어지는 거 보고 소름 돋았잖아. 그냥 공포물이냐고 ㄷㄷ",
         abilities=["벽·천장 이동", "거미줄 속박", "독 공격"],
         weakness="불·폭발물·넓은 공간",
         stats=dict(공격=55, 방어=45, 속도=75, 지능=50)),
    dict(name="로봇 스키비디 토일렛", emoji="🤖", faction="toilet",
         status="alive", type_="기계 강화형", ep="에피소드 19",
         desc="기계 부품으로 온몸을 강화한 사이보그 변기야. 금속 장갑이랑 기계 팔 덕분에 내구성이 비약적으로 올랐고 자가 수리 기능도 있어서 왠만해선 파괴가 안 돼.",
         quote="부수면 수리하고 또 부수면 또 수리하고... TV맨 EMP 없으면 진짜 귀찮음.",
         abilities=["자가 수리", "기계 팔 공격", "중장갑"],
         weakness="EMP·TV맨 전자기 공격",
         stats=dict(공격=70, 방어=80, 속도=30, 지능=55)),
    dict(name="사이보그 스키비디 토일렛", emoji="⚙️", faction="toilet",
         status="alive", type_="풀 사이보그형", ep="에피소드 21",
         desc="생체와 기계를 완전히 결합한 최첨단 유닛이야. 레이저 눈, 로켓 추진, 자폭 장치까지 다 갖추고 있어서 어떤 전투 상황에도 대응하는 올라운더 타입임.",
         quote="이거 어떻게 잡냐 진짜... 각도마다 다른 무기 꺼내는 게 말이 됩니까 ㅋㅋ",
         abilities=["레이저 눈", "로켓 추진 돌격", "자폭 공격"],
         weakness="G맨·타이탄급 동맹군",
         stats=dict(공격=82, 방어=75, 속도=60, 지능=70)),
    dict(name="핵 스키비디 토일렛", emoji="☢️", faction="toilet",
         status="alive", type_="핵무장형", ep="에피소드 32",
         desc="핵탄두를 장착한 초위험 유닛이야. 자폭 시 엄청난 반경에 방사능 피해를 줘서 동맹군 진영 전체를 날려버릴 수 있음. 등장 자체로 공포 분위기를 만들어버리는 녀석.",
         quote="이거 나왔을 때 진짜 '아 이제 어떻게 싸워' 했잖아. 자폭 카드가 있는 상대는 답이 없음.",
         abilities=["핵 자폭", "방사능 오염", "광역 파괴"],
         weakness="원거리 즉사·접근 전 차단",
         stats=dict(공격=99, 방어=50, 속도=25, 지능=40)),

    # ── 동맹군 진영 ──────────────────────────────────────────────
    dict(name="카메라맨", emoji="📷", faction="alliance",
         status="alive", type_="기본 전투원", ep="에피소드 1",
         desc="머리에 카메라를 달고 싸우는 동맹군의 기본 병사야. 카메라 플래시로 토일렛을 약화시키거나 직접 타격도 가능해. 시리즈 내내 꾸준히 활약하는 진짜 주인공 같은 존재임.",
         quote="카메라맨이 동맹군의 핵심이지. 업그레이드될수록 점점 강해지는 성장형 캐릭터야.",
         abilities=["카메라 플래시", "근접 타격", "팀 전술 조율"],
         weakness="대형 토일렛·감염 바이러스",
         stats=dict(공격=45, 방어=40, 속도=55, 지능=60)),
    dict(name="업그레이드 카메라맨", emoji="🔭", faction="alliance",
         status="alive", type_="강화 전투원", ep="에피소드 9",
         desc="기본 카메라맨이 각종 장비로 강화된 버전이야. 레이저 조준경, 방호 장갑, 고출력 플래시를 달아서 화력이 크게 올랐어. 중반부 동맹군의 주력 전투원이야.",
         quote="업글 카메라맨 나오고 나서 동맹군 전투력이 확 올라갔잖아. 변화점이 여기임.",
         abilities=["레이저 조준", "강화 플래시", "장갑 방어"],
         weakness="탱크 토일렛·집중 포화",
         stats=dict(공격=58, 방어=60, 속도=50, 지능=65)),
    dict(name="스피커맨", emoji="🔊", faction="alliance",
         status="alive", type_="음파 전투원", ep="에피소드 3",
         desc="머리에 스피커를 달고 강력한 음파로 싸우는 전사야. 카메라맨보다 전투력이 한 수 위이고 넓은 범위를 동시에 공격할 수 있어. 음파 폭발은 토일렛한테 유독 효과적임.",
         quote="스피커맨 음파 터지는 거 보면 진짜 속이 다 뻥 뚫림 ㅋㅋ 시원해.",
         abilities=["음파 공격", "초음파 폭발", "방어막 생성"],
         weakness="대형 토일렛·보스급 유닛",
         stats=dict(공격=65, 방어=55, 속도=50, 지능=65)),
    dict(name="TV맨", emoji="📺", faction="alliance",
         status="alive", type_="엘리트 전사", ep="에피소드 6",
         desc="머리에 TV를 달고 있는 동맹군 최고 엘리트 전사야. 레이저 빔, 텔레포트, EMP 공격까지 다 갖추고 있고 G맨이랑 함께 동맹군 양대 에이스임. 전략적 사고력도 뛰어나서 작전 지휘도 담당함.",
         quote="TV맨 레이저 한 방에 중형 토일렛 여럿 관통하는 거 볼 때마다 소름 ㄷㄷ",
         abilities=["레이저 빔", "텔레포트", "EMP", "전장 분석"],
         weakness="보스 토일렛·감염",
         stats=dict(공격=85, 방어=75, 속도=80, 지능=90)),
    dict(name="G맨", emoji="🕶️", faction="alliance",
         status="alive", type_="최강 전사", ep="에피소드 15",
         desc="선글라스 하나가 트레이드마크인 동맹군 절대 에이스야. 물리적 힘, 에너지 공격, 비행 능력을 모두 갖추고 보스급 토일렛이랑 1:1이 가능한 유일한 존재임. 등장만으로 전세가 바뀌는 게임 체인저.",
         quote="G맨 나오는 순간 다 됐다 싶잖아. 그냥 다 됨. 무조건 이김. 이건 공식임.",
         abilities=["에너지 폭발", "비행", "초강력 근접 전투", "보호막"],
         weakness="특수 감염 바이러스·집중 포화",
         stats=dict(공격=98, 방어=92, 속도=88, 지능=85)),
    dict(name="타이탄 카메라맨", emoji="🗼", faction="alliance",
         status="alive", type_="타이탄급", ep="에피소드 25",
         desc="카메라맨이 도시 블록 크기로 강화된 타이탄 유닛이야. 자이언트 토일렛이랑 맞짱 뜰 수 있는 규모고 광선 한 방에 건물이 날아가고 주먹 한 방에 지면이 갈라짐. 동맹군 열세를 뒤집는 역할을 함.",
         quote="이 장면 처음 봤을 때 '드디어!' 하고 소리 질렀잖아 ㅋㅋ 완전 카타르시스",
         abilities=["초대형 카메라 광선", "지면 충격파", "근접 초강타"],
         weakness="타이탄급 토일렛·보스 집중 공격",
         stats=dict(공격=96, 방어=90, 속도=20, 지능=70)),
    dict(name="타이탄 TV맨", emoji="📡", faction="alliance",
         status="alive", type_="타이탄급", ep="에피소드 27",
         desc="TV맨이 타이탄 수준으로 각성한 형태야. 광역 레이저 폭격이랑 차원 이동 능력이 극대화되어서 전장 전체를 혼자 통제하는 수준의 전투력을 가졌어.",
         quote="타이탄 TV맨이랑 타이탄 카메라맨 같이 나오는 씬은 진짜 영화임.",
         abilities=["광역 레이저 폭격", "차원 이동", "전장 통제", "EMP 광역"],
         weakness="보스 스키비디 토일렛",
         stats=dict(공격=97, 방어=89, 속도=75, 지능=96)),
    dict(name="타이탄 스피커맨", emoji="📣", faction="alliance",
         status="alive", type_="타이탄급", ep="에피소드 29",
         desc="스피커맨이 타이탄 수준으로 성장한 형태야. 초음파 광역 공격으로 넓은 범위의 토일렛을 동시에 파괴할 수 있고 그 울림이 수 킬로미터 밖에서도 느껴짐.",
         quote="이 소리 들리면 토일렛 입장에서 진짜 공포겠다 ㄷㄷ",
         abilities=["광역 초음파", "음파 충격파", "광역 방어막"],
         weakness="타이탄 토일렕·방음 장갑",
         stats=dict(공격=93, 방어=87, 속도=55, 지능=80)),
    dict(name="TV우먼", emoji="📻", faction="alliance",
         status="alive", type_="엘리트 전사", ep="에피소드 35",
         desc="TV맨의 여성형 버전으로 더욱 정밀한 전술적 판단력을 보유하고 있어. 레이저 정밀 사격과 전장 해킹 능력이 뛰어나서 TV맨과 콤비로 자주 등장하는 강력한 전사임.",
         quote="TV우먼 나왔을 때 다들 TV맨이랑 커플이냐고 댓글 폭발했잖아 ㅋㅋㅋ",
         abilities=["정밀 레이저", "전장 해킹", "전자기 방어막"],
         weakness="보스 토일렛·집중 공격",
         stats=dict(공격=83, 방어=78, 속도=82, 지능=93)),

    # ── 아스트로 진영 ──────────────────────────────────────────────
    dict(name="아스트로 카메라맨", emoji="🧑‍🚀", faction="astro",
         status="alive", type_="우주 전투원", ep="에피소드 40",
         desc="우주 공간에서 활동하는 카메라맨의 우주복 버전이야. 무중력 환경에서 자유롭게 이동하고 우주 레이저 무기를 사용해. 지구 전투랑 차원이 다른 스케일의 전쟁이 우주로 확장되면서 등장함.",
         quote="우주로 전쟁이 확장됐을 때 진짜 '와 이 시리즈 얼마나 커질 거야?' 했잖아 ㄷㄷ",
         abilities=["우주 레이저", "무중력 기동", "우주복 방어", "위성 통신"],
         weakness="우주 토일렛 집중 공격",
         stats=dict(공격=72, 방어=68, 속도=80, 지능=75)),
    dict(name="아스트로 TV맨", emoji="🛸", faction="astro",
         status="alive", type_="우주 엘리트", ep="에피소드 42",
         desc="TV맨이 우주 환경에 특화된 형태로 강화된 버전이야. 우주 공간에서의 전자기 공격 범위가 지구에서보다 훨씬 넓어지고 행성 간 텔레포트도 가능해진 무서운 존재임.",
         quote="우주 TV맨은 진짜 레벨이 다름. 텔레포트 범위가 행성 단위야 행성 단위.",
         abilities=["행성 간 텔레포트", "광역 우주 EMP", "위성 레이저", "블랙홀 포착"],
         weakness="아스트로 보스 토일렛",
         stats=dict(공격=90, 방어=82, 속도=88, 지능=96)),
    dict(name="아스트로 스피커맨", emoji="🔭", faction="astro",
         status="alive", type_="우주 음파 전투원", ep="에피소드 43",
         desc="우주 공간에서 음파 대신 전자기파를 무기로 사용하는 스피커맨의 우주 버전이야. 소리가 없는 우주에서도 전자기파 공격으로 광범위한 피해를 줄 수 있어.",
         quote="소리 없는 우주에서 스피커맨이 어떻게 싸우냐 했더니 전자기파로 싸우는 거 보고 설정 마음에 들었음.",
         abilities=["전자기파 공격", "우주 광역 충격", "전파 교란"],
         weakness="전자기 차폐 장갑",
         stats=dict(공격=80, 방어=72, 속도=65, 지능=78)),
    dict(name="아스트로 G맨", emoji="⭐", faction="astro",
         status="alive", type_="우주 최강 전사", ep="에피소드 45",
         desc="G맨이 우주 공간에서 완전히 각성한 최강 형태야. 우주 에너지를 흡수해서 전투력이 지구에서보다 몇 배 이상 강해지고 블랙홀 수준의 에너지 공격을 사용할 수 있어.",
         quote="아스트로 G맨 나왔을 때 진짜 이 시리즈 끝판왕 나왔구나 싶었음. 압도적임.",
         abilities=["우주 에너지 폭발", "블랙홀 인력", "광속 비행", "행성 파괴급 공격"],
         weakness="우주 보스 토일렛 연합 공격",
         stats=dict(공격=99, 방어=95, 속도=97, 지능=90)),
    dict(name="아스트로 타이탄 카메라맨", emoji="🌌", faction="astro",
         status="alive", type_="우주 타이탄급", ep="에피소드 47",
         desc="타이탄 카메라맨이 우주 환경에서 추가 강화된 궁극 형태야. 달이나 소행성 크기에 비견되는 거대한 몸체로 우주 전쟁의 판도를 바꾸는 절대적인 존재임.",
         quote="이 장면 보고 진짜 말을 잃었음. 규모 자체가 달랐어. 달이 움직이는 줄 알았잖아.",
         abilities=["행성급 카메라 빔", "소행성 투척", "우주 충격파", "중력 조작"],
         weakness="다중 아스트로 보스 집중 공격",
         stats=dict(공격=99, 방어=96, 속도=30, 지능=80)),
    dict(name="우주 스키비디 토일렛", emoji="🌑", faction="astro",
         status="alive", type_="우주 토일렛", ep="에피소드 41",
         desc="우주 공간에 서식하는 스키비디 토일렛의 우주 버전이야. 진공 상태에서도 활동 가능하고 운석을 투척하거나 우주 방사선을 분사하는 방식으로 공격함. 아스트로 동맹군의 주적임.",
         quote="우주에서도 변기가 나온다는 게 진짜 이 시리즈의 스케일을 보여주는 거잖아 ㅋㅋ",
         abilities=["우주 방사선 분사", "운석 투척", "진공 생존"],
         weakness="아스트로 카메라맨·아스트로 TV맨",
         stats=dict(공격=65, 방어=60, 속도=55, 지능=30)),

    # ── 중립·특수 ──────────────────────────────────────────────
    dict(name="감염된 카메라맨", emoji="😈", faction="neutral",
         status="infected", type_="감염체", ep="에피소드 11",
         desc="토일렛 진영에 감염되어 적으로 돌아선 카메라맨이야. 아군인 척 위장하고 내부에서 사보타주하거나 기습할 수 있어서 외형상으로 구분이 잘 안 돼서 더 무서운 존재임.",
         quote="이게 진짜 충격이었어. 아군이 갑자기 내 카메라맨 때리는 거 보고 '이건 반칙이다' 했잖아.",
         abilities=["위장 침투", "내부 사보타주", "아군 혼란 유발"],
         weakness="G맨 식별·정화 장치",
         stats=dict(공격=55, 방어=40, 속도=55, 지능=70)),
    dict(name="사이렌 헤드 변형체", emoji="🚨", faction="neutral",
         status="unknown", type_="사이렌형 특수체", ep="에피소드 22",
         desc="사이렌 소리를 내는 변형 스키비디 토일렛이야. 귀를 찢는 경보음으로 동맹군을 마비시키고 주변 유리를 산산조각 냄. 정확한 소속이 불분명해서 더 미스터리한 존재야.",
         quote="이 소리 헤드셋 끼고 들었다가 귀 죽는 줄 알았음 ㅋㅋㅋ",
         abilities=["경보음 마비", "유리 파괴 음파", "공포 유발"],
         weakness="방음 장비·스피커맨 역음파",
         stats=dict(공격=65, 방어=50, 속도=40, 지능=45)),
    dict(name="멀티플 스크린 TV맨", emoji="🖥️", faction="neutral",
         status="unknown", type_="미지의 존재", ep="에피소드 50",
         desc="여러 개의 TV 화면을 달고 있는 미지의 존재야. 동맹군도 토일렛도 아닌 것처럼 보이는데 정확한 소속이나 목적을 아직 아무도 몰라. 등장 자체로 엄청난 떡밥을 남겼음.",
         quote="이 존재는 진짜 모름. 아직도 정체를 모르겠어. 다음 에피소드에 답이 나오겠지...",
         abilities=["다중 화면 혼란", "현실 왜곡", "전파 장악"],
         weakness="불명",
         stats=dict(공격=88, 방어=80, 속도=70, 지능=99)),
]

# ── 에피소드 데이터 ──────────────────────────────────────────────
EPISODES = [
    dict(num="에피소드 1", title="스키비디 토일렛의 등장", arc="시즌 1",
         desc="스키비디 토일렛이 처음으로 세상에 나타나 카메라맨들을 습격하기 시작함. 변기 안에서 머리가 튀어나오는 충격적인 장면으로 시리즈가 시작됨.",
         hb="이 에피소드 보고 진짜 '이게 뭐야?' 했는데 계속 보게 되더라고. 중독성이 미쳤음."),
    dict(num="에피소드 2", title="카메라맨의 반격", arc="시즌 1",
         desc="카메라맨들이 처음으로 스키비디 토일렛에게 반격을 시도함. 카메라 플래시가 토일렛에게 효과적임을 발견하게 되는 중요한 에피소드.",
         hb="카메라 플래시가 약점이라는 걸 알게 되는 씬이야. 처음으로 희망이 생기는 느낌이었음."),
    dict(num="에피소드 3", title="스피커맨 등장", arc="시즌 1",
         desc="강력한 음파 무기를 가진 스피커맨이 처음 등장해서 토일렛 여러 마리를 한 번에 처리함. 동맹군 전력이 업그레이드되는 첫 번째 순간.",
         hb="스피커맨 음파 터지는 거 보고 진짜 '오 이제 좀 싸우겠다' 했잖아."),
    dict(num="에피소드 4", title="라지 토일렛의 위협", arc="시즌 1",
         desc="대형 스키비디 토일렛이 처음 등장해 동맹군에게 큰 피해를 입힘. 기본 카메라맨 혼자로는 처리가 불가능해서 협동 전술이 필요해지기 시작함.",
         hb="대형이 나오니까 갑자기 난이도가 확 올라간 느낌이었음."),
    dict(num="에피소드 5", title="도시 전쟁", arc="시즌 1",
         desc="전쟁이 도시 전체로 확산됨. 토일렛 군단이 건물마다 숨어서 기습하는 전술을 쓰기 시작하고 민간 지역까지 피해가 번짐.",
         hb="도시 스케일로 커지는 게 보이면서 이 시리즈가 단순한 개그물이 아니라는 걸 느꼈음."),
    dict(num="에피소드 6", title="TV맨의 등장", arc="시즌 2",
         desc="머리에 TV를 달고 있는 강력한 전사 TV맨이 처음 등장함. 레이저 빔과 텔레포트 능력으로 전황을 단번에 뒤집어 버리는 충격적인 데뷔전.",
         hb="TV맨 나왔을 때 채팅창 완전 폭발했잖아. 이 캐릭터가 왜 이렇게 멋있냐고."),
    dict(num="에피소드 7", title="스트롱 토일렛 출현", arc="시즌 2",
         desc="근육이 발달한 강화형 스트롱 토일렛이 등장해 스피커맨을 고전시킴. 토일렛 진영도 진화하고 있다는 걸 처음으로 보여준 에피소드.",
         hb="이 에피소드 보고 '아 토일렛도 강해지는구나' 했음. 단순한 구도가 아니야."),
    dict(num="에피소드 8", title="하늘에서 쏟아지는 변기", arc="시즌 2",
         desc="파라슈트 토일렛이 처음 등장해 하늘에서 기습하기 시작함. 동맹군이 공중 위협에 대한 대비가 없어서 큰 피해를 입음.",
         hb="하늘에서 변기가 쏟아진다는 발상 자체가 천재잖아 ㅋㅋ"),
    dict(num="에피소드 9", title="동맹군 업그레이드", arc="시즌 2",
         desc="카메라맨들이 새로운 장비를 장착한 업그레이드 버전으로 강화됨. 처음으로 토일렛 군단에 맞서 반격 작전에 성공하는 모습을 보여줌.",
         hb="업그레이드 카메라맨 나오고 전투씬이 훨씬 다이나믹해졌잖아."),
    dict(num="에피소드 10", title="자이언트 토일렛 충격", arc="시즌 2",
         desc="건물 크기의 자이언트 스키비디 토일렛이 처음 등장함. 등장만으로도 주변 건물이 무너지고 동맹군이 완전히 패퇴당하는 충격적인 에피소드.",
         hb="이 에피소드 진짜 입이 벌어졌음. 스케일이 완전히 달라졌잖아."),
    dict(num="에피소드 11", title="내부의 적", arc="시즌 3",
         desc="동맹군 내부에 감염된 카메라맨이 있다는 사실이 처음 드러남. 아군을 믿을 수 없게 되면서 동맹군의 전략에 큰 혼란이 생기기 시작함.",
         hb="이게 진짜 충격이었음. 배신 서사가 들어오면서 긴장감이 완전히 달라졌잖아."),
    dict(num="에피소드 12", title="투명한 적", arc="시즌 3",
         desc="카무플라주 토일렛이 등장해 기습 공격으로 동맹군을 혼란에 빠뜨림. 눈에 보이지 않는 적과 싸워야 하는 새로운 문제에 직면함.",
         hb="보이지 않는 적이라니... 전략 자체를 바꿔야 하는 상황이 됐잖아."),
    dict(num="에피소드 13", title="제트팩 공습", arc="시즌 3",
         desc="제트팩을 장착한 토일렛들이 공중에서 동맹군 기지를 폭격하기 시작함. 지상 방어만으로는 부족하다는 게 확실해진 에피소드.",
         hb="이때부터 진짜 다차원 전쟁이 된 거잖아. 땅도 하늘도 다 막아야 하니까."),
    dict(num="에피소드 14", title="반격의 서막", arc="시즌 3",
         desc="TV맨과 스피커맨이 합류해 처음으로 대규모 반격 작전을 펼침. 자이언트 토일렛 한 마리를 격파하는 데 성공하며 동맹군에게 희망의 불씨가 생김.",
         hb="이 에피소드 보고 진짜 주먹 불끈 쥐었음 ㅋㅋ 드디어 이기는 거 아니냐고."),
    dict(num="에피소드 15", title="G맨 등장", arc="시즌 3",
         desc="선글라스를 착용한 절대 강자 G맨이 처음 등장함. 보스급 토일렛을 혼자서 상대하며 전황을 단번에 바꿔버리는 압도적인 데뷔전.",
         hb="G맨 등장씬은 진짜 이 시리즈 최고의 명장면 중 하나야. 소름 돋았음."),
    dict(num="에피소드 16", title="탱크 토일렛 침략", arc="시즌 4",
         desc="중장갑 탱크 토일렛이 등장해 동맹군 기지를 정면 돌파함. G맨도 고전하게 만드는 압도적인 방어력으로 전황이 다시 어려워짐.",
         hb="G맨이 고전하는 거 처음 봤을 때 진짜 '이 시리즈 어디까지 가냐' 했음."),
    dict(num="에피소드 17", title="합동 작전", arc="시즌 4",
         desc="G맨, TV맨, 스피커맨이 처음으로 합동 작전을 펼침. 탱크 토일렛과 스트롱 토일렛을 동시에 상대하는 전면전으로 시리즈 최고 수준의 전투가 펼쳐짐.",
         hb="이 에피소드 편집이 진짜 미쳤음. 세 명이 각자 싸우는 걸 번갈아 보여주는 연출이 최고였어."),
    dict(num="에피소드 18", title="거미 변기의 공포", arc="시즌 4",
         desc="스파이더 토일렛이 등장해 건물 내부를 장악함. 벽과 천장을 자유롭게 이동하는 특성 때문에 일반 전술이 통하지 않아 동맹군이 크게 고전함.",
         hb="이거 공포물인 줄 알았음 진짜. 천장에서 뚝 하고 내려오는 거 ㄷㄷ"),
    dict(num="에피소드 19", title="기계가 된 변기", arc="시즌 4",
         desc="로봇 스키비디 토일렛이 처음 등장함. 자가 수리 능력 때문에 파괴해도 계속 일어나는 모습에 동맹군이 당황함. EMP가 유일한 해결책으로 떠오름.",
         hb="부수면 수리하고 부수면 수리하고... TV맨 EMP 맞기 전까지 진짜 답 없었음."),
    dict(num="에피소드 20", title="보스 등장", arc="시즌 5",
         desc="스키비디 토일렛 군단의 최종 지휘관 보스 토일렛이 처음 등장함. 다른 유닛들을 원격으로 강화시키고 혼자서 동맹군 최강 전력들을 상대하는 충격적인 에피소드.",
         hb="진짜 최종 보스 나온 거잖아. 이 에피소드 끝나고 일주일 동안 다음 편만 기다렸음."),
    dict(num="에피소드 21~24", title="최강들의 격돌", arc="시즌 5",
         desc="G맨과 보스 토일렛의 1:1 대결이 펼쳐짐. TV맨, 스피커맨과 연합해서 보스를 몰아붙이지만 보스의 재생 능력 때문에 완전 격파에 실패함.",
         hb="이 4연속 에피소드가 시즌 5 하이라이트야. 에너지 소모 심하게 했잖아 ㅋㅋ"),
    dict(num="에피소드 25", title="타이탄 카메라맨 탄생", arc="시즌 6",
         desc="타이탄 카메라맨이 처음 등장해 자이언트 토일렛 여러 마리를 동시에 상대함. 도시 블록 크기의 압도적인 존재감으로 시리즈의 스케일이 한 단계 올라감.",
         hb="드디어! 드디어 우리 편도 거대해졌다고! 이 장면 보면서 진짜 눈물 날 뻔했음 ㅋㅋ"),
    dict(num="에피소드 26", title="타이탄 vs 자이언트", arc="시즌 6",
         desc="타이탄 카메라맨과 자이언트 토일렛들의 전면전이 펼쳐짐. 도시 전체가 전쟁터가 되는 압도적인 스케일의 전투.",
         hb="이 전투씬 진짜 CGI 퀄리티가 미쳤음. 무료 유튜브 영상이 맞나 싶었잖아."),
    dict(num="에피소드 27", title="타이탄 TV맨 합류", arc="시즌 6",
         desc="타이탄 TV맨이 등장해 타이탄 카메라맨과 함께 보스 토일렛 진영을 압박함. 처음으로 동맹군이 수적으로도 질적으로도 우위를 점하기 시작함.",
         hb="타이탄 둘이 같이 나오는 씬이 진짜 영화였음."),
    dict(num="에피소드 28", title="핵의 위협", arc="시즌 6",
         desc="핵 스키비디 토일렛이 처음 등장해 자폭 공격으로 동맹군 타이탄에게 큰 피해를 입힘. 강하기만 해도 안 된다는 걸 보여주는 전략적 에피소드.",
         hb="핵 자폭 카드를 꺼내다니... 토일렛 진영 진짜 악랄하다 싶었음."),
    dict(num="에피소드 29", title="타이탄 스피커맨 각성", arc="시즌 7",
         desc="타이탄 스피커맨이 각성해 광역 초음파로 전장 전체를 장악함. 동맹군 3대 타이탄이 완전히 갖춰지면서 전황이 크게 기울기 시작함.",
         hb="3대 타이탄 다 모였을 때 진짜 이겼구나 싶었는데 그게 아니었잖아 ㅋㅋ"),
    dict(num="에피소드 30~34", title="보스의 역습", arc="시즌 7",
         desc="보스 토일렛이 특수 강화를 받아 3대 타이탄과 G맨을 동시에 상대함. 재생 능력에 순간이동 강화까지 더해져 동맹군 최강 전력도 고전하는 에피소드.",
         hb="이 시리즈는 동맹군이 강해질 만하면 토일렛도 강해지는 구조야. 끝이 없음."),
    dict(num="에피소드 35", title="TV우먼 등장", arc="시즌 8",
         desc="TV우먼이 처음 등장해 TV맨과 함께 보스 토일렛의 심리전에 대응함. 정밀 사격과 해킹 능력으로 새로운 전술적 가능성을 열어줌.",
         hb="TV우먼 나왔을 때 댓글창 완전 난리났잖아 ㅋㅋ 커플이냐 아니냐로 싸우고 있었음."),
    dict(num="에피소드 36~39", title="지구 최후의 결전", arc="시즌 8",
         desc="지구에서의 전쟁이 클라이맥스에 달함. 동맹군과 토일렛 군단 모두 최강 전력을 총동원한 대규모 전면전이 펼쳐짐.",
         hb="이 4개 에피소드가 지구 전쟁의 마무리야. 진짜 볼 때 손에 땀 쥐었음."),
    dict(num="에피소드 40", title="우주로의 확장", arc="아스트로 시즌 1",
         desc="전쟁이 우주 공간으로 확장됨. 아스트로 카메라맨이 처음 등장하고 우주 공간에서 새로운 형태의 스키비디 토일렛이 등장함.",
         hb="우주로 확장됐을 때 진짜 '이 시리즈 어디까지 갈 거야' 했잖아. 스케일이 미쳤음."),
    dict(num="에피소드 41", title="우주 토일렛 출현", arc="아스트로 시즌 1",
         desc="우주 공간에 서식하는 우주 스키비디 토일렛이 본격적으로 등장해 아스트로 카메라맨들을 위협함. 무중력 전투의 새로운 규칙이 만들어지기 시작함.",
         hb="무중력에서의 전투는 진짜 룰이 다르잖아. 이게 또 신선했음."),
    dict(num="에피소드 42", title="아스트로 TV맨 각성", arc="아스트로 시즌 1",
         desc="TV맨이 우주 환경에 특화된 아스트로 TV맨으로 각성함. 행성 간 텔레포트와 위성 레이저로 우주 전투를 단번에 지배하기 시작함.",
         hb="우주에서 텔레포트 범위가 행성 단위라니... 너무 사기 아니냐 ㅋㅋ"),
    dict(num="에피소드 43", title="전자기파의 전쟁", arc="아스트로 시즌 1",
         desc="아스트로 스피커맨이 등장해 전자기파 무기로 우주 토일렛들과 싸움. 소리가 없는 우주에서 전자기파를 사용하는 새로운 전투 방식이 등장함.",
         hb="소리 없는 우주에서 스피커맨이 어떻게 싸우나 했더니 전자기파 ㅋㅋ 설정 마음에 듦."),
    dict(num="에피소드 44", title="우주 전쟁의 격화", arc="아스트로 시즌 2",
         desc="우주 전쟁이 본격적으로 격화되면서 아스트로 동맹군과 우주 토일렛 군단이 전면전을 펼침. 지구 전쟁보다 훨씬 큰 스케일의 전투가 펼쳐짐.",
         hb="우주 전쟁 스케일이 지구 전쟁이랑 비교도 안 될 만큼 커졌잖아."),
    dict(num="에피소드 45", title="아스트로 G맨 각성", arc="아스트로 시즌 2",
         desc="G맨이 우주 환경에서 완전히 각성한 아스트로 G맨으로 변화함. 블랙홀 수준의 에너지 공격으로 우주 토일렛 군단을 압도하기 시작함.",
         hb="아스트로 G맨 나왔을 때 진짜 끝났구나 싶었음. 압도적이잖아."),
    dict(num="에피소드 46", title="우주 보스의 등장", arc="아스트로 시즌 2",
         desc="우주 토일렛 군단의 우주 보스가 처음 등장해 아스트로 G맨과 맞대결을 펼침. 지구 보스보다 훨씬 강력한 존재감으로 전황을 다시 불투명하게 만들어버림.",
         hb="우주 보스 나왔을 때 '아 또 시작이다' 했잖아 ㅋㅋ 패턴은 알겠는데 볼 수밖에 없음."),
    dict(num="에피소드 47", title="아스트로 타이탄의 탄생", arc="아스트로 시즌 2",
         desc="아스트로 타이탄 카메라맨이 등장해 달 크기에 비견되는 몸체로 우주 전장을 장악함. 역대 시리즈 중 가장 압도적인 스케일의 존재.",
         hb="이 장면은 진짜 말을 잃었음. 달이 움직이는 줄 알았잖아 처음에."),
    dict(num="에피소드 48", title="최종 결전의 서막", arc="아스트로 시즌 3",
         desc="지구와 우주 양쪽 전선에서 동시에 최종 결전이 시작됨. 모든 캐릭터들이 총출동하는 시리즈 최대 규모의 전투가 펼쳐지기 시작함.",
         hb="이 에피소드 끝나고 진짜 다음 편 나올 때까지 못 잠을 잤음 ㅋㅋ"),
    dict(num="에피소드 49~50", title="대단원의 막", arc="아스트로 시즌 3",
         desc="스키비디 토일렛 시리즈의 현재까지의 클라이맥스. 멀티플 스크린 TV맨이라는 정체불명의 존재가 등장하면서 새로운 떡밥을 남긴 채 일단락됨.",
         hb="멀티플 스크린 TV맨 정체가 뭔지 진짜 모르겠어. 이게 다음 시즌 복선인 거지?"),
]

# ── 색상 매핑 ──────────────────────────────────────────────────
FACTION_INFO = {
    "toilet":   ("🚽 토일렛 진영", "b-toilet"),
    "alliance": ("🤝 동맹군",      "b-alliance"),
    "astro":    ("🚀 아스트로",    "b-astro"),
    "neutral":  ("❓ 중립·특수",   "b-neutral"),
}
STATUS_INFO = {
    "alive":    ("● 생존",  "b-alive"),
    "dead":     ("✖ 사망",  "b-dead"),
    "infected": ("⚠ 감염", "b-infected"),
    "unknown":  ("? 불명",  "b-unknown"),
}
STAT_COLORS = {"공격": "#ff5533", "방어": "#33aaff", "속도": "#33ff88", "지능": "#ffdd33"}

# ── 렌더 함수 ─────────────────────────────────────────────────
def stat_html(name, val):
    c = STAT_COLORS.get(name, "#88aaff")
    w = int(val * 1.4)
    return (f'<div class="stat-row">'
            f'<span class="stat-lbl">{name}</span>'
            f'<span class="stat-val" style="color:{c};">{val}</span>'
            f'<div class="stat-bar-bg"><div class="stat-bar-fill" style="width:{w}px;background:{c};"></div></div>'
            f'</div>')

def render_char(c):
    fl, fb = FACTION_INFO.get(c["faction"], ("?", "b-neutral"))
    sl, sb = STATUS_INFO.get(c["status"], ("?", "b-unknown"))
    extra_cls = "astro-glow" if c["faction"] == "astro" else ""
    ab_html = "".join(f'<span class="ab-tag">{a}</span>' for a in c["abilities"])
    st_html  = "".join(stat_html(k, v) for k, v in c["stats"].items())
    st.markdown(f"""
<div class="wiki-card {c['faction']} {extra_cls}">
  <div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:12px;">
    <div style="font-size:3rem;width:66px;height:66px;background:#090918;border-radius:10px;
                display:flex;align-items:center;justify-content:center;flex-shrink:0;">{c['emoji']}</div>
    <div style="flex:1;">
      <div style="font-family:'Black Han Sans',cursive;font-size:1.2rem;color:#c0d8ff;margin-bottom:3px;">{c['name']}</div>
      <div style="font-size:0.78rem;color:#445577;margin-bottom:6px;">첫 등장: {c['ep']}</div>
      <span class="badge {fb}">{fl}</span>
      <span class="badge {sb}">{sl}</span>
      <span class="badge b-type">{c['type_']}</span>
    </div>
  </div>
  <div class="hb-talk">{c['quote']}</div>
  <div class="desc-box">{c['desc']}</div>
  <div class="sec-title">⚔️ 능력</div>
  <div style="margin-bottom:10px;">{ab_html}</div>
  <div class="weak-box">💀 약점: {c['weakness']}</div>
  <div class="sec-title">📊 스탯</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px 16px;">{st_html}</div>
</div>
""", unsafe_allow_html=True)

def render_episode(ep):
    arc_colors = {
        "시즌 1": "#3388ff", "시즌 2": "#33aaff", "시즌 3": "#33ccdd",
        "시즌 4": "#33ddbb", "시즌 5": "#33ee99", "시즌 6": "#aadd33",
        "시즌 7": "#ddaa33", "시즌 8": "#dd7733",
        "아스트로 시즌 1": "#aa44ff", "아스트로 시즌 2": "#cc66ff",
        "아스트로 시즌 3": "#ee88ff",
    }
    arc_c = arc_colors.get(ep["arc"], "#33ccaa")
    st.markdown(f"""
<div class="ep-card">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;flex-wrap:wrap;">
    <span class="ep-num">{ep['num']}</span>
    <span class="badge" style="background:#080818;border:1px solid {arc_c};color:{arc_c};font-size:0.7rem;">{ep['arc']}</span>
  </div>
  <div class="ep-title">{ep['title']}</div>
  <div class="ep-desc">{ep['desc']}</div>
  <div class="ep-hb">🎮 이한빈: {ep['hb']}</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
#  사이드바
# ══════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
<div style='text-align:center;padding:14px 0 6px;'>
  <div style='font-size:2.6rem;'>🚽</div>
  <div style='font-family:"Black Han Sans",cursive;font-size:1.25rem;color:#6699ff;letter-spacing:2px;line-height:1.4;'>
    이한빈의<br>스키비디 위키
  </div>
  <div style='font-size:0.72rem;color:#334466;margin-top:4px;'>완전 정복 도감</div>
</div>
<hr/>
""", unsafe_allow_html=True)

    search = st.text_input("🔍 검색", placeholder="카메라맨, 에피소드 5 등...")

    st.markdown("#### 👤 캐릭터 필터")
    faction_map = {
        "전체": "all",
        "🚽 토일렛 진영": "toilet",
        "🤝 동맹군": "alliance",
        "🚀 아스트로": "astro",
        "❓ 중립·특수": "neutral",
    }
    sel_f = faction_map[st.radio("진영", list(faction_map.keys()), label_visibility="collapsed")]

    status_map = {"전체": "all", "생존": "alive", "감염": "infected", "불명": "unknown"}
    st.markdown("#### 🔴 상태 필터")
    sel_s = status_map[st.selectbox("상태", list(status_map.keys()), label_visibility="collapsed")]

    st.markdown("#### 📺 에피소드 필터")
    arc_list = ["전체"] + sorted(set(e["arc"] for e in EPISODES), key=lambda x: EPISODES[[ep["arc"] for ep in EPISODES].index(x)]["arc"])
    arc_list = ["전체", "시즌 1", "시즌 2", "시즌 3", "시즌 4", "시즌 5",
                "시즌 6", "시즌 7", "시즌 8", "아스트로 시즌 1", "아스트로 시즌 2", "아스트로 시즌 3"]
    sel_arc = st.selectbox("아크 선택", arc_list, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.72rem;color:#222244;text-align:center;line-height:1.8;'>
  DaFuq!?Boom! 유튜브 시리즈<br>
  이한빈 스타일 비공식 팬 위키<br>
  <span style='color:#111133;'>★ 팬 해석 포함 ★</span>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
#  메인
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center;padding:20px 0 4px;">
  <div style="font-family:'Black Han Sans',cursive;font-size:2.6rem;color:#6699ff;letter-spacing:3px;">
    🚽 스키비디 토일렛 위키 🚀
  </div>
  <div style="color:#334466;font-size:0.95rem;margin-top:4px;">이한빈이 직접 설명해주는 완전 정복 도감 — 등장인물 · 에피소드 · 아스트로 포함</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hb-intro">
야 안녕~ 나 이한빈이야! 오늘은 스키비디 토일렛 시리즈를 내가 진짜 처음부터 끝까지 다 정리해줄게.
토일렛 진영, 동맹군, 아스트로까지 전부 다 있고 에피소드도 1편부터 최신까지 싹 정리했어.
왼쪽에서 진영이나 아크 필터 쓰면 원하는 것만 볼 수 있음. 그럼 시작해볼까?
</div>
""", unsafe_allow_html=True)

# 통계
t_c = sum(1 for c in CHARS if c["faction"] == "toilet")
a_c = sum(1 for c in CHARS if c["faction"] == "alliance")
r_c = sum(1 for c in CHARS if c["faction"] == "astro")
n_c = sum(1 for c in CHARS if c["faction"] == "neutral")

cols = st.columns(5)
for col, num, lbl, color in [
    (cols[0], len(CHARS),    "전체 캐릭터",    "#6699ff"),
    (cols[1], t_c,           "🚽 토일렛",      "#ff4433"),
    (cols[2], a_c,           "🤝 동맹군",      "#3388ff"),
    (cols[3], r_c,           "🚀 아스트로",    "#aa44ff"),
    (cols[4], len(EPISODES), "📺 에피소드",    "#33ccaa"),
]:
    col.markdown(
        f'<div class="stat-summary-card">'
        f'<div class="ssn" style="color:{color};">{num}</div>'
        f'<div class="ssl">{lbl}</div></div>',
        unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── 탭 ────────────────────────────────────────────────────────
tab_char, tab_ep = st.tabs(["👾 등장인물 도감", "📺 에피소드 목록"])

# ── 등장인물 탭 ───────────────────────────────────────────────
with tab_char:
    sub_tabs = st.tabs(["🗂️ 전체", "🚽 토일렛", "🤝 동맹군", "🚀 아스트로", "❓ 중립·특수"])

    def char_filter(faction_fixed=None):
        res = CHARS
        if search:
            res = [c for c in res if search.lower() in c["name"].lower()]
        if faction_fixed:
            res = [c for c in res if c["faction"] == faction_fixed]
        elif sel_f != "all":
            res = [c for c in res if c["faction"] == sel_f]
        if sel_s != "all":
            res = [c for c in res if c["status"] == sel_s]
        return res

    with sub_tabs[0]:
        chars = char_filter()
        st.markdown(f'<p style="color:#334466;font-size:0.85rem;margin-bottom:10px;">총 <strong style="color:#6699ff">{len(chars)}</strong>명 표시</p>', unsafe_allow_html=True)
        if not chars:
            st.warning("조건에 맞는 캐릭터가 없어. 필터를 바꿔봐!")
        for c in chars:
            render_char(c)

    for sub_tab, faction_key, intro in [
        (sub_tabs[1], "toilet",   "토일렛 진영이야. 이쪽이 빌런인데 진짜 다양하게 진화하면서 강해지는 게 이 시리즈의 재미임!"),
        (sub_tabs[2], "alliance", "동맹군이야! 처음엔 많이 밀리다가 점점 강해지는 성장 서사가 있어서 보는 맛이 있음."),
        (sub_tabs[3], "astro",    "아스트로 파트야! 전쟁이 우주로 확장되면서 등장하는 캐릭터들인데 스케일이 완전 다름."),
        (sub_tabs[4], "neutral",  "소속이 애매하거나 특수한 케이스들이야. 이게 스토리에서 중요한 복선이 되기도 함."),
    ]:
        with sub_tab:
            st.markdown(f'<div class="hb-talk">{intro}</div>', unsafe_allow_html=True)
            chars = char_filter(faction_key)
            if search and not chars:
                st.warning("검색 결과 없음!")
            for c in chars:
                render_char(c)

# ── 에피소드 탭 ───────────────────────────────────────────────
with tab_ep:
    st.markdown("""
<div class="hb-talk">
에피소드 전체 목록이야! 시즌 1부터 아스트로 시즌 3까지 내가 다 정리했음.
왼쪽에서 아크 필터 쓰면 원하는 시즌만 볼 수 있어. 에피소드 설명 밑에 내 감상평도 달아뒀으니까 참고해~
</div>
""", unsafe_allow_html=True)

    def ep_filter():
        res = EPISODES
        if search:
            res = [e for e in res if search.lower() in e["num"].lower()
                   or search.lower() in e["title"].lower()
                   or search.lower() in e["desc"].lower()]
        if sel_arc != "전체":
            res = [e for e in res if e["arc"] == sel_arc]
        return res

    eps = ep_filter()
    st.markdown(f'<p style="color:#334466;font-size:0.85rem;margin-bottom:10px;">총 <strong style="color:#33ccaa">{len(eps)}</strong>개 에피소드 표시</p>', unsafe_allow_html=True)

    # 아크별 그룹핑
    arc_order = ["시즌 1","시즌 2","시즌 3","시즌 4","시즌 5",
                 "시즌 6","시즌 7","시즌 8",
                 "아스트로 시즌 1","아스트로 시즌 2","아스트로 시즌 3"]
    arc_colors = {
        "시즌 1":"#3388ff","시즌 2":"#33aaff","시즌 3":"#33ccdd",
        "시즌 4":"#33ddbb","시즌 5":"#33ee99","시즌 6":"#aadd33",
        "시즌 7":"#ddaa33","시즌 8":"#dd7733",
        "아스트로 시즌 1":"#aa44ff","아스트로 시즌 2":"#cc66ff","아스트로 시즌 3":"#ee88ff",
    }

    if sel_arc != "전체":
        for e in eps:
            render_episode(e)
    else:
        for arc in arc_order:
            arc_eps = [e for e in eps if e["arc"] == arc]
            if not arc_eps:
                continue
            ac = arc_colors.get(arc, "#33ccaa")
            st.markdown(f"""
<div style="margin:20px 0 10px;padding:8px 16px;
     background:#09091e;border-left:3px solid {ac};border-radius:0 8px 8px 0;">
  <span style="font-family:'Black Han Sans',cursive;font-size:1.1rem;color:{ac};">
    📺 {arc}
  </span>
  <span style="font-size:0.78rem;color:#334455;margin-left:8px;">{len(arc_eps)}개 에피소드</span>
</div>
""", unsafe_allow_html=True)
            for e in arc_eps:
                render_episode(e)

# 푸터
st.markdown("""
<hr style="margin-top:40px;"/>
<div style="text-align:center;color:#1a1a33;font-size:0.76rem;padding:10px 0;">
  이한빈의 스키비디 토일렛 완전 정복 위키 · 비공식 팬 제작 · 원작: DaFuq!?Boom!
</div>
""", unsafe_allow_html=True)
