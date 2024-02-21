import yaml
import os
from sys import platform

TODO_FILE = "../../materials/todo.yml"
DEST = "."
HOST = "localhost"

ansible_dict = []


def generate_host(host_name):
    temp_dict = {
        "name": host_name,
        "hosts": HOST,
        "tasks": [],
    }
    ansible_dict.append(temp_dict)


def task_copy(file):
    temp_dict = {
        "name": "Copy " + file.split('/')[-1],
        "copy": {
            "src": file,
            "dest": DEST,
        }
    }
    return temp_dict


def task_command(command):
    temp_dict = {
        "name": "Run " + command,
        "command": command
    }
    return temp_dict


def install(package: list):
    if platform == "darwin":
        installer = "homebrew"
    else:
        installer = "apt"
    temp_dict = {
        "name": "Install " + " ".join(package),
        installer: {
            "name": package
        }
    }
    return temp_dict


def find_files_dir(just_files):
    files = []
    for file in just_files:
        f = []
        layer = 1
        w = os.walk("../")
        for (dripath, dirnames, filenames) in w:
            if file in filenames:
                files.append(f"{dripath}/{file}")
            if layer == 5:
                f.extend(dirnames)
                break
            layer += 1
    return files


def main():
    with open(TODO_FILE, 'r') as file:
        todo_data = yaml.safe_load(file)
    files = find_files_dir(todo_data['server']["exploit_files"])
    install_packages = todo_data['server']["install_packages"]
    commands = []
    for file in todo_data['server']["exploit_files"]:
        if file == "consumer.py":
            commands.append(
                f"python3 {file} -e {','.join(todo_data['bad_guys'])}")
        else:
            commands.append(f"python3 {file}")

    host_name = "Main Host"
    generate_host(host_name)
    ansible_dict[-1]['tasks'].append(install(install_packages))
    for file in files:
        ansible_dict[-1]['tasks'].append(task_copy(file))
    for command in commands:
        ansible_dict[-1]['tasks'].append(task_command(command))
    with open('deploy.yml', 'w') as file:
        yaml.dump(ansible_dict, file, default_flow_style=False, )


if __name__ == "__main__":
    main()
