from typing import List, Union
import pyparsing as pp
pp.ParserElement.enablePackrat() #https://github.com/pyparsing/pyparsing/wiki/Performance-Tips

Formula = Union[
    str, #Atom
    List[Union[str, 'Formula', List['Formula']]]
]

class LatexParser:
    """
    LatexParser class for parsing LaTeX-like logical expressions.

    Attributes:
        variables (pyparsing.Word): Parser for alphanumeric variables.
        _negation (pyparsing.Word): Parser for logical negation (~ or \\neg).
        _and (pyparsing.Word): Parser for logical AND (& or \wedge).
        _or (pyparsing.Word): Parser for logical OR (| or \vee).
        _implies (pyparsing.Word): Parser for logical implication (> or \rightarrow).
        operators (list): List of tuple-structured operators with their precedence and associativity.
        parser (pyparsing.infixNotation): Infix notation parser for constructing logical expressions.

    Methods:
        parse(self, line: str) -> list: Parse a single line of a logical expression and return the parsed result.
        parse_file(self, file_path: str) -> list[Any]: Parse a file containing logical expressions line by line.

    Raises:
        pp.ParseException: Raised when there is an issue parsing the logical expression.
        FileNotFoundError: Raised when the specified file is not found.
    """
    variables = pp.Word(pp.alphas, max=1)
    
    _negation = pp.Word(r'~\neg', max=0).setParseAction(lambda token: "\neg")
    _and = pp.Word(r'&\wedge').setParseAction(lambda token: "\wedge")
    _or = pp.Word(r'|\vee').setParseAction(lambda token: "\vee")
    _implies = pp.Word(r'>\rightarrow').setParseAction(lambda token: "\rightarrow")
    
    operators = [
            (_negation, 1, pp.opAssoc.RIGHT),
            (_and, 2, pp.opAssoc.LEFT),
            (_or, 2, pp.opAssoc.LEFT),
            (_implies, 2, pp.opAssoc.LEFT)
        ]

    parser = pp.infixNotation(variables | _negation, operators)

    def parse(self, line: str) -> Formula:
        """
        Parse a single line of a logical expression and return the parsed result.

        Args:
            line (str): The line containing a logical expression.

        Returns:
            Formula: Parsed result as a Formula.

        Raises:
            pp.ParseException: Raised when there is an issue parsing the logical expression.
        """
        try: 
            return self.parser.parseString(line).asList()

        except pp.ParseException:
            return None

    def parse_file(self, file_path: str) -> list[Formula]:
        """
        Parse a file containing logical expressions line by line.

        Args:
            file_path (str): Path to the file containing logical expressions.

        Returns:
            list[Formula]: List of parsed results for each line.

        Raises:
            FileNotFoundError: Raised when the specified file is not found.
        """
        try:
            with open(file=file_path, mode='r') as file:
                lines = file.readlines()
                # line = file.read()
                parses = [self.parse(line) for line in lines]
                # parse = self.parse(line)[0]
            return parses
            # return parse

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")