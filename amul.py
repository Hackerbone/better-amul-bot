import urllib.request
import json
import sys
import httpx

def get_amul_data_urllib():
    url = "https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0&cdc=1m&substore=66505ff0998183e1b1935c75"

    headers = {
        "referer": "https://shop.amul.com/",
        "authority": "shop.amul.com",
        "method": "GET",
        "scheme": "https",
        "User-Agent": "PostmanRuntime/7.47.0",
        "Accept": "application/json",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print("Products fetched:", len(data.get("data", [])))
            return data
    except Exception as e:
        print("Failed to fetch or parse data:", e)
        return None


def get_amul_data_httpx():
    url = "https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0&cdc=1m&substore=66505ff0998183e1b1935c75"

    try:
        with httpx.Client(timeout=10) as client:
            response = client.get(url)
            response.raise_for_status()
            data = response.json()
            print("Products fetched:", len(data.get("data", [])))
            return data
    except Exception as e:
        print("httpx request failed:", e)
        return None

if __name__ == "__main__":
    # Try httpx first, fall back to urllib if it fails
    data = get_amul_data_httpx()
    if data is None:
        data = get_amul_data_urllib()
    
    if data:
        # If running in GitHub Actions, write to file
        if len(sys.argv) > 1 and sys.argv[1] == "--github-actions":
            with open("amul_state.json", "w") as f:
                json.dump(data, f, indent=2)
        else:
            # Otherwise print to stdout
            print(json.dumps(data, indent=2))
