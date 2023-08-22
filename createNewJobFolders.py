import os
import sys
import yaml
import re
from GUI import window  # Importing previously written PyQt GUI function

def prompt_user(job_number_input, part_number, project_name, part_name, folder_type):
    if not (job_number_input and part_number and project_name and part_name):
        # Error functionality has been moved to the GUI, so no need to replicate it here.
        return

    if folder_type == "New Job":
        create_folder_structure(
            folder_structure, folder_location, job_number_input, part_number, project_name, part_name)
    elif folder_type == "New Part":
        create_folder_structure(
            folder_structure[0]["000_ProjectName"][1:], folder_location, job_number_input, part_number, project_name, part_name)


def create_folder_structure(structure, parent, job_number_input, part_number, project_name, part_name):
    for item in structure:
        if isinstance(item, dict):
            for key, value in item.items():
                folder_name = (
                    key.replace("000", f"{int(job_number_input):03d}")
                    .replace("01", f"{int(part_number):02d}")
                    .replace("ProjectName", project_name)
                    .replace("partName", part_name)
                )
                folder_path = os.path.join(parent, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)

                if isinstance(value, list):
                    create_folder_structure(value, folder_path, str(
                        job_number_input), part_number, project_name, part_name)
    print(f"Destination directory: {parent}")


def get_next_job_and_part_number(folder_type="New Job"):
    """Returns the next job and part number based on the job and part numbers already existing in the destination
    folder."""
    # Get current folder location
    job_numbers = [0]
    part_numbers = [1]
    highest_job_number = 0
    for folder in os.listdir(folder_location):
        match = re.match(r'(\d{3})-(\d{2})_.*', folder)
        if match:
            job_number = int(match.group(1))
            part_number = int(match.group(2))

            if job_number == highest_job_number and folder_type == "New Part":
               part_numbers.append(part_number + 1)

            if job_number >= highest_job_number:
               highest_job_number = job_number
               job_numbers.append(job_number)
    
    job_number = f"{max(job_numbers, default=0):03d}"
    part_number = f"{max(part_numbers, default=1):02d}" if folder_type == "New Part" else f"{1:02d}"
    return job_number, part_number

# Note the location of the yaml file
script_dir = os.path.dirname(os.path.abspath(__file__))
yaml_file_path = os.path.join(script_dir, 'config.yaml')

# Open and read the yaml file
with open(yaml_file_path, 'r') as f:
    folder_structure = yaml.load(f, Loader=yaml.FullLoader)

# Locations to create folders
folder_location = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

# Get existing jobs and parts
job_no, part_no = get_next_job_and_part_number()

# Create and display the GUI
window(prompt_user, job_no, part_no, "Job Name", "Part Name")