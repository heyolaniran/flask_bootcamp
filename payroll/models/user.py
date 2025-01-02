from payroll import db

class User(db.Model): 
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    verified = db.Column(db.Boolean(), default=False)
    otp_secret = db.Column(db.String(255), unique=True, nullable=True)
    role = db.Column(db.String(255), nullable=False, default='user')
    created_at = db.Column(db.DateTime(), server_default=db.func.now())

    def __repr__(self):
        return f'User {self.username}'
    
    