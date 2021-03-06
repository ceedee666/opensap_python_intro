import contextlib
import io
import json
import os
import random
import sys
import unittest
from unittest import TestCase, mock

sys.modules["assess"] = sys.modules[__name__]
dirname = os.path.dirname(__file__)


@contextlib.contextmanager
def capture():
    global captured_out
    import sys

    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [io.StringIO(), io.StringIO()]
        captured_out = out
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr


@contextlib.contextmanager
def trace(t):
    try:
        if t:
            t.start()
        yield
    finally:
        if t:
            t.stop()


def runcaptured(tracing=None, variables=None):
    filename = "exercise.py"
    with open(filename) as f:
        source = f.read()
        c = compile(source, filename, "exec")
        with capture() as out, trace(tracing):
            if variables is None:
                variables = {}
            exec(c, variables)
        return source, out[0], out[1], variables


class ReferenceSolution:
    def search_itunes(self, search_term):
        import requests

        r = requests.get(
            f"https://itunes.apple.com/search?term={search_term}&entity=album"
        )
        result_json = r.json()

        result_count = result_json["resultCount"]
        albums = [
            (result["artistName"], result["collectionName"], result["trackCount"])
            for result in result_json["results"]
        ]

        return result_count, albums


class Testing(TestCase):
    @mock.patch("builtins.input", create=True)
    def test_search_gold(self, mocked_input):
        with mock.patch("requests.get") as mock_request:
            with open("mock_search_result_gold.json") as f:
                mock_request.return_value.json.return_value = json.loads(f.read())
                mock_request.return_value.status_code = 200

            result_count, albums = ReferenceSolution().search_itunes("gold")

        with mock.patch("requests.get") as mock_request:
            with open("mock_search_result_gold.json") as f:
                mock_request.return_value.json.return_value = json.loads(f.read())
                mock_request.return_value.status_code = 200
            mocked_input.side_effect = ["gold"]
            self.code, self.std_out, self.error_out, _ = runcaptured()
            output = self.std_out.getvalue().strip()
            lines = output.split("\n")

        self.assertIn(
            "https://itunes.apple.com/search",
            mock_request.call_args.args[0],
            "You should make a request to the iTunes search API using the URL provided in the instructions.",
        )

        self.assertIn(
            str(result_count),
            lines[0],
            f"The first line of the output should contain the number of search results. For the search term 'gold' this should {result_count}.",
        )

        for album in albums:
            self.assertIn(
                album[0],
                output,
                f"For the search term 'gold' the result should contain the artist {album[0]}",
            )
            self.assertIn(
                album[1],
                output,
                f"For the search term 'gold' the result should contain the album {album[1]}",
            )
            self.assertIn(
                str(album[2]),
                output,
                f"For the search term 'gold' the result should contain the track count {album[2]}",
            )

    @mock.patch("builtins.input", create=True)
    def test_search_random(self, mocked_input):
        search_terms = [
            "blue",
            "elvis",
            "little",
            "pepper",
            "revolver",
            "pet",
            "dark",
            "moon",
            "thriller",
            "destruction",
            "nevermind",
            "computer",
        ]

        search_term = random.choice(search_terms)

        with mock.patch("requests.get") as mock_request:
            with open(f"mock_search_result_{search_term}.json") as f:
                mock_request.return_value.json.return_value = json.loads(f.read())
                mock_request.return_value.status_code = 200

            result_count, albums = ReferenceSolution().search_itunes(search_term)

        with mock.patch("requests.get") as mock_request:
            with open(f"mock_search_result_{search_term}.json") as f:
                mock_request.return_value.json.return_value = json.loads(f.read())
                mock_request.return_value.status_code = 200

            mocked_input.side_effect = [search_term]
            self.code, self.std_out, self.error_out, _ = runcaptured()
            output = self.std_out.getvalue().strip()
            lines = output.split("\n")

        self.assertIn(
            "https://itunes.apple.com/search",
            mock_request.call_args.args[0],
            "You should make a request to the iTunes search API using the URL provided in the instructions.",
        )

        self.assertIn(
            str(result_count),
            lines[0],
            f"The first line of the output should contain the number of search results. For the search term '{search_term}' this should {result_count}.",
        )

        for album in albums:
            self.assertIn(
                album[0],
                output,
                f"For the search term '{search_term}' the result should contain the artist {album[0]}",
            )
            self.assertIn(
                album[1],
                output,
                f"For the search term '{search_term}' the result should contain the album {album[1]}",
            )
            self.assertIn(
                str(album[2]),
                output,
                f"For the search term '{search_term}' the result should contain the track count {album[2]}",
            )


if __name__ == "__main__":
    unittest.main()
