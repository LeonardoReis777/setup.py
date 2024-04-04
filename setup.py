import sys
from cx_Freeze import setup, Executable

# Arquivo principal Python que deseja converter em executável
main_script = 'filename.py'

# Configuração do executável
executables = [Executable(main_script)]

# Configurações adicionais do setup
build_exe_options = {'packages': [], 'excludes': []}

# Configuração do setup
setup(name='NomeDoSeuExecutavel',
      version='1.0',
      description='Descrição do seu executável',
      options={'build_exe': build_exe_options},
      executables=executables)
