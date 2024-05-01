import sys
from cx_Freeze import setup, Executable

# Dependências necessárias para o seu código
build_exe_options = {
    "packages": ["pygame", "arrow"],
    "include_files": ["input.data", "figuras/"],
    "excludes": [],
    "include_msvcr": True  # Inclui o MSVC runtime (Windows)
}

# Configuração do executável
exe = [Executable(script="main.py", base=None)]

setup(
    name="simulador_corpos_celestes",
    version="1.0.0",
    description="Simulador de corpos celestes",
    options={"build_exe": build_exe_options},
    executables=exe
)
