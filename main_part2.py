import requests
import logging
import datetime
import time

def get_graphql_query(timestamp_start, timestamp_end):

    graphql_query = """ query  {
          transactions(
            orderBy: timestamp
            orderDirection: asc
            first: 1000
            where: {timestamp_gte: """ + f'{timestamp_start}' + """, timestamp_lt: """ + f'{timestamp_end}' + """}
          ) {
            swaps(
              where: {pair: "0xad35c15c69d0e39e467b81003d03407ea908b33f", from: "0xe3d6453f5282fbc5b567f49b921fe5c8035544f6"}
            ) {
              amountUSD
              timestamp
            }
          }
        }
    """
    return graphql_query

def total_volume(timestamp_start, time_increment=1800):

    current_time = int(time.time()) # gives singapore timezone
    subgraph_url = "https://graph-node.functionx.io/subgraphs/name/subgraphFX2"
    start_time = timestamp_start
    end_time = start_time + time_increment
    total_volume_sum_usd = 0

    while start_time <= current_time:
        print(start_time, total_volume_sum_usd)
        graphql_query = get_graphql_query(start_time, end_time)
        query_body = {"query": graphql_query}

        try:
            daily_volume_response_data = requests.post(url=subgraph_url, json=query_body)
            daily_volume_json = daily_volume_response_data.json()

            for swap_data_dictionary in daily_volume_json['data']['transactions']:
                if 'swaps' in swap_data_dictionary:
                    for swap_usd_dictionary in swap_data_dictionary['swaps']:
                        if 'amountUSD' in swap_usd_dictionary:
                            total_volume_sum_usd += float(swap_usd_dictionary['amountUSD'])

            start_time = end_time
            end_time = start_time + time_increment
        except Exception as e:
            logging.error(e)

    return total_volume_sum_usd

if __name__ == '__main__':
    unix_timestamp = 1668250800
    print("datetime greater than equal to", datetime.datetime.fromtimestamp(unix_timestamp))
    print("$", total_volume(unix_timestamp))


################ original query ###############
"""query  {
  transactions(
    orderBy: timestamp
    orderDirection: asc
    first: 1000
    where: {timestamp_gte: "1668330000", timestamp_lt: "1668333600"}
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
}  """