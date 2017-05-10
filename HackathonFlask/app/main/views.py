from flask import render_template, session, url_for, request
import json
import random

from . import main, models

names = ['Jeremy', 'Michael', 'Alisa', 'Ben', 'Chaosong', 'Karen', 'Chen', 'Sam', 'Jeff', 'Apple']

def initialize_swimmers():
	for x in range(10):
		s = models.Swimmer(x, random.randint(0, 100), random.randint(0, 50), names[x])
		swimmingPool.add_swimmer(s)
	d = models.Swimmer(10, random.randint(0, 100), random.randint(0, 50), "Drowning")
	d.is_drown = True
	d.swimming_by_self = False
	swimmingPool.add_swimmer(d)

swimmingPool = models.SwmmingPool()
initialize_swimmers();
positionChanger = models.SwimPositionChanger(swimmingPool)


@main.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@main.route('/introduction', methods=['GET'])
def introduce():
	return render_template('intro.html')

@main.route('/demo', methods=['GET'])
def demo():
	return render_template('demo.html')

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
    swimming = []
    drowning = []
    sid = 0
    did = 0
    for s in swimmingPool.get_swimmings():
    	obj = {"sid": sid, "x": s.x, "y": s.y, "hr": s.heart_rate, "stop": s.swimming_by_self, "name": s.name, "identity": s.sid}
    	swimming.append(obj)
    	sid += 1

	for d in swimmingPool.get_drownings():
		obj = {"sid": did, "x": d.x, "y": d.y, "hr": d.heart_rate, "stop": d.swimming_by_self, "name": d.name, "identity": s.sid}
		drowning.append(obj)
		did += 1

    return {'swimming':swimming, 'drowning':drowning}


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

@main.route('/test')
def test():
	return "Success"