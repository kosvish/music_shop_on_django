# Здесь будут классы которые я хочу отобразить в нашем поисковике по категориям и т.д(типо как в админке)

from ajax_select import register, LookupChannel
from .models import Artist


# Пишу кастомный класс дабы не вылезала ошибка при нашем отображении
class CustomLookupChannel(LookupChannel):

    min_length = 3

    def check_auth(self, request):
        return None




@register('artist')
class ArtistLookup(CustomLookupChannel):

    model = Artist

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q)[:10]




