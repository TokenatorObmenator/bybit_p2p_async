from typing import List


class Currency:
    def __init__(
        self,
        currencyId: str,
        exchangeId: str,
        id: str,
        orgId: str,
        scale: int
    ):
        self.currency_id = currencyId
        self.exchange_id = int(exchangeId)
        self.id = int(id)
        self.org_id = int(orgId)
        self.scale = scale


class Token:
    def __init__(
        self,
        exchangeId: str,
        id: str,
        orgId: str,
        scale: str,
        sequence: int,
        tokenId: str
    ):
        self.token_id = tokenId
        self.exchange_id = int(exchangeId)
        self.id = int(id)
        self.org_id = int(orgId)
        self.scale = scale
        self.sequence = sequence


class TradingPreferenceSet:
    def __init__(
        self,
        completeRateDay30: str,
        hasCompleteRateDay30: int,
        hasNationalLimit: int,
        hasOrderFinishNumberDay30: int,
        hasRegisterTime: int,
        hasUnPostAd: int,
        isEmail: int,
        isKyc: int,
        isMobile: int,
        nationalLimit: str,
        orderFinishNumberDay30: int,
        registerTimeThreshold: int
    ):
        self.complete_rate_day_30 = completeRateDay30
        self.has_complete_rate_day_30 = bool(hasCompleteRateDay30)
        self.has_national_limit = bool(hasNationalLimit)
        self.has_order_finish_number_day_30 = bool(hasOrderFinishNumberDay30)
        self.has_register_time = bool(hasRegisterTime)
        self.has_un_post_ad = bool(hasUnPostAd)
        self.is_email = bool(isEmail)
        self.is_kyc = bool(isKyc)
        self.id_mobile = bool(isMobile)
        self.national_limit = nationalLimit
        self.order_finish_number_day_30 = orderFinishNumberDay30
        self.register_time_threshold = registerTimeThreshold


class SymbolInfo:
    def __init__(
        self,
        buyAd,
        sellAd,
        buyFeeRate: str,
        currency: Currency,
        currencyId: str,
        currencyLowerMaxQuote: str,
        currencyMaxQuote: str,
        currencyMinQuote: str,
        exchangeId: str,
        id: str,
        itemDownRange: str,
        itemSideLimit: int,
        itemUpRange: str,
        kycCurrencyLimit: str,
        lowerLimitAlarm: int,
        orderAutoCancelMinute: int,
        orderFinishMinute: int,
        orgId: str,
        sellFeeRate: str,
        status: int,
        token: Token,
        tokenId: str,
        tokenMaxQuote: str,
        tokenMinQuote: str,
        tradeSide: int,
        upperLimitAlarm: int
    ):
        self.buy_ad = buyAd
        self.buy_fee_rate = buyFeeRate
        self.currency = currency
        self.currency_id = currencyId
        self.currency_lower_max_quote = float(currencyLowerMaxQuote)
        self.currency_max_quote = float(currencyMaxQuote)
        self.currency_lower_max_quote = float(currencyLowerMaxQuote)
        self.currency_min_quote = float(currencyMinQuote)
        self.exchange_id = int(exchangeId)
        self.id = int(id)
        self.item_down_range = float(itemDownRange)
        self.item_side_limit = itemSideLimit
        self.item_up_range = float(itemUpRange)
        self.kyc_currency_limit = float(kycCurrencyLimit)
        self.lower_limit_alarm = lowerLimitAlarm
        self.order_auto_cancel_minute = orderAutoCancelMinute
        self.order_finish_minute = orderFinishMinute
        self.org_id = int(orgId)
        self.sell_ad = sellAd
        self.sell_fee_rate = sellFeeRate
        self.status = status
        self.token = token
        self.token_id = tokenId
        self.token_max_quote = float(tokenMaxQuote)
        self.token_min_quote = float(tokenMinQuote)
        self.trade_side = tradeSide
        self.upper_limit_alarm = float(upperLimitAlarm)


class PaymentTemplateItem:
    def __init__(
        self,
        fieldName: str,
        labelDialect: str,
        placeholderDialect: str
    ):
        self.field_name = fieldName
        self.label_dialect = labelDialect
        self.placeholder_dialect = placeholderDialect


class PaymentConfig:
    def __init__(
        self,
        paymentDialect: str,
        paymentName: str,
        paymentTemplateItem: list,
        paymentType: int
    ):
        self.peyment_dialect = paymentDialect
        self.payment_name = paymentName
        self.paymentTemplateItem = [PaymentTemplateItem(**item) for item in paymentTemplateItem]
        self.payment_type = paymentType


