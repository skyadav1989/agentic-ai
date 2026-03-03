import httpx
import os

async def search_products(query):

    url = os.getenv("MAGENTO_GRAPHQL_URL")

    graphql_query = """
    query ($search: String!) {
      products(search: $search) {
        items {
          name
          sku
          price_range {
            minimum_price {
              regular_price {
                value
                currency
              }
            }
          }
        }
      }
    }
    """

    try:
        async with httpx.AsyncClient(
            timeout=httpx.Timeout(20.0, connect=10.0),
            verify=False  # TEMP: disable SSL verification
        ) as client:

            response = await client.post(
                url,
                json={
                    "query": graphql_query,
                    "variables": {"search": query}
                }
            )

            print("response\n")
            print(query)
            print(response)
            

            response.raise_for_status()
            return response.json()

    except httpx.ConnectTimeout:
        return {
            "error": "Magento connection timeout. Server unreachable."
        }

    except httpx.ReadTimeout:
        return {
            "error": "Magento server slow response."
        }

    except Exception as e:
        return {
            "error": f"Magento error: {str(e)}"
        }