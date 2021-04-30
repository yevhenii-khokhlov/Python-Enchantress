# Create your views here.
# from django.views.generic import TemplateView
#
# from .models import Dealer
#
#
# class CarDetailView(TemplateView):
#     template_name = "car_detail.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             context["dealer"] = Dealer.objects.filter(pk=dealer_id)
#         except:
#             raise NoSuchDealerId(dealer_id=dealer_id)
#         return context
