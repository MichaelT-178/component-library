import asyncio
import os
from termcolor import colored as c

os.system("clear")

# MODIFY THE PATHS HERE AS NECESSARY
paths_to_local_projects = [
    "../main-project"
]

async def count_to_seventy(stop_event: asyncio.Event):
    i = 1
    while not stop_event.is_set():
        print(i, end=" ", flush=True)
        i += 1

        if i % 11 == 0:
            print()

        await asyncio.sleep(1)

        if i > 100:  # Prevent it from counting indefinitely
            break

async def run_npm_install(path_to_project):
    print(c(f"\nUpdating project at '{path_to_project}'", "cyan"))

    os.chdir(path=path_to_project)
    print(c("Deleting outdated prismjs library...", "yellow"))
    os.system("rm -rf node_modules/prismjs")

    print(c('Successfully deleted the outdated prismjs library!', 'green'))
    print(c('\n\nDownloading new prismjs library. This will take about 20 seconds...', 'blue'))

    process = await asyncio.create_subprocess_exec(
        "npm", "install", "git+https://github.com/MichaelT-178/component-library.git",
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )

    await process.wait()
    print(c('\nSuccessfully updated the "prismjs" library in the project!\n', 'green'))

async def main():
    stop_event = asyncio.Event()

    counting_task = asyncio.create_task(count_to_seventy(stop_event))

    for path in paths_to_local_projects:
        try:
            await run_npm_install(path)
        except Exception as e:
            print(c(f"Error updating project at {path}: {str(e)}", "red"))

    stop_event.set()
    await counting_task

asyncio.run(main())