class PaymentTerm:
    def __init__(
        self,
        accountNo: str,
        bankName: str,
        branchName: str,
        businessName: str,
        clabe: str,
        concept: str,
        debitCardNumber: str,
        firstName: str,
        id: str,
        lastName: str,
        mobile: str,
        payMessage: str,
        paymentConfig: dict,
        paymentExt1: str,
        paymentExt2: str,
        paymentExt3: str,
        paymentExt4: str,
        paymentExt5: str,
        paymentExt6: str,
        paymentTemplateVersion: float,
        paymentType: str,
        qrcode: str,
        realName: str,
        realNameVerified: bool,
        secondLastName: str,
        visible: int
    ):
        self.account_no = accountNo if accountNo.strip() else None
        self.bank_name = bankName if bankName.strip() else None
        self.branch_name = branchName if branchName.strip() else None
        self.business_name = businessName if businessName.strip() else None
        self.clabe = clabe if clabe.strip() else None
        self.concept = concept if concept.strip() else None
        self.debit_card_number = debitCardNumber if debitCardNumber.strip() else None
        self.first_name = firstName if firstName.strip() else None
        self.id = int(id)
        self.last_name = lastName if lastName.strip() else None
        self.mobile = mobile if mobile.strip() else None
        self.pay_message = payMessage if payMessage.strip() else None
        self.payment_config = PaymentConfig(**paymentConfig)
        self.payment_ext_1 = paymentExt1 if paymentExt1.strip() else None
        self.payment_ext_2 = paymentExt2 if paymentExt2.strip() else None
        self.payment_ext_3 = paymentExt3 if paymentExt3.strip() else None
        self.payment_ext_4 = paymentExt4 if paymentExt4.strip() else None
        self.payment_ext_5 = paymentExt5 if paymentExt5.strip() else None
        self.payment_ext_6 = paymentExt6 if paymentExt6.strip() else None
        self.payment_template_version = paymentTemplateVersion
        self.payment_type = paymentType
        self.qrcode = qrcode if qrcode.strip() else None
        self.real_name = realName if realName.strip() else None
        self.real_name_verified = realNameVerified
        self.second_last_name = secondLastName if secondLastName.strip() else None
        self.visible = bool(visible)


class MarketAd:
    def __init__(
        self,
        accountId: str,
        createDate: str,
        currencyId: str,
        executedQuantity: str,
        fee: str,
        finishNum: str,
        frozenQuantity: str,
        id: str,
        isOnline: bool,
        itemType: str,
        lastLogoutTime: str,
        lastQuantity: str,
        maxAmount: str,
        minAmount: str,
        nickName: str,
        orderNum: int,
        paymentPeriod: int,
        payments: List[str],
        premium: str,
        price: str,
        priceType: int,
        quantity: str,
        recentExecuteRate: int,
        recentOrderNum: int,
        remark: str,
        side: int,
        status: int,
        symbolInfo: SymbolInfo,
        tokenId: str,
        tokenName: str,
        tradingPreferenceSet: TradingPreferenceSet,
        userId: str,
        verificationOrderAmount: str,
        verificationOrderLabels: list,
        verificationOrderSwitch: bool,
        version: float,
        updateDate: str = None,
        subsidyAd: bool = None,
        paymentTerms: list = None,
        feeRate = None,
        authTag: List[str] = None,
        ban: bool = None,
        baned: bool = None,
        blocked: str = None,
        makerContact: bool = None,
        recommend: bool = None,
        recommendTag: str = None,
        userMaskId: str = None,
        userType: str = None,
        authStatus: int = None,
    ):
        self.account_id = int(accountId)
        self.auth_status = authStatus
        self.auth_tag = authTag
        self.ban = ban
        self.baned = baned
        self.blocked = blocked
        self.create_date = int(createDate)
        self.currency_id = currencyId
        self.eexecuted_quantity = float(executedQuantity) if executedQuantity.strip() else None
        self.fee = float(fee) if fee.strip() else None
        self.finish_num = finishNum
        self.frozen_quantity = float(frozenQuantity) if frozenQuantity.strip() else None
        self.id = int(id)
        self.is_online = isOnline
        self.item_type = itemType
        self.last_lagout_time = int(lastLogoutTime)
        self.last_quantity = float(lastQuantity) if lastQuantity.strip() else None
        self.maker_contract = makerContact
        self.max_amount = float(maxAmount)
        self.min_amount = float(minAmount)
        self.nickname = nickName
        self.order_num = orderNum
        self.payment_period = paymentPeriod
        self.payments = payments
        self.premium = bool(premium)
        self.price = float(price)
        self.quantity = float(quantity)
        self.recent_execute_rate = recentExecuteRate
        self.recommend = recommend
        self.remark = remark
        self.side = "buy" if int(side) == 0 else "sell"
        self.status = status
        self.symbol_info = symbolInfo
        self.token_id = tokenId
        self.trading_preference_set = tradingPreferenceSet
        self.user_id = userId
        self.user_mask_id = userMaskId
        self.user_type = userType
        self.verification_order_amount = int(verificationOrderAmount)
        self.verification_order_labels = verificationOrderLabels
        self.verification_order_switch = verificationOrderSwitch
        self.version = version
        self.price_type = priceType
        self.recent_order_num = recentOrderNum
        self.token_name = tokenName
        self.recommend_tag = recommendTag
        self.update_date = updateDate
        self.subsidy_ad = subsidyAd
        self.payment_terms = [PaymentTerm(**item) for item in paymentTerms] if paymentTerms else []
        self.fee_rate = feeRate


