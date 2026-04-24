from utils.code_block_extraction import GenericCodeBlockExtractor


def test_python_code_block_extractor_finds_top_level_blocks():
    """
    """Test the GenericCodeBlockExtractor to find top-level code blocks.
    
        Args:
            content (str): The source code content to extract blocks from.
            filename (str): The name of the file containing the code.
    
        Returns:
            None: Asserts the correctness of the extracted code blocks.
        """
    """
    content = '''
def first():
    """doc"""
    return 1


class Sample:
    def method(self):
        return 2
'''.strip()

    extractor = GenericCodeBlockExtractor(content, "sample.py")

    blocks = extractor.code_block_extractor()

    assert len(blocks) == 3
    assert "def first()" in blocks[0]
    assert "class Sample:" in blocks[1]
    assert "def method(self)" in blocks[2]


def test_javascript_code_block_extractor_handles_curly_braces():
    """"""Test the GenericCodeBlockExtractor for handling JavaScript code blocks with curly braces.\n\n    Args:\n        content (str): The JavaScript code as a string.\n        filename (str): The name of the file containing the code.\n\n    Returns:\n        None: Asserts the correctness of the extracted code blocks.\n    """"""
    content = """
function greet(name) {
  return `Hello ${name}`;
}
""".strip()

    extractor = GenericCodeBlockExtractor(content, "sample.js")

    blocks = extractor.code_block_extractor()

    assert len(blocks) == 1
    assert "function greet(name)" in blocks[0]
