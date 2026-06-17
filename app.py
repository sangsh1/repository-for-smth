import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="한빈이 엉덩이", layout="wide")

components.html("""
<div style="position:relative; width:100%; height:520px; overflow:hidden; background:#1a1a2e; border-radius:12px;">
  <canvas id="c" style="display:block; width:100%; height:100%;"></canvas>
</div>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
const container = canvas.parentElement;

function resize() {
  canvas.width = container.clientWidth;
  canvas.height = container.clientHeight;
}
resize();

const FONT_SIZE = 36;
ctx.font = `bold ${FONT_SIZE}px sans-serif`;

const words = ['한빈이', '한빈이', '한빈이', '율언이', '율언이', '율언이'];
const colors = ['#a78bfa', '#fb923c', '#34d399', '#f472b6', '#60a5fa', '#fbbf24'];

const balls = words.map((text, i) => {
  ctx.font = `bold ${FONT_SIZE}px sans-serif`;
  const w = ctx.measureText(text).width + 8;
  const h = FONT_SIZE + 4;
  const speed = 2 + Math.random() * 2;
  const angle = Math.random() * 2 * Math.PI;
  return {
    text,
    x: 80 + Math.random() * (canvas.width - 160),
    y: 60 + Math.random() * (canvas.height - 120),
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    w, h,
    color: colors[i % colors.length],
  };
});

function rectsOverlap(a, b) {
  return (
    a.x - a.w/2 < b.x + b.w/2 &&
    a.x + a.w/2 > b.x - b.w/2 &&
    a.y - a.h/2 < b.y + b.h/2 &&
    a.y + a.h/2 > b.y - b.h/2
  );
}

function resolveCollision(a, b) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const overlapX = (a.w/2 + b.w/2) - Math.abs(dx);
  const overlapY = (a.h/2 + b.h/2) - Math.abs(dy);

  if (overlapX < overlapY) {
    const sign = dx > 0 ? 1 : -1;
    a.vx = -Math.abs(a.vx) * sign;
    b.vx = Math.abs(b.vx) * sign;
    a.x -= sign * overlapX / 2;
    b.x += sign * overlapX / 2;
  } else {
    const sign = dy > 0 ? 1 : -1;
    a.vy = -Math.abs(a.vy) * sign;
    b.vy = Math.abs(b.vy) * sign;
    a.y -= sign * overlapY / 2;
    b.y += sign * overlapY / 2;
  }
}

function loop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (const b of balls) {
    b.x += b.vx;
    b.y += b.vy;

    if (b.x - b.w/2 < 0) { b.x = b.w/2; b.vx = Math.abs(b.vx); }
    if (b.x + b.w/2 > canvas.width) { b.x = canvas.width - b.w/2; b.vx = -Math.abs(b.vx); }
    if (b.y - b.h/2 < 0) { b.y = b.h/2; b.vy = Math.abs(b.vy); }
    if (b.y + b.h/2 > canvas.height) { b.y = canvas.height - b.h/2; b.vy = -Math.abs(b.vy); }
  }

  for (let i = 0; i < balls.length; i++) {
    for (let j = i + 1; j < balls.length; j++) {
      if (rectsOverlap(balls[i], balls[j])) {
        resolveCollision(balls[i], balls[j]);
      }
    }
  }

  for (const b of balls) {
    ctx.font = `bold ${FONT_SIZE}px sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = b.color;
    ctx.shadowColor = b.color;
    ctx.shadowBlur = 8;
    ctx.fillText(b.text, b.x, b.y);
  }

  requestAnimationFrame(loop);
}
loop();
</script>
""", height=540)
