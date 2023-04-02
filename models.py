from database import db
from sqlalchemy.dialects.postgresql import JSON


class ToDo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String())
    params = db.Column(JSON)

    def __init__(
        self,
        todo,
        params,
    ):
        self.todo = todo
        self.params = params

    def __repr__(self):
        return f"<id {self.id}>"
