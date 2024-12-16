from flask import Blueprint, render_template, url_for

options_dashboard_route = Blueprint('options_dashboard_route', __name__)

@options_dashboard_route.route("/")
def index():
    return render_template("dashboard/options.html")
