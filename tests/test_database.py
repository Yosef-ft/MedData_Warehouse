import unittest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath('scripts'))
from database import DbConn


class TestDatabase(unittest.TestCase):

    @patch('database.psycopg2.connect')
    def test_database_connection(self, mock_connect):

        db = DbConn()

        mock_connect.assert_called_once_with(
            database= os.getenv('DB_NAME'),
            user= os.getenv('DB_USER'),
            password= os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port= os.getenv('DB_PORT')
        )        

    def test_read_data(self):
        
        dbconn = DbConn()

        with patch.object(dbconn, 'read_data') as mock_dbconn:
            expected_rows = [('Channel_Title', 'Channel_Username', 'ID', 'Message', 'Date', 'Media_Path')]
            mock_dbconn.return_value = expected_rows

            result = dbconn.read_data('RawData')

            mock_dbconn.assert_called_once_with('RawData')
            self.assertEqual(result, expected_rows)


if __name__ == "__main__":
    unittest.main(verbosity= 1)



