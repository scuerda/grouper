"""Console script for aws_transcription_grouper."""
import argparse
import sys
from .grouper import parse_transcript


def main():
    """Console script for aws_transcription_grouper."""
    parser = argparse.ArgumentParser()
 
    parser = argparse.ArgumentParser(description="Process AWS Transcripts...")
    parser.add_argument("input", nargs=1, type=str, help="JSON file from AWS")
    parser.add_argument("-o", "--output", type=str, help="TXT file to output to")
    args = parser.parse_args()
    output = args.output or f'{args.input[0].split(".")[0]}.txt'
    parse_transcript(args.input[0], output)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
