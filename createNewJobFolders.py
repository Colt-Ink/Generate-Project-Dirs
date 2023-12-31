#!/usr/bin/env python3

import os
import sys
import yaml
import re
from string import Template

from GUI import window  # Importing previously written PyQt GUI function


def prompt_user(job_number_input: int, part_number: int, project_name: str, part_name: str, folder_type: str):
    if not (job_number_input and part_number and project_name and part_name):
        # Error functionality has been moved to the GUI, so no need to replicate it here.
        return

    if folder_type == "New Job":
        create_folder_structure(
            folder_structure, folder_location, job_number_input, part_number, project_name, part_name)
    elif folder_type == "New Part":
        create_folder_structure(
            folder_structure[0]["${jobNum}_${projectName}"][1:], folder_location, job_number_input, part_number, project_name, part_name)


def create_folder_structure(structure, parent, job_number_input: int, part_number: int, project_name, part_name):
    for item in structure:
        if isinstance(item, dict):
            for key, value in item.items():
                t = Template(key)
                folder_name = t.substitute(jobNum=f"{int(job_number_input):03d}",
                                           projectName=project_name,
                                           partNum=f"{int(part_number):02d}",
                                           partName=part_name)
                folder_path = os.path.join(parent, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)

                if isinstance(value, list):
                    create_folder_structure(value, folder_path, job_number_input, part_number, project_name, part_name)
    print(f"Destination directory: {parent}")


def get_next_job_and_part_number(folder_type="New Part") -> tuple[str, str, str]:
    job_numbers = []
    part_numbers = []
    job_name = ""
    highest_job_number = 0
    for folder in os.listdir(folder_location):
        match = re.match(r'(\d{3})-(\d{2})_(\w+)_.*', folder)
        if match:
            job_number = int(match.group(1))
            part_number = int(match.group(2))
            job_name = str(match.group(3))

            if job_number > highest_job_number:
                highest_job_number = job_number
                job_numbers.append(job_number)
                part_numbers = [part_number]  # Reset part_numbers list
            elif job_number == highest_job_number:
                part_numbers.append(part_number)

    if folder_type == "New Job":
        job_number = f"{max(job_numbers, default=0) + 1:03d}"
        part_number = f"{1:02d}"
    else:  # "New Part"
        job_number = f"{max(job_numbers, default=0):03d}"
        part_number = f"{max(part_numbers, default=1) + 1:02d}"
    return job_number, part_number, job_name


if __name__ == '__main__':
    # Note the location of the yaml file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, 'config.yaml')

    # Open and read the yaml file
    with open(yaml_file_path, 'r') as f:
        folder_structure = yaml.load(f, Loader=yaml.FullLoader)

    # Locations to create folders
    folder_location = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()

    # Get existing jobs and parts
    job_no, part_no, job_name = get_next_job_and_part_number()
    if job_name == '':
        job_name = 'Job Name'

    # Create and display the GUI
    window(prompt_user, get_next_job_and_part_number, job_no, part_no, job_name, "Part Name")