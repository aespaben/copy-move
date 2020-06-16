def recursive_search(path, ext = [], _elements = []):
  from pathlib import Path

  ext = [x.lower() for x in ext]

  try:
    for e in Path(path).iterdir():
      if e.is_dir():
        recursive_search(e, ext, _elements)
      elif e.is_file():
        if len(ext):
          if e.name.split('.')[-1].lower() in ext:
            _elements.append(e)
        else:
          _elements.append(e)
  except FileNotFoundError:
    print('La ruta especificada no existe')
  
  return _elements


def separate_duplicates(original_files):
  bag = set()
  duplicated = []

  files = original_files.copy()
  for file in files:
    if file.name in bag:
      files.remove(file)
      duplicated.append(file)
    else:
      bag.add(file.name)

  return files, duplicated


def auto_rename_and_apply(original_files, dst, op):
  from pathlib import Path

  files = original_files.copy()
  renamed_files = []
  new_file_name = ''

  for file in enumerate(files):
    new_file_name = f'{file[0]} {file[1].name}'
    renamed_files.append(Path.joinpath(Path(dst), Path(new_file_name)))

  try:
    for file in enumerate(files):
      op(file[1], renamed_files[file[0]])

  except:
    print('Error')
    return False

  return True


def copy_to(file, dst):
  from shutil import copy
  from pathlib import Path

  try:
    print(f'Copiando {file.name}...', end=' ')
    copy(file, Path(dst))
    print('Archivo copiado.')
  except:
    print(f'Error al copiar el archivo {file} al directorio {dst.name}')
    return False

  return True

def move_to(file, dst):
  from pathlib import Path
  from os import rename

  try:
    print(f'Moviendo {file.name}...', end=' ')
    rename(file, Path(dst))
    print('Archivo movido.')
  except:
    print(f'Error moviendo el archivo {file} al directorio {dst.name}')
    return False
  
  return True

def apply_all(files, dst, op):
  from os import listdir
  
  if len(listdir(dst)):
    print('El destino debe estar vacío')
    return False

  for file in files:
    op(file, dst)

  return True