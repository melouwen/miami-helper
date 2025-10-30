from aiohttp import web
import asyncio

async def handle(request):
    return web.Response(text="I'm alive")

async def run():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=8080)
    await site.start()
    print("✅ Keep-alive server started on port 8080")

def keep_alive():
    loop = asyncio.get_event_loop()
    loop.create_task(run())
