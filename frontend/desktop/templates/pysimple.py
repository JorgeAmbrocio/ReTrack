import PySimpleGUI as sg

# create layout
layout = [
    [sg.Text('Hello World')],
    [sg.Button('Ok')]
]

# create window
window = sg.Window('Window Title', layout)

# event loop
while True:
    event, values = window.read()
    if event == 'Ok' or event == sg.WIN_CLOSED:
        break