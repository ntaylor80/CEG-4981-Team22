

status_values = {"0":"IDLE","1":"IN_PROCESS","2":"ERROR"}

class Drone:
    def __init__(self,id):
        self.id = id
        self.status = status["0"]
