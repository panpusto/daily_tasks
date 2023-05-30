import os 
import unittest
import zipfile
import tempfile
import shutil

from extract_zip import extract_zip


class ExtractZipTests(unittest.TestCase):
    def test_check_number_of_files_in_dir_after_extracted_zip(self):
        temp_dir = tempfile.mkdtemp()
        shutil.copy2('000.zip', temp_dir)
        os.chdir(temp_dir)

        try:
            initial_file_count = len(os.listdir())

            try:
                file = '000.zip'
                next_file = extract_zip(file)
                while True:
                    if zipfile.is_zipfile(next_file):
                        next_file = extract_zip(next_file)
                    else:
                        break
        
            except FileNotFoundError as err:
                print("File doesn't exist:", err)
            
            final_file_count = len(os.listdir())

            self.assertEqual(final_file_count, initial_file_count + 4)

        finally:
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    unittest.main()
