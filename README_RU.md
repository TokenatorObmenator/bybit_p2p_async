# bybit_p2p_async
## Асинхронная библиотека интеграции с Bybit P2P API, написанная на Python

[![pip package](https://img.shields.io/pypi/v/bybit-p2p-async)](https://pypi.org/project/bybit-p2p-async/)

`bybit_p2p_async` - асинхронный форк официального Python SDK для P2P API Bybit, обеспечивающий интеграцию ваших программных решений с [P2P-платформой Bybit](https://www.bybit.com/en/promo/global/p2p-introduce).

* Не требует самостоятельной реализации механизмов подписи запросов (HMAC, RSA)
* Прост и удобен в использовании
* Активно развивается и поддерживается
* Совместим с асинхронным программированием
* Возвращает структурированные данные в виде классов

*синхронная версия изначально разработана kolya5544*

## Возможности

bybit_p2p_async в настоящее время реализует НЕ все методы, доступные в P2P API. Библиотека находится в активной разработке, поэтому недостающие эндпоинты будут добавлены позже. Ниже список того, что умеет библиотека на данный момент:

* Получение информации об аккаунте
* Получения баланса аккаунта
* Получения списка ордеров аккаунта
* Получение списка ордеров доступных на P2P маркете

Все функции обычно доступны одним вызовом метода и не требуют углублённого понимания API для взаимодействия.

## Технологии

bybit_p2p_async использует ряд проектов и технологий:

* `aiohttp` и `aiofiles` для создания и обработки HTTP-запросов, а также запросов с мультиформ-данными
* `pycryptodome` для операций HMAC и RSA

## Установка

`bybit_p2p_async` тестировался на Python 3.11, но должен работать и на всех более новых версиях. Модуль можно установить вручную или через [PyPI](https://pypi.org/project/pybit/) с помощью `pip`:

```
pip install bybit-p2p-async
```

## Использование

После установки вы можете использовать bybit_p2p_async, импортировав его в код:

```
from bybit_p2p_async import P2P
```

Вот пример кода:

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

Класс `P2P()` используется для взаимодействия с P2P API. Здесь `testnet` означает окружение. Для Мейннета ([https://bybit.com/](https://bybit.com/)) следует использовать `testnet=False`. Для Тестнета ([https://testnet.bybit.com/](https://testnet.bybit.com/)) используйте `testnet=True`.

Пользователям RSA также следует установить `rsa=True` в конструкторе. Пользователи TR/KZ/NL/и т. д. могут изменять параметры `domain` и `tld`, например `tld="kz"`.

Полный пример кода доступен здесь: [bybit_p2p_async quickstart](https://github.com/TokenatorObmenator/bybit_p2p_async/blob/master/examples/quickstart.py).

## Документация

Библиотека bybit_p2p_async в настоящее время состоит всего из одного модуля, который используется для прямых REST-запросов к P2P API Bybit.

Получить доступ к документации P2P API можно по ссылке: [P2P API documentation](https://bybit-exchange.github.io/docs/p2p/guide)

Ниже приведено соответствие методов API методам bybit_p2p:

Объявления:

| имя метода bybit_p2p | имя метода P2P API | Путь эндпоинта P2P API                                                             |
| --------------------- | ------------------ | ---------------------------------------------------------------------------------- |
| get_online_ads()    | Получить все объявления            | [/v5/p2p/item/online](https://bybit-exchange.github.io/docs/p2p/ad/online-ad-list) |
| get_ads_list()      | Получить свои объявление         | [/v5/p2p/item/personal/list](https://bybit-exchange.github.io/docs/p2p/ad/ad-list) |

Ордера:


Пользователь:

| имя метода bybit_p2p       | имя метода P2P API         | Путь эндпоинта P2P API                                                                                    |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------- |
| get_account_information() | Получить информацию о текущем пользователе    | [/v5/p2p/user/personal/info](https://bybit-exchange.github.io/docs/p2p/user/acct-info)                    |


Разное:

| имя метода bybit_p2p   | имя метода P2P API | Путь эндпоинта P2P API                                                                                  |
| ----------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| get_current_balance() | Получить баланс монет | [/v5/asset/transfer/query-account-coins-balance](https://bybit-exchange.github.io/docs/p2p/all-balance) |
| get_market_ads() | Получить список объявлений на P2P маркете | /v5/p2p/item/online |

## Лицензия

MIT
