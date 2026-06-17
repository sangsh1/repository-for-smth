import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="한빈이 엉덩이", layout="wide")

components.html("""
<div style="position:relative; width:100%; height:500px; overflow:hidden; background:#1a1a2e; border-radius:12px;">
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
window.addEventListener('resize', resize);

const texts = ['한빈이', '엉덩이'];
const colors = ['#a78bfa', '#fb923c', '#34d399', '#f472b6', '#60a5fa', '#fbbf24'];

const balls = texts.map((text, i) => {
  const speed = 2.5 + Math.random() * 1.5;
  const angle = Math.random() * 2 * Math.PI;
  return {
    text,
    x: 100 + i * 250,
    y: 150 + i * 100,
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    color: colors[i % colors.length],
    fontSize: 40,
    rotation: 0,
    rotSpeed: (Math.random() - 0.5) * 0.05
  };
});

function loop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (const b of balls) {
    ctx.font = `bold ${b.fontSize}px sans-serif`;
    const w = ctx.measureText(b.text).width;
    const h = b.fontSize;

    b.x += b.vx;
    b.y += b.vy;
    b.rotation += b.rotSpeed;

    if (b.x - w/2 < 0) { b.x = w/2; b.vx = Math.abs(b.vx); }
    if (b.x + w/2 > canvas.width) { b.x = canvas.width - w/2; b.vx = -Math.abs(b.vx); }
    if (b.y - h < 0) { b.y = h; b.vy = Math.abs(b.vy); }
    if (b.y > canvas.height) { b.y = canvas.height; b.vy = -Math.abs(b.vy); }

    ctx.save();
    ctx.translate(b.x, b.y);
    ctx.rotate(b.rotation);
    ctx.font = `bold ${b.fontSize}px sans-serif`;
    ctx.fillStyle = b.color;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.shadowColor = b.color;
    ctx.shadowBlur = 10;
    ctx.fillText(b.text, 0, 0);
    ctx.restore();
  }

  requestAnimationFrame(loop);
}
loop();
</script>
""", height=520)
