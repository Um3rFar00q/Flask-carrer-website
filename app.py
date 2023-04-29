from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Data Analyst",
    'location': "Lahore, Pakistan",
    'salary': "Rs. 15,00,000"
  },
  {
    'id': 2,
    'title': "Data Scientist",
    'location': "Lahore, Pakistan",
    'salary': "Rs. 25,00,000"
  },
  {
    'id': 3,
    'title': "Frontend Engineer",
    'location': "remote"
  },
  {
    'id': 4,
    'title': "Data Analyst",
    'location': "Karachi, Pakistan",
    'salary': "Rs. 20,00,000"
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
