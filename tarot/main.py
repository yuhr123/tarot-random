import random
from flask import render_template, Blueprint
from .tools import cards, shuffle_deck

bp = Blueprint('main', __name__, url_prefix='')



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/three-cards', methods=['POST'])
def get_cards():
    new_deck = shuffle_deck()
    no = random.sample(range(78), 3)
    deck = cards()
    data = list()
    for i in range(3):
        # reverse = "逆位" if new_deck[no[i]] == 1 else "正位"
        card = deck[no[i]]
        data.append({
            'No': i + 1,
            'Name': card['name'],
            'Reverse': new_deck[no[i]],
            'Image': card['image'],
        })
    return render_template('cards.html', data=data)
