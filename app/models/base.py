from typing import Any, Optional

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    modified_by: Optional[str] = None
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    async def save(self, db: AsyncSession):
        try:
            db.add(self)
            return await db.commit()
        except Exception as exception:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=str(
                    f"Unexpected error has occurred while saving to {self.__tablename__} and Exception:"
                    f" {exception.__repr__()} "
                ),
            )

