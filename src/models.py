import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

user_character_favorites = Table('user_character_favorites', Base.metadata,
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('character_id', ForeignKey('character.id'), nullable=False)
)

user_planet_favorites = Table('user_planet_favorites', Base.metadata,
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('planet_id', ForeignKey('planet.id'), nullable=False)
)

character_film = Table('character_film', Base.metadata,
    Column('character_id', ForeignKey('character.id'), nullable=False),
    Column('film_id', ForeignKey('film.id'), nullable=False)
)

film_starship = Table('film_starship', Base.metadata,
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('starship_id', ForeignKey('starship.id'), nullable=False)
)

film_vehicle = Table('film_vehicle', Base.metadata,
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('vehicle_id', ForeignKey('vehicle.id'), nullable=False)
)

character_specie = Table('character_specie', Base.metadata,
    Column('character_id', ForeignKey('character.id'), nullable=False),
    Column('specie_id', ForeignKey('specie.id'), nullable=False)
)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    name= Column(String)
    skin_color = Column(String)

    homeworld = relationship('Planet')
    character_film = relationship("Film",secondary=character_film)
    character_specie = relationship("Specie",secondary=character_specie)
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    name = Column(String)
    climate = Column(String)
    diameter = Column(Numeric)
    gravity = Column(Numeric)
    orbital_period = Column(Numeric)
    population = Column(Integer)
    rotation_period = Column(Numeric)
    surface_water = Column(Numeric)
    terrain = Column(String)    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    character_favorites = relationship("Character",secondary=user_character_favorites)

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    title = Column(String)
    director = Column(String)
    producer = Column(String)
    film_starship = relationship("Starship",secondary=film_starship)
    film_vehicle = relationship("Vehicle",secondary=film_vehicle)
    # and some others ... :P

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    name = Column(String)
    model = Column(String)
    passengers = Column(Numeric)
    length = Column(Numeric)
    # and some others ... :P

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    name = Column(String)
    model = Column(String)
    passengers = Column(Numeric)
    length = Column(Numeric)
    # and some others ... :P

class Specie(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    name = Column(String)
    language = Column(String)
    designation = Column(String)
    eye_colors = Column(String)
    homeworld = relationship('Planet', back_populates="species")
    # and some others ... :P


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')