# Import the classes from our models.py file
from models import User, Moderator, ImageFile

# Create users
alice = User("Alice", "pass123")
mod = Moderator("AdminBob", "adminpass")

# User creates a thread
thread = alice.make_thread("My cake recipe", "Here is how to make a cake.")

# Moderator replies
mod.post(thread, "Great recipe, thanks for sharing!")

# User replies off-topic (we save it in a variable to delete it later)
bad_post = alice.post(thread, "Do you like my new shoes?")

# Moderator deletes the off-topic message
mod.delete(thread, bad_post)

# User replies with an attached image
my_image = ImageFile("cake.jpg", "2MB")
alice.post(thread, "Here is a photo!", file=my_image)

# Display the final state of the thread
thread.display()