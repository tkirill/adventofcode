from typing import Optional
import subprocess
from pathlib import Path
import unittest


class AocTestBase(unittest.TestCase):

    test_dir: str

    def assertAocDay(self, day: int, star1: str, star2: Optional[str]):
        filename = next((x for x in self.test_dir.iterdir() if x.name.startswith(f'{day:02d}_') and x.suffix == '.py'), None)
        if not filename:
            self.assertIsNotNone(filename, msg=f'Could not find a file for specified day in a dir {self.test_dir.absolute()}')
        self.assertAoc(filename.absolute(), star1, star2)
    
    def assertAoc(self, filename: str, star1: str, star2: Optional[str]):
        output = subprocess.run(['python', filename], capture_output=True, text=True)
        if output.returncode:
            msg = f'Script for the day finished with non-zero code\n\nOutput:\n{output.stdout}\n\nError:\n{output.stderr}'
            self.assertEqual(output.returncode, 0, msg)
        lines = output.stdout.splitlines()
        self.assertTrue(lines[0].startswith('Star 1: '), 'First line of output does not follow expected format')
        self.assertEqual(lines[0], f'Star 1: {star1}')
        if star2 is not None:
            self.assertTrue(lines[1].startswith('Star 2: '), 'Second line of output does not follow expected format')
            self.assertEqual(lines[1], f'Star 2: {star2}')