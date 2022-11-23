import requests
import logging
import datetime


def total_volume(unix_timestamp):
    """Calculates the total volume on FXSwap for a USDT/FX pair (in US dollar) after a specified date in unix timestamp"""

    try:
        subgraph_url = "https://graph-node.functionx.io/subgraphs/name/subgraphFX2"
        graphql_query = """ 
        query {

  transactions(
    orderBy: timestamp
    orderDirection: asc
    where: {blockNumber: ""}
  ) {
    swaps(
      where: {pair: "0xad35c15c69d0e39e467b81003d03407ea908b33f", from: "0xe3d6453f5282fbc5b567f49b921fe5c8035544f6"}
    ) {
      id
      amountUSD
      from
      pair {
        token1 {
          name
          symbol
        }
        token0 {
          name
          symbol
        }
        id
      }
      timestamp
      transaction {
        id
      }
    }
  }

        }
        """

        """
        query MyQuery {
  blocks(orderBy: number, orderDirection: desc, first: 1000) {
    number
    timestamp
  }
}
        """
    except Exception as e:
        pass

