import tkinter as tk
from tkinter import messagebox

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog Management System")
        self.root.geometry("800x800")
        
        self.posts = []  # To store blog posts in memory
        self.categories = ["Tech", "Lifestyle", "Travel", "Food", "Health"]
        
        # Title label
        self.title_label = tk.Label(root, text="Welcome to the Blog Management System", font=("Arial", 20))
        self.title_label.pack(pady=20)

        # Button to create a new post
        self.create_post_button = tk.Button(root, text="Create New Post", command=self.create_post_window)
        self.create_post_button.pack(pady=10)

        # Display the list of posts (scrollable listbox)
        self.post_listbox = tk.Listbox(root, width=50, height=15)
        self.post_listbox.pack(pady=10)

        # Button to refresh the list
        self.refresh_button = tk.Button(root, text="Refresh", command=self.load_posts)
        self.refresh_button.pack(pady=10)

        # Bind the click event to the listbox
        self.post_listbox.bind("<Double-1>", self.view_post_details)

    def create_post_window(self):
        """ Opens a new window to create a blog post """
        create_window = tk.Toplevel(self.root)
        create_window.title("Create New Post")
        create_window.geometry("600x500")
        
        # Add Title
        self.title_label = tk.Label(create_window, text="Post Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(create_window, width=50)
        self.title_entry.pack(pady=10)
        
        # Add Content
        self.content_label = tk.Label(create_window, text="Content:")
        self.content_label.pack()
        self.content_entry = tk.Text(create_window, width=50, height=10)
        self.content_entry.pack(pady=10)

        # Category Dropdown
        self.category_label = tk.Label(create_window, text="Category:")
        self.category_label.pack(pady=5)
        self.category_var = tk.StringVar(create_window)
        self.category_var.set(self.categories[0])  # Default category
        self.category_menu = tk.OptionMenu(create_window, self.category_var, *self.categories)
        self.category_menu.pack(pady=5)

        # Tags Entry
        self.tags_label = tk.Label(create_window, text="Tags (comma-separated):")
        self.tags_label.pack(pady=5)
        self.tags_entry = tk.Entry(create_window, width=50)
        self.tags_entry.pack(pady=5)
        
        # Add Post Button
        self.add_post_button = tk.Button(create_window, text="Add Post", command=self.add_post)
        self.add_post_button.pack(pady=10)

    def add_post(self):
        """ Adds a new post to the list """
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END).strip()
        
        if not title or not content:
            messagebox.showerror("Error", "Title and Content cannot be empty")
            return

        # Add the post to the posts list
        self.posts.append({
            'title': title, 
            'content': content, 
            'comments': []  # Initialize an empty list for comments
        })
        
        # Refresh the main window to show the new post
        self.load_posts()

    def load_posts(self):
        """ Load all blog posts into the listbox """
        self.post_listbox.delete(0, tk.END)
        
        # Display the titles of all posts in the listbox
        for post in self.posts:
            self.post_listbox.insert(tk.END, post['title'])

    def view_post_details(self, event):
        """ Show the full content of a clicked post """
        # Get the index of the clicked post
        index = self.post_listbox.curselection()
        if index:
            selected_post = self.posts[index[0]]  # Retrieve the selected post
            self.show_post_details_window(selected_post)  # Display the post details

    def show_post_details_window(self, selected_post):
        """ Show the details of the selected post in a new window """
        # Create a new window to display the post details
        details_window = tk.Toplevel(self.root)
        details_window.title("Post Details")
        details_window.geometry("600x600")

        # Display post title and content
        post_title = tk.Label(details_window, text=selected_post['title'], font=("Arial", 16))
        post_title.pack(pady=10)

        post_content = tk.Label(details_window, text=selected_post['content'], font=("Arial", 12), justify="left")
        post_content.pack(padx=20, pady=10)

        # Display Comments
        comments_frame = tk.Frame(details_window)
        comments_frame.pack(pady=10)

        comments_label = tk.Label(comments_frame, text="Comments:", font=("Arial", 14))
        comments_label.pack()

        for comment in selected_post['comments']:
            comment_label = tk.Label(comments_frame, text=f"{comment['author']}: {comment['text']}", justify="left")
            comment_label.pack(anchor="w")

        # Add Comment Section
        comment_entry = tk.Entry(details_window, width=50)
        comment_entry.pack(pady=10)

        add_comment_button = tk.Button(details_window, text="Add Comment", 
                                       command=lambda: self.add_comment(selected_post, comment_entry))
        add_comment_button.pack(pady=5)

        # Close Button
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10)

    def add_comment(self, selected_post, comment_entry):
        """ Add a comment to the selected post """
        comment_text = comment_entry.get().strip()

        if not comment_text:
            messagebox.showwarning("Empty Comment", "Please enter a comment.")
            return

        # For simplicity, we'll add a default author
        comment = {
            'author': "Anonymous",  # You could add user authentication to get the author's name
            'text': comment_text
        }

        selected_post['comments'].append(comment)

        # Reload the post details window to display the new comment
        comment_entry.delete(0, tk.END)
        self.show_post_details_window(selected_post)  # Refresh the details window with new comments

# Running the application
root = tk.Tk()
app = BlogApp(root)
root.mainloop()
