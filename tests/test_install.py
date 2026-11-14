import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
SOURCE = ROOT / 'openspec/skills/lite-feature-plan'


class InstallationTests(unittest.TestCase):
    def test_complete_self_contained_copy(self):
        with tempfile.TemporaryDirectory() as temp:
            target = installer.install(SOURCE, Path(temp))
            for source in SOURCE.rglob('*'):
                if source.is_file():
                    self.assertEqual(source.read_bytes(), (target / source.relative_to(SOURCE)).read_bytes())

    def test_existing_installation_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / SOURCE.name
            target.mkdir()
            existing = target / 'SKILL.md'
            existing.write_text('user customization')
            with self.assertRaises(FileExistsError):
                installer.install(SOURCE, Path(temp))
            self.assertEqual(existing.read_text(), 'user customization')

    def test_dangling_destination_symlink_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / SOURCE.name
            target.symlink_to(Path(temp) / 'missing')
            with self.assertRaises(FileExistsError):
                installer.install(SOURCE, Path(temp))
            self.assertTrue(target.is_symlink())

    def test_outside_source_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'external'
            source.mkdir()
            (source / 'SKILL.md').write_text('external')
            with self.assertRaises(ValueError):
                installer.install(source, Path(temp) / 'output')
            self.assertFalse((Path(temp) / 'output').exists())

    def test_source_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            link = Path(temp) / 'alias'
            link.symlink_to(SOURCE, target_is_directory=True)
            with self.assertRaises(ValueError):
                installer.install(link, Path(temp) / 'output')


if __name__ == '__main__':
    unittest.main()
