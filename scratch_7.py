import PySimpleGUI as sg

#Defines theme
sg.theme('DarkAmber')

#Using list comprehension, we create a 10x10 grid and the key of the button is (x,y) (their coordinate)
layout = [

    [sg.Button(key=(x,y) , size=(4,2)) for x in range(10)] for y in range(10)

]

###Standard code####
window = sg.Window('Final', layout)

while True:

    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break
###Standard code####

    click = window[event]

    square = click.get_text()

    if click and square == '':
        window[event].update('black', button_color='black')

    elif click and square == 'black':
        window[event].update('', button_color='yellow')

window.close()