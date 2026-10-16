import streamlit as st

st.set_page_config(
    page_title='이유리의 자기소개',
    page_icon='💜',
    layout='wide',
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

    :root {
        --ink: #382c4b;
        --muted: #746783;
        --violet: #8264b5;
        --line: rgba(113, 87, 153, 0.14);
    }

    .stApp {
        background:
            radial-gradient(ellipse at 12% 8%, rgba(255, 255, 255, 0.88), transparent 34%),
            radial-gradient(ellipse at 88% 24%, rgba(226, 210, 255, 0.72), transparent 38%),
            linear-gradient(135deg, #f7efff 0%, #eee3ff 48%, #e6eaff 100%);
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
    }

    [data-testid='stHeader'] { background: transparent; }
    [data-testid='stToolbar'] { right: 1rem; }
    .block-container { max-width: 1040px; padding-top: 3rem; padding-bottom: 4rem; }

    .intro {
        position: relative;
        overflow: hidden;
        padding: clamp(1.6rem, 4vw, 3rem);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 28px;
        background: linear-gradient(125deg, rgba(255,255,255,.86), rgba(250,245,255,.66));
        box-shadow: 0 24px 70px rgba(83, 59, 127, 0.12);
        animation: appear .7s ease-out both;
    }

    [data-testid='stImage'] img {
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 28px;
        box-shadow: 0 24px 70px rgba(83, 59, 127, 0.16);
    }

    .intro::after {
        content: '✿';
        position: absolute;
        right: 7%;
        top: 8%;
        color: rgba(157, 126, 202, .17);
        font-size: clamp(5rem, 14vw, 10rem);
        transform: rotate(16deg);
        pointer-events: none;
    }

    .eyebrow {
        color: var(--violet);
        font-size: .88rem;
        font-weight: 700;
        letter-spacing: 0;
    }

    .intro h1 {
        margin: .65rem 0 .25rem;
        color: #493663;
        font-family: 'Jua', sans-serif;
        font-size: clamp(2.5rem, 6vw, 4rem);
        font-weight: 400;
        letter-spacing: 0;
        line-height: 1.12;
    }

    .intro .subtitle { margin: .8rem 0 1.5rem; color: var(--muted); font-size: 1.08rem; }
    .tags { display: flex; flex-wrap: wrap; gap: .55rem; }
    .tag {
        display: inline-block;
        padding: .48rem .85rem;
        border: 1px solid rgba(130, 100, 181, .18);
        border-radius: 999px;
        background: rgba(255, 255, 255, .72);
        color: #5f4b7e;
        font-size: .9rem;
    }

    .section-title {
        margin: 2.4rem 0 1rem;
        color: #493663;
        font-family: 'Jua', sans-serif;
        font-size: 1.65rem;
        letter-spacing: 0;
    }

    .info-card {
        min-height: 174px;
        padding: 1.35rem 1.45rem;
        border: 1px solid rgba(255, 255, 255, .82);
        border-radius: 18px;
        background: rgba(255, 255, 255, .62);
        box-shadow: 0 12px 35px rgba(83, 59, 127, .07);
    }

    .info-card .icon { font-size: 1.55rem; }
    .info-card h3 { margin: .55rem 0 .4rem; color: #5c447d; font-family: 'Jua', sans-serif; font-size: 1.15rem; letter-spacing: 0; }
    .info-card p { margin: 0; color: var(--muted); line-height: 1.7; }

    .note {
        margin-top: 1.4rem;
        padding: 1.2rem 1.4rem;
        border-left: 4px solid #b89add;
        border-radius: 0 14px 14px 0;
        background: rgba(255, 255, 255, .48);
        color: #5e5070;
        line-height: 1.8;
    }

    .footer { margin-top: 2.4rem; color: #827391; text-align: center; font-size: .9rem; }

    @keyframes appear {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 640px) {
        .block-container { padding-top: 1.5rem; }
        .intro { border-radius: 22px; }
        .info-card { min-height: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

intro_text, intro_photo = st.columns([2, 0.7])

with intro_text:
    st.markdown(
        """
        <section class="intro">
            <div class="eyebrow">오늘보다 내일 더 반짝이는 사람 ✨</div>
            <h1>안녕하세요,<br>이유리입니다!</h1>
            <p class="subtitle">배우고 도전하며 나만의 길을 찾아가는 고등학생이에요. 🌷</p>
            <div class="tags">
                <span class="tag">🏫 경복비즈니스고등학교</span>
                <span class="tag">💻 3학년 IT과</span>
                <span class="tag">🎧 노래 듣기</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

with intro_photo:
    st.image("img/unnamed.jpg", width=260)

st.markdown(
    '<div class="section-title">저를 소개할게요 💌</div>',
    unsafe_allow_html=True,
)

first, second, third = st.columns(3)

with first:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon">🎒</div>
            <h3>학교생활</h3>
            <p>경복비즈니스고등학교 3학년 IT과에서 공부하고 있어요. 새로운 것을 하나씩 배워가는 중입니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with second:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon">🎶</div>
            <h3>좋아하는 것</h3>
            <p>취미는 노래 듣기예요. 좋아하는 음악을 들으면 기분이 좋아지고 에너지도 충전돼요!</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with third:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon">🌱</div>
            <h3>앞으로의 꿈</h3>
            <p>공무원이나 취업을 생각하고 있어요. 저에게 잘 맞는 진로를 찾아 차근차근 준비하고 싶어요.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="note">
        <strong>저의 다짐 💜</strong><br>
        작은 경험도 소중히 여기며, 맡은 일은 책임감 있게 해내는 사람이 되고 싶어요.
        앞으로의 저를 따뜻하게 지켜봐 주세요! 😊
    </div>
    <div class="footer">Yuri's little introduction · 오늘도 좋은 하루 보내세요 ☁️</div>
    """,
    unsafe_allow_html=True,
)
