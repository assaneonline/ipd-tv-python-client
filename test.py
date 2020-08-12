from random import random
from time import sleep

import ipdtv.client


while 1:

    ipdtv.client.push_data("data_source-13939", {
        "data:3": int(1000 + (10000 - 1000)*random())
    })

    """
    ipdtv.push_data("data_source-13939", {
        "data:1": "COVID voyageurs",
        "data:2": 'account-multiple-outline',
        "data:3": int(1000 + (10000 - 1000)*random()),
        "data:4": "voyageurs enregistrés"
    })
    """

    sleep(5)
