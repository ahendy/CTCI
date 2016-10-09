
class Graph():

	def __init__(self, fpath=None):
		self.file = fpath
		self.connected_graph = {
			1: [2, 3],
			2: [1, 3],
			3: [1, 2, 4],
			4: [3,],
		}

		self.disconnected_graph = {
			1: [3],
			2: [4],
			3: [1],
			4: [2],
		}
