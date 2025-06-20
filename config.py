"""Configuration settings."""

import os
from datetime import timedelta, timezone

# General settings
TIMEZONE = timezone(timedelta(hours=2))

# Browser settings
BROWSER_DEBUG_PORT = 9222
BROWSER_LOAD_DELAY = 5  # seconds
BROWSER_LOAD_TIMEOUT = 10000  # milliseconds
BROWSER_PATH = os.path.expandvars(r"%PROGRAMFILES%\BraveSoftware\Brave-Browser\Application\brave.exe")

# Instagram settings
INSTAGRAM_MAX_POST_AGE = 3  # days
INSTAGRAM_MAX_POSTS_PER_ACCOUNT = 5  # posts
INSTAGRAM_URL = "https://www.instagram.com/"

# Instagram accounts to track
INSTAGRAM_ACCOUNTS = [
    "gijon",
    "biodevas",
    "ausevagm",
    "aytoviedo",
    "nortes.me",
    "paramo_bar",
    "kbunsgijon",
    "crjasturias",
    "agendagijon",
    "conseyu_cmx",
    "sala_niagara",
    "rocketoviedo",
    "prestosofest",
    "deportesayov",
    "meidinerzclub",
    "exprime.gijon",
    "mierescultura",
    "cultura.gijon",
    "conectaoviedo",
    "juventudgijon",
    "culturallanes",
    "gonggalaxyclub",
    "juventudoviedo",
    "cinesfoncalada",
    "oviedo.turismo",
    "oviedo_secrets",
    "patioh_laboral",
    "centroniemeyer",
    "culturacolunga",
    "aytocastrillon",
    "ferialibroxixon",
    "conocerasturias",
    "kuivi_almacenes",
    "cuentosdemaleta",
    "asturias_en_vena",
    "museosgijonxixon",
    "lasalvaje.oviedo",
    "laboralcinemateca",
    "lacompaniadelalba",
    "gteatrolospintores",
    "cia.proyectopiloto",
    "youropia_asociacion",
    "traslapuertatiteres",
    "laboralciudadcultura",
    "ayuntamientocabranes",
    "bandinalagarrapiella",
    "asturiesculturaenrede",
    "bibliotecasdegijonxixon",
    "museudelpuebludasturies",
    "chigreculturallatadezinc",
]
