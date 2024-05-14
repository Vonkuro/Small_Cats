from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
#better
app = FastAPI()

@app.get("/http-cat/{status_code}")
async def redirect_to_http_cat(status_code: int):
    # List of valid HTTP status codes
    valid_status_codes = [
        100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405,
        406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431, 444,
        450, 451, 497, 498, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 511, 521, 522, 523, 525, 599
    ]

    if status_code not in valid_status_codes:
        raise HTTPException(status_code=400, detail="Invalid status code")

    url = f"https://http.cat/{status_code}"
    return RedirectResponse(url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
