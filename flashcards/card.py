class Card:
    def __init__(
            self,
            term: str,
            definition: str,
            term_example: str | None = None,
            definition_example: str | None = None,
            ):
        """
        Initialize a card.
        
        :param term: The term on the front of the card.
        :type term: str
        :param definition: The definition on the back of the card.
        :type definition: str
        :param term_example: An optional example involving the term.
        :type term_example: str | None
        :param definition_example: An optional example involving the definition.
        :type definition_example: str | None
        """
        self.term: str = term
        self.definition: str = definition
        self.term_example: str | None = term_example
        self.definition_example: str | None = definition_example
    
    @classmethod
    def from_list(
            cls,
            values: list[str | None],
            ):
        """
        Create a card with values from a list.

        The list `values` must contain either two or four elements. A list that
        contains two elements is of the form `[<term>, <definition>]`. A list
        that contains four elements is of the form `[<term>, <term example>,
        <definition>, <definition example>]`. The term and definition must not
        be `None`.

        :param values: The values on the card.
        :type values: list[str | None]
        """
        match len(values):
            case 2:
                term: str | None = values[0]
                if term is None:
                    raise Exception('The term is None.')
                
                definition: str | None = values[1]
                if definition is None:
                    raise Exception('The definition is None.')
                
                return Card(term, definition)
            case 4:
                term: str | None = values[0]
                if term is None:
                    raise Exception('The term is None.')
                
                term_example: str | None = values[1]
                
                definition: str | None = values[2]
                if definition is None:
                    raise Exception('The definition is None.')
                
                definition_example: str | None = values[3]
                
                return Card(term, definition, term_example, definition_example)
            case _:
                raise Exception(f'A list with {len(values)} was used to create\
                                a card. Expected 2 or 4.')
