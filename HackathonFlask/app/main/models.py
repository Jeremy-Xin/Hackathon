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


class Swimmer(object):
	def __init__(self, sid, x, y):
		self.sid = sid
		self.x = x
		self.y = y
		self.heartbeat = 70
		self.stop = False
		self.is_drown = False

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
				if not swimmer.stop:
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