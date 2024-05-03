from django.urls import path

from photography_blog.api.create_session_api import CreateSessionView
from photography_blog.api.session_api import SessionView
from photography_blog.api.sessions_api import SessionsView

urlpatterns = [
    path(r"api/sessions/", SessionsView.as_view(), name="sessions_api"),
    path(r"api/session/<id>/", SessionView.as_view(), name="session_api"),
    path(r"api/session/", CreateSessionView.as_view(), name="create_session_api"),
]
