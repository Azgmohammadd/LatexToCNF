from . import latex_parser as lp
import re

def iscommand(string: str) -> bool:
    """
    Check if a string represents a LaTeX command.

    Args:
        string (str): Input string.

    Returns:
        bool: True if the string is a LaTeX command, False otherwise.
    """
    return re.match(pattern=r'^\\', string=string)

def isliteral(formula: lp.Formula) -> bool:
    """
    Check if a formula is a literal.

    Args:
        formula (Formula): Input logical formula.

    Returns:
        bool: True if the formula is a literal, False otherwise.
    """
    if isinstance(formula, list):
        if formula[0] == lp.LatexParser._negation:  # negation
            return True

    elif isinstance(formula, str) and not iscommand(formula):
        return True

    else:
        return False

def well_formed_formula(parse: lp.Formula) -> bool:
    """
    Check if a parsed logical expression is well-formed.

    Args:
        parse: Parsed logical expression.

    Returns:
        bool: True if the expression is well-formed, False otherwise.
    """
    if parse is None:
        return False

    if isinstance(parse, list):
        match len(parse):
            case 1:  # (WFF)
                return well_formed_formula(parse=parse[0])

            case 2:  # \neg (WFF)
                if parse[0] != lp.LatexParser._negation:
                    return False
                
                return well_formed_formula(parse=parse[1])

            case 3:  # WFF (operator) WFF
                if parse[1] not in [lp.LatexParser._and, lp.LatexParser._or, lp.LatexParser._implies]:
                    return False

                return well_formed_formula(parse=parse[0]) and well_formed_formula(parse=parse[2])
            case _:
                return False

    elif isinstance(parse, str):  # atom
        return not iscommand(parse)

    else:
        return False

def negation(phi: lp.Formula):
    """
    Create a negation formula.

    Args:
        phi (Formula): Subformula to be negated.

    Returns:
        Formula: Negation of the subformula.
    """
    return ['\\neg', phi]

def conjunction(phi: lp.Formula, psi: lp.Formula):
    """
    Create a conjunction formula.

    Args:
        phi (Formula): Left subformula.
        psi (Formula): Right subformula.

    Returns:
        Formula: Conjunction of the two subformulas.
    """
    return [phi, '\wedge', psi]

def disjunction(phi: lp.Formula, psi: lp.Formula):
    """
    Create a disjunction formula.

    Args:
        phi (Formula): Left subformula.
        psi (Formula): Right subformula.

    Returns:
        Formula: Disjunction of the two subformulas.
    """
    return [phi, '\\vee', psi]

def implies(phi: lp.Formula, psi: lp.Formula):
    """
    Create an implication formula.

    Args:
        phi (Formula): Antecedent subformula.
        psi (Formula): Consequent subformula.
Returns:
        Formula: Implication between the two subformulas.
    """
    return [phi, '\rightarrow', psi]

def form(formula: lp.Formula) -> str:
    """
    Determine the type of a logical formula.

    Args:
        formula (Formula): Logical formula.

    Returns:
        str: Type of the formula ('NEGATION', 'CONJUNCTION', 'DISJUNCTION', 'IMPLIES', 'ATOM', or None).
    """
    if isinstance(formula, list):
        if formula[0] == lp.LatexParser._negation:
            return 'NEGATION'

        if formula[1] == lp.LatexParser._and:
            return 'CONJUNCTION'

        if formula[1] == lp.LatexParser._or:
            return 'DISJUNCTION'

        if formula[1] == lp.LatexParser._implies:
            return 'IMPLIES'

    if isinstance(formula, str) and not iscommand(formula):
        return 'ATOM'

    return None