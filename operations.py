from pathlib import Path
from shutil import copy
from os import rename, listdir

#############################################
# Busca archivos extensiones específicas 
# recursivamente dentro de un directorio y 
# sus subcarpetas.
#############################################
def recursive_search(path, ext = [], _elements = []):
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

#############################################
# Recibe una lista de archivos y devuelve
# una tupla con los archivos únicos
# y los archivos duplicados.
#############################################
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

#############################################
# Recibe una lista de archivos, los renombra
# automáticamente y les aplica una operación
# al destino especificado.
#############################################
def auto_rename_and_apply(original_files, dst, op):
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

#############################################
# Copia un archivo al destino especificado.
#############################################
def copy_to(file, dst):
  try:
    print(f'Copiando {file.name}...', end=' ')
    copy(file, Path(dst))
    print('Archivo copiado.')
  except:
    print(f'Error al copiar el archivo {file} al directorio {dst.name}')
    return False

  return True

#############################################
# Mueve un archivo al destino especificado.
#############################################
def move_to(file, dst):
  try:
    print(f'Moviendo {file.name}...', end=' ')
    rename(file, Path(dst))
    print('Archivo movido.')
  except:
    print(f'Error moviendo el archivo {file} al directorio {dst.name}')
    return False
  
  return True

#############################################
# Aplica una operación a todos los archivos
# de una lista.
#############################################
def apply_all(files, dst, op):
  if len(listdir(dst)):
    print('El destino debe estar vacío')
    return False

  for file in files:
    op(file, dst)

  return True