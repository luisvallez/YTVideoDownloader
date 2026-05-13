from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from flet import (
    run,
    Page,
    Text,
    CrossAxisAlignment,
    MainAxisAlignment,
    Colors,
    Column,
    TextField,
    TextStyle,
    SafeArea,
)


def main(page: Page) -> None:
    status_text: Text = Text()

    page.add(Text(value="YouTube Video Downloader", size=25))
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = False
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    def enter_pressed() -> None:
        try:
            with YoutubeDL(
                {
                    "format": "bestvideo+bestaudio/best",
                    "outtemplate": "%(title)s.%(ext)s",
                    "quiet": True,
                    "no_warnings": True,
                }
            ) as ydl:
                ydl.download([url_input.value])
                status_text.value = f"Descarga Completada"
                status_text.color = Colors.GREEN
                page.update()

        except DownloadError:
            status_text.value = "URL incorrecto, o el video no existe"
            status_text.color = Colors.ORANGE
            page.update()
            url_input.value = ""

    url_input: TextField = TextField(
        adaptive=True,
        label="Video URL",
        label_style=TextStyle(color=Colors.GREY_400),
        on_submit=enter_pressed,
    )
    page.add(
        SafeArea(
            content=Column(
                controls=[url_input, status_text],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        )
    )


run(main)
