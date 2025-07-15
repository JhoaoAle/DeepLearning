import os
import subprocess

# Set Kaggle config dir
os.environ["KAGGLE_CONFIG_DIR"] = "./.kaggle"

# Run download
subprocess.run([
    "kaggle",
    "datasets",
    "download",
    "-d", "oscarstep/dataset-lsc-modelo",
    "-p", "data/raw",
    "--unzip"
], check=True)