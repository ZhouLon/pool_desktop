from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# 初始化数据库实例
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhoulong:longzhou@106.52.158.123:3306/poolease'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()  # 自动创建所有模型表
    # 测试数据库连接是否成功
    try:
        with app.app_context():
            result = db.session.execute(text('SELECT 1'))
            print("数据库连接成功")
    except Exception as e:
        print(f"数据库连接失败: {e}")
