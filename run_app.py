import os
import subprocess
import sys

if __name__ == "__main__":
    # 1. Ruta del script del dashboard
    script_path = os.path.join(os.path.dirname(__file__), "HugginfaceSpotify.py")
    
    # 2. Localizar el ejecutable de streamlit dentro del .venv
    # En Debian, está en .venv/bin/streamlit
    venv_streamlit = os.path.join(os.path.dirname(__file__), ".venv", "bin", "streamlit")
    
    if os.path.exists(venv_streamlit):
        cmd = [venv_streamlit, "run", script_path]
    else:
        # Si no hay venv, intenta usar el comando global (fallará en Debian si no está instalado)
        cmd = ["streamlit", "run", script_path]
    
    print(f"Iniciando Dashboard con: {cmd[0]}")
    subprocess.run(cmd)