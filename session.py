import uuid

class SessionService:
    def create(self):
        return str(uuid.uuid4())
