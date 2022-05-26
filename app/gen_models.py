from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from sqlalchemy import (
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()
metadata = mapper_registry.metadata


@mapper_registry.mapped
@dataclass
class Character:
    __tablename__ = "character"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="character_pkey"),
        {"schema": "shakespeare"},
    )
    __sa_dataclass_metadata_key__ = "sa"

    id: str = field(metadata={"sa": Column(String(32))})
    name: str = field(metadata={"sa": Column(String(64), nullable=False)})
    speech_count: int = field(metadata={"sa": Column(Integer, nullable=False)})
    abbrev: Optional[str] = field(default=None, metadata={"sa": Column(String(32))})
    description: Optional[str] = field(
        default=None, metadata={"sa": Column(String(2056))}
    )

    work: List[Work] = field(
        default_factory=list,
        metadata={
            "sa": relationship(
                "Work",
                secondary="shakespeare.character_work",
                back_populates="character",
            )
        },
    )
    paragraph: List[Paragraph] = field(
        default_factory=list,
        metadata={"sa": relationship("Paragraph", back_populates="character")},
    )


@mapper_registry.mapped
@dataclass
class Wordform:
    __tablename__ = "wordform"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="wordform_pkey"),
        {"schema": "shakespeare"},
    )
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(metadata={"sa": Column(Integer)})
    plain_text: str = field(metadata={"sa": Column(String(64), nullable=False)})
    phonetic_text: str = field(metadata={"sa": Column(String(64), nullable=False)})
    stem_text: str = field(metadata={"sa": Column(String(64), nullable=False)})
    occurences: int = field(metadata={"sa": Column(Integer, nullable=False)})


@mapper_registry.mapped
@dataclass
class Work:
    __tablename__ = "work"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="work_pkey"),
        {"schema": "shakespeare"},
    )
    __sa_dataclass_metadata_key__ = "sa"

    id: str = field(metadata={"sa": Column(String(32))})
    title: str = field(metadata={"sa": Column(String(32), nullable=False)})
    long_title: str = field(metadata={"sa": Column(String(64), nullable=False)})
    year: int = field(metadata={"sa": Column(Integer, nullable=False)})
    genre_type: str = field(metadata={"sa": Column(String(1), nullable=False)})
    source: str = field(metadata={"sa": Column(String(16), nullable=False)})
    total_words: int = field(metadata={"sa": Column(Integer, nullable=False)})
    total_paragraphs: int = field(metadata={"sa": Column(Integer, nullable=False)})
    notes: Optional[str] = field(default=None, metadata={"sa": Column(Text)})

    character: List[Character] = field(
        default_factory=list,
        metadata={
            "sa": relationship(
                "Character",
                secondary="shakespeare.character_work",
                back_populates="work",
            )
        },
    )
    chapter: List[Chapter] = field(
        default_factory=list,
        metadata={"sa": relationship("Chapter", back_populates="work")},
    )
    paragraph: List[Paragraph] = field(
        default_factory=list,
        metadata={"sa": relationship("Paragraph", back_populates="work")},
    )


@mapper_registry.mapped
@dataclass
class Chapter:
    __tablename__ = "chapter"
    __table_args__ = (
        ForeignKeyConstraint(
            ["work_id"], ["shakespeare.work.id"], name="chapter_work_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="chapter_pkey"),
        UniqueConstraint(
            "work_id",
            "section_number",
            "chapter_number",
            name="chapter_work_id_section_number_chapter_number_key",
        ),
        {"schema": "shakespeare"},
    )
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(metadata={"sa": Column(Integer)})
    work_id: str = field(
        metadata={"sa": Column(ForeignKey("shakespeare.work.id"), nullable=False)}
    )
    section_number: int = field(metadata={"sa": Column(Integer, nullable=False)})
    chapter_number: int = field(metadata={"sa": Column(Integer, nullable=False)})
    description: str = field(metadata={"sa": Column(String(256), nullable=False)})

    work: Optional[Work] = field(
        default=None, metadata={"sa": relationship("Work", back_populates="chapter")}
    )
    paragraph: List[Paragraph] = field(
        default_factory=list,
        metadata={"sa": relationship("Paragraph", back_populates="chapter")},
    )


t_character_work = Table(
    "character_work",
    metadata,
    Column("character_id", ForeignKey("shakespeare.character.id"), nullable=False),
    Column("work_id", ForeignKey("shakespeare.work.id"), nullable=False),
    ForeignKeyConstraint(
        ["character_id"],
        ["shakespeare.character.id"],
        name="character_work_character_id_fkey",
    ),
    ForeignKeyConstraint(
        ["work_id"], ["shakespeare.work.id"], name="character_work_work_id_fkey"
    ),
    PrimaryKeyConstraint("character_id", "work_id", name="character_work_pkey"),
    schema="shakespeare",
)


@mapper_registry.mapped
@dataclass
class Paragraph:
    __tablename__ = "paragraph"
    __table_args__ = (
        ForeignKeyConstraint(
            ["character_id"],
            ["shakespeare.character.id"],
            name="paragraph_character_id_fkey",
        ),
        ForeignKeyConstraint(
            ["work_id", "section_number", "chapter_number"],
            [
                "shakespeare.chapter.work_id",
                "shakespeare.chapter.section_number",
                "shakespeare.chapter.chapter_number",
            ],
            name="paragraph_chapter_fkey",
        ),
        ForeignKeyConstraint(
            ["work_id"], ["shakespeare.work.id"], name="paragraph_work_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="paragraph_pkey"),
        {"schema": "shakespeare"},
    )
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(metadata={"sa": Column(Integer)})
    work_id: str = field(
        metadata={"sa": Column(ForeignKey("shakespeare.work.id"), nullable=False)}
    )
    paragraph_num: int = field(metadata={"sa": Column(Integer, nullable=False)})
    character_id: str = field(
        metadata={"sa": Column(ForeignKey("shakespeare.character.id"), nullable=False)}
    )
    plain_text: str = field(metadata={"sa": Column(Text, nullable=False)})
    phonetic_text: str = field(metadata={"sa": Column(Text, nullable=False)})
    stem_text: str = field(metadata={"sa": Column(Text, nullable=False)})
    paragraph_type: str = field(metadata={"sa": Column(String(1), nullable=False)})
    section_number: int = field(metadata={"sa": Column(Integer, nullable=False)})
    chapter_number: int = field(metadata={"sa": Column(Integer, nullable=False)})
    char_count: int = field(metadata={"sa": Column(Integer, nullable=False)})
    word_count: int = field(metadata={"sa": Column(Integer, nullable=False)})

    character: Optional[Character] = field(
        default=None,
        metadata={"sa": relationship("Character", back_populates="paragraph")},
    )
    chapter: Optional[Chapter] = field(
        default=None,
        metadata={"sa": relationship("Chapter", back_populates="paragraph")},
    )
    work: Optional[Work] = field(
        default=None, metadata={"sa": relationship("Work", back_populates="paragraph")}
    )


# root@cc279f7dcae6:/app# sqlacodegen --generator dataclasses --schemas shakespeare postgresql://user:secret@db:5432/user >> gen_models.py
# root@cc279f7dcae6:/app# sqlacodegen --generator declarative --schemas shakespeare postgresql://user:secret@db:5432/user >> gen_models_declarative.py
