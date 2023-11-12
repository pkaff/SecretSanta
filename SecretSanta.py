import random
names = ['Daniel', 'Maria', 'Martin', 'Kristina', 'Isabella', 'Ingemar']
random.shuffle(names)
santa_assignments = list(zip(names, names[1:] + names[:1]))
for name_from, name_to in santa_assignments:
    file = open(name_from + ".txt", encoding='iso-8859-1', mode='w+')
    instructions = f'''Hej {name_from}!

I Secret Santa kommer varje person att bli tilldelad en person att ge en julklapp till.
Alla ger således julklapp till 1 person och får julklapp från 1 person.
Du kommer att känna till vem du ska ge en julklapp till, men det är hemligt vem du kommer att få en julklapp av.
Du köper en (eller flera) julklappar, för en summa som vi gemensamt kommer överens om senare på messenger, som delas ut den 23e december.
Avsändaren ska vara hemlig! Man kan t.ex. skriva God Jul ... önskar din Secret Santa.
Efter utdelningen kan man försöka gissa vem som varit ens Secret Santa baserat på gåvorna.

OBS HÅLLS HEMLIGT: Du ska ge julklapp till {name_to}!
'''
    print(instructions)

    file.write(instructions)
    file.close()
