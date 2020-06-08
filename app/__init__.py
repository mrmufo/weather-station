from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from app.mqtt.functions import on_log, on_connect, on_disconnect, on_message
import paho.mqtt.client as mqtt
import time

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

bootstrap = Bootstrap()

mqttc = mqtt.Client("c1")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app)

    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect
    mqttc.on_log = on_log
    mqttc.on_message = on_message
    mqttc.connect(Config.MQTT_BROKER_URL)
    mqttc.loop_start()

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.mqtt import bp as mqtt_bp
    app.register_blueprint(mqtt_bp)

    return app
