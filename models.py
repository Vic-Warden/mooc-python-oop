class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"File attached: {self.name}")

class ImageFile(File):
    # Inherits everything from File
    pass

class Post:
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        print(f"[{self.time_posted}] {self.user}: {self.content}")

class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        super().display()
        self.file.display()

class Thread:
    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def add_post(self, post):
        self.posts.append(post)

    def display(self):
        for post in self.posts:
            post.display()
            print("")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Defines how the user is printed
    def __str__(self):
        return self.username

    def make_thread(self, title, content):
        post = Post(self, "Today", content)
        return Thread(title, "Today", post)

    def post(self, thread, content, file=None):
        if file:
            new_post = FilePost(self, "Today", content, file)
        else:
            new_post = Post(self, "Today", content)
        
        thread.add_post(new_post)
        return new_post

class Moderator(User):
    def delete(self, thread, post_to_delete):
        
        # Remove the post from the thread's list
        if post_to_delete in thread.posts:
            thread.posts.remove(post_to_delete)
            print(f"> System: Moderator deleted a post.\n")