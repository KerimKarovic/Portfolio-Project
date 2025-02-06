from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(200), nullable=False)
    github_link = db.Column(db.String(255), nullable=True)  # Optional GitHub link
    demo_link = db.Column(db.String(255), nullable=True)  # Optional live demo link

    def __repr__(self):
        return f"<Project {self.name}>"

class Message(db.Model):  # Message model for contact form submissions
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())  # Stores submission time

    def __repr__(self):
        return f"<Message from {self.name}>"
