import os
import pyautogui
from termcolor import colored as c
import time

def update_index_js_file():
    """
    Update the src/index.js to export all the components.
    """

    directory = "src/components"

    component_names = [
        os.path.splitext(f)[0] # splitext splits into file name and extension
        for f in os.listdir(directory)
        if f.endswith(".vue") and os.path.isfile(os.path.join(directory, f))
    ]

    imports = "\n".join([f"import {name} from './components/{name}.vue';" for name in component_names])
    exports = ",\n  ".join(component_names)

    file_content = f"{imports}\n\nexport {{\n  {exports}\n}};\n"

    with open('src/index.js', 'w') as file:
        file.write(file_content)

    print(c("The 'src/index.js' file has been updated successfully!\n", 'green'))
    

def save_all_changes_in_files():
    """
    Saves all changed unsaved files in folder.
    command + option + s
    """
    pyautogui.keyDown('command')
    pyautogui.keyDown('option')
    pyautogui.press('s')
    pyautogui.keyUp('option')
    pyautogui.keyUp('command')

    print(c("All files with changes saved successfully!\n", 'green'))


update_index_js_file()
save_all_changes_in_files()


os.system('npx rollup -c')


os.system('git add .')

print(c('\n\n✅ git add completed successfully', 'green'))


message = input(c("\nWhat's your commit message? : ", 'cyan'))

os.system(f'git commit -m "{message.strip()}"')

print(c('✅ git commit completed successfully\n', 'green'))



os.system('git push')

print(c('✅ git push completed successfully', 'green'))

time.sleep(1.5)

os.system('python3 automate_project_update.py')