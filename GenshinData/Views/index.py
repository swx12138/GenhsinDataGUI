#

from django.shortcuts import render

from GenshinData.Model.index import index_data


def index(requ):
    return render(
        requ,
        "index.html",
        context=index_data(),
    )
