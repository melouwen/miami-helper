from aiohttp import web
import threading

async def handle(request):
    return web.Response(text="I'm alive")

def run():
    app = web.Application()
    app.router.add_get("/", handle)
    web.run_app(app, host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
