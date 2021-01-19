import random
from flask import render_template, Blueprint, request, url_for, redirect, flash
from .tools import cards, shuffle_deck

bp = Blueprint('main', __name__, url_prefix='')



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/cards/', methods=['POST'])
def get_cards():
    if not request.form['num'].isdigit():
        flash('注意：请输入正确的数字')
        return redirect(url_for('main.index'))
        
    num = int(request.form['num'])
    if num > 78:
        flash('注意：抽取数量不能大于78！')
        return redirect(url_for('main.index'))

    new_deck = shuffle_deck()
    no = random.sample(range(78), num)
    deck = cards()
    data = list()
    for i in range(num):
        # reverse = "逆位" if new_deck[no[i]] == 1 else "正位"
        card = deck[no[i]]
        data.append({
            'No': i + 1,
            'Name': card['name'],
            'Reverse': new_deck[no[i]],
            'Image': card['image'],
        })
    return render_template('cards.html', data=data)
