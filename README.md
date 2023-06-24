

## How to use

### Женин скрипт
1) Поменять название файла 'Audio_lecture.wav' на необходимое.
2) Файл должен быть в формате .wav
3) Результат распознавания речи отображается в консоли и в конечном файле recognized_text.txt
4) Файл с добавлением в текст пунктуации punctuated_file.txt

### common
Устанавливаем все зависимости с помощью `pip install -r requirements.txt`
### pytube
Так как библиотека 2 года не обновлялась, есть 
[issue](https://github.com/pytube/pytube/issues/1678#issuecomment-1603948730), 
исправляющий баг с ее использованием. Воспользуемся им и поменяем в cipher.py несколько строк

    `function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    ]`