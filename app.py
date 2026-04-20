from flask import Flask, render_template, request, redirect, url_for
from models import db, JobApplication
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///applymate.db'
app.config['SQLAPCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route('/')
def index():
    jobs = JobApplication.query.all()
    return render_template('index.html', jobs= jobs)


@app.route('/add', methods = ['GET', 'POST'])
def add_jobs():
    if request.method == 'POST':
        job = JobApplication(
            company = request.form['company'],
            role = request.form['role'],
            date_applied = request.form['date_applied'],
            status = request.form['status'],
            notes =request.form['notes']
        )
        return redirect(url_for('index'))
    return render_template('add_job.html')

@app.route('/delete/<int:id>')
def delete_job(id):
    job =JobApplication.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/int:id', methods=['GET', 'POST'])
def update_status(id):
    job = JobApplication.query.get_or_404(id)
    if request.method == 'Post':
        job.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_job.html', job=job)
if __name__ == '__main__':
    app.run(debug=True)