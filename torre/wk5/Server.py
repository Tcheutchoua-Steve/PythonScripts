class Server:
    def __init__(self, fpm):
        self.file_rate = fpm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
        if self.time_remaining <= 0:
            self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.time_needed


