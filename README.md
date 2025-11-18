# bybit_p2p_async
## Asynchronous library for integration with Bybit P2P API, written in Python

[![pip package](https://img.shields.io/pypi/v/bybit-p2p-async)](https://pypi.org/project/bybit-p2p-async/)

`bybit_p2p_async` - is an asynchronous fork of the official Python SDK for the Bybit P2P API, enabling seamless integration of your software solutions with the [Bybit P2P Platform](https://www.bybit.com/en/promo/global/p2p-introduce).

* No need to manually implement request signing mechanisms (HMAC, RSA)
* Simple and user-friendly
* Actively developed and maintained
* Compatible with asynchronous programming
* Returns structured data using classes

*the original synchronous version was developed by kolya5544*

## Features

bybit_p2p_async currently does not implement all methods available in the P2P API. The library is under active development, and missing endpoints will be added gradually. Below is a list of currently supported features:

* Retrieve account information
* Retrieve account balance
* Retrieve a list of account orders
* Retrieve a list of available P2P market orders

All functions are typically accessible via a single method call and do not require deep API knowledge to use.

## Technologies

bybit_p2p_async leverages a number of technologies and libraries:

* `aiohttp` and `aiofiles` for creating and processing HTTP requests, including multipart/form-data
* `pycryptodome` for HMAC and RSA operations

## Installation

`bybit_p2p_async` was tested on Python 3.11, but should work on all higher versions as well. The module can be installed manually or via [PyPI](https://pypi.org/project/pybit/) with `pip`:
```
pip install bybit-p2p-async
```

## Usage

Once installed, you can import and use bybit_p2p_async in your code:

```
from bybit_p2p_async import P2P
```

Here is an example:

```
import asyncio

from bybit_p2p_async import P2P


async def main():
    api = P2P(
        api_key="x",
        api_secret="x"
    )

    # 1. Get account information.
    status, data = await api.get_account_information()

    if status:
        print(f"Nickname: {data.nickname}")
        print(f"Real Name: {data.real_name}")
        print(f"User ID: {data.user_id}")
        print(f"Orders: {data.order_num}")
        print()

    # 2. Get account balance.
    status, data = await api.get_current_balance(
        account_type="FUND",
        coins=["USDT", "USDC", "BTC"]
    )

    if status:
        account_type, member_id, coins = data
        print(f"User ID: {member_id}")
        print(f"Account: {account_type}")
        print("=" * 10)
        for coin in coins:
            print(f"{coin.name}")
            print(f"Wallet balance: {coin.wallet_balance}")
            print(f"Transfer balance: {coin.transfer_balance}")
            
            if coin.bonus is not None:
                print(f"Bonus: {coin.bonus}")

            print("-" * 8)
            print()


    # 3. Get account ads.
    status, data = await api.get_ads_list(
        available=False,
        side="buy",
        token_id="USDT",
        size=5,
        currency_id="USD"
    )

    if status:
        count, hidden, ads = data
        print(f"Retrieved orders: {count}")
        print(f"Hidden: {'Yes' if hidden else 'No'}")
        print("=" * 10)
        for ad in ads:
            print(f"Pair: {ad.token_name}/{ad.currency_id}")
            print(f"Price: {ad.price}")
            print(f"Quantity: {ad.quantity}")
            print(f"Remark: {ad.remark}")

            print("-" * 8)

        print()

    # 4. Get market ads.
    status, data = await api.get_market_ads(
        amount=5000,
        bulk_maker=True,
        va_maker=True,
        can_trade=True,
        currency_id="USD",
        token_id="USDT",
        side="sell",
        sort_type="TRADE_PRICE"
    )

    if status:
        count, ads = data
        print(f"Total ads: {count}")
        print("=" * 10)

        print("=" * 10)
        for ad in ads:
            print(f"Pair: {ad.token_id}/{ad.currency_id}")
            print(f"Price: {ad.price}")
            print(f"Quantity: {ad.quantity}")
            print(f"Remark: {ad.remark}")

            print("-" * 8)

        print()


    await api.close_session()

if __name__ == "__main__":
    asyncio.run(main())

```

The P2P() class is used to interact with the P2P API. The testnet parameter indicates the environment.
For Mainnet ([https://bybit.com/](https://bybit.com/)), use `testnet=False`.
For Testnet ([https://testnet.bybit.com/](https://testnet.bybit.com/)), use `testnet=True`.

RSA users should also set `rsa=True` in the constructor. Users from regions like TR/KZ/NL/etc. can customize the `domain` and `tld ` parameters, e.g., `tld="kz"`.

A full working example is available here: [bybit_p2p_async quickstart](https://github.com/TokenatorObmenator/bybit_p2p_async/blob/master/examples/quickstart.py).

## Documentation

The bybit_p2p_async library currently consists of a single module used for direct REST requests to the Bybit P2P API.

You can access the P2P API documentation here: [P2P API documentation](https://bybit-exchange.github.io/docs/p2p/guide)

Below is the mapping between API methods and bybit_p2p methods:

Ads:

| bybit_p2p method name | P2P API method name | P2P API endpoint path |
| --------------------- | ------------------ | ---------------------------------------------------------------------------------- |
| get_online_ads()    | Get all ads            | [/v5/p2p/item/online](https://bybit-exchange.github.io/docs/p2p/ad/online-ad-list) |
| get_ads_list()      | Get your ads         | [/v5/p2p/item/personal/list](https://bybit-exchange.github.io/docs/p2p/ad/ad-list) |

Orders:


User:

| bybit_p2p method name | P2P API method name | P2P API endpoint path |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------- |
| get_account_information() | Получить информацию о текущем пользователе    | [/v5/p2p/user/personal/info](https://bybit-exchange.github.io/docs/p2p/user/acct-info)                    |


Misc:

| bybit_p2p method name | P2P API method name | P2P API endpoint path |
| ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| get_current_balance() | Get coin balances | [/v5/asset/transfer/query-account-coins-balance](https://bybit-exchange.github.io/docs/p2p/all-balance) |
| get_market_ads() | Get ads list from P2P market | /v5/p2p/item/online |

## License

MIT
