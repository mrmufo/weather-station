from flask import (
    current_app,
    url_for,
    redirect,
    render_template
)

from app import mqttc
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    mqttc.subscribe("house/sensor1")
    mqttc.publish("house/sensor1", "my first message")
    return render_template('index.html', title='Home')
