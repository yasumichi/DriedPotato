from django.urls import path

from . import views

app_name = "items"
urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("approval", views.ApprovalListView.as_view(), name="approval"),
        path("create/", views.ItemCreateView.as_view(), name="create"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        path("<int:pk>/update", views.ItemUpdateView.as_view(), name="update"),
        path("<int:pk>/delete", views.ItemDeleteView.as_view(), name="delete"),
        path("<int:item_id>/comment/", views.comment, name="comment"),
        path("<int:item_id>/approve/<int:value>", views.approve, name="approve"),
        path("<int:item_id>/priority/<int:value>", views.priority, name="priority"),
]
