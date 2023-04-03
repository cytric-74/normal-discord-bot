import Estrapy
import asyncio


async def function():
    run = await Estrapy.Sfw.run()
    hug = await Estrapy.Sfw.hug()

    print(f"A Running GIF: {run.url}")
    print(f"A Hug GIF: {hug.url}")


asyncio.run(function())
