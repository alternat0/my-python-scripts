# dictionary (maps): values with unique keys
# tidak bisa di-join
# dictionary dalam python: unordered
# perubahan di git bash(penambahan command)

daftar_superhero = {'Barol': 'Johanes Pinatiti', 'Superman': 'Clark Kent', 'Batman': 'Bruce Wayne'}
print(daftar_superhero)

daftar_superhero['Spiderman'] = 'Peter Parker'
print(daftar_superhero)

print(daftar_superhero['Superman'])

daftar_superhero['Barol'] = 'Johanes'
print(daftar_superhero)

del daftar_superhero['Barol']
print(daftar_superhero)

print(len(daftar_superhero))
print(daftar_superhero.get('Batman'))
print(daftar_superhero.keys())
print(daftar_superhero.values())

