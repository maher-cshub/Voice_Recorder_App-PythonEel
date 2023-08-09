import eel

# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def Record(name):
    print(name)
    return f"recorded as {name}"

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))