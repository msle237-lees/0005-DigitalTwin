### Data available
# - Possible data suppliers for AUV:
#     - Sonar (2D Map of surroundings)
#     - IMU (Accelerometer / Gyroscope / Magenetometer)
#     - Voltage / Current Measurements (Voltage and Amperage)
#     - Hydrophone heading direction (Compass directions)
#     - Leak Detection
#     - Depth Sensor (meters)
#     - Internal Temperature
#     - External Temperature
#     - Internal Humidity
#     - Internal Pressure
#     - External Pressure
#     - ZED 3D maps of perspective view point

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_cors import CORS

from datetime import datetime
import argparse

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# Databases
# Sonar
class Sonar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    data = db.Column(db.LargeBinary, nullable=False)

# IMU
class IMU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Accelerometer = db.Column(db.LargeBinary, nullable=False)
    Gyroscope = db.Column(db.LargeBinary, nullable=False)
    Magnetometer = db.Column(db.LargeBinary, nullable=False)

# Voltage / Current Measurements
class VoltageCurrent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Voltage = db.Column(db.Float, nullable=False)
    Amperage = db.Column(db.Float, nullable=False)

# Hydrophone heading direction
class Hydrophone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Heading = db.Column(db.String(10), nullable=False)

# Leak Detection
class Leak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Leak = db.Column(db.Boolean, nullable=False)

# Depth Sensor
class Depth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Depth = db.Column(db.Float, nullable=False)

# Internal Temperature
class InternalTemperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Temperature = db.Column(db.Float, nullable=False)

# External Temperature
class ExternalTemperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Temperature = db.Column(db.Float, nullable=False)

# Internal Humidity
class InternalHumidity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Humidity = db.Column(db.Float, nullable=False)

# Internal Pressure
class InternalPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Pressure = db.Column(db.Float, nullable=False)

# External Pressure
class ExternalPressure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    Pressure = db.Column(db.Float, nullable=False)

# ZED 3D maps of perspective view point
class ZED(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.now())
    img_data = db.Column(db.LargeBinary, nullable=False)
    map_data = db.Column(db.LargeBinary, nullable=False)

# Create the database
db.create_all()

# Routes
# Sonar
@app.route('/sonar', methods=['POST', 'GET'])
def sonar():
    if request.method == 'POST':
        data = request.json
        new_data = Sonar(data=data['data'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = Sonar.query.all()
        data = [data[i].data for i in range(len(data))]
        return jsonify(data)

# IMU
@app.route('/imu', methods=['POST', 'GET'])
def imu():
    if request.method == 'POST':
        data = request.json
        new_data = IMU(Accelerometer=data['Accelerometer'], Gyroscope=data['Gyroscope'], Magnetometer=data['Magnetometer'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = IMU.query.all()
        data = [{'Accelerometer': data[i].Accelerometer, 'Gyroscope': data[i].Gyroscope, 'Magnetometer': data[i].Magnetometer} for i in range(len(data))]
        return jsonify(data)

# Voltage / Current Measurements
@app.route('/voltage_current', methods=['POST', 'GET'])
def voltage_current():
    if request.method == 'POST':
        data = request.json
        new_data = VoltageCurrent(Voltage=data['Voltage'], Amperage=data['Amperage'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = VoltageCurrent.query.all()
        data = [{'Voltage': data[i].Voltage, 'Amperage': data[i].Amperage} for i in range(len(data))]
        return jsonify(data)

# Hydrophone heading direction
@app.route('/hydrophone', methods=['POST', 'GET'])
def hydrophone():
    if request.method == 'POST':
        data = request.json
        new_data = Hydrophone(Heading=data['Heading'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = Hydrophone.query.all()
        data = [data[i].Heading for i in range(len(data))]
        return jsonify(data)

# Leak Detection
@app.route('/leak', methods=['POST', 'GET'])
def leak():
    if request.method == 'POST':
        data = request.json
        new_data = Leak(Leak=data['Leak'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = Leak.query.all()
        data = [data[i].Leak for i in range(len(data))]
        return jsonify(data)

# Depth Sensor
@app.route('/depth', methods=['POST', 'GET'])
def depth():
    if request.method == 'POST':
        data = request.json
        new_data = Depth(Depth=data['Depth'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = Depth.query.all()
        data = [data[i].Depth for i in range(len(data))]
        return jsonify(data)

# Internal Temperature
@app.route('/internal_temperature', methods=['POST', 'GET'])
def internal_temperature():
    if request.method == 'POST':
        data = request.json
        new_data = InternalTemperature(Temperature=data['Temperature'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = InternalTemperature.query.all()
        data = [data[i].Temperature for i in range(len(data))]
        return jsonify(data)

# External Temperature
@app.route('/external_temperature', methods=['POST', 'GET'])
def external_temperature():
    if request.method == 'POST':
        data = request.json
        new_data = ExternalTemperature(Temperature=data['Temperature'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = ExternalTemperature.query.all()
        data = [data[i].Temperature for i in range(len(data))]
        return jsonify(data)

# Internal Humidity
@app.route('/internal_humidity', methods=['POST', 'GET'])
def internal_humidity():
    if request.method == 'POST':
        data = request.json
        new_data = InternalHumidity(Humidity=data['Humidity'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = InternalHumidity.query.all()
        data = [data[i].Humidity for i in range(len(data))]
        return jsonify(data)

# Internal Pressure
@app.route('/internal_pressure', methods=['POST', 'GET'])
def internal_pressure():
    if request.method == 'POST':
        data = request.json
        new_data = InternalPressure(Pressure=data['Pressure'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = InternalPressure.query.all()
        data = [data[i].Pressure for i in range(len(data))]
        return jsonify(data)

# External Pressure
@app.route('/external_pressure', methods=['POST', 'GET'])
def external_pressure():
    if request.method == 'POST':
        data = request.json
        new_data = ExternalPressure(Pressure=data['Pressure'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = ExternalPressure.query.all()
        data = [data[i].Pressure for i in range(len(data))]
        return jsonify(data)

# ZED 3D maps of perspective view point
@app.route('/zed', methods=['POST', 'GET'])
def zed():
    if request.method == 'POST':
        data = request.json
        new_data = ZED(img_data=data['img_data'], map_data=data['map_data'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data saved!'}), 201
    else:
        data = ZED.query.all()
        data = [data[i].data for i in range(len(data))]
        return jsonify(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the server')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host IP')
    parser.add_argument('--port', type=int, default=5000, help='Port number')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
