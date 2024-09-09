from community_app import db

class Responses(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable = False)
    is_agree = db.Column(db.Boolean, nullable =False)

    def __str__(self):
        return f'Question no# {self.question_id}, answer {self.is_agree}'