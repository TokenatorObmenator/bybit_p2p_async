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
