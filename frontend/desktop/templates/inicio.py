import PySimpleGUI as sg

# layout to header and body
header = [
    [sg.Text('Camera', size=(10, 1), justification='center', font='Helvetica 20')],
]

# layout to show camera video
video = [
    [sg.Image(filename='', key='-IMAGE-')],
]

# layout to buttons
buttons = [
    [
        sg.Button('Start', size=(10, 1), font='Helvetica 14'),
        sg.Button('Stop', size=(10, 1), font='Helvetica 14'),
        sg.Button('Exit', size=(10, 1), font='Helvetica 14')
    ],
]

# layout to show fps
fps = [
    [sg.Text('FPS: ', size=(10, 1), justification='center', font='Helvetica 14', key='-FPS-')],   
]

# create window
window = sg.Window('Camera', header + video + buttons + fps, location=(800, 400))

# event loop
while True:
    event, values = window.read(timeout=20)
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == 'Start':
        pass

    if event == 'Stop':
        pass