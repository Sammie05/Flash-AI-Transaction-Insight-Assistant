def generate_insight(amount_sats, fee_sats, confirmation_time, network):
    insights = []

    fee_ratio = fee_sats / max(amount_sats, 1)

    if network.lower() == "bitcoin":
        if fee_ratio > 0.05:
            insights.append(
                "The transaction fee is relatively high compared to the amount sent."
            )
        else:
            insights.append(
                "The transaction fee is reasonable for an on-chain Bitcoin payment."
            )

        if confirmation_time > 30:
            insights.append(
                "The confirmation time is longer than usual, likely due to network congestion."
            )
        else:
            insights.append(
                "The transaction confirmed within a normal time frame."
            )

        insights.append(
            "For smaller or urgent payments, using Lightning could be faster and cheaper."
        )

    elif network.lower() == "lightning":
        insights.append(
            "Lightning payments are designed to be fast and low-fee."
        )

        if confirmation_time > 1:
            insights.append(
                "A delay may indicate routing or temporary liquidity issues."
            )

    return " ".join(insights)
