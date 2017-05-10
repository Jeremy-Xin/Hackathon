from threading import Thread, Event
import random
import time

class SwmmingPool(object):
	_swimmers = []

	def has_swimmer(self, id):
		for swimmer in self._swimmers:
			if swimmer.sid == id:
				return True
		return False

	def get_swimmer(self, id):
		for swimmer in self._swimmers:
			if swimmer.sid == id:
				return swimmer
		return None

	def add_swimmer(self, swimmer):
		if not self.has_swimmer(swimmer.sid):
			self._swimmers.append(swimmer)

	def remove_swimmer(self, id):
		for swimmer in self._swimmers:
			if swimmer.sid == id:
				self._swimmers.remove(swimmer)

	def update(self, id, x, y):
		for swimmer in self._swimmers:
			if swimmer.sid == id:
				swimmer.x = x
				swimmer.y = y

	def __len__(self):
		return len(self._swimmers)

	def __iter__(self):
		return iter(self._swimmers)

	def get_swimmings(self):
		l = []
		for s in self._swimmers:
		 	if not s.is_drown:
		 		l.append(s)
		return l

	def get_drownings(self):
		l = []
		for s in self._swimmers:
		 	if s.is_drown:
		 		l.append(s)
		return l


class Swimmer(object):
	def __init__(self, sid, x, y, name, tp = 0, bp = 0, hr = 0, br = 0, vs = 0, hs = 0):
		self.sid = sid
		self.x = x
		self.y = y
		self.swimming_by_self = True
		self.is_drown = False
		self.name = name
		self.temperature = tp
		self.blood_pressure = bp
		self.heart_rate = hr
		self.breathing_rate = br
		self.vertical_speed = vs
		self.horizontal_speed = hs


	def change_body_state(self, tp = 0, bp = 0, hr = 0, br = 0, vs = 0, hs = 0):
		self.temperature = tp
		self.blood_pressure = bp
		self.heart_rate = hr
		self.breathing_rate = br
		self.vertical_speed = vs
		self.horizontal_speed = hs



	def swim(self):
		self.x = self.x + random.randint(-1, 1)
		self.y = self.y + random.randint(-1, 1)
		if self.x >= 100:
			self.x = 99
		if self.x <= 0:
			self.x = 1
		if self.y >= 50:
			self.y = 49
		if self.y <= 0:
			self.y = 1



class SwimPositionChanger(Thread):
	def __init__(self, pool):
		Thread.__init__(self)
		self._pool = pool
		self._flag = Event()
		self._flag.clear()
		self._ispause = False
		self._isstarted = False
		self.setDaemon(True)


	def run(self):
		self._isstarted = True
		while True:
			if self._ispause:
				self._flag.wait()
			for swimmer in self._pool:
				if swimmer.swimming_by_self:
					swimmer.swim()
			time.sleep(1)

	def pause(self):
		self._flag.clear()
		self._ispause = True

	def resume(self):
		self._ispause = False
		self._flag.set()

	def is_paused(self):
		return self._ispause

	def is_started(self):
		return self._isstarted