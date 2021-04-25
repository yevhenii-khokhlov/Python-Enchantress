

class NoSuchId(AttributeError):
    def __init__(self, obj_id):
        self.obj_id = obj_id

    def __str__(self):
        return f"No object with id {self.obj_id}"