class CoinBalance:
    def __init__(
        self,
        bonus: str,
        coin: str,
        transferBalance: str,
        walletBalance: str
    ):
        self.bonus = float(bonus) if bonus.strip() else None
        self.name = coin
        self.transfer_balance = float(transferBalance) if transferBalance.strip else None
        self.wallet_balance = float(walletBalance) if walletBalance.strip() else None


class PrivilegeInfo:
    def __init__(self, name: str, data: str):
        self.name = name
        self.data = data


class AccountInfo:
    def __init__(
        self,
        accountCreateDays: int,
        accountId: str,
        averageReleaseTime: str,
        averageTransferTime: str,
        badAppraiseCount: int,
        blocked: str,
        canSubOnline: bool,
        contactConfig: bool,
        contactCount: int,
        curPrivilegeInfo: list,
        defaultNickName: bool,
        email: str,
        executeNum: int,
        firstTradeDays: int,
        goodAppraiseCount: int,
        goodAppraiseRate: str,
        hasUnPostAd: int,
        isOnline: bool,
        kycCountryCode: str,
        kycLevel: int,
        last30TradeCurrency: str,
        lastLogoutTime: str,
        lostRoleAffected: bool,
        mobile: str,
        nickName: str,
        openApiSwitch: int,
        orderNum: int,
        paymentCount: int,
        paymentRealNameUneditable: bool,
        realName: str,
        realNameEn: str,
        realNameMask: str,
        recentFinishCount: int,
        recentRate: float,
        recentTradeAmount: str,
        registerTime: str,
        totalFinishBuyCount: int,
        totalFinishCount: int,
        totalFinishSellCount: int,
        totalTradeAmount: str,
        userCancelCountLimit: int,
        userCurPrivilege: list,
        userId: str,
        userTag: list,
        userType: str,
        vipLevel: int,
        vipProfit: str,
        whiteFlag: int,
        authStatus: int = None,
    ):
        self.account_create_days = accountCreateDays
        self.account_id = int(accountId)
        self.auth_status = authStatus
        self.average_release_time = int(averageReleaseTime)
        self.average_transfer_time = int(averageTransferTime)
        self.bad_appraise_count = badAppraiseCount
        self.blocked = blocked
        self.can_sub_online = canSubOnline
        self.contact_config = contactConfig
        self.contact_count = contactCount
        self.cur_privilege_info = [PrivilegeInfo(**info) for info in curPrivilegeInfo]
        self.default_nickname = defaultNickName
        self.email = email if email.strip() else None
        self.execute_num = executeNum
        self.first_trade_days = firstTradeDays
        self.good_appraise_count = goodAppraiseCount
        self.good_appraise_rate = float(goodAppraiseRate)
        self.has_un_post_ad = bool(hasUnPostAd)
        self.is_online = isOnline
        self.kyc_country_code = kycCountryCode
        self.kyc_level = kycLevel
        self.last_30_days_trade_currency = last30TradeCurrency
        self.last_logout_time = int(lastLogoutTime)
        self.last_role_affected = lostRoleAffected
        self.mobile = mobile if mobile.strip() else None
        self.nickname = nickName
        self.open_api_switch = bool(openApiSwitch)
        self.order_num = orderNum
        self.payment_count = paymentCount
        self.payment_real_name_uneditable = paymentRealNameUneditable
        self.real_name = realName
        self.real_name_en = realNameEn
        self.real_name_mask = realNameMask
        self.recent_finish_count = recentFinishCount
        self.recent_rate = recentRate
        self.recent_trade_amount = float(recentTradeAmount) if recentTradeAmount.strip() else None
        self.register_time = int(registerTime)
        self.total_finish_buy_count = totalFinishBuyCount
        self.total_finish_count = totalFinishCount
        self.total_finish_sell_count = totalFinishSellCount
        self.total_trade_amount = float(totalTradeAmount) if totalTradeAmount.strip() else None
        self.user_cur_privilege = userCurPrivilege
        self.user_id = int(userId)
        self.user_tag = userTag
        self.user_type = userType
        self.vip_level = vipLevel
        self.vip_profit = vipProfit
        self.white_flag = whiteFlag
        self.user_cancel_count_limit = userCancelCountLimit
