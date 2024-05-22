import os

def list_notes():
  # Get all files in the notes directory with .md extension
  notes_dir = "notes"
  notes = [f[:-3] for f in os.listdir(notes_dir) if f.endswith(".md")]
  if notes:
    print("Available Notes:")
    for note in notes:
      print(f"- {note}")
  else:
    print("No notes found.")

def create_note(title):
  # Create a new Markdown file with the title in the notes directory
  notes_dir = "notes"
  filename = f"{title}.md"
  filepath = os.path.join(notes_dir, filename)
  with open(filepath, "w") as f:
    f.write(f"# {title}\n")  # Add title as heading in the note
  # Open the new file in the default text editor
  os.system(f"open {filepath}")  # Replace with appropriate command for your OS

def open_note(title):
  # Open the specified note file in the default text editor
  notes_dir = "notes"
  filename = f"{title}.md"
  filepath = os.path.join(notes_dir, filename)
  if os.path.exists(filepath):
    os.system(f"open {filepath}")  # Replace with appropriate command for your OS
  else:
    print(f"Note '{title}' not found.")

def delete_note(title):
  # Delete the specified note file after confirmation
  notes_dir = "notes"
  filename = f"{title}.md"
  filepath = os.path.join(notes_dir, filename)
  if os.path.exists(filepath):
    confirmation = input(f"Are you sure you want to delete '{title}'? (y/n): ").lower()
    if confirmation == 'y':
      os.remove(filepath)
      print(f"Note '{title}' deleted.")
  else:
    print(f"Note '{title}' not found.")

def main():
  while True:
    print("\nMarkdown Note Taking App")
    print("1. Create New Note")
    print("2. List Notes")
    print("3. Open Note")
    print("4. Delete Note")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
      title = input("Enter title for your new note: ")
      create_note(title)
    elif choice == '2':
      list_notes()
    elif choice == '3':
      title = input("Enter title of the note to open: ")
      open_note(title)
    elif choice == '4':
      title = input("Enter title of the note to delete: ")
      delete_
