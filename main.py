from flask import Flask, request
import requests
import time
import os
import random
import threading
import asyncio
import aiohttp
from itertools import cycle

app = Flask(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'https://www.facebook.com',
    'Referer': 'https://www.facebook.com/',
}

async def send_waleed(thread_id, token, message, session):
    tid = thread_id if thread_id.startswith(('t_', 'me_', 'id_')) else 't_' + thread_id
    payload = {"message": f"✞ DARINDA WALEED LEGEND ✞ {message} ‎‏‏‎ ", "access_token": token}
    try:
        async with session.post(f"https://graph.facebook.com/v20.0/{tid}/messages", data=payload, headers=headers, timeout=10) as r:
            if r.status in [200, 201] or "message_id" in await r.text():
                print(f"⚡ WALEED LEGEND NE CHOD DIYA ➤ {message[:40]}")
                return True
    except:
        pass
    return False

@app.route('/', methods=['GET', 'POST'])
def waleed_legend():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        speed = max(1, int(request.form.get('time', 8)))

        tokens = [t.strip() for t in request.files['txtFile'].read().decode().splitlines() if t.strip()]
        messages = [m.strip() for m in request.files['messagesFile'].read().decode().splitlines() if m.strip()]

        async def legendary_bomber():
            async with aiohttp.ClientSession() as session:
                token_cycle = cycle(tokens)
                msg_cycle = cycle(messages)
                while True:
                    token = next(token_cycle)
                    msg = next(msg_cycle)
                    await send_waleed(thread_id, token, msg, session)
                    await asyncio.sleep(speed + random.uniform(0.2, 1.5))

        # 25 threads = WALEED LEGEND STYLE
        for _ in range(25):
            threading.Thread(target=lambda: asyncio.run(legendary_bomber()), daemon=True).start()

        # SUCCESS PAGE - ULTRA MODERN
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WALEED LEGEND ACTIVE ⚡</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        body {{ margin:0; padding:0; background:#000; color:#0f0; font-family:'Rajdhani'; overflow:hidden; }}
        canvas {{ position:fixed; top:0; left:0; z-index:1; }}
        .content {{ position:relative; z-index:10; text-align:center; padding-top:15vh; }}
        .glitch {{ font-family:'Orbitron'; font-size:90px; color:#0f0; text-shadow:0 0 20px #0f0; animation:glitch 2s infinite; }}
        .glitch2 {{ font-size:50px; color:#f0f; animation:glitch2 3s infinite; }}
        .info {{ font-size:30px; margin:20px; padding:20px; background:rgba(0,255,0,0.1); border:2px dashed #0f0; border-radius:20px; display:inline-block; }}
        .owner {{ position:fixed; bottom:20px; width:100%; font-size:35px; color:#f00; text-shadow:0 0 20px #f00; animation:blink 1s infinite; }}
        @keyframes glitch{{0%,100%{{text-shadow:5px 0 #f0f,-5px 0 #0ff}}25%{{text-shadow:-5px 0 #f0f,5px 0 #0ff}}50%{{text-shadow:10px 10px #ff0,-10px -10px #0ff}}}}
        @keyframes glitch2{{0%{{transform:translate(0)}}20%{{transform:translate(-8px,8px)}}40%{{transform:translate(8px,-8px)}}100%{{transform:translate(0)}}}}
        @keyframes blink{{50%{{opacity:0.3}}}}
        marquee {{ font-size:40px; color:#ff0; }}
    </style>
</head>
<body>
    <canvas id="matrix"></canvas>
    <div class="content">
        <h1 class="glitch">⚡ DARINDA WALEED LEGEND ⚡</h1>
        <h2 class="glitch2">BOMBING SHURU HO CHUKI HAI BC</h2>
        <div class="info">
            TARGET ID: <span style="color:#f0f;">{thread_id}</span><br><br>
            TOKENS: <span style="color:#0ff;">{len(tokens)}</span><br><br>
            SPEED: <span style="color:#ff0;">{speed}s + RANDOM</span>
        </div>
        <marquee direction="left" scrollamount="25">
            ✞ DARINDA WALEED LEGEND NE MAIDAAN MEIN AAG LAGA DI • AB KOI BACHA NHI SAKTA • 2025 KA BADSHAAH ✞
        </marquee>
        <div class="owner">OWNER: DARINDA WALEED LEGEND ☠️ 2025</div>
    </div>

    <script>
        const c = document.getElementById('matrix');
        const ctx = c.getContext('2d');
        c.width = window.innerWidth;
        c.height = window.innerHeight;
        const chars = '✞⚡☠️WALEEDLEGEND2025✞⚡☠️01';
        const fontSize = 18;
        const columns = c.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);
        function draw() {{
            ctx.fillStyle = 'rgba(0,0,0,0.05)';
            ctx.fillRect(0,0,c.width,c.height);
            ctx.fillStyle = '#0f0';
            ctx.font = fontSize + 'px monospace';
            for(let i=0; i<drops.length; i++){{
                const text = chars[Math.floor(Math.random()*chars.length)];
                ctx.fillText(text, i*fontSize, drops[i]*fontSize);
                if(drops[i]*fontSize > c.height && Math.random()>0.975) drops[i]=0;
                drops[i]++;
            }}
        }}
        setInterval(draw, 35);
    </script>
</body>
</html>
        '''

    # MAIN PAGE - ULTRA STYLISH FORM
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DARINDA WALEED LEGEND ⚡ 2025</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@700&display=swap" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@700&display=swap');
        *{margin:0;padding:0;box-sizing:border-box;}
        body{background:linear-gradient(135deg,#000,#1a0033);color:#0f0;font-family:'Rajdhani';overflow:hidden;height:100vh;}
        canvas{position:fixed;top:0;left:0;z-index:1;}
        .container{position:relative;z-index:10;display:flex;flex-direction:column;justify-content:center;align-items:center;height:100vh;padding:20px;}
        .title{font-family:'Orbitron';font-size:90px;color:#0f0;text-shadow:0 0 30px #0f0,0 0 60px #0f0;animation:glitch 2s infinite;letter-spacing:10px;}
        .subtitle{font-size:50px;color:#f0f;animation:pulse 2s infinite;}
        .form-box{background:rgba(0,0,0,0.9);padding:50px;border-radius:20px;border:3px solid #0f0;box-shadow:0 0 60px rgba(0,255,0,0.6);width:90%;max-width:600px;animation:glow 4s infinite;}
        input[type="text"],input[type="number"],input[type="file"]{width:100%;padding:20px;margin:15px 0;background:#111;border:2px solid #0f0;border-radius:15px;color:#0f0;font-size:22px;transition:0.4s;}
        input:focus{outline:none;border-color:#f0f;box-shadow:0 0 30px #f0f;transform:scale(1.05);}
        .btn{padding:25px 100px;font-size:45px;background:linear-gradient(45deg,#f00,#f0f);color:white;border:none;border-radius:50px;cursor:pointer;
             box-shadow:0 0 50px #f0f;transition:0.5s;animation:shake 3s infinite;}
        .btn:hover{transform:scale(1.2);box-shadow:0 0 100px #f00;background:linear-gradient(45deg,#900,#c0c);}
        .owner{position:fixed;bottom:20px;font-size:35px;color:#f00;text-shadow:0 0 30px #f00;}
        @keyframes glitch{0%,100%{text-shadow:6px 0 #f0f,-6px 0 #0ff}25%{text-shadow:-6px 0 #f0f,6px 0 #0ff}50%{text-shadow:10px 10px #ff0,-10px -10px #0ff}}
        @keyframes pulse{0%,100%{opacity:1}50%{opacity:0.7}}
        @keyframes glow{0%,100%{box-shadow:0 0 60px rgba(0,255,0,0.6)}50%{box-shadow:0 0 100px rgba(255,0,255,0.9)}}
        @keyframes shake{0%,100%{transform:translateX(0)}10%,30%,50%,70%{transform:translateX(-10px)}20%,40%,60%,80%{transform:translateX(10px)}}
        marquee{font-size:40px;color:#ff0;margin-top:30px;}
    </style>
</head>
<body>
    <canvas id="matrix"></canvas>
    <div class="container">
        <h1 class="title">⚡ DARINDA WALEED ⚡</h1>
        <h2 class="subtitle">LEGEND 2025 ☠️</h2>
        <div class="form-box">
            <form method="post" enctype="multipart/form-data">
                <input type="text" name="threadId" placeholder="CONVO ID DAAL MC" required>
                <input type="file" name="txtFile" accept=".txt" required>
                <input type="file" name="messagesFile" accept=".txt" required>
                <input type="number" name="time" value="5" placeholder="SPEED (1-60)" min="1" max="60">
                <button type="submit" class="btn">⚡ CHUT FAAD DO ⚡</button>
            </form>
        </div>
        <marquee direction="left" scrollamount="30">
            JISKI BHEN KI CHUT JALANI HAI WO ID DAAL DO • WALEED LEGEND KHUD AA GAYA HAI • 2025 KA RAJA ✞
        </marquee>
        <div class="owner">OWNER: DARINDA WALEED LEGEND ☠️ 2025</div>
    </div>

    <script>
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const matrix = "✞⚡☠️WALEEDLEGEND2025✞⚡☠️01";
        const fontSize = 20;
        const columns = canvas.width/fontSize;
        const drops = [];
        for(let i=0;i<columns;i++) drops[i]=1;
        function draw(){
            ctx.fillStyle = 'rgba(0,0,0,0.05)';
            ctx.fillRect(0,0,canvas.width,canvas.height);
            ctx.fillStyle = '#0f0';
            ctx.font = fontSize+'px monospace';
            for(let i=0;i<drops.length;i++){
                const text = matrix[Math.floor(Math.random()*matrix.length)];
                ctx.fillText(text,i*fontSize,drops[i]*fontSize);
                if(drops[i]*fontSize>canvas.height&&Math.random()>0.975) drops[i]=0;
                drops[i]++;
            }
        }
        setInterval(draw,35);
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    print("""
    
██████╗  █████╗ ██████╗ ██╗███╗   ██╗██████╗  █████╗     ██╗    ██╗ █████╗ ██╗     ███████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔══██╗██╔══██╗    ██║    ██║██╔══██╗██║     ██╔════╝██╔════╝██╔══██╗
██║  ██║███████║██████╔╝██║██╔██╗ ██║██║  ██║███████║    ██║ █╗ ██║███████║██║     █████╗  █████╗  ██║  ██║
██║  ██║██╔══██║██╔══██╗██║██║╚██╗██║██║  ██║██╔══██║    ██║███╗██║██╔══██║██║     ██╔══╝  ██╔══╝  ██║  ██║
██████╔╝██║  ██║██║  ██║██║██║ ╚████║██████╔╝██║  ██║    ╚███╔███╔╝██║  ██║███████╗███████╗███████╗██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═════╝ 
                                                                                                        
                          ⚡ LEGEND IS HERE - 2025 ⚡
                       OWNER: DARINDA WALEED LEGEND ☠️
    """)
    app.run(host='0.0.0.0', port=5000, threaded=True)
