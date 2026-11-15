# Verification only (not part of the fix): prints the query count of each
# list page with 17 and with 21 diaper changes / 3 and 7 notes / 3 and 7
# temperatures on one page.
from core.tests.tests_views import ListQueriesTestCase


class PrintCounts(ListQueriesTestCase):
    def test_query_count_does_not_grow_with_the_entries(self):
        self.add_entries(2)
        for url in self.urls:
            self.client.get(url)
        few = {url: self.count_queries(url) for url in self.urls}
        rows_few = {
            "changes": __import__("core").models.DiaperChange.objects.count(),
        }
        self.add_entries(4)
        many = {url: self.count_queries(url) for url in self.urls}
        rows_many = {
            "changes": __import__("core").models.DiaperChange.objects.count(),
        }
        print(f"\nQUERYCOUNTS rows={rows_few}->{rows_many} few={few} many={many}")
