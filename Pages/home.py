import requests
import streamlit as st


def app():
    # region Helper Methods
    def build_query(_wallet_address):
        _query_part_two = """    
                        id
                        lastBalance {
                          sohmBalance
                          ohmBalance
                          dollarBalance
                          timestamp
                        }
                      }
                    }
                    """
        return ''.join(("{ ohmies(where: {id: \"", _wallet_address, "\"}) {", _query_part_two))

    def run_query(_query):
        # endpoint where you are making the request
        request = requests.post('https://api.thegraph.com/subgraphs/name/drondin/olympus-graph'
                                '',
                                json={'query': _query})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, _query))

    # endregion

    wallet_address = st.text_input('Wallet Address', value="0x2be68e381eaad342b9892961beb822270ef1fbd4")
    # Olympus treasury Addr 0x31F8Cc382c9898b273eff4e0b7626a6987C846E8

    # Assign the results
    result = run_query(build_query(wallet_address))

    # results come as a list of dictionaries, which is in a nested dictionary. so we have to extract the dictionary we care about
    dataDict = result["data"]

    st.write(f"{dataDict}")
