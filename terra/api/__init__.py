from enum import Enum


class ApiNetwork(Enum):
    MAINNET = "https://lcd.terra.dev"
    TESTNET__VODKA = "https://vodka-lcd.terra.dev"
    TESTNET__SOJU = "https://soju-lcd.terra.dev"
