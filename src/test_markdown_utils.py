import unittest
from markdown_utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        markdown = "# This is a title\nSome content"
        self.assertEqual(extract_title(markdown), "This is a title")

    def test_no_title(self):
        markdown = "This is just some content\nwithout a title"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_headers(self):
        markdown = "# Main Title\n## Subtitle\n### Subsubtitle"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_whitespace(self):
        markdown = "#    Title with spaces    \nContent"
        self.assertEqual(extract_title(markdown), "Title with spaces")

    def test_title_second_line(self):
        markdown = "Some text\n# Title on second line"
        self.assertEqual(extract_title(markdown), "Title on second line")

    def test_multiple_top_level_headers(self):
        markdown = "# First Title\nSome content\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_no_top_level_header(self):
        markdown = "## Not a top level header\nSome content"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_empty_markdown(self):
        with self.assertRaises(ValueError):
            extract_title("")

    # Add more test methods here

if __name__ == '__main__':
    unittest.main()