"""Console script for aws_transcription_grouper."""
import argparse
import sys
from .grouper import parse_transcript


def main():
    """Console script for aws_transcription_grouper."""
    parser = argparse.ArgumentParser()
 
    parser = argparse.ArgumentParser(description="Process AWS Transcripts...")
    parser.add_argument("-i", "--input", type=str, help="JSON file from AWS")
    parser.add_argument("-o", "--output", type=str, help="TXT file to output to")
    args = parser.parse_args()
    parse_transcript(args.input, args.output)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
