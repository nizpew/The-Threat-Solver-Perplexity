from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QFileDialog, QGridLayout, QWidget, QApplication, QCheckBox, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import os
import glob
import requests
import json

class WorkerThread(QThread):
    result_ready = pyqtSignal(str)
    error_ready = pyqtSignal(str)
    analysis_complete = pyqtSignal(bool)

    def __init__(self, paths, analysis_type, api_key):
        super().__init__()
        self.paths = paths
        self.analysis_type = analysis_type
        self.api_key = api_key
        self.api_url = "https://api.perplexity.ai/chat/completions"  # Perplexity API endpoint
        self.model = "sonar-small-online"  # Specify the model here

    def run(self):
        full_output = ""
        for path in self.paths:
            if not os.path.isfile(path):
                self.error_ready.emit(f"File not found: {path}")
                continue

            try:
                with open(path, 'r') as file:
                    code = file.read()

                max_block_size = 3000
                blocks = [code[i:i + max_block_size] for i in range(0, len(code), max_block_size)]

                for block in blocks:
                    prompt = f"Explain code for {self.analysis_type}:\n\n{block}"
                    headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {self.api_key}'
                    }
                    data = {
                        'model': self.model,
                        'messages': [
                            {'role': 'system', 'content': 'You are a helpful code analyzer.'},
                            {'role': 'user', 'content': prompt}
                        ]
                    }

                    try:
                        response = requests.post(self.api_url, headers=headers, json=data)
                        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                        json_response = response.json()

                        if 'choices' in json_response and len(json_response['choices']) > 0:
                            tgpt_output = json_response['choices'][0]['message']['content']
                            full_output += tgpt_output + "\n\n"
                        else:
                            self.error_ready.emit(f"Unexpected response format from Perplexity API: {json_response}")
                            continue # Continue to the next file if there's an API error
                    except requests.exceptions.RequestException as e:
                        self.error_ready.emit(f"Error during Perplexity API request: {e}")
                        continue # Continue to the next file if there's an API error
                    except json.JSONDecodeError as e:
                        self.error_ready.emit(f"Error decoding JSON response from Perplexity API: {e}")
                        continue # Continue to the next file if there's an API error

                if "The code itself does not directly contain malicious functionality" in full_output:
                    self.analysis_complete.emit(True)
                else:
                    self.analysis_complete.emit(False)

                self.result_ready.emit(full_output)

            except Exception as e:
                self.error_ready.emit(f"An error occurred: {e}")

class CodeAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Analyzer")
        self.setGeometry(100, 100, 600, 400)
        self.filepaths = []
        self.api_key = os.environ.get("PPLX_API_KEY")  # Get API key from environment variable
        if not self.api_key:
            print("Error: Perplexity API key not found in environment variable PPLX_API_KEY")

        # Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)

        # Botões e checkboxes
        self.summary_checkbox = QCheckBox("Explain/Resume Code")
        self.malicious_checkbox = QCheckBox("Identify Malicious Code")
        self.layout.addWidget(self.summary_checkbox, 0, 0)
        self.layout.addWidget(self.malicious_checkbox, 0, 1)
        
        self.button = QPushButton("Import Code Folder")
        self.button.clicked.connect(self.on_folder_clicked)
        self.layout.addWidget(self.button, 1, 0, 1, 2)

        # Texto para exibir código e resultados
        self.textview = QTextEdit()
        self.layout.addWidget(self.textview, 2, 0, 1, 2)
        
        # Indicadores visuais
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label, 3, 0, 1, 2)

    def on_folder_clicked(self):
        if not self.api_key:
            self.textview.setText("Perplexity API key is missing. Set PPLX_API_KEY environment variable.")
            return

        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            folder_path = dialog.selectedFiles()[0]
            self.filepaths = glob.glob(os.path.join(folder_path, '*'))  # Assumindo que você quer analisar todos os arquivos
            if not self.filepaths:
                self.textview.setText("No files found in the selected folder.")
                return

            analysis_type = "summary" if self.summary_checkbox.isChecked() else "malicious" if self.malicious_checkbox.isChecked() else "summary"
            self.thread = WorkerThread(self.filepaths, analysis_type, self.api_key)
            self.thread.result_ready.connect(self.update_textview)
            self.thread.error_ready.connect(self.show_error)
            self.thread.analysis_complete.connect(self.update_indicator)
            self.thread.start()

    def update_textview(self, output):
        QTimer.singleShot(0, lambda: self.textview.setText(output))

    def show_error(self, error_message):
        QTimer.singleShot(0, lambda: self.textview.setText(error_message))

    def update_indicator(self, is_safe):
        if is_safe:
            self.result_label.setText("Code is safe.")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.result_label.setText("Code contains potential malicious content.")
            self.result_label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication([])
    win = CodeAnalyzer()
    win.show()
    app.exec_()

