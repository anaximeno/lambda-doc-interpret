from fastapi import APIRouter

router = APIRouter(prefix='/test')


@router.get('')
async def get_test():
    return {"hell": "yeah"}


__all__ = ['router']
