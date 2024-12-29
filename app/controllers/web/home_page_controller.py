from fastapi import Request, Response, HTTPException, status
from fastapi.templating import Jinja2Templates 

templates = Jinja2Templates(directory="resources/templates")
async def home_page_controller(request:Request, response:Response):


    greeting = "Hello, World!!! \n This is a FastAPI Server!!!"


    return templates.TemplateResponse("pages/home_page.html",{
        "request": request,  # Pass the request object
        "greeting": greeting
    })