#"Sa", "Re", "Ga", "Ma", "Pa", "Dha", "Ni", "Sa'"
from urllib.request import urlopen
#import soundfile as sf

Raag={

    "bhoop": [".Sa", ".Re", ".Ga", ".Pa", ".Dha", "Sa",
              "Re", "Ga", "Pa", "Dha", "Sa'",
              "Sa'", "Re'", "Ga'", "Pa'", "Dha'"],

    "bheempalasi": [".Sa", ".Re", ".ga", ".Ma", ".Pa", ".Dha", ".ni", "Sa",
                    "Re", "ga", "Ma", "Pa", "Dha", "ni", "Sa'",
                    "Re'", "ga'", "Ma'", "Pa'", "Dha'", "ni'"],

    "bageshree": [".Sa", ".Re", ".ga", ".Ma", ".Pa", ".Dha", ".ni", "Sa",
                  "Re", "ga", "Ma", "Pa", "Dha", "ni", "Sa'",
                  "Re'", "ga'", "Ma'", "Pa'", "Dha'", "ni'"],

    "khamaj": [".Sa", ".Re", ".Ga", ".Ma", ".Pa", ".Dha", ".Ni", ".ni", "Sa",
               "Re", "Ga", "Ma", "Pa", "Dha", "Ni", "ni", "Sa'",
               "Re'", "Ga'", "Ma'", "Pa'", "Dha'", "Ni'", "ni'"],

    "des": [".Sa", ".Re", ".Ga", ".Ma", ".Pa", ".Dha", ".Ni", ".ni", "Sa",
            "Re", "Ga", "Ma", "Pa", "Dha", "Ni", "ni", "Sa'",
            "Re'", "Ga'", "Ma'", "Pa'", "Dha'", "Ni'", "ni'"],

    "kafi": [".Sa", ".Re", ".ga", ".Ma", ".Pa", ".Dha", ".ni", "Sa",
             "Re", "ga", "Ma", "Pa", "Dha", "ni", "Sa'",
             "Re'", "ga'", "Ma'", "Pa'", "Dha'", "ni'"],

    "durga": [".Sa", ".Re", ".Ma", ".Pa", ".Dha", "Sa",
              "Re", "Ma", "Pa", "Dha", "Sa'",
              "Re'", "Ma'", "Pa'", "Dha'"],

    "yaman": [".Sa", ".Re", ".Ga", ".ma", ".Pa", ".Dha", ".Ni", "Sa",
              "Re", "Ga", "ma", "Pa", "Dha", "Ni", "Sa'",
              "Re'", "Ga'", "ma'", "Pa'", "Dha'", "Ni'"]


}



pandhari_1 = {

    ".Sa":"c3.wav", ".Re":"d3.wav", ".Ga":"e3.wav", ".Ma":"f3.wav", ".Pa":"g3.wav", ".Dha":"a3.wav", ".Ni":"b3.wav",
    ".re":"c-3.wav", ".ga":"d-3.wav", ".ma":"f-3.wav", ".dha":"g-3.wav", ".ni":"a-3.wav",
    "Sa":"c4.wav", "Re":"d4.wav", "Ga":"e4.wav", "Ma":"f4.wav", "Pa":"g4.wav", "Dha":"a4.wav", "Ni":"b4.wav",
    "re":"c-4.wav", "ga":"d-4.wav", "ma":"f-4.wav", "dha":"g-4.wav", "ni":"a-4.wav",
    "Sa'": "c5.wav", "Re'": "d5.wav", "Ga'": "e5.wav", "Ma'": "f5.wav", "Pa'": "g5.wav", "Dha'": "a5.wav", "Ni'": "b5.wav",
    "re'": "c-5.wav", "ga'": "d-5.wav", "ma'": "f-5.wav", "dha'": "g-5.wav", "ni'": "a-5.wav"
}

kali_1 = {

    ".Sa":"c-3.wav", ".Re":"d-3.wav", ".Ga":"f3.wav", ".Ma":"f-3.wav", ".Pa":"g-3.wav", ".Dha":"a-3.wav", ".Ni":"c4.wav",
    ".re":"d3.wav", ".ga":"e3.wav", ".ma":"g3.wav", ".dha":"a3.wav", ".ni":"b3.wav",
    "Sa":"c-4.wav", "Re":"d-4.wav", "Ga":"f4.wav", "Ma":"f-4.wav", "Pa":"g-4.wav", "Dha":"a-4.wav", "Ni":"c4.wav",
    "re":"d4.wav", "ga":"e4.wav", "ma":"g4.wav", "dha":"a4.wav", "ni":"b4.wav",
    "Sa'": "c-5.wav", "Re'": "d-5.wav", "Ga'": "f5.wav", "Ma'": "f-5.wav", "Pa'": "g-5.wav", "Dha'": "a-5.wav",
    "re'": "d5.wav", "ga'": "e5.wav", "ma'": "g5.wav", "dha'": "a5.wav", "ni'": "b5.wav"

}

pandhari_2 = {

    ".Sa":"d3.wav", ".Re":"e3.wav", ".Ga":"f-3.wav", ".Ma":"g3.wav", ".Pa":"a3.wav", ".Dha":"b3.wav", ".Ni":"c-4.wav",
    ".re":"d-3.wav", ".ga":"f3.wav", ".ma":"g-3.wav", ".dha":"a-3.wav", ".ni":"c4.wav",
    "Sa":"d4.wav", "Re":"e4.wav", "Ga":"f-4.wav", "Ma":"g4.wav", "Pa":"a4.wav", "Dha":"b4.wav", "Ni":"c-5.wav",
    "re":"d-4.wav", "ga":"f4.wav", "ma":"g-4.wav", "dha":"a-4.wav", "ni":"c5.wav",
    "Sa'": "d5.wav", "Re'": "e5.wav", "Ga'": "f-5.wav", "Ma'": "g5.wav", "Pa'": "a5.wav", "Dha'": "b5.wav",
    "re'": "d-5.wav", "ga'": "f5.wav", "ma'": "g-5.wav", "dha'": "a-5.wav"

}

kali_2 = {

    ".Sa":"d-3.wav", ".Re":"f3.wav", ".Ga":"g3.wav", ".Ma":"g-3.wav", ".Pa":"a-3.wav", ".Dha":"c4.wav", ".Ni":"d4.wav",
    ".re":"e3.wav", ".ga":"f-3.wav", ".ma":"a3.wav", ".dha":"b3.wav", ".ni":"c-4.wav",
    "Sa":"d-4.wav", "Re":"f4.wav", "Ga":"g4.wav", "Ma":"g-4.wav", "Pa":"a-4.wav", "Dha":"c5.wav", "Ni":"d5.wav",
    "re":"e4.wav", "ga":"f-4.wav", "ma":"a4.wav", "dha":"b4.wav", "ni":"c-5.wav",
    "Sa'": "d-5.wav", "Re'": "f5.wav", "Ga'": "g5.wav", "Ma'": "g-5.wav", "Pa'": "a-5.wav",
    "re'": "e5.wav", "ga'": "f-5.wav", "ma'": "a5.wav", "dha'": "b5.wav"

}