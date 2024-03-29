import re
import tkinter as tk

def extract_name(url):
    # Your regex pattern seems fine if it's working in the standalone script.
    # Use it here to match and return the desired part of the URL.
    matches = re.search(r"^(?:https?://)?(?:www\.)?linkedin\.com/in/([a-z]+)(?:[-]+)([a-z]+)", url, re.IGNORECASE)
    if matches:
        return matches.group(1)[0].upper()+matches.group(1)[1:] + " " + matches.group(2)[0].upper()+matches.group(2)[1:]  # This should return the username part of the URL.
    return "Not found"

def show_extracted_name():
    url = url_entry.get()  # Get the URL from the entry widget.
    username = extract_name(url)
    result_label.config(text=f"Extracted Name: {username}")

# Set up the Tkinter window.
root = tk.Tk()
root.title("LinkedIn Name Extractor")

# Create an entry widget for the URL input.
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Button to trigger name extraction.
extract_button = tk.Button(root, text="Extract Name", command=show_extracted_name)
extract_button.pack()

# Label to display the result.
result_label = tk.Label(root, text="Extracted Name: ")
result_label.pack()

# Start the Tkinter event loop.
root.mainloop()
