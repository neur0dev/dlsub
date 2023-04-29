# main.py
import os
from helper import parse_arguments
from transcript_downloader import TranscriptDownloader
from transcript_processor import TranscriptProcessor

def main():
    # Parse command line arguments
    args = parse_arguments()

    # Download transcript
    downloader = TranscriptDownloader(args.download)
    downloader.save_transcript(args.output)

    # Process transcript
    if args.format or args.minify:
        with open(args.output, 'r', encoding='utf-8') as f:
            raw_transcript = f.readlines()

        processor = TranscriptProcessor(raw_transcript)

        if args.format:
            formatted_transcript = processor.format_transcript()
            output_file = os.path.splitext(args.output)[0] + '_formatted.txt'

        if args.minify:
            minified_transcript = processor.minify_transcript()
            output_file = os.path.splitext(args.output)[0] + '_minified.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            if args.format:
                for line in formatted_transcript:
                    f.write(f"{line}\n")

            if args.minify:
                f.write(minified_transcript)

        print(f"Processed transcript saved in {output_file}.")

if __name__ == '__main__':
    main()