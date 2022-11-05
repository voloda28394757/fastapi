from fastapi import FastAPI


app=FastAPI()


@app.get("/")
async def main():
    return {"msg":111}


@app.get("/user/{userid}")
async def main(userid):
    return {"msg":userid}