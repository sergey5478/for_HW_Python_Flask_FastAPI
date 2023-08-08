import asyncio
import os
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import aiohttp
import aiofiles


async def download_image(session, url, output_folder):
    """Записывает 1 картинку."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                filename = os.path.basename(url)
                output_path = os.path.join(output_folder, filename)
                os.makedirs(output_folder, exist_ok=True)
                start_time1 = time.time()
                async with aiofiles.open(output_path, 'wb') as f:
                    await f.write(content)
                end_time1 = time.time()
                total_time1 = end_time1 - start_time1
                print(f"Image {filename} downloaded successfully. Time: {total_time1:.3f}")
            else:
                print(f"Failed to download image from {url}")
    except Exception as epr_1:
        print(f"An error occurred while downloading image from {url}: {epr_1}")


async def download_images_async(urls, output_folder):
    """Работаем с асинхронным подходом."""
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, output_folder) for url in urls]
        await asyncio.gather(*tasks)


def download_images_thread(urls, output_folder):
    """Работаем с потоками."""
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_images_async(urls, output_folder))


def download_images_process(urls, output_folder):
    """Работаем с процессами."""
    with ProcessPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_images_async(urls, output_folder))


def main():
    """Парсит командную строку и запускает три подхода"""
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs='+')
    parser.add_argument("--output_folder", default="images")
    args = parser.parse_args()

    start_time = time.time()

    download_images_thread(args.urls, args.output_folder)

    download_images_process(args.urls, args.output_folder)

    asyncio.run(download_images_async(args.urls, args.output_folder))

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
