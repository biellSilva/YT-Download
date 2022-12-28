import flet
from pytube import YouTube
from datetime import timedelta
import os

app_name = 'Youtube Downloader'


def main(page: flet.Page):

    def search(a):
        yt = YouTube(url.value)
        titulo.value = f'Titulo: {yt.title}'
        duraçao.value = f'Duração: {timedelta(seconds=yt.length)}'
        views.value = f'Visualizações: {yt.views}'
        thumb.src = yt.thumbnail_url
        
        container_buttons.disabled=False
        page.update()


    def audio_only(a):
        if os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\Downloads')):
            pass
        else:
            os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\Downloads'))

        try:
            yt = YouTube(url.value)
            yt.streams.get_audio_only().download(
                filename=f'{yt.title}.mp3',
                skip_existing=True,
                max_retries=5,
                output_path=os.path.join(os.path.join(
                    os.environ['USERPROFILE']), 'Desktop\Downloads')
            )

            bs_text.value = f'Concluido'
            bs.open = True

        except Exception as err:
            bs_text.value = f'{err}'
            bs.open = True

        page.update()


    def download(a):
        if os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\Downloads')):
            pass
        else:
            os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\Downloads'))
        
        try:
            yt = YouTube(url.value)
            yt.streams.get_highest_resolution().download(
                filename=f'{yt.title}.mp4',
                skip_existing=True,
                max_retries=5,
                output_path=os.path.join(os.path.join(
                    os.environ['USERPROFILE']), 'Desktop\Downloads')
            )

            bs_text.value = f'Concluido'
            bs.open = True

        except Exception as err:
            bs_text.value=f'{err}'
            bs.open=True

        page.update()


    #   -----------------------------------
    #   -----------------------------------


    page.title = app_name
    page.window_resizable=False
    page.window_width=700
    page.window_height=430

    page.bgcolor=flet.LinearGradient(
        begin=flet.alignment.bottom_left,
        end=flet.alignment.top_right,
        colors=['#0f0f0f', '#242424'],
    ),

    url = flet.TextField(
        hint_text='https://youtube.com/watch',
        border_color='white',
        border_width=0.5,
        width=550
        )

    go_button = flet.ElevatedButton(
        text='Procurar',
        style=flet.ButtonStyle(
            color=flet.colors.WHITE,
            bgcolor=flet.colors.RED_900,
        ),
        on_click=search
        )

    titulo = flet.Text(
        value='Titulo: ',
        no_wrap=False,
    )

    duraçao = flet.Text(
        value='Duração: ',
    )

    views = flet.Text(
        value='Visualizações: ',
    )

    Audio_only_button = flet.ElevatedButton(
        text='Apenas Audio',
        style=flet.ButtonStyle(
            color=flet.colors.WHITE,
            bgcolor=flet.colors.RED_900,
        ),
        on_click=audio_only
    )

    Video_button = flet.ElevatedButton(
        text='Download',
        style=flet.ButtonStyle(
            color=flet.colors.WHITE,
            bgcolor=flet.colors.RED_900,
        ),
        on_click=download
    )
    
    thumb = flet.Image(
        src='https://imagepng.org/wp-content/uploads/2017/09/youtube-play-icone.png',
        height=200,
        fit=flet.ImageFit.CONTAIN,
        border_radius=15
    )

    bs_text = flet.Text(
        value='',
    )

    bs = flet.BottomSheet(
        flet.Container(
            flet.Column(
                [
                    bs_text
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=False,

    )
    page.overlay.append(bs)
    


    container_base = flet.Container(
        flet.Row(
            alignment=flet.MainAxisAlignment.CENTER,
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            controls=[
                url, go_button
            ],
        ),
    )

    container_thumb = flet.Container(
        flet.Stack([
            flet.Column(
                controls=[
                    thumb
                    ]
            ),
            flet.Column(
                left=300,
                top=30,
                wrap=True,
                controls=[
                    titulo,
                    duraçao,
                    views,
                    ],
                ), 
            ]),
        bgcolor=flet.colors.WHITE10,
        border_radius=15,
        margin=5,
        width=page.width,
        padding=15
    )

    container_buttons = flet.Container(
        flet.Row(
            alignment=flet.MainAxisAlignment.CENTER,
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            controls=[
                Audio_only_button,
                Video_button
            ]
        ),
        disabled=True,
        alignment=flet.alignment.center
    )
 

    page.add(container_base, container_thumb, container_buttons)
    page.update


flet.app(target=main)
