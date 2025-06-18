from flask import Blueprint, jsonify, request
from ..utils.signals_db import find_signals_in_range, get_all_signals

signals_routes = Blueprint('signals', __name__)

@signals_routes.route('/api/signals', methods=['GET'])
def get_signals():
    """Получить все сигналы или найти сигналы по частоте"""
    freq = request.args.get('freq', type=float)
    
    if freq is not None:
        signals = find_signals_in_range(freq)
        return jsonify({
            'frequency': freq,
            'signals': signals
        })
    
    return jsonify({
        'signals': get_all_signals()
    })
