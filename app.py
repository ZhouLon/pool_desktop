from flask import Flask,render_template
from db import init_db
from routes.merchant import merchant_bp
from routes.user import user_bp
from routes.order import order_bp
from routes.feedback import feedback_bp
from routes.employee import employee_bp
from routes.notification import notification_bp

app = Flask(__name__)

# 数据库初始化
init_db(app)

# 注册路由
app.register_blueprint(merchant_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(notification_bp)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_merchant')
def add_merchant_page():
    return render_template('add_merchant.html')

@app.route('/get_merchant')
def get_merchant_page():
    return render_template('get_merchant.html')

@app.route('/update_merchant')
def update_merchant_page():
    return render_template('update_merchant.html')
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=2024)
