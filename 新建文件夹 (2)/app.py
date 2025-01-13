from flask import Flask, render_template, request

app = Flask(__name__)

# 奖项列表
prize_list = [
    "一等奖", "二等奖", "三等奖", "幸运奖", "安慰奖", 
    "奖品1", "奖品2", "奖品3", "奖品4", "奖品5"
]
drawn_prizes = []  # 记录已抽奖项
participants = []  # 记录参与者信息和抽奖结果

@app.route('/')
def index():
    """前台抽奖页面"""
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    """处理抽奖逻辑"""
    name = request.form.get('name')  # 获取客户姓名
    account = request.form.get('account')  # 获取客户域账号

    # 校验输入
    if not name or not account:
        return render_template('index.html', message="请输入完整的姓名和域账号！")

    # 检查是否还有奖项
    if len(drawn_prizes) >= len(prize_list):
        return render_template('index.html', message="所有奖项已被抽完！")

    # 抽奖逻辑
    remaining_prizes = list(set(prize_list) - set(drawn_prizes))
    prize = remaining_prizes[0]  # 先到先得
    drawn_prizes.append(prize)

    # 记录参与者信息
    participants.append({'name': name, 'account': account, 'prize': prize})

    # 显示抽奖结果
    return render_template('index.html', prize=prize)

@app.route('/admin')
def admin():
    """后台页面：显示抽奖记录"""
    return render_template('admin.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)
