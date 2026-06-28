import tkinter as tk
from tkinter import messagebox

def predict():
    url = entry.get()

    if url == "":
        messagebox.showwarning("Warning", "Please enter a URL")
        return

    # Demo result
    messagebox.showinfo("Prediction", f"URL: {url}\n\nResult: Legitimate Website")

root = tk.Tk()
root.title("Phishing Website Detection")
root.geometry("400x200")

tk.Label(root, text="Phishing Website Detection", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter URL").pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Predict", command=predict).pack(pady=10)

root.mainloop()