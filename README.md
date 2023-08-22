1. **Install Python:** Download and install Python from https://www.python.org/. During installation, ensure that Python is added to your environment variables (there should be a checkbox option for this during the installation process).

2. **Set up your Python environment:** It's generally a best practice to create and use a virtual environment for your project to avoid any possible dependency conflicts. Here is how you can set it up:

  - Open command prompt and change directory to your project folder:

    ```bash
    cd path/to/your/project-dir
    ```

  - Create a new virtual environment:

    ```bash
    python -m venv env
    ```

  - Activate the environment:

    ```bash
    env\Scripts\activate
    ```

3. **Install Required Libraries:** Use the requirements file you created to install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script:** After the environment set up, you can run your python script:

    ```bash
    python createNewJobFolder.py
    ```
   
   The PyQt GUI should show up and you can interact with the program.

5. **Set up the Context Menu (Optional):** If you want to run this script from the Windows Context Menu, follow the instructions mentioned in the previous responses to create a `.bat` file and add a new key to the Windows Registry. Note: This requires Administrator privileges on your machine and any misuse of the Windows Registry can cause system instability. Please follow the instructions carefully.