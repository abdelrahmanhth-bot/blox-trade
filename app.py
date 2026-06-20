from flask import Flask, render_template_string, request

app = Flask(__name__)

# مخزن العروض
trades = []

# شكل الموقع (الواجهة)
html = """
<html>
<body>
    <h1>موقع ترييد Blox Fruits</h1>
    <form action="/add" method="POST">
        <input name="have" placeholder="معي فاكهة..." required>
        <input name="want" placeholder="أريد فاكهة..." required>
        <button type="submit">إضافة العرض</button>
    </form>
    <ul>
        {% for trade in trades %}
        <li>معي: {{ trade.have }} | أريد: {{ trade.want }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html, trades=trades)

@app.route('/add', methods=['POST'])
def add():
    h = request.form.get('have')
    w = request.form.get('want')
    trades.append({'have': h, 'want': w})
    return render_template_string(html, trades=trades)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)