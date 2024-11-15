import asyncio
import os
from termcolor import colored as c

os.system("clear")

# MODIFY THE PATH HERE AS NECESSARY
path_to_local_project = "../main-project"

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

async def run_npm_install():

    print(c("Updates successfully pushed to Github. Now updating your prismjs library in your project.", "cyan"))
    os.chdir(path=path_to_local_project)
    os.system("rm -rf node_modules/prismjs")

    print(c('\nSuccessfully deleted the outdated prismjs library in your project!', 'green'))
    print(c('\nDownloading new prismjs library in your project. This will take about 20 seconds...', 'blue'))
    
    # rm -rf node_modules/prismjs
    # npm install git+https://github.com/username/vue-component-library.git
    process = await asyncio.create_subprocess_exec(
        "npm", "install", "git+https://github.com/MichaelT-178/component-library.git",
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )
    
    await process.wait()
    print(c('\n\nSuccessfully updated your "prismjs" library in your project!\n', 'green'))

async def main():
    stop_event = asyncio.Event()

    counting_task = asyncio.create_task(count_to_seventy(stop_event))

    await run_npm_install()

    stop_event.set()
    await counting_task

asyncio.run(main())