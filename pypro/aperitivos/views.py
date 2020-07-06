from django.shortcuts import render


videos = [
    {
        'slug': 'motivacao',
        'titulo': 'Vídeo Aperitivo: Motivação',
        'vimeo_id': 434538400,
    },
    {
        'slug': 'instalacao-windows',
        'titulo': 'Instalação no Windows',
        'vimeo_id': 435485443,
    },
]

videos_dct = {video['slug']: video for video in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
