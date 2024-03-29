from src.utils.operators import *

# TODO: Recheck Following Functions:
#
# [✔] Due To Ternary Operator: ( 11 Functions )
#      1, 7, 9, 10, 21, 23, 24, 27, 46, 49, 51
#
# [ ] Due To IndClass : ( 18 Functions )
#      48, 58, 59, 63, 67, 69, 70, 76, 79, 80, 82, 87, 89, 90, 91, 93, 97, 100
#
# [ ] Due To Market Cap : ( 1 Function )
#      56
#
# [✔] Verify Use of ^ : ( 15 Functions )
#      33, 41, 48 ,54, 67, 69, 70, 71, 78, 80, 81, 85, 90, 94, 95
#
# [ ] Empty Value in : ( 3 Functions )
#      28, 31, 54
#
# [✔] Due to ts_argmax, ts_argmin : ( 5 Functions )
#      1, 57, 60, 96, 98
# 
# [ ] Filled values in :
#     96




def alpha_1(close, returns, **kwargs):
    return (
        rank(
            ts_argmax(
                signedpower(pd.Series(np.where((returns < 0), stddev(returns, 20), close)), 2.0),
                5,
            )
        )
        - 0.5
    )


def alpha_2(open, close, volume, **kwargs):
    return -1 * correlation(rank(delta(log(volume), 2)), rank(((close - open) / open)), 6)


def alpha_3(open, volume, **kwargs):
    return -1 * correlation(rank(open), rank(volume), 10)


def alpha_4(low, **kwargs):
    return -1 * ts_rank(rank(low), 9)


def alpha_5(open, close, vwap, **kwargs):
    return rank((open - (sum(vwap, 10) / 10))) * (-1 * abs(rank((close - vwap))))


def alpha_6(open, volume, **kwargs):
    return -1 * correlation(open, volume, 10)


def alpha_7(close, volume, adv20, **kwargs):
    return pd.Series(
        np.where(
            (adv20 < volume),
            ((-1 * ts_rank(abs(delta(close, 7)), 60)) * sign(delta(close, 7))),
            (-1 * 1),
        )
    )


def alpha_8(open, returns, **kwargs):
    return -1 * rank(((sum(open, 5) * sum(returns, 5)) - delay((sum(open, 5) * sum(returns, 5)), 10)))


def alpha_9(close, **kwargs):
    return pd.Series(
        np.where(
            (0 < ts_min(delta(close, 1), 5)),
            delta(close, 1),
            np.where(
                (ts_max(delta(close, 1), 5) < 0),
                delta(close, 1),
                (-1 * delta(close, 1)),
            ),
        )
    )


def alpha_10(close, **kwargs):
    return rank(
        pd.Series(
            np.where(
                (0 < ts_min(delta(close, 1), 4)),
                delta(close, 1),
                np.where(
                    (ts_max(delta(close, 1), 4) < 0),
                    delta(close, 1),
                    (-1 * delta(close, 1)),
                ),
            )
        )
    )


def alpha_11(close, volume, vwap, **kwargs):
    return (rank(ts_max((vwap - close), 3)) + rank(ts_min((vwap - close), 3))) * rank(delta(volume, 3))


def alpha_12(close, volume, **kwargs):
    return sign(delta(volume, 1)) * (-1 * delta(close, 1))


def alpha_13(close, volume, **kwargs):
    return -1 * rank(covariance(rank(close), rank(volume), 5))


def alpha_14(open, volume, returns, **kwargs):
    return (-1 * rank(delta(returns, 3))) * correlation(open, volume, 10)


def alpha_15(high, volume, **kwargs):
    return -1 * sum(rank(correlation(rank(high), rank(volume), 3)), 3)


def alpha_16(high, volume, **kwargs):
    return -1 * rank(covariance(rank(high), rank(volume), 5))


def alpha_17(close, volume, adv20, **kwargs):
    return ((-1 * rank(ts_rank(close, 10))) * rank(delta(delta(close, 1), 1))) * rank(ts_rank((volume / adv20), 5))


