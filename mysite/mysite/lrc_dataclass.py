""""Convert lrc files to a dataclass"""
from dataclasses import dataclass


def read_lrc_file(filename: str):
    """"Return a list of LyricTimeStamp"""
    with open(filename) as file:
        lines = file.readlines()

        start = 0
        i = 0
        while not lines[i].startswith('[0'):
            start += 1
            i += 1

        processed = [process_row(lines[row]) for row in range(start, len(lines))]
        title = lines[0][4:(len(lines[0]) - 2)]
    return (title, processed)


@dataclass
class LyricTimeStamp:
    """A lyric with its timestamp

    Instance Attributes:
      - timestamp: timestamp of the lyric
      - lyric: song lyric
    """
    timestamp: float
    lyric: str


def process_row(row: str) -> LyricTimeStamp:
    """Convert a row lyrics and timestamp into a LyricTimeStamp object"""
    return LyricTimeStamp(str_to_seconds(row), clean_lyrics(row))


def clean_lyrics(lyrics: str) -> str:
    """Remove \n from the lyrics"""
    lyrics = lyrics.replace('\n', '')
    lyrics = lyrics.replace('(', '')
    lyrics = lyrics.replace(')', '')
    length = len(lyrics)

    clean = ''

    for i in range(10, length):
        clean = clean + lyrics[i]

    return clean


def str_to_seconds(combined: str) -> float:
    """Return timestamp as an integer"""
    timestamp_str = combined[1:9]
    seconds = float(timestamp_str[3:9])
    minutes = float(timestamp_str[0:2]) * 60

    return seconds + minutes
