#Student Showcase 2026
# Glee Club Checker
from pyscript import display, document


def view_member(e):
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last)

    Glee_members = ['Jalainie Abdullah', 'Clara Sabanal', 'Alexa Salcedo', 'Rafael Magdayao', 'Julianne Canuday', 'Theos Tomas', 'Amanda Bower',]
    member_checker = student_name in Glee_members # checks boolean 0 or 1

    display_message = (f'Sorry, you are not included in Glee club', f'Congratulations {student_name}, you are part of Glee club')
    display(display_message[member_checker], target='result') 

Teacher = {'Em Teola'}
G10 = {'Niqa Agasi', 'Al-Makram Arbison','Alyanna Barlisan', 'Amanda Bower', 'Julianne Canuday', 'Lara Estrada', 'Samantha Jose', 'Rafael Magdayao'}
G11 = {'Jalainie Abdullah', 'Sang-heon Choi', 'Skyler Escobar', 'Charlize Galang', 'Carl Rufo',}
G12= {'Areef Batara', 'Areef Hadjisalic', 'Alexander Holgado', 'Clara Sabanal', 'Alexa Salcedo'}

Glee_Complete = G10 | G11 | G12 | Teacher #Union

def add_member(e):
    document.getElementById('results').innerHTML = ' '
    student_first = document.getElementById('first_name').value
    student_last = document.getElementById('last_name').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values


    Glee_Complete.add(student_name)

    display(f'Here is a list of All the members: {Glee_Complete}', target='results')

    display(f'There are {len(Glee_Complete)} Members Total', target='results')

def check_element(e):
    document.getElementById('result').innerHTML = ' '
    element = document.getElementById('symbol').value.strip().capitalize()
    #Elements:
    Element_list = {
        'H': {
            'Symbol': 'H',
            'Element': 'Hydrogen',
            'Atomic Number': '1',
            'Atomic Mass': '1.00784'
        },
        'He': {
            'Symbol': 'He',
            'Element': 'Helium',
            'Atomic Number': '2',
            'Atomic Mass': '4.0026'
        },
         'C': {
            'Symbol': 'C',
            'Element': 'Carbon',
            'Atomic Number': '6',
            'Atomic Mass': '12'
        },
         'N': {
            'Symbol': 'N',
            'Element': 'Nitrogen',
            'Atomic Number': '7',
            'Atomic Mass': '14'
        },
         'O': {
            'Symbol': 'O',
            'Element': 'Oxygen',
            'Atomic Number': '8',
            'Atomic Mass': '16'
        },
         'F': {
            'Symbol': 'F',
            'Element': 'Fluorine',
            'Atomic Number': '9',
            'Atomic Mass': '18.998'
        },
         'P': {
            'Symbol': 'P',
            'Element': 'Phosphorus',
            'Atomic Number': '15',
            'Atomic Mass': '30'
        },
         'S': {
            'Symbol': 'S',
            'Element': 'Sulfur',
            'Atomic Number': '16',
            'Atomic Mass': '32'
        },
         'Cl': {
            'Symbol': 'Cl',
            'Element': 'Chlorine',
            'Atomic Number': '17',
            'Atomic Mass': '35'
        },
         'Se': {
            'Symbol': 'Se',
            'Element': 'Selenium',
            'Atomic Number': '34',
            'Atomic Mass': '78.960'
        },
         'Br': {
            'Symbol': 'Br',
            'Element': 'Bromine',
            'Atomic Number': '35',
            'Atomic Mass': '79.904'
        },
         'I': {
            'Symbol': 'I',
            'Element': 'Iodine',
            'Atomic Number': '53',
            'Atomic Mass': '126.90'
        },
         'Ne': {
            'Symbol': 'Ne',
            'Element': 'Neon',
            'Atomic Number': '10',
            'Atomic Mass': '20.180'
        },
         'Ar': {
            'Symbol': 'Ar',
            'Element': 'Argon',
            'Atomic Number': '18',
            'Atomic Mass': '39.148'
        },
         'Kr': {
            'Symbol': 'Kr',
            'Element': 'Krypton',
            'Atomic Number': '36',
            'Atomic Mass': '83.798'
        },
         'Xe': {
            'Symbol': 'Xe',
            'Element': 'Xenon',
            'Atomic Number': '54',
            'Atomic Mass': '131.29'
        },
         'Rn': {
            'Symbol': 'Rn',
            'Element': 'Radon',
            'Atomic Number': '86',
            'Atomic Mass': '222'
        }   
    }
    checkE = element in Element_list


    display_message = (f'Element not found', f"{Element_list.get(element, [])}")
    display(display_message[checkE], target='result')