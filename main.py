from fastapi import FastAPI,Path
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, PlainTextResponse
from fastapi import Response


app=FastAPI()


@app.get("/")
async def main():
    return {"msg":111}


@app.get("/add")
async def main():
    return JSONResponse({"msg":111})

@app.get("/f", response_class=JSONResponse)
async def main():
    return {"msg":111}

@app.get("/a")
async def main():
    return HTMLResponse("<h1>перивет</h1>")

@app.get("/b")
async def main():
    return PlainTextResponse("<h1>перивет</h1>")

@app.get("/test")
async def main():
    return FileResponse("public/index.html")

@app.get("/h")
async def main():
    return FileResponse("public/index.html",
                        filename="file.html",
                        media_type="application/octet-stream")

@app.get("/number/{phone}")
async def main(phone:str=Path(regex="^\d{11}$")):
    return {"phone":phone}

@app.get("/user/{userid}/{age}")
async def main(userid:str=Path(min_length=3,max_length=10),
                age:int=Path(ge=1, lt=100)):
    return {"msg":userid, "age":age}
