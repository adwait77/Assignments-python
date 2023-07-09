import tkinter as tk
import webbrowser

# Function to handle form submission
def submit_form():
    course = course_entry.get()
    source = source_var.get()
    
    if source == "Instagram Ads":
        faq_url = "https://help.instagram.com"
    elif source == "YouTube Ads":
        faq_url = "https://support.google.com/youtube/thread/202433711/frequently-asked-questions?hl=en"
    else:
        faq_url = "https://www.facebook.com/help"

    webbrowser.open(faq_url)

# Create the main window
window = tk.Tk()
window.title("Course Enquiry Form")

# Create form labels and entries
course_label = tk.Label(window, text="Course:")
course_label.pack()

course_entry = tk.Entry(window)
course_entry.pack()

source_label = tk.Label(window, text="Source:")
source_label.pack()

# Create a variable to store the selected source
source_var = tk.StringVar(window)
source_var.set("Instagram Ads")

# Create a dropdown menu for the source options
source_dropdown = tk.OptionMenu(window, source_var, "Instagram Ads", "YouTube Ads", "Facebook Ads")
source_dropdown.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

# Run the GUI main loop
window.mainloop()
