from flask import render_template, session, url_for, request
import json
import random

from . import main, models

def initialize_swimmers():
	for x in range(10):
		s = models.Swimmer(x, random.randint(0, 100), random.randint(0, 50))
		swimmingPool.add_swimmer(s)


swimmingPool = models.SwmmingPool()
initialize_swimmers();
positionChanger = models.SwimPositionChanger(swimmingPool)


@main.route('/', methods=['GET'])
def index():
	param_dict = {"name": "Jeremy"}
	return render_template('index.html', params=param_dict)


@main.route('/swimming', methods=['GET'])
def swimming():
	return render_template('swimming.html')


@main.route('/add', methods=['GET', 'POST'])
def add_swimmer():
	if request.method == 'GET':
		return render_template('add.html')

	if request.method == 'POST':
		sid = request.form['sid']
		x = request.form['x']
		y = request.form['y']
		if not swimmingPool.has_swimmer(sid):
			s = models.Swimmer(sid, x, y)
			swimmingPool.add_swimmer(s)
			return "added, {0}, {1}, {2}".format(sid, x, y) + ", {0} swimmers in total. ".format(len(swimmingPool))
		else:
			swimmingPool.update(sid, x, y)
			return "updated, {0}, {1}, {2}".format(sid, x, y) + ", {0} swimmers in total. ".format(len(swimmingPool))


@main.route('/remove', methods=['GET', 'POST'])
def remove_swimmer():
	if request.method == 'GET':
		return render_template('remove.html')

	if request.method == 'POST':
		sid = request.form['sid']
		if not swimmingPool.has_swimmer(sid):
			return "swimmer{0} not found".format(sid) + ", {0} swimmers in total. ".format(len(swimmingPool))
		else:
			swimmingPool.remove_swimmer(sid)
			return "removed {0}".format(sid) + ", {0} swimmers in total. ".format(len(swimmingPool))


@main.route('/swimmer_status', methods=['GET'])
def swimmer_status():
	return json.dumps(swimmingPool, default=serialize_pool)


def serialize_pool(swimmingPool):
    d = []
    for s in swimmingPool:
    	obj = {"sid": s.sid, "x": s.x, "y": s.y, "hb": s.heartbeat, "stop": s.stop}
    	d.append(obj)
    return d


@main.route('/start_moving', methods=['GET'])
def start_moving():
	if not positionChanger.is_started():
		positionChanger.start()
	elif positionChanger.is_paused():
		positionChanger.resume()
	return "OK"


@main.route('/stop_moving', methods=['GET'])
def stop_moving():
	if positionChanger.is_started() and not positionChanger.is_paused():
		positionChanger.pause()
	return "OK"