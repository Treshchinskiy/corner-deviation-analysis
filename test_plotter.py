import unittest
from plotter import Plotter
import os

class TestPlotter(unittest.TestCase):

    def setUp(self):
        self.plots_dir = 'plots'
        self.plotter = Plotter(self.plots_dir)

    def test_folder_created(self):
        self.assertTrue(os.path.isdir(self.plots_dir), "Папка не была создана")

    def test_draw_plots(self):
        json_file = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
    
        self.plotter.draw_plots(json_file)
            
        files_in_directory = os.listdir(self.plots_dir)
            
        expected_file_count = 3
            
        self.assertEqual(len(files_in_directory), expected_file_count)

if __name__ == '__main__':
    unittest.main()
