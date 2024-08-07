import openai
from openai import OpenAI
import fitz
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import Text, filedialog
import PIL
import PIL.Image
from tkinter import *
from PIL import ImageTk


# function to analyze the given exam
def analyze_exam(text):
    respone = openai.completions.create(model="davinci-002",prompt = "Analyze the following exampaper and output the main Topics one should focus on to be well prepared. The output should be written in the same language as the input file: \n\n{text}")
    return respone.choices[0].text.strip()

# function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
        return text

# handling drag and drop
def drop(event):
    pdf_path = event.data
    pdf_text.get(extract_text_from_pdf(pdf_path))

# analyzing the text
def analyze():
    text = pdf_text.get("1.0", tk.END)
    if text.strip():
        analysis = analyze_exam(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, analysis)

# main window
root = TkinterDnD.Tk()
root.title("AI Exam Extractor")
root.geometry("980x720")

# drag & drop
pdf_text = Text(root, wrap='word', height=10,)
pdf_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
pdf_text.drop_target_register(DND_FILES)
pdf_text.dnd_bind('<<Drop>>', drop)


# Button to analyze exam
analyze_button = tk.Button(root, text="Analyze", command=analyze)
analyze_button.pack(pady=10)

# output
output_text = Text(root, wrap='word', height=10)
output_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()

