import requests
import logging
import datetime


def total_volume(unix_timestamp):
    """Calculates the total volume on FXSwap for a USDT/FX pair (in US dollar) after a specified date in unix timestamp"""

    try:
        subgraph_url = "https://graph-node.functionx.io/subgraphs/name/subgraphFX2"
        graphql_query = """
            query ($token0: String = "0x80b5a32e4f032b2a058b4f29ec95eefeeb87adcd",
            $token1: String = "0xeceeefcee421d8062ef8d6b4d814efe4dc898265",
            $date_gte: Int = """ + f'{unix_timestamp}' + """) 
            {
              pairDayDatas(
                orderBy: date
                orderDirection: desc
                where: {token0: $token0, token1: $token1, date_gte: $date_gte}
              ) {
                dailyVolumeUSD
                date
                id
                token0 {
                  name
                  id
                }
                token1 {
                  name
                  id
                }
              }
            }
        """
        query_body = {"query": graphql_query}
        daily_volume_response_data = requests.post(url=subgraph_url, json=query_body)
        daily_volume_json = daily_volume_response_data.json()
        daily_volume_data = daily_volume_json['data']['pairDayDatas']
        total_volume_USD_FX_USDT_pair = sum(float(volume_data['dailyVolumeUSD']) for volume_data in daily_volume_data)
        return total_volume_USD_FX_USDT_pair
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    unix_timestamp = 1666483200
    print("datetime greater than equal to", datetime.datetime.fromtimestamp(unix_timestamp))
    print("$", total_volume(unix_timestamp))

