import subprocess

def list_installed_packages(output_file):
    # Subprocess ke zariye pip freeze command chalana
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)

    # Packages ka result ko file main likhna (file automatically banegi agar exist nahi karti)
    with open(output_file, 'a') as f:
        f.write(result.stdout)

    print(f"Installed packages list has been written to {output_file}")

# Function ko call karna aur output file(requirment.txt) ka naam specify karna
list_installed_packages('requirements.txt')

# ////////////////////////////////////////////////////////////////////////////////

# def install_package(package_name):
#     # Subprocess ke zariye pip install command chalana
#     result = subprocess.run(['pip', 'install', package_name], capture_output=True, text=True)

#     print(result.stdout)

# # Function ko call karna aur package name specify karna
# install_package('requests')
