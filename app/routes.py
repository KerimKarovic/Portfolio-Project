from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import ContactForm
from app.models import db, Project

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/skills")
def skills():
    return render_template("skills.html")

@main.route("/experience")
def experience():
    return render_template("experience.html")

@main.route("/projects")
def projects():
    projects = Project.query.all()  # Fetch projects from the database
    return render_template("projects.html", projects=projects)

@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Simulate sending an email (actual logic requires Flask-Mail setup)
        flash("Message sent successfully!", "success")
        return redirect(url_for("main.contact"))
    
    return render_template("contact.html", form=form)
