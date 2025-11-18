from typing import List, Tuple, Union

from ._classes import AccountInfo, CoinBalance, MarketAd
from ._p2p_helper import P2PMethods
from ._p2p_manager import P2PManager


class P2PRequests(P2PManager):

    async def get_current_balance(
        self,
        account_type: str = "FUND",
        with_bonus: bool = False,
        member_id: int | str = None,
        coins: List[str] = None
    ) -> Tuple[bool, Union[Tuple[int, str], Tuple[str, int, List[CoinBalance]]]]:
        """
        Obtain wallet balance, query asset information of each currency.
        By default, currency information with assets or liabilities of 0 is not returned.

        Args:
            account_type (str, optional): Account type. UNIFIED, FUND or CONTRACT.
            with_bonus (bool, optional): With bonus filter. Default False.
            member_id (int | str, options): User Id. It is required when you use master api key to check sub account coin balance.
            coins (List[str]): Coin names

        Returns:
            Tuple[str, int, List[CoinBalance]]: Success status and tuple. If success tuple is account_type, member_id and a list of CoinBalance. If not success tuple is retCode and retMsg.
        """

        params = {
            "accountType": account_type,
            "withBonus": "0" if not with_bonus else "1"
        }

        if member_id:
            params["memberId"] = member_id

        if coins:
            params["coin"] = ",".join(coins)

        status, data = await self._request(
            method=P2PMethods.GET_CURRENT_BALANCE,
            params=params
        )

        if not status:
            return status, data

        balances = [CoinBalance(**coin) for coin in data["balance"]]

        return status, (data["accountType"], int(data["memberId"]), balances)

    async def get_market_ads(
        self,
        amount: int | str = None,
        bulk_maker: bool = False,
        can_trade: bool = False,
        currency_id: str = "USD",
        item_region: int = 1,
        page: int | str = 1,
        payment: List[str] = [],
        payment_period: List[int] = [],
        side: str = "buy",
        size: int | str = 10,
        sort_type: str = "OVERALL_RANKING",
        token_id: str = "USDT",
        va_maker: bool = False,
        verification_filter: bool = False
    ) -> Tuple[bool, Union[Tuple[int, str], Tuple[int, List[MarketAd]]]]:
        """
        Get market ads from the P2P marketplace.

        Args:
            amount (int | str, optional): Searching amount.
            bulk_maker (bool, optional): Show only block advertisers.
            can_trade (bool, optional): Show only eligible ads.
            currency_id (str, optional): Currency id. For example: HKD, EUR, USD.
            item_region (int, optional): Item region.
            page (int | str, optional): Ads page.
            payment (List[str], optional): Payment method ids.
            payment_period (List[int], optional): Payment period filter.
            side (str, optional): 'buy' or 'sell'.
            sort_type (str, optional): Sorting filter. Options: OVERALL_RANKING, TRADE_VOLUME, TRADE_COMPLETION_RATE, TRADE_PRICE.
            token_id (str, optional): Token id, like USDT, BTC, ETH, or USDC.
            va_maker (bool, optional): Show only verified makers.
            verification_filter (bool, optional): Ads with no verification needed filter.

        Returns:
            Tuple[int, List[MarketAd]]: Success status and tuple. If success tuple is total_count and a list of MarketAd instances. If not success tuple is retCode and retMsg.
        """

        side = side.lower()

        params = {
            "tokenId": token_id,
            "currencyId": currency_id,
            "side": "1" if side == "buy" else "0",
            "verificationFilter": 2 if not verification_filter else 0,
            "vaMaker": va_maker,
            "page": str(page),
            "size": str(size),
            "itemRegion": item_region,
            "canTrade": can_trade,
            "bulkMaker": bulk_maker,
            "payment": payment,
            "paymentPeriod": payment_period,
            "sortType": sort_type,
        }

        if amount:
            params["amount"] = str(amount)

        status, data = await self._request(
            method=P2PMethods.GET_ONLINE_ADS,
            params=params
        )

        if not status:
            return status, data
        
        total_count = data["count"]
        items = data["items"]

        ads = [MarketAd(**item) for item in items]
        return status, (total_count, ads)

    async def get_account_information(
        self,
        **kwargs
    ) -> Tuple[bool, Union[Tuple[int, str], AccountInfo]]:
        """
        Get Account Information

        Return Tuple[bool, Union[Tuple[int, str], AccountInfo]]: Success status and AccountInfo instance if success. If not success tuple: retCode and retMsg.
        """

        status, data = await self._request(
            method=P2PMethods.GET_ACCOUNT_INFORMATION,
            params=kwargs
        )

        return status, AccountInfo(**data)

    async def get_ads_list(
        self,
        item_id: int | str = None,
        available: bool = False,
        side: str = "buy",
        token_id: str = "USDT",
        page: int | str = 1,
        size: int | str = 10,
        currency_id: str = "USD"
    ) -> Tuple[bool, Union[Tuple[int, str], Tuple[int, bool, List[MarketAd]]]]:
        """
        Get account ads list.

        Args:
            item_id (int | str, optional): Ad id.
            available (bool, optional): Available or not. Default False
            side (str, optional): Ad side, "buy" or "sell". Default "buy".
            size (int | str, optional): Page size. Default 10.
            currency_id (str, optional): Currency id, for example: HKD, USD, EUR. Defautl USD.
            token_id (str, optional): Token id, for example: USDT, USDC, BTC. Default USDT.
            page (int | str, optional): Page number, default 1.
            size (int | str, optional): Page size, default 10,
            currency_id (str, optional): Currency id, for example: HKD, USD, EUR. Default USD.
        
        Returns:
            Tuple[bool, Union[Tuple[int, str], Tuple[int, bool, List[MarketAd]]]]: Success status and tuple. If success tuple is ads count, hidden flag and list of MarketAd instances. If not succes tuple is retCode and retMsg.
        """

        params = {
            "side": "0" if side == "buy" else "1",
            "status": "2" if available else "1",
            "tokenId": token_id,
            "page": str(page),
            "size": str(size),
            "currency_id": currency_id
        }

        if item_id:
            params["itemId"] = str(item_id)

        status, data = await self._request(
            method=P2PMethods.GET_ADS_LIST,
            params=params
        )

        if not status:
            return status, data

        return status, (data["count"], data["hiddenFlag"], [MarketAd(**info) for info in data["items"]])