def alpha_18(open, close, **kwargs):
    return -1 * rank(((stddev(abs((close - open)), 5) + (close - open)) + correlation(close, open, 10)))


def alpha_19(close, returns, **kwargs):
    return (-1 * sign(((close - delay(close, 7)) + delta(close, 7)))) * (1 + rank((1 + sum(returns, 250))))


def alpha_20(open, low, high, close, **kwargs):
    return ((-1 * rank((open - delay(high, 1)))) * rank((open - delay(close, 1)))) * rank((open - delay(low, 1)))


def alpha_21(close, volume, adv20, **kwargs):
    return pd.Series(
        np.where(
            (((sum(close, 8) / 8) + stddev(close, 8)) < (sum(close, 2) / 2)),
            (-1 * 1),
            np.where(
                ((sum(close, 2) / 2) < ((sum(close, 8) / 8) - stddev(close, 8))),
                1,
                np.where(((1 <= (volume / adv20))), 1, (-1 * 1)),
            ),
        )
    )


def alpha_22(high, close, volume, **kwargs):
    return -1 * (delta(correlation(high, volume, 5), 5) * rank(stddev(close, 20)))


def alpha_23(high, **kwargs):
    return pd.Series(np.where(((sum(high, 20) / 20) < high), (-1 * delta(high, 2)), 0))


def alpha_24(close, **kwargs):
    return pd.Series(
        np.where(
            ((delta((sum(close, 100) / 100), 100) / delay(close, 100)) <= 0.05),
            (-1 * (close - ts_min(close, 100))),
            (-1 * delta(close, 3)),
        )
    )


def alpha_25(high, close, vwap, adv20, returns, **kwargs):
    return rank(((((-1 * returns) * adv20) * vwap) * (high - close)))


def alpha_26(high, volume, **kwargs):
    return -1 * ts_max(correlation(ts_rank(volume, 5), ts_rank(high, 5), 5), 3)


def alpha_27(volume, vwap, **kwargs):
    return pd.Series(
        np.where(
            (0.5 < rank((sum(correlation(rank(volume), rank(vwap), 6), 2) / 2.0))),
            (-1 * 1),
            1,
        )
    )


def alpha_28(low, high, close, adv20, **kwargs):
    return scale(((correlation(adv20, low, 5) + ((high + low) / 2)) - close))


def alpha_29(close, returns, **kwargs):
    return min(
        product(
            rank(
                rank(
                    scale(
                        log(
                            sum(
                                ts_min(rank(rank((-1 * rank(delta((close - 1), 5))))), 2),
                                1,
                            )
                        )
                    )
                )
            ),
            1,
        ),
        5,
    ) + ts_rank(delay((-1 * returns), 6), 5)


def alpha_30(close, volume, **kwargs):
    return (
        (
            1.0
            - rank(
                (
                    (sign((close - delay(close, 1))) + sign((delay(close, 1) - delay(close, 2))))
                    + sign((delay(close, 2) - delay(close, 3)))
                )
            )
        )
        * sum(volume, 5)
    ) / sum(volume, 20)


def alpha_31(low, close, adv20, **kwargs):
    return (rank(rank(rank(decay_linear((-1 * rank(rank(delta(close, 10)))), 10)))) + rank((-1 * delta(close, 3)))) + sign(
        scale(correlation(adv20, low, 12))
    )


def alpha_32(close, vwap, **kwargs):
    return scale(((sum(close, 7) / 7) - close)) + (20 * scale(correlation(vwap, delay(close, 5), 230)))


def alpha_33(open, close, **kwargs):
    return rank((-1 * np.logical_xor((1 - (open / close)), 1)))


def alpha_34(close, returns, **kwargs):
    return rank(((1 - rank((stddev(returns, 2) / stddev(returns, 5)))) + (1 - rank(delta(close, 1)))))


def alpha_35(low, high, close, volume, returns, **kwargs):
    return (ts_rank(volume, 32) * (1 - ts_rank(((close + high) - low), 16))) * (1 - ts_rank(returns, 32))


