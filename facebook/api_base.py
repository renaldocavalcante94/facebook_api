import requests


class APIBase():

    def __init__(self):
        self.requests = 0

    def make_get(self,uri,params=None,return_type='json'):
        self.requests += 1
        
        if self.request_count:
            print(self.requests)
        

        # ! To Do - Create an logging to the external requests

        result = requests.get(uri,params=params)

        if return_type == 'json':
            return result.json()
        elif return_type == 'results':
            return result

    def paging_processment(self,data,paging):
        if type(data)!=list:
            raise TypeError("Data have to be a list of json results")
        
        while 'next' in paging.keys():
            next_uri = paging['next']


            new_result = self.make_get(next_uri,'json')
            new_data = new_result['data']
            new_paging = new_result['paging']

            
            paging = new_paging

            data += new_data

        return data

    def make_get_processing(self,uri,params):
        
        result = self.make_get(uri,params,'json')

        try:
            data = result['data']
            if data != []:
                paging = result['paging']
            else:
                return data

        except Exception as error:
            print(result)
            raise error

        data = self.paging_processment(data,paging)

        return data

