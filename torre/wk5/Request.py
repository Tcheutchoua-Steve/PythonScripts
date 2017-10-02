
class Request:
    def __init__(self, start_time,file_req, time_need):
        self.start_time = start_time
        self.request = file_req
        self.time_needed = time_need

    def get_start(self):
        return self.start_time

    def get_file(self):
        return self.request

    def wait_time(self):
        return self.time_needed
