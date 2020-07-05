from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 434538400},
        'instalacao-windows': {
            'titulo': 'Instalação no Windows',
            'vimeo_id': 435485443,
        },
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
