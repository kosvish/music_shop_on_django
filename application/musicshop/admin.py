from django.contrib import admin
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


class AlbumsArtistInLine(admin.TabularInline):
    model = Artist.albums_of_artist.through


class MembersInLine(admin.TabularInline):
    model = Artist.members.through


class ImageGalleryInLine(GenericTabularInline):
    model = ImageGallery
    readonly_fields = ('image_url',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    inlines = [ImageGalleryInLine]


@admin.register(Artist)
class Artist(admin.ModelAdmin):
    inlines = [MembersInLine, ImageGalleryInLine, AlbumsArtistInLine]
    exclude = ('members', 'albums_of_artist')


admin.site.register(Genre)
admin.site.register(Member)
admin.site.register(MediaType)
admin.site.register(ImageGallery)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
admin.site.register(Session)
admin.site.register(AlbumArtist)
