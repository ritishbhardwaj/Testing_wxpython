from pywinauto import Desktop

# Find the Microsoft Edge window
edge_window = Desktop(backend="uia").window(title_re=".*Microsoft Edge.*")

# Get the title of the dialog box
dialog_title = edge_window.child_window(control_type="Window").window_text()

print("Dialog box title:", dialog_title)