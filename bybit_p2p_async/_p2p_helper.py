from ._p2p_method import P2PMethod


class P2PMethods:
    GET_CURRENT_BALANCE = P2PMethod(
        "/v5/asset/transfer/query-account-coins-balance",
        "GET",
        [
            "accountType"
        ]
    )
    GET_ACCOUNT_INFORMATION = P2PMethod(
        "/v5/p2p/user/personal/info",
        "POST",
        []
    )
    GET_ADS_LIST = P2PMethod(
        "/v5/p2p/item/personal/list",
        "POST",
        []
    )
    GET_ONLINE_ADS = P2PMethod(
        "/v5/p2p/item/online",
        "POST",
        [
            "tokenId",
            "currencyId",
            "side"
        ]
    )

