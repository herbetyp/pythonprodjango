from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=[self.slug])


videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação', 434538400),
    Video('instalacao-windows', 'Instalação no Windows', 435485443),
]

videos_dct = {video.slug: video for video in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
