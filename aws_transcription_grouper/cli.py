"""Console script for aws_transcription_grouper."""
import argparse
import sys
import os
from .grouper import parse_transcript

def build_name(f_path, f_name, f_extra=None):
    modifier = '' if f_extra is None else f'_{f_extra}'
    final_name = f'{f_name}{modifier}.txt'
    f_path = f_path if f_path else '.'
    return f'{f_path}/{final_name}'


def unique_file(filename):
    f_path, f_name = os.path.split(filename)
    f_basename, _ = os.path.splitext(f_name)

    final_name = build_name(f_path, f_basename)

    counter = 0
    while os.path.exists(final_name):
        counter += 1
        final_name = build_name(f_path, f_basename, counter)

    return final_name


def main():
    """Console script for aws_transcription_grouper."""
    parser = argparse.ArgumentParser()
 
    parser = argparse.ArgumentParser(description="Process AWS Transcripts...")
    parser.add_argument("input", nargs=1, type=str, help="JSON file from AWS")
    parser.add_argument("-o", "--output", type=str, help="TXT file to output to")
    args = parser.parse_args()
    output = args.output or f'{args.input[0].split(".")[0]}.txt'
    output = args.output or args.input[0]
    output = unique_file(output)
    parse_transcript(args.input[0], output)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
