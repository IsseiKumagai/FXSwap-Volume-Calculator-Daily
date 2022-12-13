"""query ($timestamp_gte: BigInt, $timestamp_lt: BigInt, $from: String) {
  swaps(
    orderBy: timestamp
    orderDirection: desc
    where: {timestamp_gte: $timestamp_gte, timestamp_lt: $timestamp_lt, from: $from}
  ) {
    id
    timestamp
    amountOutUSD
    amountInUSD
    tokenIn {
      name
      symbol
    }
    tokenOut {
      name
      symbol
    }
    amountIn
    amountOut
    pool {
      id
    }
  }
}"""