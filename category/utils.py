from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from category.models import Instructions


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Instructions.objects.filter(id=int(query))
    vector = SearchVector("name", "summary")
    query = SearchQuery(query)
    result = (
        Instructions.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span style='background-color: rgba(255, 162, 0, 0.3);'>",
            stop_sel="</span>",
        ),
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "summary",
            query,
            start_sel="<span style='background-color: rgba(255, 162, 0, 0.3);'>",
            stop_sel="</span>",
        )
    )

    return result
