import tscribe
import csv
from itertools import groupby
import tempfile


def group_transcript(transcript_csv):
    with open(transcript_csv, "r") as input:
        reader = csv.DictReader(input)
        rows = list(reader)

    grouped_rows = []
    for k, g in groupby(rows, lambda x: x['speaker']):
        grouped_rows.append((k, list(g)))

    return grouped_rows

def output_grouped_transcript(grouped_rows, output):
    with open(output, 'w') as output:
        for speaker, speach in grouped_rows:
            start_time = speach[0]['start_time']
            end_time = speach[-1]['end_time']
            combined_text = " ".join([s['comment'] for s in speach])
            row = f"{speaker} [{start_time}--{end_time}]: {combined_text}\n"
            output.write(row)
            output.write("\n")

def parse_transcript(json_file_path, output):
    tscribe.write(json_file_path, format="csv", save_as="temp.csv")
    output_grouped_transcript(group_transcript("temp.csv"), output)

