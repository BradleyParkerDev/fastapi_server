import json
from app.lib.logger import get_logger
from fastapi import Request, Response, HTTPException, status

# get user controller
async def get_user_controller(request:Request, response:Response):
    logger = get_logger("user")
    logger.info("User successefully retrieved!!!")
    return {"message": "User data successefully retrieved!!!"}
