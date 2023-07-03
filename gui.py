import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv
from main import analyze_video_data

class GUI:
    def __init__(self):

        self.result = None
        self.root = tk.Tk()
        self.root.title("YouTube Video Analysis")
        self.root.geometry("600x500")
        self.root.configure(bg="#2c2c2c")  # Set background color

        self.about_button = tk.Button(self.root, text="About", command=self.show_about, bg="#4f4f4f", fg="white", activebackground="#8c8c8c", activeforeground="white")
        self.about_button.pack(anchor=tk.NE, padx=1, pady=1)

        self.label = tk.Label(self.root, text="Enter desired query", fg="white", bg="#2c2c2c", font=('Helvetica bold', 20))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.root, text="Analyze", command=self.analyze, bg="#4f4f4f", fg="white", activebackground="#8c8c8c", activeforeground="white", font=('Helvetica bold', 15))
        self.button.pack(pady=10)

        self.results_label = tk.Label(self.root, text="Results:", fg="white", bg="#2c2c2c", font=('Helvetica bold', 15))
        self.results_label.pack(pady=10)

        self.results_text = tk.Text(self.root, height=10, width=50, bg="#1e1e1e", fg="white", font=('Helvetica bold', 10))
        self.results_text.pack()

        self.average_views_text = tk.Label(self.root, text="", fg="white", bg="#2c2c2c")
        self.average_views_text.pack()

        self.button = tk.Button(self.root, text="Export", command=self.export, bg="#4f4f4f", fg="white", activebackground="#8c8c8c", activeforeground="white", font=('Helvetica bold', 10))
        self.button.pack(pady=10)

        self.root.resizable(False, False)
        self.root.mainloop()

    def analyze(self):
        

        query = self.entry.get()

        if not query :
            messagebox.showwarning("Empty Query", "Please enter a query before analyzing.")
            return

        sorted_entities, average_views = analyze_video_data(query)

        self.result = (sorted_entities, average_views)

        # Update results
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Most common named entities (NOUN) in video titles:\n")
        for entity, frequency in sorted_entities:
            self.results_text.insert(tk.END, f"{entity}: {frequency}\n")
        self.results_text.pack()

        # Update average views
        self.average_views_text.config(text=f"Average Views: {average_views}", font=('Helvetica bold', 15))


    def show_about(self):
        messagebox.showinfo("About", "Video Analysis Program\n\nThis program analyzes first 10 YouTube video titles based on a user-provided query. It identifies the most common named entities (NOUN) in the titles and displays their frequencies. Additionally, it calculates the average views of the analyzed videos. \n\nDeveloped by CoderFaris.")


    def export(self):
        query = self.entry.get()

        result = self.result

        if not query:
            messagebox.showwarning("Empty Query", "Please enter a query before exporting.")
            return

        if not result:
            messagebox.showwarning("No Data", "There is no data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Export Results")

        if file_path:
            try:
                with open(file_path, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Entity", "Frequency"])
                    for entity, frequency in result[0]:
                        writer.writerow([entity, frequency])
                    writer.writerow([])
                    writer.writerow(["Average Views", result[1]])

                messagebox.showinfo("Export Successful", "Results exported successfully!")
            except Exception as e:
                messagebox.showerror("Export Error", f"Error exporting results: {str(e)}")
        else:
            messagebox.showinfo("Export Canceled", "Export canceled.")


if __name__ == "__main__":
    gui = GUI()