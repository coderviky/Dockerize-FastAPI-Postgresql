from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from item import schemas, models
from auth import oauth2
from auth import schemas as authschemas
from core import database


router = APIRouter(
    prefix="/item",
    tags=['items']
)

get_db = database.get_db


# Get all items
@router.get('/', response_model=List[schemas.ShowItem])
def all(db: Session = Depends(get_db),
        # user: authschemas.User = Depends(oauth2.get_current_user)
        ):
    items = db.query(models.Item).filter(
        # models.Item.user_id == user.id
    ).all()
    return items


@router.get('/{id}', status_code=200, response_model=schemas.ShowItem)
def show(id: int, db: Session = Depends(get_db),
         # user: authschemas.User = Depends(oauth2.get_current_user)
         ):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with the id {id} is not available")
    return item


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Item, db: Session = Depends(get_db), user: authschemas.User = Depends(oauth2.get_current_user)):
    print(request.dict())
    new_item = models.Item(**request.dict(), user_id=user.id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.UpdateItem, db: Session = Depends(get_db), user: authschemas.User = Depends(oauth2.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == id, models.Item.user_id == user.id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with id {id} not found")
    item.update(request.dict())
    db.commit()
    return 'updated'


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.UpdateItem, db: Session = Depends(get_db), user: authschemas.User = Depends(oauth2.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == id, models.Item.user_id == user.id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with id {id} not found")
    item.update(request.dict())
    db.commit()
    return 'updated'


@router.delete('/{id}', )  # status_code=status.HTTP_204_NO_CONTENT
def destroy(id: int, db: Session = Depends(get_db), user: authschemas.User = Depends(oauth2.get_current_user)):
    item = db.query(models.Item).filter(
        models.Item.id == id, models.Item.user_id == user.id
    )
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"item with id {id} not found")
    item.delete(synchronize_session=False)
    db.commit()
    return 'done'
