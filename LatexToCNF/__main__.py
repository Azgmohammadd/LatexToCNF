from . import latex_parser as lp
from .cnf_builder import parseToCNF 
import argparse

def main():
    args = parse_args()
    
    latex_parser = lp.LatexParser()
    
    input_source = args.filepath
    
    if not input_source.lower().endswith(('.tex', '.txt')):
        raise argparse.ArgumentTypeError('Not a .txt or .tex file! Argument filename must be of type *.txt or *.tex') 

    formulas = latex_parser.parse_file(input_source)

    results = list(map(parseToCNF, formulas))
    
    for idx, result in enumerate(results):
        print(f"line-{idx + 1}: {result}")
     
def parse_args():
    ap = argparse.ArgumentParser(description="Perform operations on logical formula")
    
    ap.add_argument(
        "-f",
        "--filepath", 
        type=str,
        required=True,
        help="Input filepath in .tex or .txt format",
    )
    
    return ap.parse_args()
