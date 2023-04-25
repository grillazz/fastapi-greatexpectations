from typing import Any, Optional

from fastapi import HTTPException, status
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Session, as_declarative


@as_declarative()
class Base:
    id: Any
    modified_by: Optional[str] = None
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def save(self, db: Session):
        try:
            db.add(self)
            return db.commit()
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(
                    f"Unexpected error has occurred while saving to {self.__tablename__} and Exception:"
                    f" {exception.__repr__()} "
                ),
            )