def alpha_36(open, close, volume, vwap, adv20, returns, **kwargs):
    return (
        (
            ((2.21 * rank(correlation((close - open), delay(volume, 1), 15))) + (0.7 * rank((open - close))))
            + (0.73 * rank(ts_rank(delay((-1 * returns), 6), 5)))
        )
        + rank(abs(correlation(vwap, adv20, 6)))
    ) + (0.6 * rank((((sum(close, 200) / 200) - open) * (close - open))))


def alpha_37(open, close, **kwargs):
    return rank(correlation(delay((open - close), 1), close, 200)) + rank((open - close))


def alpha_38(open, close, **kwargs):
    return (-1 * rank(ts_rank(close, 10))) * rank((close / open))


def alpha_39(close, volume, adv20, returns, **kwargs):
    return (-1 * rank((delta(close, 7) * (1 - rank(decay_linear((volume / adv20), 9)))))) * (1 + rank(sum(returns, 250)))


def alpha_40(high, volume, **kwargs):
    return (-1 * rank(stddev(high, 10))) * correlation(high, volume, 10)


def alpha_41(low, high, vwap, **kwargs):
    return np.logical_xor((high * low), 0.5) - vwap


def alpha_42(close, vwap, **kwargs):
    return rank((vwap - close)) / rank((vwap + close))


def alpha_43(close, volume, adv20, **kwargs):
    return ts_rank((volume / adv20), 20) * ts_rank((-1 * delta(close, 7)), 8)


def alpha_44(high, volume, **kwargs):
    return -1 * correlation(high, rank(volume), 5)


def alpha_45(close, volume, **kwargs):
    return -1 * (
        (rank((sum(delay(close, 5), 20) / 20)) * correlation(close, volume, 2))
        * rank(correlation(sum(close, 5), sum(close, 20), 2))
    )


