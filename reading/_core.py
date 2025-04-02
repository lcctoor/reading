import webbrowser

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文本朗读</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .container {
            background-color: #fff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            width: 600px;
        }
        textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 6px;
            resize: vertical;
            font-size: 16px;
        }
        .button-container {
            display: flex;
            justify-content: space-between;
        }
        .right-buttons {
            display: flex;
        }
        button {
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            margin-left: 10px;
        }
        #play-file {
            background-color: #3498db;
            color: white;
        }
        #clear {
            background-color: #e74c3c;
            color: white;
        }
        #play {
            background-color: #2ecc71;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <textarea id="inputText" rows="15" placeholder="请输入要朗读的文本"></textarea>
        <div class="button-container">
            <button id="play-file">播放文本文件</button>
            <div class="right-buttons">
                <button id="clear">清空</button>
                <button id="play">播放</button>
            </div>
        </div>
    </div>
    <input type="file" id="fileInput" style="display: none;">
    <script>
        const inputText = document.getElementById('inputText');
        const clearButton = document.getElementById('clear');
        const playButton = document.getElementById('play');
        const playFileButton = document.getElementById('play-file');
        const fileInput = document.getElementById('fileInput');

        clearButton.addEventListener('click', () => {
            inputText.value = '';
        });

        playButton.addEventListener('click', () => {
            const text = inputText.value;
            if (text) {
                const utterance = new SpeechSynthesisUtterance(text);
                window.speechSynthesis.speak(utterance);
            }
        });

        playFileButton.addEventListener('click', () => {
            fileInput.click();
        });

        fileInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const text = e.target.result;
                    const utterance = new SpeechSynthesisUtterance(text);
                    window.speechSynthesis.speak(utterance);
                };
                reader.readAsText(file);
            }
        });
    </script>
</body>
</html>
"""


class MainHandler(RequestHandler):
    def get(self):
        self.write(html)

def reading_server(port=9355):
    app = Application([(r"/", MainHandler)])
    app.listen(port)
    webbrowser.open('http://localhost:9355')
    IOLoop.current().start()