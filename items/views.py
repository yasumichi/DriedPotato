from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Item, Comment
from .forms import ItemForm
# Create your views here.
class IndexView(ListView):
    template_name = "items/index.html"
    context_object_name = "latest_item_list"

    def get_queryset(self):
        return Item.objects.filter(approval = False).order_by("-priority", "id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = 'index'
        return context

class ApprovalListView(ListView):
    template_name = "items/index.html"
    context_object_name = "latest_item_list"

    def get_queryset(self):
        return Item.objects.filter(approval = True).order_by("-priority", "id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = 'approval'
        return context

class DetailView(DetailView):
    model = Item
    template_name = "items/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_list"] = Comment.objects.filter(item = self.get_object())
        return context

class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = "items/item_create.html"
    form_class = ItemForm
    success_url = reverse_lazy("items:create")

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.author = self.request.user
        qryset.save()
        return HttpResponseRedirect(reverse("items:index"))

    def get_success_url(self):
        messages.success(self.request, 'Item created')
        return resolve_url("items:index")

class ItemUpdateView(UpdateView):
    template_name = "items/item_create.html"
    form_class = ItemForm
    model = Item

    def get_success_url(self):
        return reverse_lazy("items:index")

class ItemDeleteView(DeleteView):
    template_name = "items/item_delete.html"
    model = Item
    success_url = reverse_lazy("items:index")

@login_required
def comment(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    print(request.POST)
    try:
        usercomment = request.POST["comment"]
        if request.user.is_authenticated:
            c = Comment(item = item, comment=usercomment, author=request.user)
            c.save()
    except (KeyError, Item.DoesNotExist):
        return render(
            request,
            "items/detail.html",
            {
                "item": item,
                "error_message": "Error",
            },
        )
    else:
        return HttpResponseRedirect(reverse("items:detail", args=(item.id,)))

@staff_member_required
def approve(request, item_id, value):
    item = get_object_or_404(Item, pk=item_id)
    if value == 1:
        item.approval = True
    else:
        item.approval = False

    item.save()

    return HttpResponseRedirect(reverse("items:detail", args=(item.id,)))

@staff_member_required
def priority(request, item_id, value): 
    item = get_object_or_404(Item, pk=item_id)
    item.priority = value
    item.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
