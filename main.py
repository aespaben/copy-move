from operations import apply_all, auto_rename_and_apply, copy_to, move_to, recursive_search, separate_duplicates

def action(act, op):
  word = ''
  if act == 'copy':
    word = 'copiar'
  elif act == 'move':
    word = 'mover'

  src = input('\nIngrese la dirección del directorio donde desea buscar\n:').strip(r'\'|"')

  ext = input(f'\nIngrese las extensiones de archivo (sin el punto) que desea {word} separadas por un espacio\n:').split()

  dst = input(f'\nIngrese la dirección del directorio de destino donde desea {word} los archivos (debe estar vacío)\n:').strip(r'\'|"')

  all_files = recursive_search(src, ext)
  uniques, duplicates = separate_duplicates(all_files)

  print('\nSe encontraron los siguientes archivos:\n')
  for file in uniques:
    print(f'\nDIRECTORIO: {file.parent}')
    print(f'ARCHIVO: {file.name}')

  if len(duplicates):
    print('\n\nAdicionalmente se encontraron los siguientes archivos duplicados:')

    for file in duplicates:
      print(f'\nDIRECTORIO: {file.parent}')
      print(f'ARCHIVO: {file.name}')

  if input(f'\n\n¿Seguro que desea {word} los archivos al directorio {dst}? Se renombraran automáticamente los duplicados.\n(s | n):').lower() == 's':
    apply_all(uniques, dst, op)
    auto_rename_and_apply(duplicates, dst, op)
  else:
    print('Operación cancelada')

def main():
  print('::: Copy/Move :::')
  print('Programa que copia o mueve archivos con extensión específica a una nueva localidad (resursivo)')
  print('¿Qué desea hacer?')
  while True:
    option = input('\n\n1 - Copiar archivos.\n2 - Mover archivos.\n0 - Salir\n:')
    if option == '1':
      action('copy', copy_to)
      
    elif option == '2':
      action('move', move_to)

    elif option == '0':
      break


if __name__ == '__main__':
  main()