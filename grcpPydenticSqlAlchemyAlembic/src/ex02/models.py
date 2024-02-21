from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    CheckConstraint,
    Float,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from data import CLASS_TYPE


class Base(DeclarativeBase):
    pass


class Spaceship(Base):
    __tablename__ = "spaceship"
    id = Column(Integer, primary_key=True, autoincrement=True)
    alignment = Column(String, CheckConstraint("alignment IN ('Enemy', 'Ally')"))
    name = Column("name", String(50))
    class_ = Column("class_", String, CheckConstraint(f"class_ IN {tuple(CLASS_TYPE)}"))
    length = Column("length", Float)
    crew_size = Column("crew_size", Integer)
    armed = Column("armed", Boolean)

    def __init__(self, alignment, name, class_, length, crew_size, armed) -> None:
        self.alignment = alignment
        self.name = name
        self.class_ = class_
        self.length = length
        self.crew_size = crew_size
        self.armed = armed


class Officer(Base):
    __tablename__ = "officer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    rank = Column("rank", String(50))
    spaceship_id = Column(Integer, ForeignKey("spaceship.id"))

    def __init__(self, first_name, last_name, rank, spaceship_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.spaceship_id = spaceship_id


def insert_to_spaceship(
    session,
    alignment,
    name,
    class_,
    length,
    crew_size,
    armed,
) -> int:
    ship = {
        "alignment": alignment,
        "name": name,
        "class_": class_,
        "length": length,
        "crew_size": crew_size,
        "armed": armed,
    }
    existing_spaceship = session.query(Spaceship).filter_by(**ship).first()
    if existing_spaceship is None:
        new_ship = Spaceship(**ship)
        session.add(new_ship)
        session.commit()
        return new_ship.id
    else:
        return existing_spaceship.id


def insert_to_officer(session, first_name, last_name, rank, id) -> int:
    officer = {
        "first_name": first_name,
        "last_name": last_name,
        "rank": rank,
        "spaceship_id": id,
    }
    exist = session.query(Officer).filter_by(**officer).first()
    if exist is None:
        new_officer = Officer(**officer)
        session.add(new_officer)
        session.commit()
        return new_officer.id
    else:
        return exist.id


def get_traitors(session):
    officers_enemy = (
        session.query(Officer.first_name, Officer.last_name, Officer.rank)
        .join(Spaceship, Spaceship.id == Officer.spaceship_id)
        .where(Spaceship.alignment == "Enemy")
    )
    traitors = (
        session.query(Officer.first_name, Officer.last_name, Officer.rank)
        .join(Spaceship, Spaceship.id == Officer.spaceship_id)
        .where(Spaceship.alignment == "Ally")
        .intersect(officers_enemy)
        .all()
    )
    return traitors
