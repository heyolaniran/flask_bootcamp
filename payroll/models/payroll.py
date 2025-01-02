from payroll import db

class Payroll(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    base_name = db.Column(db.String(255), nullable=False)
    base_url= db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())

    def __repr__(self): 
        return f'Payroll for {self.base_name}'