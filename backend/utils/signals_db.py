from typing import TypedDict, Optional, Dict, Any

class SignalInfo(TypedDict):
    name: str
    start: float
    end: float
    modulation: str
    usage: str
    manufacturer: str
    channel: str
    signal_type: str
    codec: str
    encryption: str
    extra: Dict[str, Any]

FREQ_DB: list[SignalInfo] = [
    {
        "name": "VHF авиация",
        "start": 118.0,
        "end": 137.0,
        "modulation": "AM",
        "usage": "Гражданская авиационная связь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"note": "ATC, авиарация"}
    },
    {
        "name": "VHF морская связь",
        "start": 156.0,
        "end": 162.0,
        "modulation": "FM",
        "usage": "Морская радиосвязь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос/Данные",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"channels": "16, 70 и др."}
    },
    {
        "name": "FM-радио",
        "start": 87.5,
        "end": 108.0,
        "modulation": "FM",
        "usage": "Вещательное радио",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Аудио",
        "codec": "-",
        "encryption": "Нет",
        "extra": {}
    },
    {
        "name": "AM-радио",
        "start": 0.52,
        "end": 1.71,
        "modulation": "AM",
        "usage": "Вещательное радио",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Аудио",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"units": "МГц"}
    },
    {
        "name": "CB-радио",
        "start": 26.965,
        "end": 27.405,
        "modulation": "AM/FM",
        "usage": "Гражданский диапазон",
        "manufacturer": "-",
        "channel": "1-40",
        "signal_type": "Голос",
        "codec": "-",
        "encryption": "Нет",
        "extra": {}
    },
    {
        "name": "FRS/GMRS",
        "start": 462.0,
        "end": 467.0,
        "modulation": "FM",
        "usage": "Личная радиосвязь (США)",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос",
        "codec": "-",
        "encryption": "Нет",
        "extra": {}
    },
    {
        "name": "L-Band спутники",
        "start": 1525.0,
        "end": 1660.5,
        "modulation": "Разные",
        "usage": "Спутниковая связь",
        "manufacturer": "Iridium/Inmarsat/Thuraya",
        "channel": "-",
        "signal_type": "Данные/Голос",
        "codec": "-",
        "encryption": "Да",
        "extra": {}
    },
    {
        "name": "S-Band спутники",
        "start": 2025.0,
        "end": 2290.0,
        "modulation": "Разные",
        "usage": "Спутниковая связь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные",
        "codec": "-",
        "encryption": "Да",
        "extra": {"uplink": "2025-2110", "downlink": "2200-2290"}
    },
    {
        "name": "C-Band спутники",
        "start": 3400.0,
        "end": 4200.0,
        "modulation": "Разные",
        "usage": "Спутниковое ТВ и связь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные/ТВ",
        "codec": "-",
        "encryption": "Да",
        "extra": {"uplink": "5925-6425"}
    },
    {
        "name": "Ku-Band спутники",
        "start": 10700.0,
        "end": 12750.0,
        "modulation": "Разные",
        "usage": "Спутниковое ТВ и VSAT",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные/ТВ",
        "codec": "-",
        "encryption": "Да",
        "extra": {"uplink": "13750-14500"}
    },
    {
        "name": "Ka-Band спутники",
        "start": 17700.0,
        "end": 21200.0,
        "modulation": "Разные",
        "usage": "Спутниковый интернет",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные",
        "codec": "-",
        "encryption": "Да",
        "extra": {"uplink": "27500-31000"}
    },
    {
        "name": "WiMAX",
        "start": 3400.0,
        "end": 3600.0,
        "modulation": "OFDM",
        "usage": "Беспроводной интернет",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные",
        "codec": "-",
        "encryption": "Да",
        "extra": {}
    },
    {
        "name": "ZigBee/IEEE 802.15.4",
        "start": 2400.0,
        "end": 2483.5,
        "modulation": "O-QPSK/BPSK",
        "usage": "IoT/датчики",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Данные",
        "codec": "-",
        "encryption": "Да",
        "extra": {"региональные диапазоны": "868, 915, 2400 МГц"}
    },
    {
        "name": "Amateur Radio HF",
        "start": 1.8,
        "end": 29.7,
        "modulation": "SSB/CW/AM/FM",
        "usage": "Любительская радиосвязь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос/Данные",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"band": "HF"}
    },
    {
        "name": "Amateur Radio VHF",
        "start": 50.0,
        "end": 54.0,
        "modulation": "FM/SSB/CW",
        "usage": "Любительская радиосвязь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос/Данные",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"band": "6 метров"}
    },
    {
        "name": "Amateur Radio VHF",
        "start": 144.0,
        "end": 148.0,
        "modulation": "FM/SSB/CW",
        "usage": "Любительская радиосвязь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос/Данные",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"band": "2 метра"}
    },
    {
        "name": "Amateur Radio UHF",
        "start": 430.0,
        "end": 440.0,
        "modulation": "FM/SSB/CW",
        "usage": "Любительская радиосвязь",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос/Данные",
        "codec": "-",
        "encryption": "Нет",
        "extra": {"band": "70 см"}
    },
    {
        "name": "DAB (цифровое радио)",
        "start": 174.0,
        "end": 240.0,
        "modulation": "OFDM",
        "usage": "Цифровое аудио",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Аудио",
        "codec": "MPEG Audio Layer II",
        "encryption": "Нет",
        "extra": {}
    },
    {
        "name": "PMR446",
        "start": 446.0,
        "end": 446.2,
        "modulation": "FM",
        "usage": "Рация",
        "manufacturer": "-",
        "channel": "-",
        "signal_type": "Голос",
        "codec": "-",
        "encryption": "Нет",
        "extra": {}
    }
]

def find_signals_in_range(freq: float) -> list[SignalInfo]:
    """
    Найти все сигналы, которые могут быть в заданной частоте
    
    Args:
        freq: Частота в МГц
        
    Returns:
        Список сигналов, в диапазон которых попадает частота
    """
    return [
        signal for signal in FREQ_DB
        if signal["start"] <= freq <= signal["end"]
    ]

def get_all_signals() -> list[SignalInfo]:
    """
    Получить все известные сигналы
    
    Returns:
        Список всех сигналов в базе данных
    """
    return FREQ_DB
