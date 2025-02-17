from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.responses import HTMLResponse

app = FastAPI()

# json类型
# @app.get("/items/", response_class=ORJSONResponse)
# async def read_items():
#     return ORJSONResponse([{"item_id": "Foo"}])


# HTML响应
# @app.get("/items/", response_class=HTMLResponse)
# async def read_items():
#     return """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look ma! HTML!</h1>
#         </body>
#     </html>
#     """


# @app.get("/items/")
# async def read_items():
#     html_content = """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look ma! HTML!</h1>
#         </body>
#     </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    # return generate_html_response()
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)