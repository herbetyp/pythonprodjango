from django.shortcuts import get_object_or_404
from django.shortcuts import render

from pypro.aperitivos.models import Video


videos = [
    Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id=434538400),
    Video(slug='instalacao-windows', titulo='Instalação no Windows', vimeo_id=435485443),
]

videos_dct = {video.slug: video for video in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
