from facebook.api_base import APIBase
import pandas as pd
import requests
import json

class FacebookAdsAPI(APIBase):

    def __init__(self,ad_account_id,access_token):
        
        self.ad_account_id = ad_account_id
        self.base_url = "https://graph.facebook.com/v8.0/"
        self.access_token = access_token
        self.access_token_uri = f"access_token={access_token}"
        super().__init__()
        
    def get_ad_account(self):
        uri = self.base_url + f"{self.ad_account_id}/" + "?"
        params = {"access_token": self.access_token}
        result = self.make_get(uri,params,return_type='json')
    
        return result

    def get_all_campaings(self,as_df=False):
            node_name = "campaigns"
            fields = """id,account_id,budget_remaining,buying_type,configured_status,created_time,
                        daily_budget,effective_status,lifetime_budget,name,objective,
                        start_time,status,stop_time,updated_time"""

            params = {"fields": fields,
            "access_token":self.access_token,
            "date_preset": "lifetime"
            }
            uri = self.base_url + f"{self.ad_account_id}/{node_name}?"

            data = self.make_get_processing(uri,params)

            if as_df:
                df_data = pd.DataFrame(data)
                return df_data
            else:
                return data

    def get_all_campaigns_insights(self,campaign_id_list):

        full_data = []

        for campaing_id in campaign_id_list:
            campaing_id = str(campaing_id)
            data = self.get_campaign_insights(campaing_id)
            full_data += data

        return full_data



    def get_campaign_insights(self,campaign_id,time_increment=1,as_df=False):
        fields = """account_currency,account_id,account_name,campaign_id,campaign_name,
            buying_type,clicks,date_start,date_stop,frequency,impressions,
            inline_link_clicks,inline_post_engagement,objective,reach,social_spend,
            spend,unique_clicks,unique_inline_link_clicks,unique_link_clicks_ctr,action_values,
            actions,cost_per_action_type,cost_per_unique_click,
            cpc,cpm,cpp,ctr,purchase_roas,unique_actions,unique_ctr,
            cost_per_thruplay,video_30_sec_watched_actions,
            video_avg_time_watched_actions,video_p100_watched_actions,video_p25_watched_actions,
            video_p50_watched_actions,video_p75_watched_actions,video_p95_watched_actions,video_play_actions"""


        params = {"access_token":self.access_token,
                "fields":fields,
                "date_preset":"lifetime",
                "time_increment":time_increment}
        uri = f"{self.base_url}{campaign_id}/insights?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data

