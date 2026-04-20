from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class JobApplicationn(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable= False)
    data_applied = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable= False, default='Applied')
    notes = db.Column(db.Text, nullable= True)
    
    def __repr__(self):
        return f'<JobApplication {self.company} - {self.role}>'