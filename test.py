from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

 # TODO -- write tests for every view function / feature!
    def test_home_page(self):

        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', resp.data)
            self.assertIn(b'Score:', resp.data)
            self.assertIn(b'Seconds Left:', resp.data)
          


    # def test_check_word(self):

    #     with app.test_client() as client:
    #         resp = client.get('/check-word')
    #        self.assertEqual(resp.status_code,200)
    #        self.assertIn(session,'board')

           
    def test_valid_word(self):

        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [["M", "A", "L", "U", "S"], 
                                 ["M", "A", "L", "U", "S "], 
                                 ["M", "A", "L", "U", "S"], 
                                 ["M", "A", "L", "U", "S"], 
                                 ["M", "A", "L", "U", "S"]]
        response = client.get('/check-word?word=mall')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        
        with app.test_client() as client:

            client.get('/')
            response = client.get('/check-word?word=impossible')
            self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""
        with app.test_client() as client:

            client.get('/')
            response = client.get('/check-word?word=fsjdakfkldsfjdslkfjdlksf')
            self.assertEqual(response.json['result'], 'not-word')