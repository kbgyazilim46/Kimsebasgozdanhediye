from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SİMA HİRA SENİ SEVİYORUMMMMM</title>
        <style>
            body {
                margin: 0;
                background: #000;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                height: 100vh;
                color: white;
                font-family: sans-serif;
            }
            h1 {
                position: absolute;
                font-size: 2rem;
                color: white;
            }
            canvas {
                border: none;
            }
        </style>
    </head>
    <body>
        <h1>SENİ ÇOK SEVİYORUM SİMA HİRAM</h1>
        <canvas id="heartCanvas" width="600" height="600"></canvas>
        <script>
            const canvas = document.getElementById("heartCanvas");
            const ctx = canvas.getContext("2d");

            function drawHeart(x, y, size, color) {
                ctx.beginPath();
                for (let t = 0; t < Math.PI * 2; t += 0.01) {
                    const px = size * 16 * Math.pow(Math.sin(t), 3);
                    const py = -size * (13 * Math.cos(t) - 5 * Math.cos(2 * t)
                        - 2 * Math.cos(3 * t) - Math.cos(4 * t));
                    ctx.lineTo(x + px, y + py);
                }
                ctx.closePath();
                ctx.shadowBlur = 25;
                ctx.shadowColor = color;
                ctx.strokeStyle = color;
                ctx.lineWidth = 2;
                ctx.stroke();
            }

            let time = 0;

            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                const r = Math.floor(128 + 128 * Math.sin(time));
                const b = Math.floor(128 + 128 * Math.cos(time));
                const color = `rgb(${r}, 0, ${b})`;
                drawHeart(canvas.width / 2, canvas.height / 2, 10, color);
                time += 0.05;
                requestAnimationFrame(animate);
            }

            animate();
        </script>
    </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')

if __name__ == "__main__":
    app.run()