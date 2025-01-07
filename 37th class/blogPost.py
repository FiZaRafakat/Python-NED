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

        # Search bar
        self.search_label = tk.Label(root, text="Search Blog Posts", font=("Arial", 14))
        self.search_label.pack(pady=10)
        self.search_entry = tk.Entry(root)
        self.search_entry.pack(pady=10)
        self.search_button = tk.Button(root, text="Search", command=self.search_posts)
        self.search_button.pack(pady=10)

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
        
        # Create tags for text formatting (bold and italic)
        self.content_entry.tag_configure("bold", font=("Arial", 12, "bold"))
        self.content_entry.tag_configure("italic", font=("Arial", 12, "italic"))

        # Bold and Italic buttons
        bold_button = tk.Button(create_window, text="Bold", command=self.bold_text)
        bold_button.pack(side=tk.LEFT, padx=5)
        
        italic_button = tk.Button(create_window, text="Italic", command=self.italic_text)
        italic_button.pack(side=tk.LEFT, padx=5)

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
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END).strip()
        category = self.category_var.get()  # Get the selected category
        tags = self.tags_entry.get().strip()  # Get the tags
    
        if not title or not content:
            messagebox.showerror("Error", "Title and Content cannot be empty")
            return
        
        self.posts.append({
            'title': title, 
            'content': content, 
            'comments': []  # Initialize an empty list for comments
        })

    # Add the post to the posts list with the selected category and tags
        self.posts.append({'title': title, 'content': content, 'category': category, 'tags': tags})
    
    # Refresh the main window to show the new post
        self.load_posts()

    def load_posts(self):
        """ Load all blog posts into the listbox """
        self.post_listbox.delete(0, tk.END)
        
        # Display the titles of all posts in the listbox
        for post in self.posts:
            self.post_listbox.insert(tk.END, post['title'])

    def search_posts(self):
        """ Search for blog posts based on title """
        search_term = self.search_entry.get().lower()
        self.post_listbox.delete(0, tk.END)

        for post in self.posts:
            if search_term in post['title'].lower():
                self.post_listbox.insert(tk.END, post['title'])
     
    def bold_text(self):
        """ Apply bold tag to selected text """
        try:
            current_tags = self.content_entry.tag_names("sel.first")
            if "bold" in current_tags:
                self.content_entry.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.content_entry.tag_add("bold", "sel.first", "sel.last")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select text to apply bold.")

    def italic_text(self):
        """ Apply italic tag to selected text """
        try:
            current_tags = self.content_entry.tag_names("sel.first")
            if "italic" in current_tags:
                self.content_entry.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.content_entry.tag_add("italic", "sel.first", "sel.last")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select text to apply italic.")

    def show_post_details_window(self, post):
        details_window = tk.Toplevel(self.root)
        details_window.title("Post Details")
        details_window.geometry("600x400")

    # Display post title and content
        post_title = tk.Label(details_window, text=post['title'], font=("Arial", 16))
        post_title.pack(pady=10)

        post_content = tk.Label(details_window, text=post['content'], font=("Arial", 12), justify="left")
        post_content.pack(padx=20, pady=10)

    # Edit Button
        edit_button = tk.Button(details_window, text="Edit Post", command=lambda: self.edit_post(post, details_window))
        edit_button.pack(pady=10)

    # Delete Button
        delete_button = tk.Button(details_window, text="Delete Post", command=lambda: self.delete_post(post, details_window))
        delete_button.pack(pady=10)

    # Close Button
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10)


    # def view_post_details(self, event):
    #     """ Show the full content of a clicked post """
    #     # Get the index of the clicked post
    #     index = self.post_listbox.curselection()
    #     if index:
    #         post = self.posts[index[0]]
            

    #         # Create a new window to display the post details
    #         details_window = tk.Toplevel(self.root)
    #         details_window.title("Post Details")
    #         details_window.geometry("600x600")

    #         # Display post title and content
    #         post_title = tk.Label(details_window, text=post['title'], font=("Arial", 16))
    #         post_title.pack(pady=10)

    #         post_content = tk.Label(details_window, text=post['content'], font=("Arial", 12), justify="left")
    #         post_content.pack(padx=20, pady=10)

    #         # Display Comments
    #         comments_frame = tk.Frame(details_window)
    #         comments_frame.pack(pady=10)

    #         comments_label = tk.Label(comments_frame, text="Comments:", font=("Arial", 14))
    #         comments_label.pack()

    #         for comment in post['comments']:
    #             comment_label = tk.Label(comments_frame, text=f"{comment['author']}: {comment['text']}", justify="left")
    #             comment_label.pack(anchor="w")

    #         # Add Comment Section
    #         comment_entry = tk.Entry(details_window, width=50)
    #         comment_entry.pack(pady=10)

    #         add_comment_button = tk.Button(details_window, text="Add Comment", 
    #                                        command=lambda: self.add_comment(post, comment_entry))
    #         add_comment_button.pack(pady=5)

    #         # Close Button
    #         close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
    #         close_button.pack(pady=10)


    def view_post_details(self, event):
        """ Show the full content of a clicked post """
        # Get the index of the clicked post
        index = self.post_listbox.curselection()  # Get the selected index
        if index:
        # Get the selected post from the list
            selected_post = self.posts[index[0]]
            self.show_post_details_window(selected_post)

    def edit_post(self, post, details_window):
    
    # Create a new window for editing
        edit_window = tk.Toplevel(details_window)
        edit_window.title("Edit Post")
        edit_window.geometry("600x600")

    # Add Title
        title_label = tk.Label(edit_window, text="Post Title:")
        title_label.pack()
        title_entry = tk.Entry(edit_window, width=50)
        title_entry.insert(tk.END, post['title'])
        title_entry.pack(pady=10)

    # Add Content
        content_label = tk.Label(edit_window, text="Content:")
        content_label.pack()
        content_entry = tk.Text(edit_window, width=50, height=10)
        content_entry.insert(tk.END, post['content'])
        content_entry.pack(pady=10)

    # Category Dropdown
        category_label = tk.Label(edit_window, text="Category:")
        category_label.pack(pady=5)
        category_var = tk.StringVar(edit_window)
        category_var.set(post.get('category', self.categories[0]))  # Default to first category if not set
        category_menu = tk.OptionMenu(edit_window, category_var, *self.categories)
        category_menu.pack(pady=5)

    # Tags Entry
        tags_label = tk.Label(edit_window, text="Tags (comma-separated):")
        tags_label.pack(pady=5)
        tags_entry = tk.Entry(edit_window, width=50)
        tags_entry.insert(tk.END, post.get('tags', ''))  # Default to empty if no tags
        tags_entry.pack(pady=5)

    # Save Button
        save_button = tk.Button(edit_window, text="Save Changes", command=lambda: self.save_edited_post(post, title_entry, content_entry, category_var, tags_entry, edit_window))
        save_button.pack(pady=10)


    def save_edited_post(self, post, title_entry, content_entry, category_var, tags_entry, edit_window):
        """ Save the changes made to the post """
        post['title'] = title_entry.get()
        post['content'] = content_entry.get("1.0", tk.END).strip()
        post['category'] = category_var.get()
        post['tags'] = tags_entry.get().strip()

        # Refresh the main window to show the updated post
        self.load_posts()

        # Close the edit window
        edit_window.destroy()

    def add_comment(self, post, comment_entry):
        """ Add a comment to a post """
        comment_text = comment_entry.get().strip()

        if not comment_text:
            messagebox.showwarning("Empty Comment", "Please enter a comment.")
            return

        # For simplicity, we'll add a default author
        comment = {
            'author': "Anonymous",  # You could add user authentication to get the author's name
            'text': comment_text
        }

        post['comments'].append(comment)

        # Reload the post details window to display the new comment
        comment_entry.delete(0, tk.END)
        self.view_post_details(None)

    def delete_post(self, post, details_window):
        """ Confirm and delete the post """
        confirm = messagebox.askyesno("Delete Post", "Are you sure you want to delete this post?")
        if confirm:
            self.posts.remove(post)
            self.load_posts()
            details_window.destroy()




# Running the application
root = tk.Tk()
app = BlogApp(root)
root.mainloop()


'''
 def view_post_details(self, event):
        """ Show the full content of a clicked post """
        # Get the index of the clicked post
        index = self.post_listbox.curselection()  # Get the selected index
        if index:
        # Get the selected post from the list
            selected_post = self.posts[index[0]]
            self.show_post_details_window(selected_post)

'''