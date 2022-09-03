import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['picosec to microsec', 'microsec to millisec', 'millisec to sec', 'sec to min', 'min to hr', 'hr to day(s)', 'day(s) to week(s)', 'week(s) to year(s)'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Time Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'picosec to microsec':
                    output = round(float(input_value) * 1000000, 2)
                    output_string = f'{input_value} picosecond(s) eqauals to {output} microsecond(s)'
                case 'microsec to millisec':
                    output = round(float(input_value) * 1000, 2)
                    output_string = f'{input_value} microsecond(s) eqauals to {output} millisecond(s)'
                case 'millisec to sec':
                    output = round(float(input_value) * 1000, 2)
                    output_string = f'{input_value} millisecond(s) eqauals to {output} second(s)'
                case 'sec to min':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} second(s) eqauals to {output} minute(s)'
                case 'min to hr':
                    output = round(float(input_value) * 60, 2)
                    output_string = f'{input_value} minute(s) eqauals to {output} hour(s)'
                case 'hr to day(s)':
                    output = round(float(input_value) * 24, 2)
                    output_string = f'{input_value} hour(s) eqauals to {output} day(s)'
                case 'day(s) to week(s)':
                    output = round(float(input_value) * 7, 2)
                    output_string = f'{input_value} day(s) eqauals to {output} week(s)'
                case 'week(s) to year(s)':
                    output = round(float(input_value) * 52, 2)
                    output_string = f'{input_value} week(s) eqauals to {output} year(s)'
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')
    
window.close()