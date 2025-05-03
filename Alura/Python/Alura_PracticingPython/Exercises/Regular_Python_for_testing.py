import asyncio

files = {
    "document_01.pdf":12,
    "document_02.pdf":80,
    "document_03.pdf":35,
    "document_04.pdf":42,
    "document_05.pdf":31,
}

badnwidth = 42

async def start_download(name, size):
    print(f"Starting download of file: {name} (Size: {size}MB)...")
    download_progress = 0
    s = 0
    while download_progress < size:
        await asyncio.sleep(1)
        s += 1
        download_progress += (badnwidth / (len(asyncio.all_tasks()) - 1)) ## Minus 1 for the main() function which is running
        download_progress = min(size, download_progress)
        print(f"[{s}s]{name}: {download_progress}MB downloaded. {(download_progress/size)*100:.2f}%")
    print(f"{name} finished donwloading!")
    
async def main():
    print("Startin downloads...\n")
    tasks = [asyncio.create_task(start_download(name, size)) for name, size in files.items()]
    await asyncio.gather(*tasks)
    print("\nAll downloads concluded.")
    
asyncio.run(main())
