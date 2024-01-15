import os.path, time

file = 'README.md'

print("Modified :", time.ctime(os.path.getmtime(file)))
print("Created :", time.ctime(os.path.getctime(file)))