def alpha_46(close, **kwargs):
    return pd.Series(
        np.where(
            (0.25 < (((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10))),
            (-1 * 1),
            np.where(
                ((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < 0),
                1,
                ((-1 * 1) * (close - delay(close, 1))),
            ),
        )
    )


def alpha_47(high, close, volume, vwap, adv20, **kwargs):
    return (((rank((1 / close)) * volume) / adv20) * ((high * rank((high - close))) / (sum(high, 5) / 5))) - rank(
        (vwap - delay(vwap, 5))
    )


def alpha_48(close, indclass, **kwargs):
    return indneutralize(
        ((correlation(delta(close, 1), delta(delay(close, 1), 1), 250) * delta(close, 1)) / close),
        indclass.subindustry,
    ) / sum(np.logical_xor((delta(close, 1) / delay(close, 1)), 2), 250)


def alpha_49(close, **kwargs):
    return pd.Series(
        np.where(
            ((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < (-1 * 0.1)),
            1,
            ((-1 * 1) * (close - delay(close, 1))),
        )
    )


def alpha_50(volume, vwap, **kwargs):
    return -1 * ts_max(rank(correlation(rank(volume), rank(vwap), 5)), 5)


def alpha_51(close, **kwargs):
    return pd.Series(
        np.where(
            ((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < (-1 * 0.05)),
            1,
            ((-1 * 1) * (close - delay(close, 1))),
        )
    )


def alpha_52(low, volume, returns, **kwargs):
    return (((-1 * ts_min(low, 5)) + delay(ts_min(low, 5), 5)) * rank(((sum(returns, 240) - sum(returns, 20)) / 220))) * ts_rank(
        volume, 5
    )


def alpha_53(low, high, close, **kwargs):
    return -1 * delta((((close - low) - (high - close)) / (close - low)), 9)


def alpha_54(open, low, high, close, **kwargs):
    return (-1 * ((low - close) * np.logical_xor(open, 5))) / ((low - high) * np.logical_xor(close, 5))


def alpha_55(low, high, close, volume, **kwargs):
    return -1 * correlation(
        rank(((close - ts_min(low, 12)) / (ts_max(high, 12) - ts_min(low, 12)))),
        rank(volume),
        6,
    )


def alpha_56(cap, returns, **kwargs):
    return 0 - (1 * (rank((sum(returns, 10) / sum(sum(returns, 2), 3))) * rank((returns * cap))))


def alpha_57(close, vwap, **kwargs):
    return 0 - (1 * ((close - vwap) / decay_linear(rank(ts_argmax(close, 30)), 2)))


def alpha_58(volume, vwap, indclass, **kwargs):
    return -1 * ts_rank(
        decay_linear(correlation(indneutralize(vwap, indclass.sector), volume, 3.92795), 7.89291),
        5.50322,
    )


def alpha_59(volume, vwap, indclass, **kwargs):
    return -1 * ts_rank(
        decay_linear(
            correlation(
                indneutralize(((vwap * 0.728317) + (vwap * (1 - 0.728317))), indclass.industry),
                volume,
                4.25197,
            ),
            16.2289,
        ),
        8.19648,
    )


def alpha_60(low, high, close, volume, **kwargs):
    return 0 - (
        1 * ((2 * scale(rank(((((close - low) - (high - close)) / (high - low)) * volume)))) - scale(rank(ts_argmax(close, 10))))
    )


def alpha_61(vwap, adv180, **kwargs):
    return rank((vwap - ts_min(vwap, 16.1219))) < rank(correlation(vwap, adv180, 17.9282))


def alpha_62(open, low, high, vwap, adv20, **kwargs):
    return (
        rank(correlation(vwap, sum(adv20, 22.4101), 9.91009))
        < rank(((rank(open) + rank(open)) < (rank(((high + low) / 2)) + rank(high))))
    ) * -1


def alpha_63(open, close, vwap, indclass, adv180, **kwargs):
    return (
        rank(decay_linear(delta(indneutralize(close, indclass.industry), 2.25164), 8.22237))
        - rank(
            decay_linear(
                correlation(
                    ((vwap * 0.318108) + (open * (1 - 0.318108))),
                    sum(adv180, 37.2467),
                    13.557,
                ),
                12.2883,
            )
        )
    ) * -1


def alpha_64(open, low, high, vwap, adv120, **kwargs):
    return (
        rank(
            correlation(
                sum(((open * 0.178404) + (low * (1 - 0.178404))), 12.7054),
                sum(adv120, 12.7054),
                16.6208,
            )
        )
        < rank(delta(((((high + low) / 2) * 0.178404) + (vwap * (1 - 0.178404))), 3.69741))
    ) * -1


def alpha_65(open, vwap, adv60, **kwargs):
    return (
        rank(
            correlation(
                ((open * 0.00817205) + (vwap * (1 - 0.00817205))),
                sum(adv60, 8.6911),
                6.40374,
            )
        )
        < rank((open - ts_min(open, 13.635)))
    ) * -1


def alpha_66(open, low, high, vwap, **kwargs):
    return (
        rank(decay_linear(delta(vwap, 3.51013), 7.23052))
        + ts_rank(
            decay_linear(
                ((((low * 0.96633) + (low * (1 - 0.96633))) - vwap) / (open - ((high + low) / 2))),
                11.4157,
            ),
            6.72611,
        )
    ) * -1


def alpha_67(high, vwap, indclass, adv20, **kwargs):
    return (
        np.logical_xor(
            rank((high - ts_min(high, 2.14593))),
            rank(
                correlation(
                    indneutralize(vwap, indclass.sector),
                    indneutralize(adv20, indclass.subindustry),
                    6.02936,
                )
            ),
        )
        * -1
    )


def alpha_68(low, high, close, adv15, **kwargs):
    return (
        ts_rank(correlation(rank(high), rank(adv15), 8.91644), 13.9333)
        < rank(delta(((close * 0.518371) + (low * (1 - 0.518371))), 1.06157))
    ) * -1


def alpha_69(close, vwap, indclass, adv20, **kwargs):
    return (
        np.logical_xor(
            rank(ts_max(delta(indneutralize(vwap, indclass.industry), 2.72412), 4.79344)),
            ts_rank(
                correlation(((close * 0.490655) + (vwap * (1 - 0.490655))), adv20, 4.92416),
                9.0615,
            ),
        )
        * -1
    )


def alpha_70(close, vwap, indclass, adv50, **kwargs):
    return pd.Series(
        np.logical_xor(
            rank(delta(vwap, 1.29456)),
            ts_rank(
                correlation(indneutralize(close, indclass.industry), adv50, 17.8256),
                17.9171,
            ),
        )
        * -1
    )


def alpha_71(open, low, close, vwap, adv180, **kwargs):
    return max(
        ts_rank(
            decay_linear(
                correlation(ts_rank(close, 3.43976), ts_rank(adv180, 12.0647), 18.0175),
                4.20501,
            ),
            15.6948,
        ),
        ts_rank(
            decay_linear(
                pd.Series(np.logical_xor(rank(((low + open) - (vwap + vwap))), 2)),
                16.4662,
            ),
            4.4388,
        ),
    )


def alpha_72(low, high, volume, vwap, adv40, **kwargs):
    return rank(decay_linear(correlation(((high + low) / 2), adv40, 8.93345), 10.1519)) / rank(
        decay_linear(
            correlation(ts_rank(vwap, 3.72469), ts_rank(volume, 18.5188), 6.86671),
            2.95011,
        )
    )


def alpha_73(open, low, vwap, **kwargs):
    return (
        max(
            rank(decay_linear(delta(vwap, 4.72775), 2.91864)),
            ts_rank(
                decay_linear(
                    (
                        (
                            delta(((open * 0.147155) + (low * (1 - 0.147155))), 2.03608)
                            / ((open * 0.147155) + (low * (1 - 0.147155)))
                        )
                        * -1
                    ),
                    3.33829,
                ),
                16.7411,
            ),
        )
        * -1
    )


def alpha_74(high, close, volume, vwap, adv30, **kwargs):
    return (
        rank(correlation(close, sum(adv30, 37.4843), 15.1365))
        < rank(
            correlation(
                rank(((high * 0.0261661) + (vwap * (1 - 0.0261661)))),
                rank(volume),
                11.4791,
            )
        )
    ) * -1


def alpha_75(low, volume, vwap, adv50, **kwargs):
    return rank(correlation(vwap, volume, 4.24304)) < rank(correlation(rank(low), rank(adv50), 12.4413))


def alpha_76(low, vwap, indclass, adv81, **kwargs):
    return (
        max(
            rank(decay_linear(delta(vwap, 1.24383), 11.8259)),
            ts_rank(
                decay_linear(
                    ts_rank(
                        correlation(indneutralize(low, indclass.sector), adv81, 8.14941),
                        19.569,
                    ),
                    17.1543,
                ),
                19.383,
            ),
        )
        * -1
    )


def alpha_77(low, high, vwap, adv40, **kwargs):
    return min(
        rank(decay_linear(((((high + low) / 2) + high) - (vwap + high)), 20.0451)),
        rank(decay_linear(correlation(((high + low) / 2), adv40, 3.1614), 5.64125)),
    )


def alpha_78(low, volume, vwap, adv40, **kwargs):
    return np.logical_xor(
        rank(
            correlation(
                sum(((low * 0.352233) + (vwap * (1 - 0.352233))), 19.7428),
                sum(adv40, 19.7428),
                6.83313,
            )
        ),
        rank(correlation(rank(vwap), rank(volume), 5.77492)),
    )


def alpha_79(open, close, vwap, indclass, adv150, **kwargs):
    return rank(
        delta(
            indneutralize(((close * 0.60733) + (open * (1 - 0.60733))), indclass.sector),
            1.23438,
        )
    ) < rank(correlation(ts_rank(vwap, 3.60973), ts_rank(adv150, 9.18637), 14.6644))


def alpha_80(open, high, indclass, adv10, **kwargs):
    return pd.Series(
        np.logical_xor(
            rank(
                sign(
                    delta(
                        indneutralize(
                            ((open * 0.868128) + (high * (1 - 0.868128))),
                            indclass.industry,
                        ),
                        4.04545,
                    )
                )
            ),
            ts_rank(correlation(high, adv10, 5.11456), 5.53756),
        )
        * -1
    )


def alpha_81(volume, vwap, adv10, **kwargs):
    return (
        rank(
            log(
                product(
                    rank(pd.Series(np.logical_xor(rank(correlation(vwap, sum(adv10, 49.6054), 8.47743)), 4))),
                    14.9655,
                )
            )
        )
        < rank(correlation(rank(vwap), rank(volume), 5.07914))
    ) * -1


def alpha_82(open, volume, indclass, **kwargs):
    return (
        min(
            rank(decay_linear(delta(open, 1.46063), 14.8717)),
            ts_rank(
                decay_linear(
                    correlation(
                        indneutralize(volume, indclass.sector),
                        ((open * 0.634196) + (open * (1 - 0.634196))),
                        17.4842,
                    ),
                    6.92131,
                ),
                13.4283,
            ),
        )
        * -1
    )


def alpha_83(low, high, close, volume, vwap, **kwargs):
    return (rank(delay(((high - low) / (sum(close, 5) / 5)), 2)) * rank(rank(volume))) / (
        ((high - low) / (sum(close, 5) / 5)) / (vwap - close)
    )


def alpha_84(close, vwap, **kwargs):
    return signedpower(ts_rank((vwap - ts_max(vwap, 15.3217)), 20.7127), delta(close, 4.96796))


def alpha_85(low, high, close, volume, adv30, **kwargs):
    return pd.Series(
        np.logical_xor(
            rank(correlation(((high * 0.876703) + (close * (1 - 0.876703))), adv30, 9.61331)),
            rank(
                correlation(
                    ts_rank(((high + low) / 2), 3.70596),
                    ts_rank(volume, 10.1595),
                    7.11408,
                )
            ),
        )
    )


def alpha_86(open, close, vwap, adv20, **kwargs):
    return (ts_rank(correlation(close, sum(adv20, 14.7444), 6.00049), 20.4195) < rank(((open + close) - (vwap + open)))) * -1


def alpha_87(close, vwap, indclass, adv81, **kwargs):
    return (
        max(
            rank(
                decay_linear(
                    delta(((close * 0.369701) + (vwap * (1 - 0.369701))), 1.91233),
                    2.65461,
                )
            ),
            ts_rank(
                decay_linear(
                    abs(correlation(indneutralize(adv81, indclass.industry), close, 13.4132)),
                    4.89768,
                ),
                14.4535,
            ),
        )
        * -1
    )


def alpha_88(open, low, high, close, adv60, **kwargs):
    return min(
        rank(decay_linear(((rank(open) + rank(low)) - (rank(high) + rank(close))), 8.06882)),
        ts_rank(
            decay_linear(
                correlation(ts_rank(close, 8.44728), ts_rank(adv60, 20.6966), 8.01266),
                6.65053,
            ),
            2.61957,
        ),
    )


def alpha_89(low, vwap, indclass, adv10, **kwargs):
    return ts_rank(
        decay_linear(
            correlation(((low * 0.967285) + (low * (1 - 0.967285))), adv10, 6.94279),
            5.51607,
        ),
        3.79744,
    ) - ts_rank(
        decay_linear(delta(indneutralize(vwap, indclass.industry), 3.48158), 10.1466),
        15.3012,
    )


def alpha_90(low, close, indclass, adv40, **kwargs):
    return pd.Series(
        np.logical_xor(
            rank((close - ts_max(close, 4.66719))),
            ts_rank(
                correlation(indneutralize(adv40, indclass.subindustry), low, 5.38375),
                3.21856,
            ),
        )
        * -1
    )


def alpha_91(close, volume, vwap, indclass, adv30, **kwargs):
    return (
        ts_rank(
            decay_linear(
                decay_linear(
                    correlation(indneutralize(close, indclass.industry), volume, 9.74928),
                    16.398,
                ),
                3.83219,
            ),
            4.8667,
        )
        - rank(decay_linear(correlation(vwap, adv30, 4.01303), 2.6809))
    ) * -1


def alpha_92(open, low, high, close, adv30, **kwargs):
    return min(
        ts_rank(
            decay_linear(((((high + low) / 2) + close) < (low + open)), 14.7221),
            18.8683,
        ),
        ts_rank(decay_linear(correlation(rank(low), rank(adv30), 7.58555), 6.94024), 6.80584),
    )


def alpha_93(close, vwap, indclass, adv81, **kwargs):
    return ts_rank(
        decay_linear(correlation(indneutralize(vwap, indclass.industry), adv81, 17.4193), 19.848),
        7.54455,
    ) / rank(decay_linear(delta(((close * 0.524434) + (vwap * (1 - 0.524434))), 2.77377), 16.2664))


def alpha_94(vwap, adv60, **kwargs):
    return pd.Series(
        np.logical_xor(
            rank((vwap - ts_min(vwap, 11.5783))),
            ts_rank(
                correlation(ts_rank(vwap, 19.6462), ts_rank(adv60, 4.02992), 18.0926),
                2.70756,
            ),
        )
        * -1
    )


def alpha_95(open, low, high, adv40, **kwargs):
    return rank((open - ts_min(open, 12.4105))) < ts_rank(
        pd.Series(
            np.logical_xor(
                rank(correlation(sum(((high + low) / 2), 19.1351), sum(adv40, 19.1351), 12.8742)),
                5,
            ),
            11.7584,
        )
    )


def alpha_96(close, volume, vwap, adv60, **kwargs):
    return (
        max(
            ts_rank(
                decay_linear(correlation(rank(vwap), rank(volume), 3.83878), 4.16783),
                8.38151,
            ),
            ts_rank(
                decay_linear(
                    ts_argmax(
                        correlation(ts_rank(close, 7.45404), ts_rank(adv60, 4.13242), 3.65459),
                        12.6556,
                    ),
                    14.0365,
                ),
                13.4143,
            ),
        )
        * -1
    )


def alpha_97(low, vwap, indclass, adv60, **kwargs):
    return (
        rank(
            decay_linear(
                delta(
                    indneutralize(((low * 0.721001) + (vwap * (1 - 0.721001))), indclass.industry),
                    3.3705,
                ),
                20.4523,
            )
        )
        - ts_rank(
            decay_linear(
                ts_rank(
                    correlation(ts_rank(low, 7.87871), ts_rank(adv60, 17.255), 4.97547),
                    18.5925,
                ),
                15.7152,
            ),
            6.71659,
        )
    ) * -1


def alpha_98(open, vwap, adv5, adv15, **kwargs):
    return rank(decay_linear(correlation(vwap, sum(adv5, 26.4719), 4.58418), 7.18088)) - rank(
        decay_linear(
            ts_rank(
                ts_argmin(correlation(rank(open), rank(adv15), 20.8187), 8.62571),
                6.95668,
            ),
            8.07206,
        )
    )


def alpha_99(low, high, volume, adv60, **kwargs):
    return (
        rank(correlation(sum(((high + low) / 2), 19.8975), sum(adv60, 19.8975), 8.8136)) < rank(correlation(low, volume, 6.28259))
    ) * -1


def alpha_100(low, high, close, volume, indclass, adv20, **kwargs):
    return 0 - (
        1
        * (
            (
                (
                    1.5
                    * scale(
                        indneutralize(
                            indneutralize(
                                rank(((((close - low) - (high - close)) / (high - low)) * volume)),
                                indclass.subindustry,
                            ),
                            indclass.subindustry,
                        )
                    )
                )
                - scale(
                    indneutralize(
                        (correlation(close, rank(adv20), 5) - rank(ts_argmin(close, 30))),
                        indclass.subindustry,
                    )
                )
            )
            * (volume / adv20)
        )
    )


def alpha_101(open, low, high, close, **kwargs):
    return (close - open) / ((high - low) + 0.001)
