from flask import Blueprint, render_template, request, redirect, url_for, flash
# # from .forms import UserCreationForm, LoginForm
# from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

