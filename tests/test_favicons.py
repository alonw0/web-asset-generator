"""Regression tests for generated browser icon sizes."""
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPTS = (Path(__file__).resolve().parents[1] / 'skills' /
           'web-asset-generator' / 'scripts')
sys.path.insert(0, str(SCRIPTS))
from generate_favicons import generate_icons


class FaviconTests(unittest.TestCase):
    def test_ico_contains_both_browser_sizes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source.png'
            Image.new('RGBA', (64, 64), (20, 40, 60, 255)).save(source)
            output = root / 'output'
            generate_icons(source, output, 'favicon')

            with Image.open(output / 'favicon.ico') as image:
                self.assertEqual(image.ico.sizes(), {(16, 16), (32, 32)})
            for size in (16, 32, 96):
                with Image.open(output / f'favicon-{size}x{size}.png') as image:
                    self.assertEqual(image.size, (size, size))


if __name__ == '__main__':
    unittest.main()
