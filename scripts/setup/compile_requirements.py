#!/usr/bin/env python3

"""
Requirements compiler script.
This script helps manage project dependencies using pip-tools.
"""

import subprocess
import sys
from pathlib import Path

def compile_requirements():
    """Compile requirements.in to requirements.txt"""
    try:
        # Get the project root directory
        project_root = Path(__file__).parent.parent.parent
        
        # Compile requirements.in to requirements.txt
        subprocess.run([
            sys.executable, 
            "-m", 
            "piptools", 
            "compile",
            "--generate-hashes",
            "-o", 
            str(project_root / "requirements.txt"),
            str(project_root / "requirements.in")
        ], check=True)
        
        print("✅ Successfully compiled requirements")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error compiling requirements: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_requirements()
